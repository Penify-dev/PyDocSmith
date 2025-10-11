このプロジェクトは元のプロジェクトのフォークです - https://github.com/rr-/docstring_parser/



# PyDocSmith

PyDocSmith は、さまざまなスタイルの docstrings を解析、検出、作成するために設計された多用途の Python パッケージです。reStructuredText (reST)、Google、NumPydoc、Epydoc などの複数の docstring 規約をサポートし、Python 開発者向けのドキュメント実践に柔軟性を提供します。

## 機能

- **Docstring スタイル検出：** シンプルなヒューリスティックを使用して docstrings のスタイル（例: reST、Google、NumPydoc、Epydoc）を自動的に検出します。
- **Docstring 解析：** docstrings を構造化表現に変換し、ドキュメントの分析と操作を容易にします。
- **Docstring 作成：** 構造化された docstrings をテキストにレンダリングし、自動生成と変更を可能にします。
- **属性 Docstrings：** クラスおよびモジュールレベルで定義された属性 docstrings を解析し、クラスプロパティとモジュールレベル変数のドキュメントを強化します。

## インストール

```bash
pip install PyDocSmith
```

## 使用方法

### Docstring スタイル検出

与えられたテキストの docstring スタイルを検出します：

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

### Docstrings 解析

docstring をそのコンポーネントに解析します：

```python
from PyDocSmith import parse, DocstringStyle

parsed_docstring = parse(docstring, style=DocstringStyle.AUTO)
print(parsed_docstring)
```

### Docstrings 作成

解析された docstring をテキストにレンダリングします：

```python
from PyDocSmith import compose

docstring_text = compose(parsed_docstring, style=DocstringStyle.REST)
print(docstring_text)
```

## 高度な機能

- **オブジェクトから解析：** PyDocSmith は、クラスやモジュールを含む Python オブジェクトから直接 docstrings を解析し、属性 docstrings を構造化表現に組み込むことができます。
- **カスタムレンダリングスタイル：** コンパクトまたは詳細なスタイルで docstrings のレンダリングをカスタマイズし、生成された docstring テキストのカスタムインデントを指定します。

## docstring_parser に関して変更されたもの

1. Docstring スタイル検出のためのより良いヒューリスティック
2. Google Docstring は Notes、Examples を収容するために変更されました
3. 時々 GoogleDoc string は適切なインデントを持たず、特に GPT や Mistral などの LLMs から生成された場合。PyDocSmith はこれらの悪い docstrings を修正できます。
4. さまざまなスタイルの GoogleDocstring を収容するために追加のテストケースが追加されました

私はこれを - https://www.penify.dev の使用ケースに基づいて更新しました

## 貢献

貢献を歓迎します！プロジェクトの GitHub ページでプルリクエストを送信するか、問題を報告してください。