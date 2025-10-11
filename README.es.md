El proyecto es un fork del proyecto original - https://github.com/rr-/docstring_parser/

# PyDocSmith

PyDocSmith es un paquete Python versátil diseñado para analizar, detectar y componer docstrings en varios estilos. Soporta múltiples convenciones de docstrings, incluyendo reStructuredText (reST), Google, NumPydoc y Epydoc, proporcionando flexibilidad en las prácticas de documentación para desarrolladores de Python.

## Features

- **Docstring Style Detection:** Detectar automáticamente el estilo de los docstrings (por ejemplo, reST, Google, NumPydoc, Epydoc) usando heurísticas simples.
- **Docstring Parsing:** Convertir docstrings en representaciones estructuradas, facilitando el análisis y manipulación de la documentación.
- **Docstring Composition:** Renderizar docstrings estructuradas de vuelta a texto, permitiendo la generación y modificación automatizada de docstrings.
- **Attribute Docstrings:** Analizar docstrings de atributos definidos a nivel de clase y módulo, mejorando la documentación de propiedades de clase y variables a nivel de módulo.

## Installation

```bash
pip install PyDocSmith
```

## Usage

### Detecting Docstring Style

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

### Parsing Docstrings

Analizar un docstring en sus componentes:

```python
from PyDocSmith import parse, DocstringStyle

parsed_docstring = parse(docstring, style=DocstringStyle.AUTO)
print(parsed_docstring)
```

### Composing Docstrings

Renderizar un docstring analizado de vuelta a texto:

```python
from PyDocSmith import compose

docstring_text = compose(parsed_docstring, style=DocstringStyle.REST)
print(docstring_text)
```

## Advanced Features

- **Parse From Object:** PyDocSmith puede analizar docstrings directamente desde objetos Python, incluyendo clases y módulos, incorporando docstrings de atributos en la representación estructurada.
- **Custom Rendering Styles:** Personalizar el renderizado de docstrings con estilos compactos o detallados, y especificar indentación personalizada para el texto de docstring generado.

## Things that have been modified wrt to docstring_parser

1. Mejores heurísticas para detectar el estilo de docstring
2. Google Docstring ha sido modificado para acomodar Notes, Examples
3. A veces la cadena GoogleDoc no tiene indentación apropiada, especialmente cuando se genera desde LLMs como GPT o Mistral. PyDocSmith puede corregir esas malas docstrings.
4. Casos de prueba adicionales fueron añadidos para acomodar un estilo diferente de GoogleDocstring

He actualizado esto basado en el caso de uso para - https://www.penify.dev

## Contributing

¡Las contribuciones son bienvenidas! Por favor, envíe pull requests o reporte problemas en la página de GitHub del proyecto.