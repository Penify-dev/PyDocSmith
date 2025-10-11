El proyecto es un fork del proyecto original - https://github.com/rr-/docstring_parser/



# PyDocSmith

PyDocSmith es un paquete Python versátil diseñado para analizar, detectar y componer docstrings en varios estilos. Soporta múltiples convenciones de docstrings, incluyendo reStructuredText (reST), Google, NumPydoc y Epydoc, proporcionando flexibilidad en las prácticas de documentación para desarrolladores de Python.

## Características

- **Detección de Estilo de Docstring:** Detecta automáticamente el estilo de los docstrings (por ejemplo, reST, Google, NumPydoc, Epydoc) utilizando heurísticas simples.
- **Análisis de Docstrings:** Convierte docstrings en representaciones estructuradas, facilitando el análisis y manipulación de la documentación.
- **Composición de Docstrings:** Renderiza docstrings estructurados de vuelta a texto, permitiendo la generación y modificación automatizada de docstrings.
- **Docstrings de Atributos:** Analiza docstrings de atributos definidos en niveles de clase y módulo, mejorando la documentación de propiedades de clase y variables a nivel de módulo.

## Instalación

```bash
pip install PyDocSmith
```

## Uso

### Detección de Estilo de Docstring

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

### Análisis de Docstrings

Analiza un docstring en sus componentes:

```python
from PyDocSmith import parse, DocstringStyle

parsed_docstring = parse(docstring, style=DocstringStyle.AUTO)
print(parsed_docstring)
```

### Composición de Docstrings

Renderiza un docstring analizado de vuelta a texto:

```python
from PyDocSmith import compose

docstring_text = compose(parsed_docstring, style=DocstringStyle.REST)
print(docstring_text)
```

## Características Avanzadas

- **Analizar Desde Objeto:** PyDocSmith puede analizar docstrings directamente desde objetos Python, incluyendo clases y módulos, incorporando docstrings de atributos en la representación estructurada.
- **Estilos de Renderizado Personalizados:** Personaliza el renderizado de docstrings con estilos compactos o detallados, y especifica indentación personalizada para el texto de docstring generado.

## Cosas que han sido modificadas con respecto a docstring_parser

1. Mejores heurísticas para detectar el estilo de docstring
2. El Docstring de Google ha sido modificado para acomodar Notas, Ejemplos
3. A veces, el docstring de Google no tiene una indentación adecuada, especialmente cuando se genera desde LLMs como GPT o Mistral. PyDocSmith puede corregir esos docstrings defectuosos.
4. Se agregaron casos de prueba adicionales para acomodar un estilo diferente de GoogleDocstring

Lo he actualizado basado en el caso de uso para - https://www.penify.dev

## Contribuyendo

¡Las contribuciones son bienvenidas! Por favor, envía solicitudes de extracción o reporta problemas en la página de GitHub del proyecto.