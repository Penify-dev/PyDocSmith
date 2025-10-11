该项目是从原始项目分叉而来的 - https://github.com/rr-/docstring_parser/



# PyDocSmith

PyDocSmith 是一个多功能的 Python 包，专为解析、检测和编写各种样式的文档字符串而设计。它支持多种文档字符串约定，包括 reStructuredText (reST)、Google、NumPydoc 和 Epydoc，为 Python 开发者提供灵活的文档实践。

## 功能

- **文档字符串样式检测：** 使用简单启发式方法自动检测文档字符串的样式（例如，reST、Google、NumPydoc、Epydoc）。
- **文档字符串解析：** 将文档字符串转换为结构化表示，便于分析和操作文档。
- **文档字符串编写：** 将结构化文档字符串重新渲染为文本，允许自动生成和修改文档字符串。
- **属性文档字符串：** 解析在类和模块级别定义的属性文档字符串，增强类属性和模块级变量的文档。

## 安装

```bash
pip install PyDocSmith
```

## 使用

### 检测文档字符串样式

检测给定文本的文档字符串样式：

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

将解析后的文档字符串重新渲染为文本：

```python
from PyDocSmith import compose

docstring_text = compose(parsed_docstring, style=DocstringStyle.REST)
print(docstring_text)
```

## 高级功能

- **从对象解析：** PyDocSmith 可以直接从 Python 对象解析文档字符串，包括类和模块，将属性文档字符串纳入结构化表示。
- **自定义渲染样式：** 使用紧凑或详细样式自定义文档字符串的渲染，并为生成的文档字符串文本指定自定义缩进。

## 与 docstring_parser 相比修改的内容

1. 更好的启发式方法来检测文档字符串样式
2. Google 文档字符串已修改以适应 Notes、Examples
3. 有时 GoogleDoc 字符串没有正确的缩进，特别是从像 GPT 或 Mistral 这样的 LLM 生成时。PyDocSmith 可以修复这些错误的文档字符串。
4. 添加了额外的测试用例以适应不同样式的 GoogleDocstring

我已根据 - https://www.penify.dev 的用例进行了更新

## 贡献

欢迎贡献！请在项目的 GitHub 页面提交拉取请求或报告问题。