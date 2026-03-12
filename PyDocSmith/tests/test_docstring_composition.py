"""Tests for docstring composition and formatting functionality."""

import pytest
from PyDocSmith.common import DocstringStyle, RenderingStyle
from PyDocSmith.parser import parse
from PyDocSmith.google import compose as google_compose
from PyDocSmith.numpydoc import compose as numpy_compose
from PyDocSmith.rest import compose as rest_compose


def test_cross_format_conversion() -> None:
    """Test converting docstrings between different formats."""
    # Original Google-style docstring
    google_docstring = """
    Calculate the area of geometric shapes.
    
    This function supports multiple geometric shapes including
    circles, rectangles, and triangles.
    
    Args:
        shape (str): Type of shape ('circle', 'rectangle', 'triangle')
        dimensions (Dict[str, float]): Shape-specific dimensions
        precision (int, optional): Decimal precision. Defaults to 2.
        
    Returns:
        float: Calculated area rounded to specified precision
        
    Raises:
        ValueError: If shape type is not supported
        TypeError: If dimensions are not numeric
        
    Example:
        >>> calculate_area('circle', {'radius': 5.0})
        78.54
        >>> calculate_area('rectangle', {'width': 4, 'height': 3})
        12.0
    """
    
    # Parse the Google docstring
    parsed = parse(google_docstring)
    assert parsed.style == DocstringStyle.GOOGLE
    
    # Verify parsed content
    assert "Calculate the area" in parsed.short_description
    assert len(parsed.params) == 3
    assert parsed.params[0].arg_name == "shape"
    assert parsed.params[1].arg_name == "dimensions"
    assert parsed.params[2].arg_name == "precision"
    assert parsed.params[2].is_optional
    assert parsed.params[2].default == "2"
    
    assert parsed.returns is not None
    assert parsed.returns.type_name == "float"
    
    assert len(parsed.raises) == 2
    assert len(parsed.examples) == 1
    
    # Test composition back to Google format
    recomposed_google = google_compose(parsed)
    assert "Args:" in recomposed_google
    assert "Returns:" in recomposed_google
    assert "Raises:" in recomposed_google
    
    # Test composition to NumPy format
    recomposed_numpy = numpy_compose(parsed)
    assert "Parameters" in recomposed_numpy
    assert "----------" in recomposed_numpy
    assert "Returns" in recomposed_numpy
    
    # Test composition to ReST format
    recomposed_rest = rest_compose(parsed)
    assert ":param shape:" in recomposed_rest
    assert ":returns:" in recomposed_rest
    assert ":raises ValueError:" in recomposed_rest


def test_rendering_styles() -> None:
    """Test different rendering styles for docstring composition."""
    docstring_text = """
    Process user input with validation.
    
    Args:
        user_input (str): Raw input from user
        strict_mode (bool, optional): Enable strict validation. Defaults to False.
        
    Returns:
        Dict[str, Any]: Processed and validated input data
    """
    
    parsed = parse(docstring_text)
    
    # Test COMPACT rendering style
    compact = google_compose(parsed, rendering_style=RenderingStyle.COMPACT)
    # Compact should have minimal spacing
    lines = compact.split('\n')
    # Should not have extra blank lines between sections
    consecutive_blanks = 0
    max_consecutive_blanks = 0
    for line in lines:
        if line.strip() == '':
            consecutive_blanks += 1
            max_consecutive_blanks = max(max_consecutive_blanks, consecutive_blanks)
        else:
            consecutive_blanks = 0
    assert max_consecutive_blanks <= 1  # At most one blank line between sections
    
    # Test CLEAN rendering style  
    clean = google_compose(parsed, rendering_style=RenderingStyle.CLEAN)
    # Clean should normalize optional parameter formatting
    assert "(bool, optional)" in clean or "(bool?)" in clean
    
    # Test EXPANDED rendering style
    expanded = google_compose(parsed, rendering_style=RenderingStyle.EXPANDED)
    # Expanded should have more detailed formatting
    assert "user_input" in expanded
    assert "strict_mode" in expanded


