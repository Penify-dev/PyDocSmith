Проект является форком оригинального проекта - https://github.com/rr-/docstring_parser/



# PyDocSmith

PyDocSmith - это универсальный пакет Python, предназначенный для анализа, обнаружения и составления docstrings в различных стилях. Он поддерживает несколько соглашений о docstrings, включая reStructuredText (reST), Google, NumPydoc и Epydoc, обеспечивая гибкость в практиках документирования для разработчиков Python.

## Особенности

- **Обнаружение стиля docstring:** Автоматически обнаруживать стиль docstrings (например, reST, Google, NumPydoc, Epydoc) с использованием простых эвристик.
- **Анализ docstrings:** Преобразовывать docstrings в структурированные представления, облегчая анализ и манипуляцию документацией.
- **Составление docstrings:** Рендерить структурированные docstrings обратно в текст, позволяя автоматизированное создание и модификацию docstrings.
- **Docstrings атрибутов:** Анализировать docstrings атрибутов, определенные на уровне классов и модулей, улучшая документацию свойств классов и переменных уровня модуля.

## Установка

```bash
pip install PyDocSmith
```

## Использование

### Обнаружение стиля docstring

Обнаружить стиль docstring данного текста:

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

### Анализ docstrings

Анализировать docstring на его компоненты:

```python
from PyDocSmith import parse, DocstringStyle

parsed_docstring = parse(docstring, style=DocstringStyle.AUTO)
print(parsed_docstring)
```

### Составление docstrings

Рендерить проанализированный docstring обратно в текст:

```python
from PyDocSmith import compose

docstring_text = compose(parsed_docstring, style=DocstringStyle.REST)
print(docstring_text)
```

## Продвинутые особенности

- **Анализ из объекта:** PyDocSmith может анализировать docstrings непосредственно из объектов Python, включая классы и модули, включая docstrings атрибутов в структурированное представление.
- **Пользовательские стили рендеринга:** Настраивать рендеринг docstrings с компактными или детализированными стилями и указывать пользовательский отступ для генерируемого текста docstring.

## Вещи, которые были изменены по сравнению с docstring_parser

1. Лучшие эвристики для обнаружения стиля docstring
2. Google Docstring был изменен для размещения Notes, Examples
3. Иногда GoogleDoc string не имеет правильного отступа, особенно когда генерируется из LLMs вроде GPT или Mistral. PyDocSmith может исправить эти плохие docstrings.
4. Дополнительные тестовые случаи были добавлены для размещения различных стилей GoogleDocstring

Я обновил его на основе случая использования для - https://www.penify.dev

## Вклад

Вклады приветствуются! Пожалуйста, отправляйте pull requests или сообщайте о проблемах на странице проекта GitHub.