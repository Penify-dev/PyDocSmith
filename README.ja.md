このプロジェクトは元のプロジェクトのフォークです - https://github.com/rr-/docstring_parser/



# PyDocSmith

PyDocSmith は、さまざまなスタイルのドックストリングを解析、検出、作成するために設計された多用途の Python パッケージです。reStructuredText (reST)、Google、NumPydoc、Epydoc などの複数のドックストリング規約をサポートし、Python 開発者のドキュメント実践に柔軟性を提供します。

## 機能

- **ドックストリングスタイルの検出：** シンプルなヒューリスティクスを使用してドックストリングのスタイル（例: reST、Google、NumPydoc、Epydoc）を自動的に検出します。
- **ドックストリングの解析：** ドックストリングを構造化表現に変換し、ドキュメントの分析と操作を容易にします。
- **ドックストリングの作成：** 構造化ドックストリングをテキストに戻してレンダリングし、ドックストリングの自動生成と変更を可能にします。
- **属性ドックストリング：** クラスおよびモジュールレベルで定義された属性ドックストリングを解析し、クラスプロパティとモジュールレベル変数のドキュメントを強化します。

## インストール

```bash
pip install PyDocSmith
```

## 使用法

### ドックストリングスタイルの検出

与えられたテキストのドックストリングスタイルを検出します：

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

### ドックストリングの解析

ドックストリングをそのコンポーネントに解析します：

```python
from PyDocSmith import parse, DocstringStyle

parsed_docstring = parse(docstring, style=DocstringStyle.AUTO)
print(parsed_docstring)
```

### ドックストリングの作成

解析されたドックストリングをテキストに戻してレンダリングします：

```python
from PyDocSmith import compose

docstring_text = compose(parsed_docstring, style=DocstringStyle.REST)
print(docstring_text)
```

## さらなる例

### NumPy スタイルの Docstring の解析

NumPy スタイルの docstring を解析します:

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

### Python オブジェクトからの解析

Python の関数やクラスから直接 docstring を解析します:

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

### 異なるスタイルでの構成

解析されたスタイルとは異なるスタイルで docstring を構成します:

```python
from PyDocSmith import compose, DocstringStyle

# Assuming you have a parsed_docstring from previous examples
docstring_text = compose(parsed_docstring, style=DocstringStyle.GOOGLE)
print(docstring_text)
```

### Google スタイル Docstrings の解析

Google スタイルの docstring を解析します:

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

### Epydoc スタイル Docstrings の解析

Epydoc スタイルの docstring を解析します:

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

### クラスからの属性 Docstrings の解析

属性 docstrings を含むクラスから docstrings を解析します:

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

### カスタムインデントでの構成

カスタムインデントで docstring を構成します:

```python
from PyDocSmith import compose, DocstringStyle

# Assuming you have a parsed_docstring from previous examples
docstring_text = compose(parsed_docstring, style=DocstringStyle.REST, indent=4)
print(docstring_text)
```

## 高度な機能

- **オブジェクトからの解析：** PyDocSmith は、クラスやモジュールを含む Python オブジェクトから直接ドックストリングを解析でき、属性ドックストリングを構造化表現に組み込みます。
- **カスタムレンダリングスタイル：** コンパクトまたは詳細なスタイルでドックストリングのレンダリングをカスタマイズし、生成されたドックストリングテキストのカスタムインデントを指定します。


