该项目是原始项目的分支 - https://github.com/rr-/docstring_parser/

# PyDocSmith

PyDocSmith 是一个多功能的 Python 包，旨在解析、检测和编写各种风格的文档字符串。它支持多种文档字符串约定，包括 reStructuredText (reST)、Google、NumPydoc 和 Epydoc，为 Python 开发者提供文档实践的灵活性。

## Features

- **Docstring Style Detection:** 使用简单启发式自动检测文档字符串的风格（例如，reST、Google、NumPydoc、Epydoc）。
- **Docstring Parsing:** 将文档字符串转换为结构化表示，便于分析和操作文档。
- **Docstring Composition:** 将结构化文档字符串渲染回文本，允许自动生成和修改文档字符串。
- **Attribute Docstrings:** 解析在类和模块级别定义的属性文档字符串，增强类属性和模块级变量的文档。

## Installation

```bash
pip install PyDocSmith
```

## Usage

### Detecting Docstring Style

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

### Parsing Docstrings

将文档字符串解析为其组件：

```python
from PyDocSmith import parse, DocstringStyle

parsed_docstring = parse(docstring, style=DocstringStyle.AUTO)
print(parsed_docstring)
```

### Composing Docstrings

将解析的文档字符串渲染回文本：

```python
from PyDocSmith import compose

docstring_text = compose(parsed_docstring, style=DocstringStyle.REST)
print(docstring_text)
```

## Advanced Features

- **Parse From Object:** PyDocSmith 可以直接从 Python 对象解析文档字符串，包括类和模块，将属性文档字符串纳入结构化表示。
- **Custom Rendering Styles:** 使用紧凑或详细风格自定义文档字符串的渲染，并为生成的文档字符串文本指定自定义缩进。

## Things that have been modified wrt to docstring_parser

1. 更好的启发式来检测文档字符串风格
2. Google Docstring 已被修改以容纳 Notes、Examples
3. 有时 GoogleDoc 字符串没有正确的缩进，特别是当从像 GPT 或 Mistral 这样的 LLMs 生成时。PyDocSmith 可以修复这些坏的文档字符串。
4. 添加了额外的测试案例以容纳不同的 GoogleDocstring 风格

我基于使用案例更新了它 - https://www.penify.dev

## Contributing

欢迎贡献！请在项目的 GitHub 页面上提交拉取请求或报告问题。