def test_docstring_roundtrip_fidelity() -> None:
    """Test that parsing and composing preserves docstring information."""
    original_docstrings = [
        # Google style with complex formatting
        """
        Advanced machine learning model trainer.
        
        This class provides comprehensive training capabilities for various
        machine learning models with support for:
        
        - Custom loss functions
        - Learning rate scheduling  
        - Early stopping mechanisms
        - Distributed training
        
        Args:
            model (torch.nn.Module): PyTorch model to train
            optimizer (torch.optim.Optimizer): Optimization algorithm
            loss_fn (Callable[[Tensor, Tensor], Tensor]): Loss function
            scheduler (Optional[torch.optim.lr_scheduler._LRScheduler]): 
                Learning rate scheduler, defaults to None
            early_stopping (bool, optional): Enable early stopping. Defaults to True.
            patience (int, optional): Early stopping patience. Defaults to 10.
            
        Returns:
            TrainingResults: Object containing training metrics and model state
            
        Raises:
            ValueError: If model and optimizer are incompatible
            RuntimeError: If training fails due to hardware constraints
            
        Yields:
            EpochResults: Results from each training epoch
            
        Note:
            Requires CUDA-compatible GPU for optimal performance.
            Memory usage scales with batch size and model complexity.
            
        Example:
            >>> trainer = ModelTrainer(model, optimizer, loss_fn)
            >>> results = trainer.train(train_loader, epochs=100)
            >>> print(f"Final accuracy: {results.accuracy:.2f}")
        """,
        
        # NumPy style with detailed sections
        """
        Compute statistical measures for time series data.
        
        Parameters
        ----------
        data : numpy.ndarray
            Time series data array
        window_size : int, optional
            Rolling window size, by default 30
        method : {'mean', 'median', 'std'}, optional
            Statistical method to apply, by default 'mean'
            
        Returns
        -------
        numpy.ndarray
            Array of computed statistical measures
            
        Raises
        ------
        ValueError
            If window_size is larger than data length
        TypeError
            If data is not a numeric array
            
        See Also
        --------
        pandas.DataFrame.rolling : Similar functionality for DataFrames
        numpy.convolve : For custom convolution operations
        
        Examples
        --------
        >>> data = np.random.randn(100)
        >>> stats = compute_stats(data, window_size=10, method='mean')
        >>> len(stats) == len(data) - 9
        True
        """
    ]
    
    for original in original_docstrings:
        # Parse the original
        parsed = parse(original)
        
        # Compose back to string
        if parsed.style == DocstringStyle.GOOGLE:
            recomposed = google_compose(parsed)
        elif parsed.style == DocstringStyle.NUMPYDOC:
            recomposed = numpy_compose(parsed)
        else:
            recomposed = rest_compose(parsed)
        
        # Parse the recomposed version
        reparsed = parse(recomposed)
        
        # Verify key information is preserved
        assert parsed.short_description == reparsed.short_description
        assert len(parsed.params) == len(reparsed.params)
        
        # Check parameter details are preserved
        for orig_param, reparsed_param in zip(parsed.params, reparsed.params):
            assert orig_param.arg_name == reparsed_param.arg_name
            assert orig_param.type_name == reparsed_param.type_name
            assert orig_param.is_optional == reparsed_param.is_optional
        
        # Check returns information
        if parsed.returns and reparsed.returns:
            assert parsed.returns.type_name == reparsed.returns.type_name
        
        # Check raises information  
        assert len(parsed.raises) == len(reparsed.raises)
        for orig_raise, reparsed_raise in zip(parsed.raises, reparsed.raises):
            assert orig_raise.type_name == reparsed_raise.type_name
        
        # Check examples are preserved
        assert len(parsed.examples) == len(reparsed.examples)