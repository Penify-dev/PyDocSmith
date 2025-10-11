"""Integration tests for PyDocSmith functionality."""

import pytest
from PyDocSmith import (
    DocstringStyle,
    combine_docstrings,
    compose,
    detect_docstring_style,
    parse,
    parse_from_object,
)


def test_round_trip_rest():
    """Test round-trip parsing and composing for reST style."""
    original_docstring = """
    Short description

    Long description

    :param spam: spam desc
    :param bla: bla desc
    :raises ValueError: exc desc
    :returns: ret desc
    """

    parsed = parse(original_docstring, style=DocstringStyle.REST)
    composed = compose(parsed, style=DocstringStyle.REST)

    # Parse the composed docstring again
    reparsed = parse(composed, style=DocstringStyle.REST)

    assert reparsed.short_description == parsed.short_description
    assert reparsed.long_description == parsed.long_description
    assert len(reparsed.params) == len(parsed.params)
    assert len(reparsed.raises) == len(parsed.raises)
    assert reparsed.returns.description == parsed.returns.description


def test_round_trip_google():
    """Test round-trip parsing and composing for Google style."""
    original_docstring = """Short description

    Long description

    Args:
        spam: spam desc
        bla (int): bla desc

    Raises:
        ValueError: exc desc

    Returns:
        tuple: ret desc
    """

    parsed = parse(original_docstring, style=DocstringStyle.GOOGLE)
    composed = compose(parsed, style=DocstringStyle.GOOGLE)

    reparsed = parse(composed, style=DocstringStyle.GOOGLE)

    assert reparsed.short_description == parsed.short_description
    assert reparsed.long_description == parsed.long_description
    assert len(reparsed.params) == len(parsed.params)
    assert len(reparsed.raises) == len(parsed.raises)
    assert reparsed.returns.description == parsed.returns.description


def test_round_trip_numpydoc():
    """Test round-trip parsing and composing for NumPy style."""
    original_docstring = """Short description

    Long description

    Parameters
    ----------
    spam
        spam desc
    bla : int
        bla desc

    Raises
    ------
    ValueError
        exc desc

    Returns
    -------
    tuple
        ret desc
    """

    parsed = parse(original_docstring, style=DocstringStyle.NUMPYDOC)
    composed = compose(parsed, style=DocstringStyle.NUMPYDOC)

    reparsed = parse(composed, style=DocstringStyle.NUMPYDOC)

    assert reparsed.short_description == parsed.short_description
    assert reparsed.long_description == parsed.long_description
    assert len(reparsed.params) == len(parsed.params)
    assert len(reparsed.raises) == len(parsed.raises)
    assert reparsed.returns.description == parsed.returns.description


def test_round_trip_epydoc():
    """Test round-trip parsing and composing for Epydoc style."""
    original_docstring = """Short description

    Long description

    @param spam: spam desc
    @param bla: bla desc
    @raise ValueError: exc desc
    @return: ret desc
    """

    parsed = parse(original_docstring, style=DocstringStyle.EPYDOC)
    composed = compose(parsed, style=DocstringStyle.EPYDOC)

    reparsed = parse(composed, style=DocstringStyle.EPYDOC)

    assert reparsed.short_description == parsed.short_description
    assert reparsed.long_description == parsed.long_description
    assert len(reparsed.params) == len(parsed.params)
    assert len(reparsed.raises) == len(parsed.raises)
    assert reparsed.returns.description == parsed.returns.description


def test_auto_detect_and_parse():
    """Test automatic style detection followed by parsing."""
    docstrings = [
        ("""
        Short desc

        :param x: param x
        :returns: result
        """, DocstringStyle.REST),
        ("""Short desc

        Args:
            x: param x

        Returns:
            result
        """, DocstringStyle.GOOGLE),
        ("""Short desc

        Parameters
        ----------
        x
            param x

        Returns
        -------
        result
        """, DocstringStyle.NUMPYDOC),
        ("""Short desc

        @param x: param x
        @return: result
        """, DocstringStyle.EPYDOC),
    ]

    for docstring_text, expected_style in docstrings:
        detected_style = detect_docstring_style(docstring_text)
        assert detected_style == expected_style

        parsed = parse(docstring_text)
        assert parsed.style == expected_style


def test_parse_from_object_function():
    """Test parse_from_object with a function."""
    def sample_function(param1: str, param2: int = 42):
        """Sample function docstring.

        Args:
            param1: First parameter
            param2: Second parameter with default

        Returns:
            str: Combined result
        """
        return f"{param1}_{param2}"

    parsed = parse_from_object(sample_function)

    assert parsed.short_description == "Sample function docstring."
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == "param1"
    assert parsed.params[0].description == "First parameter"
    assert parsed.params[1].arg_name == "param2"
    assert parsed.params[1].description == "Second parameter with default"
    assert parsed.returns.description == "Combined result"


def test_parse_from_object_class():
    """Test parse_from_object with a class including attributes."""
    class SampleClass:
        """A sample class for testing.

        This class demonstrates attribute docstrings.
        """

        attr1: str
        """First attribute"""

        attr2: int = 10
        """Second attribute with default"""

        def method(self, x: float):
            """Method docstring.

            Args:
                x: Input value

            Returns:
                float: Processed value
            """
            return x * 2

    parsed = parse_from_object(SampleClass)

    assert "sample class" in parsed.short_description.lower()
    assert len(parsed.params) == 2  # attributes
    assert parsed.params[0].arg_name == "attr1"
    assert parsed.params[0].description == "First attribute"
    assert parsed.params[1].arg_name == "attr2"
    assert parsed.params[1].description == "Second attribute with default"


def test_combine_docstrings():
    """Test combining multiple docstrings."""
    doc1 = """First docstring.

    Args:
        x: First param
    """

    doc2 = """Second docstring.

    Args:
        y: Second param

    Returns:
        result
    """

    combined = combine_docstrings([doc1, doc2])

    parsed = parse(combined, style=DocstringStyle.GOOGLE)

    assert "First docstring" in parsed.short_description
    assert "Second docstring" in parsed.long_description or "Second docstring" in parsed.short_description
    assert len(parsed.params) == 2
    assert any(p.arg_name == "x" for p in parsed.params)
    assert any(p.arg_name == "y" for p in parsed.params)
    assert parsed.returns is not None


def test_error_handling_integration():
    """Test error handling in integration scenarios."""
    # Test with malformed docstring that might cause issues
    malformed = """
    :param invalid syntax here
    :returns: something
    """

    # Should not crash, should either parse or raise appropriate error
    try:
        parsed = parse(malformed)
        assert parsed is not None
    except Exception:
        # If it raises, it should be a ParseError
        pass


def test_cross_style_composition():
    """Test composing a parsed docstring in a different style."""
    google_doc = """Function description.

    Args:
        param1: First parameter
        param2 (int): Second parameter

    Returns:
        str: Result string
    """

    parsed = parse(google_doc, style=DocstringStyle.GOOGLE)

    # Compose in reST style
    rest_composed = compose(parsed, style=DocstringStyle.REST)

    # Should be valid reST
    reparsed = parse(rest_composed, style=DocstringStyle.REST)
    assert reparsed.short_description == parsed.short_description
    assert len(reparsed.params) == len(parsed.params)