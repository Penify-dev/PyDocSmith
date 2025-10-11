Ce projet est un fork du projet original - https://github.com/rr-/docstring_parser/

# PyDocSmith

PyDocSmith est un package Python polyvalent conçu pour analyser, détecter et composer des docstrings dans divers styles. Il prend en charge plusieurs conventions de docstrings, y compris reStructuredText (reST), Google, NumPydoc et Epydoc, offrant une flexibilité dans les pratiques de documentation pour les développeurs Python.

## Features

- **Docstring Style Detection:** Détecter automatiquement le style des docstrings (par exemple, reST, Google, NumPydoc, Epydoc) en utilisant des heuristiques simples.
- **Docstring Parsing:** Convertir les docstrings en représentations structurées, facilitant l'analyse et la manipulation de la documentation.
- **Docstring Composition:** Rendre les docstrings structurées en texte, permettant la génération et la modification automatisées des docstrings.
- **Attribute Docstrings:** Analyser les docstrings d'attributs définis au niveau des classes et des modules, améliorant la documentation des propriétés de classe et des variables au niveau du module.

## Installation

```bash
pip install PyDocSmith
```

## Usage

### Detecting Docstring Style

Détecter le style de docstring d'un texte donné:

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

Analyser une docstring en ses composants:

```python
from PyDocSmith import parse, DocstringStyle

parsed_docstring = parse(docstring, style=DocstringStyle.AUTO)
print(parsed_docstring)
```

### Composing Docstrings

Rendre une docstring analysée en texte:

```python
from PyDocSmith import compose

docstring_text = compose(parsed_docstring, style=DocstringStyle.REST)
print(docstring_text)
```

## Advanced Features

- **Parse From Object:** PyDocSmith peut analyser les docstrings directement à partir d'objets Python, y compris les classes et les modules, incorporant les docstrings d'attributs dans la représentation structurée.
- **Custom Rendering Styles:** Personnaliser le rendu des docstrings avec des styles compacts ou détaillés, et spécifier une indentation personnalisée pour le texte de docstring généré.

## Things that have been modified wrt to docstring_parser

1. Meilleures heuristiques pour détecter le style de docstring
2. Google Docstring a été modifié pour accueillir Notes, Examples
3. Parfois, la chaîne GoogleDoc n'a pas une indentation appropriée, surtout lorsqu'elle est générée à partir de LLMs comme GPT ou Mistral. PyDocSmith peut corriger ces mauvaises docstrings.
4. Des cas de test supplémentaires ont été ajoutés pour accueillir un style différent de GoogleDocstring

J'ai mis à jour cela basé sur le cas d'utilisation pour - https://www.penify.dev

## Contributing

Les contributions sont les bienvenues ! Veuillez soumettre des pull requests ou signaler des problèmes sur la page GitHub du projet.