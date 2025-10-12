このプロジェクトは元のプロジェクトのフォークです - https://github.com/rr-/docstring_parser/



# PyDocSmith

PyDocSmith は、さまざまなスタイルの docstrings を解析、検出、作成するために設計された多用途の Python パッケージです。reStructuredText (reST)、Google、NumPydoc、Epydoc などの複数の docstring 規約をサポートし、Python 開発者のドキュメント実践に柔軟性を提供します。

## 機能

- **Docstring スタイル検出：** シンプルなヒューリスティックを使用して docstrings のスタイル（例: reST、Google、NumPydoc、Epydoc）を自動的に検出します。
- **Docstring 解析：** docstrings を構造化表現に変換し、ドキュメントの分析と操作を容易にします。
- **Docstring 作成：** 構造化された docstrings をテキストに戻してレンダリングし、自動 docstring 生成と変更を可能にします。
- **属性 Docstrings：** クラスおよびモジュールレベルで定義された属性 docstrings を解析し、クラスプロパティとモジュールレベル変数のドキュメントを強化します。

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
これはサンプル docstring です。
:param param1: param1 の説明
:return: 戻り値の説明
"""
style = detect_docstring_style(docstring)
print(style)  # 出力: DocstringStyle.EPYDOC
```

### Docstrings の解析

docstring をそのコンポーネントに解析します：

```python
from PyDocSmith import parse, DocstringStyle

parsed_docstring = parse(docstring, style=DocstringStyle.AUTO)
print(parsed_docstring)
```

### Docstrings の作成

解析された docstring をテキストに戻してレンダリングします：

```python
from PyDocSmith import compose

docstring_text = compose(parsed_docstring, style=DocstringStyle.REST)
print(docstring_text)
```

### Notes と Examples を含む Google Docstring の解析

Notes と Examples を含む指定されたテキストの docstring スタイルを検出します：

```python
from PyDocSmith import parse, DocstringStyle

docstring = """
この関数は何かをします。

Args:
    param1 (str): param1 の説明

Returns:
    str: 戻り値の説明

Notes:
    これはノートです。

Examples:
    >>> func('hello')
    'hello world'
"""

parsed = parse(docstring, style=DocstringStyle.GOOGLE)
print(parsed)
```

### オブジェクトからの Docstrings の解析

Python オブジェクトから docstrings を解析します：

```python
from PyDocSmith import parse_from_object

class MyClass:
    """これはクラス docstring です。"""

    attr: str
    """これは属性 docstring です。"""

parsed = parse_from_object(MyClass)
print(parsed)
```

### カスタムインデントを使用した Docstrings の作成

カスタムインデントを使用して解析された docstring をレンダリングします：

```python
from PyDocSmith import compose

# parsed_docstring が利用可能であると仮定
docstring_text = compose(parsed_docstring, style=DocstringStyle.GOOGLE, indent='    ')
print(docstring_text)
```

## 高度な機能

- **オブジェクトからの解析：** PyDocSmith は、クラスやモジュールを含む Python オブジェクトから直接 docstrings を解析し、属性 docstrings を構造化表現に組み込むことができます。
- **カスタムレンダリングスタイル：** コンパクトまたは詳細なスタイルで docstrings のレンダリングをカスタマイズし、生成された docstring テキストのカスタムインデントを指定します。

## docstring_parser と比較して変更されたこと

1. Docstring スタイル検出のためのより良いヒューリスティック
2. Google Docstring は Notes、Examples を収容するために変更されました
3. 時々 GoogleDoc string は適切なインデントを持たない、特に LLMs のような GPT や Mistral から生成された場合。PyDocSmith はこれらの悪い docstrings を修正できます。
4. 異なるスタイルの GoogleDocstring を収容するために追加のテストケースが追加されました

## 貢献

貢献は歓迎されます！プロジェクトの GitHub ページでプルリクエストを送信するか、問題を報告してください。