Le projet est un fork du projet original - https://github.com/rr-/docstring_parser/



# PyDocSmith

PyDocSmith est un package Python polyvalent conçu pour analyser, détecter et composer des docstrings dans divers styles. Il prend en charge plusieurs conventions de docstrings, y compris reStructuredText (reST), Google, NumPydoc et Epydoc, offrant une flexibilité dans les pratiques de documentation pour les développeurs Python.

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

## Fonctionnalités avancées

- **Analyser depuis l'objet :** PyDocSmith peut analyser les docstrings directement depuis les objets Python, y compris les classes et les modules, en incorporant les docstrings d'attributs dans la représentation structurée.
- **Styles de rendu personnalisés :** Personnaliser le rendu des docstrings avec des styles compacts ou détaillés, et spécifier une indentation personnalisée pour le texte de docstring généré.

## Choses qui ont été modifiées par rapport à docstring_parser

1. Meilleures heuristiques pour détecter le style de docstring
2. Google Docstring a été modifié pour accommoder Notes, Examples
3. Parfois, GoogleDoc string n'a pas la bonne indentation, surtout lorsqu'il est généré à partir de LLMs comme GPT ou Mistral. PyDocSmith peut corriger ces mauvaises docstrings.
4. Des cas de test supplémentaires ont été ajoutés pour accommoder différents styles de GoogleDocstring

J'ai mis à jour cela basé sur le cas d'utilisation pour - https://www.penify.dev

## Contribution

Les contributions sont les bienvenues ! Veuillez soumettre des pull requests ou signaler des problèmes sur la page GitHub du projet.