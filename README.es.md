Este proyecto es un fork del proyecto original - https://github.com/rr-/docstring_parser/



# PyDocSmith

PyDocSmith es un paquete Python versátil diseñado para analizar, detectar y componer docstrings en varios estilos. Soporta múltiples convenciones de docstrings, incluyendo reStructuredText (reST), Google, NumPydoc y Epydoc, proporcionando flexibilidad en las prácticas de documentación para desarrolladores de Python.

## Características

- **Detección de estilo de docstring:** Detecta automáticamente el estilo de los docstrings (por ejemplo, reST, Google, NumPydoc, Epydoc) utilizando heurísticas simples.
- **Análisis de docstrings:** Convierte docstrings en representaciones estructuradas, facilitando el análisis y manipulación de la documentación.
- **Composición de docstrings:** Renderiza docstrings estructuradas de vuelta en texto, permitiendo la generación y modificación automatizada de docstrings.
- **Docstrings de atributos:** Analiza docstrings de atributos definidos en niveles de clase y módulo, mejorando la documentación de propiedades de clase y variables de nivel de módulo.

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
This is an example docstring.
:param param1: Description of param1
:return: Description of return value
"""
style = detect_docstring_style(docstring)
print(style)  # Outputs: DocstringStyle.EPYDOC
```

### Análisis de docstrings

Analiza una docstring en sus componentes:

```python
from PyDocSmith import parse, DocstringStyle

parsed_docstring = parse(docstring, style=DocstringStyle.AUTO)
print(parsed_docstring)
```

### Composición de docstrings

Renderiza una docstring analizada de vuelta en texto:

```python
from PyDocSmith import compose

docstring_text = compose(parsed_docstring, style=DocstringStyle.REST)
print(docstring_text)
```

## Características avanzadas

- **Analizar desde objeto:** PyDocSmith puede analizar docstrings directamente desde objetos Python, incluyendo clases y módulos, incorporando docstrings de atributos en la representación estructurada.
- **Estilos de renderizado personalizados:** Personaliza el renderizado de docstrings con estilos compactos o detallados, y especifica indentación personalizada para el texto de docstring generado.

## Cosas que han sido modificadas con respecto a docstring_parser

1. Mejores heurísticas para detectar el estilo de docstring
2. El docstring de Google ha sido modificado para acomodar Notes, Examples
3. A veces, la cadena GoogleDoc no tiene indentación apropiada, especialmente cuando se genera desde LLMs como GPT o Mistral. PyDocSmith puede corregir esas malas docstrings.
4. Se agregaron casos de prueba adicionales para acomodar diferentes estilos de GoogleDocstring

He actualizado esto basado en el caso de uso para - https://www.penify.dev

## Contribución

¡Las contribuciones son bienvenidas! Por favor, envíe pull requests o reporte problemas en la página de GitHub del proyecto.