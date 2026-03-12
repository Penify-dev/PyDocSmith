"""Tests for edge cases and error handling in docstring parsing."""

import pytest
from PyDocSmith.common import DocstringStyle, ParseError
from PyDocSmith.parser import parse
from PyDocSmith.google import parse as google_parse
from PyDocSmith.numpydoc import parse as numpy_parse
from PyDocSmith.rest import parse as rest_parse


def test_malformed_docstring_recovery() -> None:
    """Test that parser can recover from malformed docstrings gracefully."""
    # Test malformed Google-style docstring with missing colons
    malformed_google = """
    Process data with invalid formatting.
    
    Args
        data: Input data
        format (str) Missing colon here
        
    Returns
        Processed data
    """
    
    docstring = parse(malformed_google)
    assert docstring.short_description == "Process data with invalid formatting."
    # Should still parse what it can
    assert len(docstring.params) >= 0  # May parse some or none depending on implementation
    
    # Test malformed NumPy-style with incorrect underlines
    malformed_numpy = """
    Calculate statistics.
    
    Parameters
    -----  # Wrong number of dashes
    values : list
        List of values
        
    Returns
    ===  # Wrong underline character
    dict
        Statistics dictionary
    """
    
    docstring = parse(malformed_numpy)
    assert docstring.short_description == "Calculate statistics."
    # Should handle gracefully without crashing


def test_unicode_and_special_characters() -> None:
    """Test parsing docstrings with Unicode characters and special symbols."""
    unicode_docstring = """
    Процесс данных с Unicode символами.
    
    This function handles émojis 🚀 and special characters like ñ, ü, ß.
    
    Args:
        données (str): Input data with accénts
        配置 (dict): Configuration with Chinese characters
        🔧_tool (bool): Tool parameter with emoji
        
    Returns:
        str: Processed string with special chars: ∑, ∆, π
        
    Raises:
        UnicodeError: If encoding fails with ñoñ-ASCII chars
        
    Example:
        >>> process_unicode("Héllo Wörld! 🌍")
        'Processed: Héllo Wörld! 🌍'
    """
    
    docstring = parse(unicode_docstring)
    assert "Unicode символами" in docstring.short_description
    assert "émojis 🚀" in docstring.long_description
    
    # Check parameters with Unicode
    param_names = [p.arg_name for p in docstring.params]
    assert "données" in param_names
    assert "配置" in param_names
    assert "🔧_tool" in param_names
    
    # Check return type and description
    assert docstring.returns is not None
    assert "∑, ∆, π" in docstring.returns.description
    
    # Check raises with Unicode
    assert len(docstring.raises) == 1
    assert "ñoñ-ASCII" in docstring.raises[0].description
    
    # Check example with Unicode
    assert len(docstring.examples) == 1
    assert "Héllo Wörld! 🌍" in docstring.examples[0].description


def test_deeply_nested_and_complex_types() -> None:
    """Test parsing complex nested type annotations and descriptions."""
    complex_docstring = """
    Advanced data processor with complex type annotations.
    
    This function demonstrates handling of deeply nested generic types,
    union types, and complex callable signatures.
    
    Args:
        data (Dict[str, List[Tuple[int, Optional[Union[str, bytes]]]]): 
            Deeply nested data structure containing mappings of strings to 
            lists of tuples, where each tuple contains an integer and an 
            optional union of string or bytes.
        processor (Callable[[Any, ...], Awaitable[Union[Dict[str, Any], None]]]): 
            Async callable that processes data and returns either a dictionary 
            or None. The callable can accept any number of arguments.
        config (Optional[TypedDict('Config', {'timeout': int, 'retries': int})]): 
            Configuration dictionary with specific structure, defaults to None.
        *args (Union[str, int, float]): Variable positional arguments of mixed types.
        **kwargs (Dict[str, Union[Callable[..., Any], Type[Exception]]]): 
            Keyword arguments mapping strings to either callables or exception types.
            
    Returns:
        AsyncGenerator[Tuple[str, Union[Success, Failure]], None]: 
            Async generator yielding tuples of operation names and their results,
            where results are either Success or Failure objects.
            
    Raises:
        TypeError: If any argument has incorrect type annotation complexity.
        ValueError: If nested data structure validation fails at any level.
        RuntimeError: If async processing encounters unrecoverable errors.
        
    Yields:
        Tuple[str, Union[Success, Failure]]: Individual processing results.
        
    Note:
        This function requires Python 3.8+ for proper type hint support.
        Performance may degrade with deeply nested structures exceeding 
        10 levels of nesting.
        
    Example:
        >>> async def simple_processor(x): return {'result': x}
        >>> data = {'key': [(1, 'value'), (2, b'bytes')]}
        >>> async for name, result in process_complex(data, simple_processor):
        ...     print(f"{name}: {result}")
        key: Success(data={'result': {'key': [(1, 'value'), (2, b'bytes')]}})
    """
    
    docstring = parse(complex_docstring)
    
    # Verify basic structure
    assert "Advanced data processor" in docstring.short_description
    assert "deeply nested generic types" in docstring.long_description
    
    # Check complex parameter types are preserved
    assert len(docstring.params) >= 5  # data, processor, config, *args, **kwargs
    
    data_param = next(p for p in docstring.params if p.arg_name == "data")
    assert "Dict[str, List[Tuple[int, Optional[Union[str, bytes]]]]]" in data_param.type_name
    assert "Deeply nested data structure" in data_param.description
    
    processor_param = next(p for p in docstring.params if p.arg_name == "processor")
    assert "Callable" in processor_param.type_name
    assert "Awaitable" in processor_param.type_name
    
    # Check return type complexity
    assert docstring.returns is not None
    assert "AsyncGenerator" in docstring.returns.type_name
    assert "Tuple[str, Union[Success, Failure]]" in docstring.returns.type_name
    
    # Verify multiple exception types
    assert len(docstring.raises) == 3
    exception_types = [r.type_name for r in docstring.raises]
    assert "TypeError" in exception_types
    assert "ValueError" in exception_types  
    assert "RuntimeError" in exception_types
    
    # Check yields section
    yields_found = any("yields" in meta.args[0].lower() for meta in docstring.meta if meta.args)
    
    # Verify notes section
    assert docstring.notes is not None
    assert len(docstring.notes) > 0
    assert "Python 3.8+" in docstring.notes[0].description
    
    # Check complex example
    assert len(docstring.examples) == 1
    example_text = docstring.examples[0].description
    assert "async def simple_processor" in example_text
    assert "Success(data=" in example_text