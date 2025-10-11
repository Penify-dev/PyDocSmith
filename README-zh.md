该项目是原始项目的分支 - https://github.com/rr-/docstring_parser/



# PyDocSmith

PyDocSmith 是一个多功能的 Python 包，旨在解析、检测和编写各种风格的 docstrings。它支持多种 docstring 约定，包括 reStructuredText (reST)、Google、NumPydoc 和 Epydoc，为 Python 开发者提供文档实践的灵活性。

## 功能

- **Docstring 风格检测：** 使用简单启发式自动检测 docstrings 的风格（例如，reST、Google、NumPydoc、Epydoc）。
- **Docstring 解析：** 将 docstrings 转换为结构化表示，便于分析和操作文档。
- **Docstring 编写：** 将结构化 docstrings 渲染回文本，允许自动生成和修改 docstrings。
- **属性 Docstrings：** 解析在类和模块级别定义的属性 docstrings，增强类属性和模块级变量的文档。

## 安装

```bash
pip install PyDocSmith
```

## 使用

### Docstring 风格检测

检测给定文本的 docstring 风格：

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

### Docstrings 解析

将 docstring 解析为其组件：

```python
from PyDocSmith import parse, DocstringStyle

parsed_docstring = parse(docstring, style=DocstringStyle.AUTO)
print(parsed_docstring)
```

### Docstrings 编写

将解析的 docstring 渲染回文本：

```python
from PyDocSmith import compose

docstring_text = compose(parsed_docstring, style=DocstringStyle.REST)
print(docstring_text)
```

## 高级功能

- **从对象解析：** PyDocSmith 可以直接从 Python 对象解析 docstrings，包括类和模块，将属性 docstrings 纳入结构化表示。
- **自定义渲染风格：** 使用紧凑或详细风格自定义 docstrings 的渲染，并为生成的 docstring 文本指定自定义缩进。

## 与 docstring_parser 相比修改的事项

1. 更好的启发式来检测 docstring 风格
2. Google Docstring 已修改以适应 Notes、Examples
3. 有时 GoogleDoc string 没有正确的缩进，特别是当从 LLMs 如 GPT 或 Mistral 生成时。PyDocSmith 可以修复这些坏的 docstrings。
4. 添加了额外的测试案例以适应不同风格的 GoogleDocstring

我基于使用案例更新了它 - https://www.penify.dev

## 贡献

欢迎贡献！请在项目的 GitHub 页面提交拉取请求或报告问题。