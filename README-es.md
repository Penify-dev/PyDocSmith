El proyecto es un fork del proyecto original - https://github.com/rr-/docstring_parser/



# PyDocSmith

PyDocSmith es un paquete Python versátil diseñado para analizar, detectar y componer docstrings en varios estilos. Soporta múltiples convenciones de docstring, incluyendo reStructuredText (reST), Google, NumPydoc y Epydoc, proporcionando flexibilidad en las prácticas de documentación para desarrolladores Python.

## Características

- **Detección de estilo de docstring:** Detecta automáticamente el estilo de los docstrings (por ejemplo, reST, Google, NumPydoc, Epydoc) usando heurísticas simples.
- **Análisis de docstrings:** Convierte docstrings en representaciones estructuradas, facilitando el análisis y manipulación de la documentación.
- **Composición de docstrings:** Renderiza docstrings estructuradas de vuelta a texto, permitiendo la generación y modificación automatizada de docstrings.
- **Docstrings de atributos:** Analiza docstrings de atributos definidos en niveles de clase y módulo, mejorando la documentación de propiedades de clase y variables a nivel de módulo.

## Instalación

```bash
pip install PyDocSmith
```

## Uso

### Detección de estilo de docstring

Detecta el estilo de docstring de un texto dado:

```python
from PyDocSmith import detect_docstring_style, DocstringStyle

docstring = """
Este es un ejemplo de docstring.
:param param1: Descripción de param1
:return: Descripción del valor de retorno
"""
style = detect_docstring_style(docstring)
print(style)  # Muestra: DocstringStyle.EPYDOC
```

### Análisis de docstrings

Analiza una docstring en sus componentes:

```python
from PyDocSmith import parse, DocstringStyle

parsed_docstring = parse(docstring, style=DocstringStyle.AUTO)
print(parsed_docstring)
```

### Composición de docstrings

Renderiza una docstring analizada de vuelta a texto:

```python
from PyDocSmith import compose

docstring_text = compose(parsed_docstring, style=DocstringStyle.REST)
print(docstring_text)
```

### Análisis de docstring de Google con Notas y Ejemplos

Detecta el estilo de docstring de un texto dado que contiene Notas y Ejemplos:

```python
from PyDocSmith import parse, DocstringStyle

docstring = """
Esta función hace algo.

Args:
    param1 (str): Descripción de param1

Returns:
    str: Descripción del valor de retorno

Notes:
    Esta es una nota.

Examples:
    >>> func('hello')
    'hello world'
"""

parsed = parse(docstring, style=DocstringStyle.GOOGLE)
print(parsed)
```

### Análisis de docstrings desde un objeto

Analiza docstrings desde objetos Python:

```python
from PyDocSmith import parse_from_object

class MyClass:
    """Esta es una docstring de clase."""

    attr: str
    """Esta es una docstring de atributo."""

parsed = parse_from_object(MyClass)
print(parsed)
```

### Composición de docstrings con indentación personalizada

Renderiza una docstring analizada con indentación personalizada:

```python
from PyDocSmith import compose

# Asumiendo que parsed_docstring está disponible
docstring_text = compose(parsed_docstring, style=DocstringStyle.GOOGLE, indent='    ')
print(docstring_text)
```

## Características avanzadas

- **Analizar desde objeto:** PyDocSmith puede analizar docstrings directamente desde objetos Python, incluyendo clases y módulos, incorporando docstrings de atributos en la representación estructurada.
- **Estilos de renderizado personalizados:** Personaliza el renderizado de docstrings con estilos compactos o detallados, y especifica indentación personalizada para el texto de docstring generado.

## Cosas que han sido modificadas con respecto a docstring_parser

1. Mejores heurísticas para detectar el estilo de docstring
2. La docstring de Google ha sido modificada para acomodar Notas, Ejemplos
3. A veces la docstring de Google no tiene una indentación adecuada, especialmente cuando se genera desde LLMs como GPT o Mistral. PyDocSmith puede corregir esas malas docstrings.
4. Se agregaron casos de prueba adicionales para acomodar un estilo diferente de GoogleDocstring

## Contribuyendo

¡Las contribuciones son bienvenidas! Por favor, envíe pull requests o reporte problemas en la página de GitHub del proyecto.