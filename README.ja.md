このプロジェクトは、元のプロジェクト - https://github.com/rr-/docstring_parser/ のフォークです。



# PyDocSmith

PyDocSmith は、さまざまなスタイルの docstring を解析、検出、作成するための多用途の Python パッケージです。reStructuredText (reST)、Google、NumPydoc、Epydoc などの複数の docstring 規約をサポートし、Python 開発者のドキュメント作成に柔軟性を提供します。

## 機能

- **Docstring スタイル検出:** シンプルなヒューリスティックを使用して、docstring のスタイル（例: reST、Google、NumPydoc、Epydoc）を自動的に検出します。
- **Docstring 解析:** docstring を構造化された表現に変換し、ドキュメントの分析と操作を容易にします。
- **Docstring 作成:** 構造化された docstring をテキストに戻してレンダリングし、自動化された docstring 生成と修正を可能にします。
- **属性 Docstring:** クラスおよびモジュールレベルで定義された属性 docstring を解析し、クラスプロパティとモジュールレベル変数のドキュメントを強化します。

## インストール

```bash
pip install PyDocSmith
```

## 使用方法

### Docstring スタイルの検出

指定されたテキストの docstring スタイルを検出します：

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

### Docstring の解析

docstring をその構成要素に解析します：

```python
from PyDocSmith import parse, DocstringStyle

parsed_docstring = parse(docstring, style=DocstringStyle.AUTO)
print(parsed_docstring)
```

### Docstring の作成

解析された docstring をテキストに戻してレンダリングします：

```python
from PyDocSmith import compose

docstring_text = compose(parsed_docstring, style=DocstringStyle.REST)
print(docstring_text)
```

## 高度な機能

- **オブジェクトからの解析:** PyDocSmith は、クラスやモジュールなどの Python オブジェクトから直接 docstring を解析し、属性 docstring を構造化された表現に組み込むことができます。
- **カスタムレンダリングスタイル:** コンパクトまたは詳細なスタイルで docstring のレンダリングをカスタマイズし、生成された docstring テキストにカスタムインデントを指定できます。

## docstring_parser との変更点

1. Docstring スタイル検出のためのより優れたヒューリスティック
2. Google Docstring が Notes と Examples を収容するように変更
3. GPT や Mistral などの LLM から生成された場合、GoogleDoc string が適切なインデントを持たないことがあります。PyDocSmith はこれらの不良 docstring を修正できます。
4. さまざまなスタイルの GoogleDocstring を収容するために追加のテストケースが追加されました

https://www.penify.dev のユースケースに基づいて更新しました。

## 貢献

貢献を歓迎します！プロジェクトの GitHub ページでプルリクエストを送信するか、問題を報告してください。