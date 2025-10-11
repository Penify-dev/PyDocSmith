このプロジェクトは元のプロジェクトのフォークです - https://github.com/rr-/docstring_parser/

# PyDocSmith

PyDocSmith は、さまざまなスタイルのドックストリングを解析、検出、作成するために設計された多用途の Python パッケージです。reStructuredText (reST)、Google、NumPydoc、Epydoc などの複数のドックストリング規約をサポートし、Python 開発者のドキュメント実践に柔軟性を提供します。

## Features

- **Docstring Style Detection:** シンプルなヒューリスティックを使用してドックストリングのスタイル（例: reST、Google、NumPydoc、Epydoc）を自動的に検出します。
- **Docstring Parsing:** ドックストリングを構造化表現に変換し、ドキュメントの分析と操作を容易にします。
- **Docstring Composition:** 構造化ドックストリングをテキストに戻してレンダリングし、自動ドックストリング生成と変更を可能にします。
- **Attribute Docstrings:** クラスおよびモジュールレベルで定義された属性ドックストリングを解析し、クラスプロパティとモジュールレベル変数のドキュメントを強化します。

## Installation

```bash
pip install PyDocSmith
```

## Usage

### Detecting Docstring Style

指定されたテキストのドックストリングスタイルを検出します：

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

ドックストリングをそのコンポーネントに解析します：

```python
from PyDocSmith import parse, DocstringStyle

parsed_docstring = parse(docstring, style=DocstringStyle.AUTO)
print(parsed_docstring)
```

### Composing Docstrings

解析されたドックストリングをテキストに戻してレンダリングします：

```python
from PyDocSmith import compose

docstring_text = compose(parsed_docstring, style=DocstringStyle.REST)
print(docstring_text)
```

## Advanced Features

- **Parse From Object:** PyDocSmith は、クラスやモジュールを含む Python オブジェクトから直接ドックストリングを解析でき、属性ドックストリングを構造化表現に組み込みます。
- **Custom Rendering Styles:** コンパクトまたは詳細なスタイルでドックストリングのレンダリングをカスタマイズし、生成されたドックストリングテキストのカスタムインデントを指定します。

## Things that have been modified wrt to docstring_parser

1. ドックストリングスタイルを検出するためのより良いヒューリスティック
2. Google Docstring は Notes、Examples を収容するために変更されました
3. 時々 GoogleDoc 文字列は適切なインデントを持たず、特に GPT や Mistral などの LLMs から生成された場合。PyDocSmith はこれらの悪いドックストリングを修正できます。
4. 異なるスタイルの GoogleDocstring を収容するために追加のテストケースが追加されました

私はこれを - https://www.penify.dev のユースケースに基づいて更新しました

## Contributing

貢献は歓迎されます！プロジェクトの GitHub ページでプルリクエストを送信するか、問題を報告してください。