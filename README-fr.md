Le projet est un fork du projet original - https://github.com/rr-/docstring_parser/



# PyDocSmith

PyDocSmith est un package Python polyvalent conçu pour analyser, détecter et composer des docstrings dans divers styles. Il prend en charge plusieurs conventions de docstring, y compris reStructuredText (reST), Google, NumPydoc et Epydoc, offrant une flexibilité dans les pratiques de documentation pour les développeurs Python.

## Fonctionnalités

- **Détection du style de docstring :** Détecte automatiquement le style des docstrings (par exemple, reST, Google, NumPydoc, Epydoc) en utilisant des heuristiques simples.
- **Analyse des docstrings :** Convertit les docstrings en représentations structurées, facilitant l'analyse et la manipulation de la documentation.
- **Composition des docstrings :** Rend les docstrings structurées en texte, permettant la génération et la modification automatisées des docstrings.
- **Docstrings d'attributs :** Analyse les docstrings d'attributs définis aux niveaux de classe et de module, améliorant la documentation des propriétés de classe et des variables au niveau du module.

## Installation

```bash
pip install PyDocSmith
```

## Utilisation

### Détection du style de docstring

Détecte le style de docstring d'un texte donné :

```python
from PyDocSmith import detect_docstring_style, DocstringStyle

docstring = """
Ceci est un exemple de docstring.
:param param1: Description de param1
:return: Description de la valeur de retour
"""
style = detect_docstring_style(docstring)
print(style)  # Affiche : DocstringStyle.EPYDOC
```

### Analyse des docstrings

Analyse une docstring en ses composants :

```python
from PyDocSmith import parse, DocstringStyle

parsed_docstring = parse(docstring, style=DocstringStyle.AUTO)
print(parsed_docstring)
```

### Composition des docstrings

Rend une docstring analysée en texte :

```python
from PyDocSmith import compose

docstring_text = compose(parsed_docstring, style=DocstringStyle.REST)
print(docstring_text)
```

### Analyse d'une docstring Google avec Notes et Examples

Détecte le style de docstring d'un texte donné contenant Notes et Examples :

```python
from PyDocSmith import parse, DocstringStyle

docstring = """
Cette fonction fait quelque chose.

Args:
    param1 (str): Description de param1

Returns:
    str: Description de la valeur de retour

Notes:
    Ceci est une note.

Examples:
    >>> func('hello')
    'hello world'
"""

parsed = parse(docstring, style=DocstringStyle.GOOGLE)
print(parsed)
```

### Analyse des docstrings à partir d'un objet

Analyse les docstrings à partir d'objets Python :

```python
from PyDocSmith import parse_from_object

class MyClass:
    """Ceci est une docstring de classe."""

    attr: str
    """Ceci est une docstring d'attribut."""

parsed = parse_from_object(MyClass)
print(parsed)
```

### Composition des docstrings avec une indentation personnalisée

Rend une docstring analysée avec une indentation personnalisée :

```python
from PyDocSmith import compose

# En supposant que parsed_docstring est disponible
docstring_text = compose(parsed_docstring, style=DocstringStyle.GOOGLE, indent='    ')
print(docstring_text)
```

## Fonctionnalités avancées

- **Analyser à partir d'un objet :** PyDocSmith peut analyser les docstrings directement à partir d'objets Python, y compris les classes et les modules, en incorporant les docstrings d'attributs dans la représentation structurée.
- **Styles de rendu personnalisés :** Personnalise le rendu des docstrings avec des styles compacts ou détaillés, et spécifie une indentation personnalisée pour le texte de docstring généré.

## Choses qui ont été modifiées par rapport à docstring_parser

1. Meilleures heuristiques pour détecter le style de docstring
2. La docstring Google a été modifiée pour accueillir Notes, Exemples
3. Parfois, la docstring Google n'a pas une indentation correcte, surtout lorsqu'elle est générée à partir de LLMs comme GPT ou Mistral. PyDocSmith peut corriger ces mauvaises docstrings.
4. Des cas de test supplémentaires ont été ajoutés pour accommoder un style différent de GoogleDocstring

## Contribution

Les contributions sont les bienvenues ! Veuillez soumettre des pull requests ou signaler des problèmes sur la page GitHub du projet.