Проект является форком оригинального проекта - https://github.com/rr-/docstring_parser/



# PyDocSmith

PyDocSmith - это универсальный пакет Python, предназначенный для анализа, обнаружения и составления docstrings в различных стилях. Он поддерживает несколько соглашений о docstrings, включая reStructuredText (reST), Google, NumPydoc и Epydoc, обеспечивая гибкость в практиках документирования для разработчиков Python.

## Особенности

- **Обнаружение стиля docstring:** Автоматически обнаруживает стиль docstrings (например, reST, Google, NumPydoc, Epydoc) с использованием простых эвристик.
- **Анализ docstrings:** Преобразует docstrings в структурированные представления, облегчая анализ и манипуляцию документацией.
- **Составление docstrings:** Рендерит структурированные docstrings обратно в текст, позволяя автоматизированное создание и модификацию docstrings.
- **Docstrings атрибутов:** Анализирует docstrings атрибутов, определенные на уровнях класса и модуля, улучшая документирование свойств класса и переменных уровня модуля.

## Установка

```bash
pip install PyDocSmith
```

## Использование

### Обнаружение стиля docstring

Обнаруживает стиль docstring данного текста:

```python
from PyDocSmith import detect_docstring_style, DocstringStyle

docstring = """
Это пример docstring.
:param param1: Описание param1
:return: Описание возвращаемого значения
"""
style = detect_docstring_style(docstring)
print(style)  # Выводит: DocstringStyle.EPYDOC
```

### Анализ docstrings

Анализирует docstring на его компоненты:

```python
from PyDocSmith import parse, DocstringStyle

parsed_docstring = parse(docstring, style=DocstringStyle.AUTO)
print(parsed_docstring)
```

### Составление docstrings

Рендерит проанализированный docstring обратно в текст:

```python
from PyDocSmith import compose

docstring_text = compose(parsed_docstring, style=DocstringStyle.REST)
print(docstring_text)
```

## Продвинутые особенности

- **Анализ из объекта:** PyDocSmith может анализировать docstrings непосредственно из объектов Python, включая классы и модули, включая docstrings атрибутов в структурированное представление.
- **Пользовательские стили рендеринга:** Настраивает рендеринг docstrings с компактными или детализированными стилями и указывает пользовательскую отступ для сгенерированного текста docstring.

## Вещи, которые были изменены по сравнению с docstring_parser

1. Лучшие эвристики для обнаружения стиля docstring
2. Google Docstring был изменен для размещения Notes, Examples
3. Иногда GoogleDoc string не имеет правильного отступа, особенно когда генерируется из LLMs вроде GPT или Mistral. PyDocSmith может исправить эти плохие docstrings.
4. Были добавлены дополнительные тестовые случаи для размещения другого стиля GoogleDocstring

## Вклад

Вклады приветствуются! Пожалуйста, отправляйте pull requests или сообщайте о проблемах на странице GitHub проекта.