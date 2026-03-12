"""Tests for performance characteristics and memory usage of docstring parsing."""

import gc
import sys
import time
from typing import List
import pytest
from PyDocSmith.parser import parse
from PyDocSmith.google import parse as google_parse, compose as google_compose
from PyDocSmith.numpydoc import parse as numpy_parse, compose as numpy_compose


def test_large_docstring_parsing_performance() -> None:
    """Test parsing performance with very large docstrings."""
    # Generate a large docstring with many parameters
    large_docstring_parts = [
        "Process large datasets with comprehensive parameter validation.",
        "",
        "This function handles massive datasets with extensive configuration",
        "options and provides detailed logging and monitoring capabilities.",
        "",
        "Args:"
    ]
    
    # Add 100 parameters to test scalability
    for i in range(100):
        param_type = ["str", "int", "float", "bool", "List[str]", "Dict[str, Any]"][i % 6]
        optional = ", optional" if i % 3 == 0 else ""
        default = f". Defaults to {i}." if optional else ""
        
        large_docstring_parts.extend([
            f"    param_{i:03d} ({param_type}{optional}): Description for parameter {i}",
            f"        with detailed explanation of its purpose{default}"
        ])
    
    # Add returns and raises sections
    large_docstring_parts.extend([
        "",
        "Returns:",
        "    Dict[str, Any]: Comprehensive results dictionary containing:",
        "        - processed_data: The main processed dataset",
        "        - metadata: Processing metadata and statistics", 
        "        - warnings: List of any warnings encountered",
        "        - performance_metrics: Timing and memory usage data",
        "",
        "Raises:"
    ])
    
    # Add many exception types
    exception_types = [
        "ValueError", "TypeError", "RuntimeError", "MemoryError", "IOError",
        "KeyError", "IndexError", "AttributeError", "ImportError", "OSError"
    ]
    
    for exc_type in exception_types:
        large_docstring_parts.extend([
            f"    {exc_type}: If {exc_type.lower()} condition is encountered",
            f"        during processing of the large dataset"
        ])
    
    large_docstring = "\n".join(large_docstring_parts)
    
    # Measure parsing time
    start_time = time.time()
    parsed = parse(large_docstring)
    parse_time = time.time() - start_time
    
    # Verify parsing completed successfully
    assert parsed is not None
    assert len(parsed.params) == 100
    assert len(parsed.raises) == 10
    assert parsed.returns is not None
    
    # Performance assertion - should parse large docstring in reasonable time
    assert parse_time < 1.0, f"Large docstring parsing took {parse_time:.3f}s, expected < 1.0s"
    
    # Test composition performance
    start_time = time.time()
    composed = google_compose(parsed)
    compose_time = time.time() - start_time
    
    assert compose_time < 0.5, f"Large docstring composition took {compose_time:.3f}s, expected < 0.5s"
    assert len(composed) > 1000  # Should be a substantial docstring


