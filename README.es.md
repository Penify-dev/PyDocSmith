El proyecto es un fork del proyecto original - https://github.com/rr-/docstring_parser/



# PyDocSmith

PyDocSmith es un paquete Python versátil diseñado para analizar, detectar y componer docstrings en varios estilos. Soporta múltiples convenciones de docstrings, incluyendo reStructuredText (reST), Google, NumPydoc y Epydoc, proporcionando flexibilidad en las prácticas de documentación para desarrolladores de Python.

## Características

- **Detección de estilo de docstring:** Detectar automáticamente el estilo de docstrings (por ejemplo, reST, Google, NumPydoc, Epydoc) usando heurísticas simples.
- **Análisis de docstrings:** Convertir docstrings en representaciones estructuradas, facilitando el análisis y manipulación de la documentación.
- **Composición de docstrings:** Renderizar docstrings estructuradas de vuelta a texto, permitiendo la generación y modificación automatizada de docstrings.
- **Docstrings de atributos:** Analizar docstrings de atributos definidos a nivel de clase y módulo, mejorando la documentación de propiedades de clase y variables a nivel de módulo.

## Instalación

```bash
pip install PyDocSmith
```

## Uso

### Detección de estilo de docstring

Detectar el estilo de docstring de un texto dado:

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

### Análisis de docstrings

Analizar una docstring en sus componentes:

```python
from PyDocSmith import parse, DocstringStyle

parsed_docstring = parse(docstring, style=DocstringStyle.AUTO)
print(parsed_docstring)
```

### Composición de docstrings

Renderizar una docstring analizada de vuelta a texto:

```python
from PyDocSmith import compose

docstring_text = compose(parsed_docstring, style=DocstringStyle.REST)
print(docstring_text)
```

## Características avanzadas

- **Analizar desde objeto:** PyDocSmith puede analizar docstrings directamente desde objetos Python, incluyendo clases y módulos, incorporando docstrings de atributos en la representación estructurada.
- **Estilos de renderizado personalizados:** Personalizar el renderizado de docstrings con estilos compactos o detallados, y especificar indentación personalizada para el texto de docstring generado.


