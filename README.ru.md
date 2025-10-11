Этот проект является форком оригинального проекта - https://github.com/rr-/docstring_parser/

# PyDocSmith

PyDocSmith - это универсальный пакет Python, предназначенный для анализа, обнаружения и составления докстрингов в различных стилях. Он поддерживает несколько соглашений о докстрингах, включая reStructuredText (reST), Google, NumPydoc и Epydoc, обеспечивая гибкость в практиках документирования для разработчиков Python.

## Features

- **Docstring Style Detection:** Автоматически определять стиль докстрингов (например, reST, Google, NumPydoc, Epydoc) с использованием простых эвристик.
- **Docstring Parsing:** Преобразовывать докстринги в структурированные представления, облегчая анализ и манипуляцию документацией.
- **Docstring Composition:** Рендерить структурированные докстринги обратно в текст, позволяя автоматизированную генерацию и модификацию докстрингов.
- **Attribute Docstrings:** Анализировать докстринги атрибутов, определенные на уровне классов и модулей, улучшая документацию свойств классов и переменных уровня модуля.

## Installation

```bash
pip install PyDocSmith
```

## Usage

### Detecting Docstring Style

Определить стиль докстринга данного текста:

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

Разобрать докстринг на его компоненты:

```python
from PyDocSmith import parse, DocstringStyle

parsed_docstring = parse(docstring, style=DocstringStyle.AUTO)
print(parsed_docstring)
```

### Composing Docstrings

Рендерить разобранный докстринг обратно в текст:

```python
from PyDocSmith import compose

docstring_text = compose(parsed_docstring, style=DocstringStyle.REST)
print(docstring_text)
```

## Advanced Features

- **Parse From Object:** PyDocSmith может анализировать докстринги непосредственно из объектов Python, включая классы и модули, включая докстринги атрибутов в структурированное представление.
- **Custom Rendering Styles:** Настраивать рендеринг докстрингов с компактными или детализированными стилями и указывать пользовательский отступ для генерируемого текста докстринга.

## Things that have been modified wrt to docstring_parser

1. Лучшие эвристики для обнаружения стиля докстринга
2. Google Docstring был модифицирован для размещения Notes, Examples
3. Иногда GoogleDoc строка не имеет правильного отступа, особенно когда генерируется из LLMs вроде GPT или Mistral. PyDocSmith может исправить эти плохие докстринги.
4. Дополнительные тестовые случаи были добавлены для размещения другого стиля GoogleDocstring

Я обновил это на основе варианта использования для - https://www.penify.dev

## Contributing

Вклады приветствуются! Пожалуйста, отправляйте pull requests или сообщайте о проблемах на странице проекта GitHub.