def test_memory_usage_with_many_docstrings() -> None:
    """Test memory usage when parsing many docstrings."""
    # Create a variety of docstring templates
    docstring_templates = [
        """
        Simple function with basic parameters.
        
        Args:
            param1 (str): First parameter
            param2 (int): Second parameter
            
        Returns:
            bool: Success status
        """,
        
        """
        Complex data processing function.
        
        This function performs advanced data transformations with multiple
        configuration options and error handling mechanisms.
        
        Args:
            data (List[Dict[str, Any]]): Input data structures
            config (ProcessingConfig): Configuration object
            parallel (bool, optional): Enable parallel processing. Defaults to True.
            workers (int, optional): Number of worker threads. Defaults to 4.
            
        Returns:
            ProcessingResult: Object containing processed data and metadata
            
        Raises:
            ProcessingError: If data processing fails
            ConfigurationError: If configuration is invalid
            
        Example:
            >>> result = process_data(data, config)
            >>> print(result.success_rate)
        """,
        
        """
        Mathematical computation with numpy arrays.
        
        Parameters
        ----------
        matrix : numpy.ndarray
            Input matrix for computation
        axis : int, optional
            Axis along which to perform computation, by default 0
        keepdims : bool, optional
            Whether to keep dimensions, by default False
            
        Returns
        -------
        numpy.ndarray
            Computed result array
            
        Notes
        -----
        This function uses optimized BLAS routines for performance.
        """
    ]
    
    # Measure initial memory usage
    gc.collect()  # Force garbage collection
    initial_memory = sys.getsizeof(gc.get_objects())
    
    # Parse many docstrings
    parsed_docstrings = []
    num_iterations = 1000
    
    start_time = time.time()
    for i in range(num_iterations):
        template = docstring_templates[i % len(docstring_templates)]
        # Vary the docstring slightly to avoid caching effects
        varied_docstring = template.replace("param1", f"param1_{i % 100}")
        parsed = parse(varied_docstring)
        parsed_docstrings.append(parsed)
    
    total_time = time.time() - start_time
    
    # Measure final memory usage
    gc.collect()
    final_memory = sys.getsizeof(gc.get_objects())
    memory_increase = final_memory - initial_memory
    
    # Performance assertions
    avg_time_per_parse = total_time / num_iterations
    assert avg_time_per_parse < 0.01, f"Average parse time {avg_time_per_parse:.4f}s too slow"
    
    # Memory usage should be reasonable (less than 1MB per 1000 docstrings)
    memory_per_docstring = memory_increase / num_iterations
    assert memory_per_docstring < 1024, f"Memory usage {memory_per_docstring} bytes per docstring too high"
    
    # Verify all docstrings were parsed correctly
    assert len(parsed_docstrings) == num_iterations
    assert all(d is not None for d in parsed_docstrings)


def test_parsing_stress_with_malformed_input() -> None:
    """Test parser robustness with various malformed inputs."""
    # Collection of potentially problematic inputs
    stress_test_inputs = [
        # Empty and whitespace-only strings
        "",
        "   ",
        "\n\n\n",
        "\t\t\t",
        
        # Very long single lines
        "A" * 10000,
        "Short desc\n" + "B" * 5000,
        
        # Deeply nested indentation
        "Function with deep nesting.\n\nArgs:\n" + "    " * 50 + "param: deep param",
        
        # Mixed line endings
        "Mixed line endings\r\nArgs:\r\n    param1: desc\nReturns:\r    result",
        
        # Unicode edge cases
        "Function with null char: \x00",
        "Function with control chars: \x01\x02\x03",
        "Function with high unicode: \U0001F600\U0001F601\U0001F602",
        
        # Malformed sections
        "Args:\n    param without colon",
        "Args:\n    : description without param name",
        "Args:\n    param (: malformed type annotation",
        "Args:\n    param (type: missing closing paren",
        
        # Inconsistent indentation
        "Function desc\nArgs:\n  param1: desc1\n    param2: desc2\n param3: desc3",
        
        # Very long parameter descriptions
        "Function\nArgs:\n    param: " + "Very long description. " * 1000,
        
        # Circular references in descriptions
        "Self-referencing function.\nArgs:\n    self: This parameter refers to self",
        
        # Special characters in parameter names
        "Function\nArgs:\n    param-with-dashes: desc\n    param_with_underscores: desc",
        
        # Multiple return types
        "Function\nReturns:\n    int: first return\n    str: second return\n    bool: third return",
    ]
    
    successful_parses = 0
    total_time = 0
    
    for i, test_input in enumerate(stress_test_inputs):
        try:
            start_time = time.time()
            result = parse(test_input)
            parse_time = time.time() - start_time
            total_time += parse_time
            
            # Parser should not crash, even with malformed input
            assert result is not None
            successful_parses += 1
            
            # Individual parse should complete quickly even with problematic input
            assert parse_time < 0.1, f"Stress test {i} took {parse_time:.3f}s, too slow"
            
        except Exception as e:
            # Some malformed inputs may legitimately raise ParseError
            # but should not cause crashes or infinite loops
            assert "ParseError" in str(type(e)) or "ValueError" in str(type(e)), \
                f"Unexpected exception type for input {i}: {type(e)}"
    
    # Should successfully parse at least 70% of inputs (some are intentionally malformed)
    success_rate = successful_parses / len(stress_test_inputs)
    assert success_rate > 0.7, f"Success rate {success_rate:.2f} too low"
    
    # Average time per parse should be reasonable even with stress tests
    avg_time = total_time / len(stress_test_inputs)
    assert avg_time < 0.05, f"Average stress test time {avg_time:.4f}s too slow"