El proyecto es un fork del proyecto original - https://github.com/rr-/docstring_parser/



# PyDocSmith

PyDocSmith es un paquete Python versátil diseñado para analizar, detectar y componer docstrings en varios estilos. Soporta múltiples convenciones de docstrings, incluyendo reStructuredText (reST), Google, NumPydoc y Epydoc, proporcionando flexibilidad en las prácticas de documentación para desarrolladores Python.

## Características

- **Detección de estilo de docstring:** Detecte automáticamente el estilo de las docstrings (por ejemplo, reST, Google, NumPydoc, Epydoc) utilizando heurísticas simples.
- **Análisis de docstrings:** Convierta docstrings en representaciones estructuradas, facilitando el análisis y manipulación de la documentación.
- **Composición de docstrings:** Renderice docstrings estructuradas de vuelta en texto, permitiendo la generación y modificación automatizada de docstrings.
- **Docstrings de atributos:** Analice docstrings de atributos definidos a nivel de clase y módulo, mejorando la documentación de propiedades de clase y variables a nivel de módulo.

## Instalación

```bash
pip install PyDocSmith
```

## Uso

### Detección de estilo de docstring

Detecte el estilo de docstring de un texto dado:

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

Analice una docstring en sus componentes:

```python
from PyDocSmith import parse, DocstringStyle

parsed_docstring = parse(docstring, style=DocstringStyle.AUTO)
print(parsed_docstring)
```

### Composición de docstrings

Renderice una docstring analizada de vuelta en texto:

```python
from PyDocSmith import compose

docstring_text = compose(parsed_docstring, style=DocstringStyle.REST)
print(docstring_text)
```

## Características avanzadas

- **Analizar desde objeto:** PyDocSmith puede analizar docstrings directamente desde objetos Python, incluyendo clases y módulos, incorporando docstrings de atributos en la representación estructurada.
- **Estilos de renderizado personalizados:** Personalice el renderizado de docstrings con estilos compactos o detallados, y especifique indentación personalizada para el texto de docstring generado.

## Cosas que han sido modificadas con respecto a docstring_parser

1. Mejores heurísticas para detectar el estilo de docstring
2. Google Docstring ha sido modificado para acomodar Notas, Ejemplos
3. A veces GoogleDoc string no tiene la indentación adecuada, especialmente cuando se genera desde LLMs como GPT o Mistral. PyDocSmith puede arreglar esas malas docstrings.
4. Casos de prueba adicionales fueron añadidos para acomodar un estilo diferente de GoogleDocstring

He actualizado esto basado en el caso de uso para - https://www.penify.dev

## Contribución

¡Las contribuciones son bienvenidas! Por favor, envíe pull requests o reporte problemas en la página de GitHub del proyecto.