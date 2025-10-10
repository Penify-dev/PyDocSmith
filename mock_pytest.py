# Mock pytest module to replace pytest imports
class MockMark:
    @staticmethod
    def parametrize(names, values):
        """Mock pytest.mark.parametrize decorator."""
        def decorator(func):
            # Store the parametrized values on the function
            func._parametrize_values = list(values) if isinstance(values, (list, tuple)) else [values]
            func._parametrize_names = names.split(', ') if isinstance(names, str) else names
            return func
        return decorator

class MockPytest:
    """Mock pytest module to allow test files to run without pytest."""
    
    mark = MockMark()
    
    @staticmethod
    def parametrize(names, values):
        """Mock pytest.parametrize decorator."""
        def decorator(func):
            # Store the parametrized values on the function
            func._parametrize_values = list(values) if isinstance(values, (list, tuple)) else [values]
            func._parametrize_names = names.split(', ') if isinstance(names, str) else names
            return func
        return decorator
    
    @staticmethod
    def raises(exception_type):
        """Mock pytest.raises context manager."""
        class RaisesContext:
            def __enter__(self):
                return self
            def __exit__(self, exc_type, exc_val, exc_tb):
                if exc_type is None:
                    raise AssertionError(f"Expected {exception_type.__name__} but no exception was raised")
                if not issubclass(exc_type, exception_type):
                    raise AssertionError(f"Expected {exception_type.__name__} but got {exc_type.__name__}")
                return True  # Suppress the exception
        return RaisesContext()

# Create the mock module
import sys
sys.modules['pytest'] = MockPytest()
