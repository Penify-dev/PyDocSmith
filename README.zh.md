该项目是原始项目的分支 - https://github.com/rr-/docstring_parser/



# PyDocSmith

PyDocSmith 是一个多功能的 Python 包，旨在解析、检测和编写各种风格的文档字符串。它支持多种文档字符串约定，包括 reStructuredText (reST)、Google、NumPydoc 和 Epydoc，为 Python 开发者提供文档实践的灵活性。

## 功能

- **文档字符串风格检测：** 使用简单启发式自动检测文档字符串的风格（例如，reST、Google、NumPydoc、Epydoc）。
- **文档字符串解析：** 将文档字符串转换为结构化表示，便于分析和操作文档。
- **文档字符串编写：** 将结构化文档字符串渲染回文本，允许自动生成和修改文档字符串。
- **属性文档字符串：** 解析在类和模块级别定义的属性文档字符串，增强类属性和模块级变量的文档。

## 安装

```bash
pip install PyDocSmith
```

## 使用

### 检测文档字符串风格

检测给定文本的文档字符串风格：

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

### 解析文档字符串

将文档字符串解析为其组件：

```python
from PyDocSmith import parse, DocstringStyle

parsed_docstring = parse(docstring, style=DocstringStyle.AUTO)
print(parsed_docstring)
```

### 编写文档字符串

将解析的文档字符串渲染回文本：

```python
from PyDocSmith import compose

docstring_text = compose(parsed_docstring, style=DocstringStyle.REST)
print(docstring_text)
```

## 更多示例

### 解析 NumPy 风格的 Docstring

解析 NumPy 风格的 docstring:

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

### 从 Python 对象解析

直接从 Python 函数或类解析 docstring:

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

### 使用不同风格组合

以不同于解析的风格组合 docstring:

```python
from PyDocSmith import compose, DocstringStyle

# Assuming you have a parsed_docstring from previous examples
docstring_text = compose(parsed_docstring, style=DocstringStyle.GOOGLE)
print(docstring_text)
```

### 解析 Google 风格 Docstrings

解析 Google 风格的 docstring:

```python
from PyDocSmith import parse, DocstringStyle

docstring = """
Short description.

Long description.

Args:
    param1 (int): Description of param1
    param2 (str, optional): Description of param2

Returns:
    int: Description of return value
"""

parsed = parse(docstring, style=DocstringStyle.GOOGLE)
print(parsed)
```

### 解析 Epydoc 风格 Docstrings

解析 Epydoc 风格的 docstring:

```python
from PyDocSmith import parse, DocstringStyle

docstring = """
Short description.

@param param1: Description of param1
@type param1: int
@param param2: Description of param2
@type param2: str
@return: Description of return value
@rtype: int
"""

parsed = parse(docstring, style=DocstringStyle.EPYDOC)
print(parsed)
```

### 从类解析属性 Docstrings

从包含属性 docstrings 的类解析 docstrings:

```python
from PyDocSmith import parse_from_object

class ExampleClass:
    """Class docstring."""

    attr1: int
    """Attribute 1 description."""

    attr2: str = "default"
    """Attribute 2 description."""

    def method(self):
        pass

parsed = parse_from_object(ExampleClass)
print(parsed)
```

### 使用自定义缩进进行组合

使用自定义缩进组合 docstring:

```python
from PyDocSmith import compose, DocstringStyle

# Assuming you have a parsed_docstring from previous examples
docstring_text = compose(parsed_docstring, style=DocstringStyle.REST, indent=4)
print(docstring_text)
```

## 高级功能

- **从对象解析：** PyDocSmith 可以直接从 Python 对象解析文档字符串，包括类和模块，将属性文档字符串纳入结构化表示。
- **自定义渲染风格：** 使用紧凑或详细风格自定义文档字符串的渲染，并为生成的文档字符串文本指定自定义缩进。


