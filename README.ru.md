Этот проект является форком оригинального проекта - https://github.com/rr-/docstring_parser/



# PyDocSmith

PyDocSmith - это универсальный пакет Python, предназначенный для анализа, обнаружения и составления докстрингов в различных стилях. Он поддерживает несколько соглашений о докстрингах, включая reStructuredText (reST), Google, NumPydoc и Epydoc, обеспечивая гибкость в практиках документирования для разработчиков Python.

## Особенности

- **Обнаружение стиля докстринга:** Автоматически обнаруживать стиль докстрингов (например, reST, Google, NumPydoc, Epydoc) с использованием простых эвристик.
- **Анализ докстрингов:** Преобразовывать докстринги в структурированные представления, облегчая анализ и манипуляцию документацией.
- **Составление докстрингов:** Рендерить структурированные докстринги обратно в текст, позволяя автоматизированное создание и модификацию докстрингов.
- **Докстринги атрибутов:** Анализировать докстринги атрибутов, определенные на уровне классов и модулей, улучшая документирование свойств классов и переменных уровня модуля.

## Установка

```bash
pip install PyDocSmith
```

## Использование

### Обнаружение стиля докстринга

Обнаружить стиль докстринга данного текста:

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

### Анализ докстрингов

Разобрать докстринг на его компоненты:

```python
from PyDocSmith import parse, DocstringStyle

parsed_docstring = parse(docstring, style=DocstringStyle.AUTO)
print(parsed_docstring)
```

### Составление докстрингов

Рендерить разобранный докстринг обратно в текст:

```python
from PyDocSmith import compose

docstring_text = compose(parsed_docstring, style=DocstringStyle.REST)
print(docstring_text)
```

## Дополнительные примеры

### Парсинг Docstring в стиле NumPy

Разобрать docstring в стиле NumPy:

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

### Парсинг из объектов Python

Разобрать docstring напрямую из функций или классов Python:

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

### Составление с разными стилями

Составить docstring в стиле, отличном от того, в котором он был проанализирован:

```python
from PyDocSmith import compose, DocstringStyle

# Assuming you have a parsed_docstring from previous examples
docstring_text = compose(parsed_docstring, style=DocstringStyle.GOOGLE)
print(docstring_text)
```

### Разбор Docstrings в стиле Google

Разобрать docstring в стиле Google:

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

### Разбор Docstrings в стиле Epydoc

Разобрать docstring в стиле Epydoc:

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

### Разбор Docstrings атрибутов из класса

Разобрать docstrings из класса, включая docstrings атрибутов:

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

### Составление с пользовательским отступом

Составить docstring с пользовательским отступом:

```python
from PyDocSmith import compose, DocstringStyle

# Assuming you have a parsed_docstring from previous examples
docstring_text = compose(parsed_docstring, style=DocstringStyle.REST, indent=4)
print(docstring_text)
```

## Продвинутые особенности

- **Анализ из объекта:** PyDocSmith может анализировать докстринги непосредственно из объектов Python, включая классы и модули, включая докстринги атрибутов в структурированное представление.
- **Пользовательские стили рендеринга:** Настраивать рендеринг докстрингов с компактными или детализированными стилями и указывать пользовательский отступ для генерируемого текста докстринга.


