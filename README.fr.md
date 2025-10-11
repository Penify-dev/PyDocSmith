Le projet est un fork du projet original - https://github.com/rr-/docstring_parser/



# PyDocSmith

PyDocSmith est un package Python polyvalent conçu pour analyser, détecter et composer des docstrings dans divers styles. Il prend en charge plusieurs conventions de docstrings, y compris reStructuredText (reST), Google, NumPydoc et Epydoc, offrant de la flexibilité dans les pratiques de documentation pour les développeurs Python.

## Fonctionnalités

- **Détection du style de docstring :** Détecter automatiquement le style des docstrings (par exemple, reST, Google, NumPydoc, Epydoc) en utilisant des heuristiques simples.
- **Analyse des docstrings :** Convertir les docstrings en représentations structurées, facilitant l'analyse et la manipulation de la documentation.
- **Composition des docstrings :** Rendre les docstrings structurées en texte, permettant la génération et la modification automatisées des docstrings.
- **Docstrings d'attributs :** Analyser les docstrings d'attributs définis au niveau des classes et des modules, améliorant la documentation des propriétés de classe et des variables au niveau du module.

## Installation

```bash
pip install PyDocSmith
```

## Utilisation

### Détection du style de docstring

Détecter le style de docstring d'un texte donné :

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

### Analyse des docstrings

Analyser une docstring en ses composants :

```python
from PyDocSmith import parse, DocstringStyle

parsed_docstring = parse(docstring, style=DocstringStyle.AUTO)
print(parsed_docstring)
```

### Composition des docstrings

Rendre une docstring analysée en texte :

```python
from PyDocSmith import compose

docstring_text = compose(parsed_docstring, style=DocstringStyle.REST)
print(docstring_text)
```

## Plus d'Exemples

### Analyse des Docstrings de Style NumPy

Analyser une docstring de style NumPy:

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

### Analyse depuis les Objets Python

Analyser les docstrings directement depuis les fonctions ou classes Python:

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

### Composition avec Différents Styles

Composer une docstring dans un style différent de celui analysé:

```python
from PyDocSmith import compose, DocstringStyle

# Assuming you have a parsed_docstring from previous examples
docstring_text = compose(parsed_docstring, style=DocstringStyle.GOOGLE)
print(docstring_text)
```

## Fonctionnalités avancées

- **Analyser depuis l'objet :** PyDocSmith peut analyser les docstrings directement depuis les objets Python, y compris les classes et les modules, en incorporant les docstrings d'attributs dans la représentation structurée.
- **Styles de rendu personnalisés :** Personnaliser le rendu des docstrings avec des styles compacts ou détaillés, et spécifier une indentation personnalisée pour le texte de docstring généré.


