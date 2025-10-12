このプロジェクトは元のプロジェクトのフォークです - https://github.com/rr-/docstring_parser/



# PyDocSmith

PyDocSmith は、さまざまなスタイルのドックストリングを解析、検出、作成するために設計された多用途の Python パッケージです。reStructuredText (reST)、Google、NumPydoc、Epydoc などの複数のドックストリング規約をサポートし、Python 開発者のドキュメント作成プラクティスに柔軟性を提供します。

## 機能

- **ドックストリングスタイルの検出：** シンプルなヒューリスティックを使用してドックストリングのスタイル（例: reST、Google、NumPydoc、Epydoc）を自動的に検出します。
- **ドックストリングの解析：** ドックストリングを構造化表現に変換し、ドキュメントの分析と操作を容易にします。
- **ドックストリングの作成：** 構造化ドックストリングをテキストに戻してレンダリングし、ドックストリングの自動生成と変更を可能にします。
- **属性ドックストリング：** クラスおよびモジュールレベルで定義された属性ドックストリングを解析し、クラスプロパティとモジュールレベル変数のドキュメントを強化します。

## インストール

```bash
pip install PyDocSmith
```

## 使用方法

### ドックストリングスタイルの検出

与えられたテキストのドックストリングスタイルを検出します：

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

### ドックストリングの解析

ドックストリングをそのコンポーネントに解析します：

```python
from PyDocSmith import parse, DocstringStyle

parsed_docstring = parse(docstring, style=DocstringStyle.AUTO)
print(parsed_docstring)
```

### ドックストリングの作成

解析されたドックストリングをテキストに戻してレンダリングします：

```python
from PyDocSmith import compose

docstring_text = compose(parsed_docstring, style=DocstringStyle.REST)
print(docstring_text)
```

## 高度な機能

- **オブジェクトからの解析：** PyDocSmith は Python オブジェクトから直接ドックストリングを解析でき、クラスやモジュールを含み、属性ドックストリングを構造化表現に組み込みます。
- **カスタムレンダリングスタイル：** コンパクトまたは詳細なスタイルでドックストリングのレンダリングをカスタマイズし、生成されたドックストリングテキストのカスタムインデントを指定します。

## docstring_parser に関して変更されたもの

1. ドックストリングスタイルを検出するためのより良いヒューリスティック
2. Google Docstring は Notes、Examples を収容するために変更されました
3. 時々 GoogleDoc string は、特に GPT や Mistral などの LLMs から生成された場合、正しいインデントを持っていません。PyDocSmith はこれらの悪いドックストリングを修正できます。
4. 異なるスタイルの GoogleDocstring を収容するために追加のテストケースが追加されました

私はこれを - https://www.penify.dev の使用ケースに基づいて更新しました

## 貢献

貢献は歓迎されます！プロジェクトの GitHub ページでプルリクエストを送信するか、問題を報告してください。