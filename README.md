The project is a fork from the original project - https://github.com/rr-/docstring_parser/



# PyDocSmith

PyDocSmith is a versatile Python package designed for parsing, detecting, and composing docstrings in various styles. It supports multiple docstring conventions, including reStructuredText (reST), Google, NumPydoc, and Epydoc, providing flexibility in documentation practices for Python developers.

## Features

- **Docstring Style Detection:** Automatically detect the style of docstrings (e.g., reST, Google, NumPydoc, Epydoc) using simple heuristics.
- **Docstring Parsing:** Convert docstrings into structured representations, making it easier to analyze and manipulate documentation.
- **Docstring Composition:** Render structured docstrings back into text, allowing for automated docstring generation and modification.
- **Attribute Docstrings:** Parse attribute docstrings defined at class and module levels, enhancing the documentation of class properties and module-level variables.

## Installation

```bash
pip install PyDocSmith
```

## Usage

### Detecting Docstring Style

Detect the docstring style of a given text:

```python
from PyDocSmith import detect_docstring_style, DocstringStyle

docstring = """
This is an example docstring.
:param param1: Description of param1
:return: Description of return value
"""
style = detect_docstring_style(docstring)
print(style)  # Outputs: DocstringStyle.EPYDOC
```

### Parsing Docstrings

Parse a docstring into its components:

```python
from PyDocSmith import parse, DocstringStyle

parsed_docstring = parse(docstring, style=DocstringStyle.AUTO)
print(parsed_docstring)
```

### Composing Docstrings

Render a parsed docstring back into text:

```python
from PyDocSmith import compose

docstring_text = compose(parsed_docstring, style=DocstringStyle.REST)
print(docstring_text)
```

## More Examples

### Parsing NumPy Style Docstrings

Parse a NumPy-style docstring:

```python
from PyDocSmith import parse, DocstringStyle

docstring = """
Short description

Long description

Parameters
----------
param1 : int
    Description of param1
param2 : str, optional
    Description of param2

Returns
-------
int
    Description of return value
"""

parsed = parse(docstring, style=DocstringStyle.NUMPYDOC)
print(parsed)
```

### Parsing from Python Objects

Parse docstrings directly from Python functions or classes:

```python
from PyDocSmith import parse_from_object

def example_function(param1: int, param2: str = "default") -> int:
    """
    This is an example function.

    Args:
        param1 (int): First parameter
        param2 (str): Second parameter

    Returns:
        int: The result
    """
    return param1 + len(param2)

parsed = parse_from_object(example_function)
print(parsed)
```

### Composing with Different Styles

Compose a docstring in a different style than it was parsed from:

```python
from PyDocSmith import compose, DocstringStyle

# Assuming you have a parsed_docstring from previous examples
docstring_text = compose(parsed_docstring, style=DocstringStyle.GOOGLE)
print(docstring_text)
```

## Advanced Features

- **Parse From Object:** PyDocSmith can parse docstrings directly from Python objects, including classes and modules, incorporating attribute docstrings into the structured representation.
- **Custom Rendering Styles:** Customize the rendering of docstrings with compact or detailed styles, and specify custom indentation for the generated docstring text.



