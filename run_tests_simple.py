#!/usr/bin/env python3
"""Simple test runner to identify failing test cases without pytest."""
import sys
import os
import traceback
from pathlib import Path

# Add PyDocSmith to path 
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

# Import mock pytest before any test modules
import mock_pytest

def run_test_file(test_file_path):
    """Import and run a test file, catching errors."""
    print(f"\n{'='*60}")
    print(f"Testing: {test_file_path}")
    print(f"{'='*60}")
    
    try:
        # Import the module
        module_name = os.path.basename(test_file_path)[:-3]  # Remove .py
        spec = __import__(f"PyDocSmith.tests.{module_name}", fromlist=[''])
        
        # Find test functions
        test_functions = [name for name in dir(spec) if name.startswith('test_')]
        
        print(f"Found {len(test_functions)} test functions")
        
        failures = []
        successes = []
        
        for test_func_name in test_functions:
            try:
                test_func = getattr(spec, test_func_name)
                if callable(test_func):
                    print(f"  Running {test_func_name}...", end=" ")
                    
                    # Check if function has parametrized values
                    if hasattr(test_func, '_parametrize_values'):
                        # Run for each parametrized set
                        param_failures = 0
                        param_successes = 0
                        for i, values in enumerate(test_func._parametrize_values):
                            try:
                                if isinstance(values, (list, tuple)):
                                    test_func(*values)
                                else:
                                    test_func(values)
                                param_successes += 1
                            except Exception as e:
                                param_failures += 1
                        
                        if param_failures == 0:
                            print(f"PASS ({param_successes} variations)")
                            successes.append(test_func_name)
                        else:
                            print(f"FAIL ({param_failures}/{param_successes + param_failures} variations failed)")
                            failures.append((test_func_name, f"{param_failures} parametrized tests failed", ""))
                    else:
                        test_func()
                        print("PASS")
                        successes.append(test_func_name)
            except Exception as e:
                print(f"FAIL - {str(e)}")
                failures.append((test_func_name, str(e), traceback.format_exc()))
                
        print(f"\nResults for {test_file_path}:")
        print(f"  Passed: {len(successes)}")
        print(f"  Failed: {len(failures)}")
        
        if failures:
            print("\nFailures:")
            for func_name, error, tb in failures:
                print(f"  {func_name}: {error}")
                
        return failures
        
    except Exception as e:
        print(f"Failed to import module: {e}")
        traceback.print_exc()
        return [(f"import_{module_name}", str(e), traceback.format_exc())]

def main():
    test_dir = Path("PyDocSmith/tests")
    test_files = list(test_dir.glob("test_*.py"))
    
    all_failures = []
    
    for test_file in test_files:
        failures = run_test_file(str(test_file))
        all_failures.extend(failures)
    
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"Total failures: {len(all_failures)}")
    
    return len(all_failures) > 0

if __name__ == "__main__":
    sys.exit(main())
