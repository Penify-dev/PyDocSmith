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

## Más Ejemplos

### Analizando Docstrings de Estilo NumPy

Analizar una docstring de estilo NumPy:

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

### Analizando desde Objetos Python

Analizar docstrings directamente desde funciones o clases de Python:

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

### Componiendo con Diferentes Estilos

Componer una docstring en un estilo diferente al que se analizó:

```python
from PyDocSmith import compose, DocstringStyle

# Assuming you have a parsed_docstring from previous examples
docstring_text = compose(parsed_docstring, style=DocstringStyle.GOOGLE)
print(docstring_text)
```

## Características avanzadas

- **Analizar desde objeto:** PyDocSmith puede analizar docstrings directamente desde objetos Python, incluyendo clases y módulos, incorporando docstrings de atributos en la representación estructurada.
- **Estilos de renderizado personalizados:** Personalizar el renderizado de docstrings con estilos compactos o detallados, y especificar indentación personalizada para el texto de docstring generado.


