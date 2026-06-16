---
title: Python で PDF テキストをフォーマットする
linktitle: PDF 内のテキストフォーマット
type: docs
weight: 70
url: /ja/python-net/text-formatting-inside-pdf/
description: Python でスペース、境界線、インデント、スタイルオプションを使用して PDF ドキュメント内のテキストをフォーマットする方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF ファイル内のテキストの書式設定とスタイルを設定する
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメント内のテキストをフォーマットする方法について説明します。Python でスペース、インデント、境界線、下線、取り消し線効果、その他のテキストスタイルオプションを制御する方法を学びましょう。
---

## 行と文字の間隔

### 行間隔を使用する

#### Pythonでカスタム行間隔を使用してテキストをフォーマットする方法-単純なケース

Aspose.PDF for Python では、行間隔を調整してテキストのレイアウトと読みやすさを制御する簡単な方法が用意されています。

このコードスニペットは、PDF ドキュメントの行間隔を制御する方法を示しています。ファイルからテキストを読み取り（またはフォールバックメッセージを使用して）、カスタムフォントサイズと行間隔を適用し、フォーマットされたテキストを PDF の新しいページに追加します。

1. 新しい PDF ドキュメントを作成します。
1. ソーステキストをロードします。
1. TextFragment オブジェクトを初期化し、読み込まれたテキストをそれに割り当てます。
1. テキストのフォントと間隔のプロパティを設定します。これらの値によって、テキストの行がどの程度きつく表示されるか、緩く表示されるかが決まります。
    -フォントサイズ:12 ポイント
    -行間隔:16 ポイント
1. フォーマットされたテキストフラグメントをページの段落コレクションに挿入します。
1. 文書を保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def specify_line_spacing_simple_case(outfile):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = "Lorem ipsum text not found."

    text_fragment = ap.text.TextFragment(text)
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.line_spacing = 16
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

#### Pythonでカスタム行間隔を使用してテキストをフォーマットする方法-特定のケース

カスタム TrueType フォント (TTF) を使用して PDF 文書にさまざまな行間隔モードを適用する方法を確認しましょう。
ファイルからテキストを読み込み、特定のフォントを埋め込み、同じテキストを PDF ページに 2 回レンダリングします。そのたびに異なる行間隔モードを使用します。

- FONT_SIZE モード:行間隔はフォントサイズと同じです。
- FULL_SIZE モード:行間隔は、昇順と降順を含むフォントの高さ全体を占めます。

この例は、選択したモードによって行間隔の動作がどのように異なるかを示しています。

1. 新しい PDF ドキュメントを作成します。
1. カスタムフォントファイルとテキストソースファイルの両方のパスを指定します。
1. テキストコンテンツをロードします。
1. カスタムフォントを開きます。
1. 最初のテキストフラグメントを作成して設定します (FONT_SIZE モード)。line_spacing を 'textFormattingOptions.LinespacingMode.FONT_SIZE' に設定します。つまり、行間隔はフォントサイズと等しくなります。
1. 2 番目のテキストフラグメントを作成して設定します (FULL_SIZE モード)。line_spacing を 'textFormattingOptions.LinespacingMode.FULL_Size' に設定します。これはフォントの高さ全体を使用します。
1. 両方のテキストフラグメントを同じ PDF ページに追加します。
1. 完成した文書を指定した出力場所に保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def specify_line_spacing_specific_case(outfile):
    document = ap.Document()
    page = document.pages.add()

    font_file = path.join(DATA_DIR, "HPSimplified.ttf")
    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = "Lorem ipsum text not found."

    with open(font_file, "rb") as font_stream:
        font = ap.text.FontRepository.open_font(font_stream, ap.text.FontTypes.TTF)

        fragment1 = ap.text.TextFragment(text)
        fragment1.text_state.font = font
        fragment1.text_state.formatting_options = ap.text.TextFormattingOptions()
        fragment1.text_state.formatting_options.line_spacing = (
            ap.text.TextFormattingOptions.LineSpacingMode.FONT_SIZE
        )
        page.paragraphs.add(fragment1)

        fragment2 = ap.text.TextFragment(text)
        fragment2.text_state.font = font
        fragment2.text_state.formatting_options = ap.text.TextFormattingOptions()
        fragment2.text_state.formatting_options.line_spacing = (
            ap.text.TextFormattingOptions.LineSpacingMode.FULL_SIZE
        )
        page.paragraphs.add(fragment2)

    document.save(outfile)
```

![カスタム行間隔でテキストを表示する PDF ドキュメント。行間が 16 ポイントの間隔になっているため、読みやすくなり、テキストレイアウトのフォーマットも向上します。](line_spacing.png)

### 文字間隔を使用する

#### TextFragment クラスを使用して PDF テキストの文字間隔を制御する方法

文字間隔は、テキスト行内の個々の文字間の距離を決定します。これは、テキストの外観を微調整したり、特定のタイポグラフィ効果を実現したりするのに役立ちます。

1. 新しい Document オブジェクトを初期化し、テキストを配置するための空白ページを追加します。
1. フラグメントジェネレーターを定義します。ヘルパー関数 make_fragment (スペーシング) を実装しています。
    -サンプルテキストを使用してテキストフラグメントを作成します。
    -フォントを設定します。
1. 間隔値が異なるテキストフラグメントを追加します。
1. 文書を保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def character_spacing_using_text_fragment(outfile):
    document = ap.Document()
    page = document.pages.add()

    def make_fragment(spacing):
        fragment = ap.text.TextFragment("Sample Text with character spacing")
        fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
        fragment.text_state.font_size = 14
        fragment.text_state.character_spacing = spacing
        return fragment

    page.paragraphs.add(make_fragment(2.0))
    page.paragraphs.add(make_fragment(1.0))
    page.paragraphs.add(make_fragment(0.75))

    document.save(outfile)
```

![同じテキストが 3 行表示される PDF ドキュメント文字間隔のあるサンプルテキスト。1 行目の文字間隔は広く、中行は適度な間隔、一番下の行は最も近い文字間隔で、PDF テキストフォーマットにおけるさまざまな文字間隔値の視覚効果を示すものです。](character_spacing_simple.png)

#### テキストパラグラフとテキストビルダーを使用して PDF テキストの文字間隔を制御する方法

Aspose.PDF では、TextParagraph と TextBuilder を使用して PDF ドキュメントにテキストを追加するときに、カスタムの文字間隔を適用できます。
ページ上の特定の領域を定義し、テキストの折り返しを設定し、文字間の間隔を調整してテキストフラグメントをレンダリングします。

TextParagraph の使用は、構造化されたテキストブロックや複数列のテキストブロックを作成するときなど、テキストの配置とレイアウトを正確に制御する必要がある場合に最適です。

1. 新しい PDF ドキュメントを作成します。
1. ページの TextBuilder インスタンスを初期化します。
1. テキストパラグラフを作成して設定します。
    -ワードラップモードを「textFormattingOptions.wordwrapMode.by_words」に設定します。
1. カスタム文字間隔で TextFragment を作成します。
    -新しい TextFragment を作成し、そのテキストを設定します (例:「文字間隔のあるサンプルテキスト」)。
    -Arial やフォントサイズ 14 ptなどのフォント属性を指定します。
    -文字間隔 = 2.0 を適用すると、文字間のスペースが増えます。
1. テキストフラグメントをテキストパラグラフに追加します。
1. テキストパラグラフをページに追加します。
1. PDF ドキュメントを保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def character_spacing_using_text_paragraph(outfile):
    document = ap.Document()
    page = document.pages.add()

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(100, 700, 500, 750, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    fragment = ap.text.TextFragment("Sample Text with character spacing")
    fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment.text_state.font_size = 14
    fragment.text_state.character_spacing = 2.0

    paragraph.append_line(fragment)
    builder.append_paragraph(paragraph)
    document.save(outfile)
```

## リストの作成

PDF ファイルを扱う場合、箇条書き、番号付き、HTML や LaTeX でフォーマットされているかどうかにかかわらず、リストなどの構造化された情報を表示する必要がある場合があります。
Aspose.PDF for Python via .NET には、PDF ドキュメント内で直接リストを作成およびフォーマットする複数の柔軟な方法が用意されており、レイアウト、フォント、スタイルを完全に制御できます。

この記事では、プレーンテキスト形式から高度な HTML や LaTeX レンダリングまで、PDF でリストを作成する複数の方法を紹介します。いずれの方法も、プログラムによる正確な制御を好むのか、便利なマークアップベースのスタイルを好むのかなど、特定の用途に適しています。

この記事を読み終える頃には、以下の方法がわかるはずです。

- TextParagraph と TextBuilder を使用して、カスタムの箇条書きリストと番号付きリストを作成します。

- HTML フラグメント (HTMLFragment) を使用すると、「<ul>」リストと「<ol>」リストを PDF に簡単にレンダリングできます。

- LaTeX フラグメント (TexFragment) を活用して、数学または科学的なリストのフォーマットを行います。

- ページ内のテキストの折り返し、フォントスタイル、レイアウトの位置を制御します。

- 手動によるリスト構築とマークアップ主導のアプローチの違いを理解してください。

### 番号付きリストを作成

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list(outfile):
    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(80, 200, 400, 800, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    for item in items:
        fragment = ap.text.TextFragment("• " + item)
        fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
        fragment.text_state.font_size = 12
        paragraph.append_line(fragment)

    builder.append_paragraph(paragraph)
    document.save(outfile)
```

### 箇条書きリストを作成する

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list(outfile):
    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(80, 200, 400, 800, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    for i, item in enumerate(items):
        fragment = ap.text.TextFragment(f"{i + 1}. {item}")
        fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
        fragment.text_state.font_size = 12
        paragraph.append_line(fragment)

    builder.append_paragraph(paragraph)
    document.save(outfile)
```

### 番号付きリスト HTML バージョンの作成

HTML フラグメントを使用して PDF 文書に番号付き (順序付き) リストを作成します。Python の文字列リストを HTML に変換します。 `<ol>` エレメントを作成し、それを HTML フラグメントとして PDF ページに挿入します。

HTML フラグメントを使用すると、番号付きリスト、太字、斜体などの HTML ベースの書式設定機能を PDF に直接組み込むことができます。

1. 新しい PDF ドキュメントを作成し、ページを追加します。
1. リスト項目を準備します。
1. リストを HTML 形式の順序付きリストに変換します。
    -使用する `<ol>` 番号付きリストのタグ。
    -リスト内包表記を使用して、各項目を「li」タグで囲みます。
1. HTML 文字列を PDF ページに追加できる HTMLFragment オブジェクトに変換します。
1. HTMLFragment をページの段落コレクションに挿入します。
1. PDF ドキュメントを保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list_html_version(outfile):
    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    html_list = "<ol>" + "".join([f"<li>{item}</li>" for item in items]) + "</ol>"
    html_fragment = ap.HtmlFragment(html_list)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![自動的に番号が付けられた 4 つの項目を示す PDF 文書に表示される番号付きリスト:1.リストの 1 番目の項目は 2 です。ラッピング動作を示すためにテキストを増やした 2 番目の項目、3.3 番目の項目、および 4。4 番目の項目。このリストは、PDF 構造内で HTML 形式の順序付きリストを、適切な数値順序、インデント、および項目間の間隔でレンダリングする方法を示しています。](numbered_list_html.png)

### 箇条書きリスト HTML バージョンの作成

私たちのライブラリは、HTMLフラグメントを使用してPDF文書に箇条書き（順序なし）リストを作成する方法を示しています。Python の文字列リストを HTML に変換します。 `<ul>` エレメントを作成し、それを HTML フラグメントとして PDF ページに挿入します。HTML フラグメントを使用すると、HTML フォーマット機能（リスト、太字、斜体など）を PDF で直接活用できます。

1. 新しい PDF ドキュメントを作成し、ページを追加します。
1. リスト項目を準備します。
1. リストを HTML の順序なしリストに変換します。
    -使用する `<ul>` 順序のない (箇条書き) リストのタグ。
    -リスト内包表記を使用して、各項目を「li」タグで囲みます。
1. HTML フラグメントを作成します。HTML 文字列を PDF ページに追加できる HTMLFragment オブジェクトに変換します。
1. HTMLFragment をページの段落コレクションに挿入します。
1. PDF ドキュメントを保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list_html_version(outfile):
    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    html_list = "<ul>" + "".join([f"<li>{item}</li>" for item in items]) + "</ul>"
    html_fragment = ap.HtmlFragment(html_list)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![PDF ドキュメントに表示された箇条書きリストには、リストの最初の項目、折り返し動作を示すテキストが多い 2 番目の項目、3 番目の項目、4 番目の項目の 4 つが表示されます。各項目の前には標準の箇条書きが付いており、PDF 構造内で HTML 形式のリストが適切なインデントと間隔でレンダリングされる様子を示しています。](bullet_list_html.png)

### LaTeX バージョンの箇条書きリストを作成

LaTeX フラグメント (TexFragment) を使用して PDF に箇条書き (順序付けされていない) リストを作成します。Python の文字列リストを LaTeX アイテム化環境に変換して PDF ページに挿入します。LaTeX フラグメントの使用は、数学式、記号、または構造化されたリストを正確な書式でレンダリングする場合に最適です。

1. 新しい PDF ドキュメントを作成し、ページを追加します。
1. LaTeX アイテム化環境で箇条書きになる文字列の Python リストを定義します。
1. リストを LaTeX アイテム化環境に変換します。
    -アイテムを\ begin {itemize} と\ end {itemize} で囲みます。
    -各項目には、リスト内包表記を使用して\ item というプレフィックスが付きます。
1. LaTeX 文字列を PDF でレンダリングできるテキストフラグメントオブジェクトに変換します。
1. LaTeX フラグメントをページに追加します。
1. PDF ドキュメントを保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list_latex_version(outfile):
    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    tex_list = (
        "Lists are easy to create: \\begin{itemize}"
        + "".join([f"\\item {i}" for i in items])
        + "\\end{itemize}"
    )
    tex_fragment = ap.TeXFragment(tex_list)
    page.paragraphs.add(tex_fragment)
    document.save(outfile)
```

![LaTeX でレンダリングされたテキスト形式の箇条書きリストを PDF 形式で表示すると簡単に作成できます。その後に 4 つの箇条書きの項目 (1 番目の項目、折り返し動作を示すテキストが多い第 2 項目、3 番目の項目、4 番目の項目) が続きます。このリストは、適切な箇条書きフォーマット、一貫したスペース、およびテキストの折り返し機能を、すっきりとした PDF 文書レイアウト内で行う、プロ仕様の LaTeX タイプセッティングを示しています。](bullet_list_latex.png)

### LaTeX バージョンの番号付きリストを作成

LaTeX フラグメント (TexFragment) を使用して PDF に番号付き (順序付き) リストを作成します。Python の文字列リストを LaTeX 列挙環境に変換して PDF ページに挿入します。LaTeX フラグメントの使用は、PDF の正確な書式設定、構造化されたリスト、または数学表記が必要な場合に最適です。

1. 新しい PDF ドキュメントを作成し、ページを追加します。
1. LaTeX 列挙環境で番号付きの項目になる文字列の Python リストを定義します。
1. リストを LaTeX 列挙環境に変換します。
1. LaTeX 文字列を PDF でレンダリングできるテキストフラグメントオブジェクトに変換します。
1. LaTeX フラグメントをページに追加します。
1. PDF ドキュメントを保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list_latex_version(outfile):
    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    tex_list = (
        "Lists are easy to create: \\begin{enumerate}"
        + "".join([f"\\item {i}" for i in items])
        + "\\end{enumerate}"
    )
    tex_fragment = ap.TeXFragment(tex_list)
    page.paragraphs.add(tex_fragment)
    document.save(outfile)
```

![LaTeX でレンダリングされたフォーマットを示す番号付きリストが PDF に表示され、項目 1 が表示されます。1 番目の項目は 2 です。ラッピング動作を示すためにテキストを増やした 2 番目の項目、3.3 番目の項目、および 4。4 番目の項目で、その前にテキストが付きます。リストは簡単に作成できます。](numbered_list_latex.png)

## 脚注と文末脚注

### 脚注を追加

脚注は、関連するテキストの横に連続した上付き文字番号を付けることで、文書本文内の注記を参照するために使用されます。これらの番号は詳細な注記に対応していますが、通常はインデントされて同じページの下部に配置されるので、追加の文脈、引用、または解説が得られます。

.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメント内のテキストフラグメントに脚注を追加します。脚注は、メインの内容を乱雑にすることなく、補足情報、引用、説明を提供するのに役立ちます。この方法により、脚注が PDF レイアウトに視覚的かつ構造的に統合されます。

1. 新しい文書を作成します。
1. メインコンテンツを含むテキストフラグメントを作成します。
1. インラインテキストを追加します。同じ段落に続く TextFragment をもう1つ作成します。
1. 文書を保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.foot_note = ap.Note("This is the footnote content.")
    page.paragraphs.add(text_fragment)

    inline_text = ap.text.TextFragment(
        " This is another text after footnote in the same paragraph."
    )
    inline_text.is_in_line_paragraph = True
    inline_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    inline_text.text_state.font_size = 14
    page.paragraphs.add(inline_text)

    document.save(outfile)
```

### PDF にカスタムスタイルで脚注を追加

1. 新しい PDF ドキュメントを初期化し、空白ページを追加します。
1. メインテキストフラグメントを作成します。
1. 脚注を作成してスタイルを設定します (フォント、サイズ、色、スタイル)。
1. 脚注付きのスタイル付きテキストフラグメントをページに挿入します。
1. 脚注なしで別のテキストフラグメントを追加します。
1. 文書を保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_custom_text_style(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14

    note = ap.Note("This is the footnote content with custom text style.")
    note.text_state = ap.text.TextState()
    note.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    note.text_state.font_size = 10
    note.text_state.foreground_color = ap.Color.red
    note.text_state.font_style = ap.text.FontStyles.ITALIC
    text_fragment.foot_note = note

    page.paragraphs.add(text_fragment)

    another_text = ap.text.TextFragment(" This is another text without footnote.")
    another_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    another_text.text_state.font_size = 14
    page.paragraphs.add(another_text)

    document.save(outfile)
```

### PDF にカスタム記号付きの脚注を追加

.NET 経由の Aspose.PDF for Python を使用して PDF ドキュメント内のテキストフラグメントに脚注を追加できます。脚注マーカーシンボルをカスタマイズすることもできます。

1. PDF ドキュメントとページを作成します。
1. カスタム脚注シンボルを含む最初のテキストフラグメントを追加します。
1. 脚注なしで段落を続けるテキストフラグメントをもう1つ追加します。
1. デフォルトの脚注を含む2番目のテキストフラグメントを追加します。
1. 文書を保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_custom_text(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14

    note = ap.Note("This is the footnote content with custom text style.")
    note.text = "*"
    text_fragment.foot_note = note
    page.paragraphs.add(text_fragment)

    another_text = ap.text.TextFragment(" This is another text without footnote.")
    another_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    another_text.text_state.font_size = 14
    page.paragraphs.add(another_text)

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.foot_note = ap.Note("This is the footnote content.")
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

### PDF にカスタム線スタイルの脚注を追加

Python ライブラリを使用して PDF 文書内の脚注行の視覚的外観をカスタマイズします。脚注行をカスタマイズすると、レポート、学術論文、注釈付きの出版物などの文書の見た目が明確になり、文体の一貫性が保たれます。

1. 新しい PDF ドキュメントを作成し、ページを追加します。
1. 脚注コネクタのカスタムラインスタイル (色、幅、ダッシュパターン) を定義します。
1. 脚注付きの複数のテキストフラグメントを追加します。
1. 最終文書を保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_with_custom_line_style(outfile):
    document = ap.Document()
    page = document.pages.add()

    # Define custom line style
    graph_info = ap.GraphInfo()
    graph_info.line_width = 2
    graph_info.color = ap.Color.red
    graph_info.dash_array = [3]
    graph_info.dash_phase = 1
    page.note_line_style = graph_info

    # First text fragment with footnote
    text1 = ap.text.TextFragment("This is a sample text with a footnote.")
    text1.foot_note = ap.Note("foot note for text 1")
    page.paragraphs.add(text1)

    # Second text fragment with footnote
    text2 = ap.text.TextFragment("This is yet another sample text with a footnote.")
    text2.foot_note = ap.Note("foot note for text 2")
    page.paragraphs.add(text2)

    document.save(outfile)
```

### PDF に画像と表を含む脚注を追加

.NET 経由の Aspose.PDF for Pythonを使用して画像、スタイル付きテキスト、および表を埋め込むことで、PDF文書の脚注を充実させるにはどうすればよいですか?

1. 新しい PDF ドキュメントを作成し、ページを追加します。
1. 脚注を添付したテキストフラグメントを追加します。
1. 脚注の中に画像、スタイル付きテキスト、表を埋め込みます。
1. 文書を保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_with_image_and_table(outfile):
    document = ap.Document()
    page = document.pages.add()

    text = ap.text.TextFragment("This is a sample text with a footnote.")
    page.paragraphs.add(text)

    note = ap.Note()

    # Add image
    image_note = ap.Image()
    image_note.file = path.join(DATA_DIR, "logo.jpg")
    image_note.fix_height = 20
    image_note.fix_width = 20
    note.paragraphs.add(image_note)

    # Add text
    text_note = ap.text.TextFragment("This is the footnote content.")
    text_note.text_state.font_size = 20
    text_note.is_in_line_paragraph = True
    note.paragraphs.add(text_note)

    # Add table
    table = ap.Table()
    table.rows.add().cells.add("Cell 1,1")
    table.rows.add().cells.add("Cell 1,2")
    note.paragraphs.add(table)

    text.foot_note = note

    document.save(outfile)
```

### PDF 文書への文末脚注の追加

文末脚注は、読者を文書の最後にある指定されたセクションに誘導する一種の引用です。そこでは、引用、言い換えたアイデア、または要約された内容の完全な参考文献を見つけることができます。文末脚注を使用する場合、参照先の資料の直後に上付き文字番号を付けて、論文の最後にある対応する注記に読者を誘導します。

このコードスニペットは、PDF ドキュメント内のテキストフラグメントに文末脚注を追加する方法を示しています。参照テキストの近くに表示される脚注とは異なり、文末脚注は通常、文書またはセクションの末尾に配置されます。この方法では、長い文書をシミュレートして、拡張コンテンツで文末脚注がどのように動作するかを示すこともできます。

1. PDF ドキュメントとページを作成します。
1. 文末脚注にテキストフラグメントを追加します。
1. 外部テキストコンテンツをロードします。
1. 長い文書をシミュレートします。ロードしたテキストを複数回追加して、長いドキュメントをシミュレートします。
1. 文書を保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def add_endnote(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    page.paragraphs.add(text_fragment)

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, encoding="utf-8") as f:
            text_content = f.read()
    else:
        text_content = "Lorem ipsum sample text not found."

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

### PDF にカスタムマーカーテキストを含む文末脚注を追加

PDF ドキュメント内のテキストフラグメントに、カスタムマーカー記号（「***」など）を付けて文末脚注を追加します。通常、文末脚注は文書またはセクションの末尾に配置され、追加の文脈、引用、または解説を提供する場合に便利です。

1. PDF ドキュメントとページを作成します。
1. 文末脚注付きのスタイル付きテキストフラグメントを追加します。
1. 文末脚注マーカーのテキストをカスタマイズします。
1. .txt ファイルから外部コンテンツをロードします。
1. 長文のコンテンツをシミュレートして、文末脚注の配置を説明します。
1. PDF ドキュメントを保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def add_endnote_custom_text(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    text_fragment.end_note.text = "***"
    page.paragraphs.add(text_fragment)

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, encoding="utf-8") as f:
            text_content = f.read()
    else:
        text_content = "Lorem ipsum sample text not found."

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

## レイアウトとページコントロール

### PDF の表を強制的に新しいページで開始する

.NET 経由の Aspose.PDF for Python を使用して、PDF ドキュメントの新しいページから開始する特定のコンテンツを追加します。
プロパティ 'is_in_new_page' を設定すると、ページのレイアウトと構造を正確に制御でき、特定のセクション (表、レポート、要約など) が常に新しいページから始まるようにできます。これは、ドキュメントのフォーマット、印刷可能なレポート、または整理された出力の生成に最適です。

1. テーブルを作成して設定します。
1. テーブルにデータを追加します。
1. テーブルの新しいページを強制的に作成します。これにより、現在のページに既存のコンテンツがあっても、テーブルは新しいページの先頭から開始するようになります。
1. テーブルをページに追加します。'page.paragraphs.add () 'を使用してテーブルを PDF レイアウトに追加します。
1. 文書を保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def force_new_page(output_file_name):
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create a table
    table = ap.Table()
    table.column_widths = "150 150 150"
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL)

    # Add rows with sample data
    for i in range(5):
        row = table.rows.add()
        row.cells.add(f"Row {i + 1} - Col 1")
        row.cells.add(f"Row {i + 1} - Col 2")
        row.cells.add(f"Row {i + 1} - Col 3")

    # --- Key part: force table to start on a new PDF page ---
    table.is_in_new_page = True

    # Add table to page
    page.paragraphs.add(table)

    # Save the PDF
    document.save(output_file_name)
```

### PDF でのインライン段落プロパティの使用

ライブラリでは、「is_in_line_paragraph」プロパティを使用して、PDF内のテキストと画像間のインラインフローを制御できます。
通常、新しい要素（テキストフラグメントや画像など）を追加すると、各要素は新しい行または新しい段落から始まります。
'is_in_line_column = True' を設定すると、エレメントを同じ行または同じ段落内に表示させることができ、スムーズなインラインレイアウトを作成できます。文章内にロゴ、アイコン、記号を追加するなど、テキストと画像をインラインで組み合わせるのに最適です。

最初のテキストフラグメント、画像、および 2 番目のテキストフラグメントは同じ行に表示され、連続したインライン段落を形成します。
3 番目のテキストフラグメントは、デフォルトの改行動作を示す新しい段落の始まりです。

1. 新しい PDF ドキュメントを作成します。
1. 最初のテキストフラグメントを追加します。
1. インライン画像を挿入します。
1. インラインテキストをさらに追加します。
1. 新しい段落を追加します。
1. PDF を保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def using_inline_paragraph_property(output_file_name):
    # Create a PDF document
    document = ap.Document()
    page = document.pages.add()

    # --- First text fragment (normal paragraph) ---
    fragment1 = ap.text.TextFragment("This is the first part of the paragraph. ")
    fragment1.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment1.text_state.font_size = 14
    page.paragraphs.add(fragment1)

    # --- Inline image (continues same paragraph flow) ---
    image = ap.Image()
    image.is_in_line_paragraph = True  # Makes image inline with previous paragraph
    image.file = path.join(DATA_DIR, "logo.jpg")
    image.fix_height = 30
    image.fix_width = 30
    page.paragraphs.add(image)

    # --- Second inline text fragment (keeps same paragraph flow) ---
    fragment2 = ap.text.TextFragment("This is the second part of the same paragraph.")
    fragment2.is_in_line_paragraph = True
    fragment2.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment2.text_state.font_size = 14
    page.paragraphs.add(fragment2)

    # --- Third fragment (starts new paragraph automatically) ---
    fragment3 = ap.text.TextFragment("This is a new paragraph.")
    fragment3.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment3.text_state.font_size = 14
    page.paragraphs.add(fragment3)

    # Save PDF
    document.save(output_file_name)
```

### 複数列の PDF の作成

.NET 経由の Aspose.PDF for Python を使用して、PDF に複数列の新聞スタイルのレイアウトを作成します。
テキスト、HTML フォーマット、グラフィックを FloatingBox 内で組み合わせて、複数コラムの雑誌やニュースレターのデザインと同様の高度なレイアウト制御を可能にする方法を紹介しています。

1. PDF ドキュメントを初期化します。
1. 上部に水平の区切り線を追加します。
1. スタイル付きの HTML 見出しを追加します。
1. レイアウトコントロール用のフローティングボックスを作成します。
1. 複数列のレイアウトを設定します。
1. 著者情報を追加してください。
1. 別の内部水平線を引きます。
1. 記事のテキストを追加します。
1. 最終版の PDF を保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def create_multi_column_pdf(output_file_name):
    # Create PDF document
    document = ap.Document()

    # Set margins
    document.page_info.margin.left = 40
    document.page_info.margin.right = 40

    page = document.pages.add()

    #
    # Draw horizontal line at the top
    #
    graph1 = ap.drawing.Graph(500.0, 2.0)
    page.paragraphs.add(graph1)

    pos_arr = [1.0, 2.0, 500.0, 2.0]
    line1 = ap.drawing.Line(pos_arr)
    graph1.shapes.add(line1)

    #
    # Add HTML heading text
    #
    html = "<span style=\"font-family: 'Times New Roman'; font-size: 18px;\"><strong>How to Steer Clear of money scams</strong></span>"
    heading_text = ap.HtmlFragment(html)
    page.paragraphs.add(heading_text)

    #
    # Floating box: enables multi-column layout
    #
    box = ap.FloatingBox()

    box.column_info.column_count = 2  # Two columns
    box.column_info.column_spacing = "5"  # Space between columns
    box.column_info.column_widths = "105 105"  # Width of each column

    #
    # Add title text to the FloatingBox
    #
    text1 = ap.text.TextFragment("By A Googler (The Official Google Blog)")
    text1.text_state.font_size = 8
    text1.text_state.line_spacing = 2
    box.paragraphs.add(text1)

    text1.text_state.font_size = 10
    text1.text_state.font_style = ap.text.FontStyles.ITALIC

    #
    # Add another horizontal line inside the box
    #
    graph2 = ap.drawing.Graph(50.0, 10.0)

    pos_arr2 = [1.0, 10.0, 100.0, 10.0]
    line2 = ap.drawing.Line(pos_arr2)
    graph2.shapes.add(line2)

    box.paragraphs.add(graph2)

    #
    # Add long text content
    #
    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            lorem_text = f.read()
    else:
        lorem_text = "Lorem ipsum text not found."
    text2 = ap.text.TextFragment(lorem_text * 5)
    box.paragraphs.add(text2)

    page.paragraphs.add(box)

    # Save PDF
    document.save(output_file_name)
```

### PDF のテキスト配置用のカスタムタブストップ

テーブル構造に頼らずに、カスタムタブストップを使用してテーブルのようなテキストレイアウトをPDFに作成できます。
タブストップの位置、配置、およびリーダースタイルを定義することで、テキストを列全体で正確に揃えることができます。これは請求書、レポート、または構造化テキストデータに役立ちます。

1. 新しい PDF ドキュメントを作成します。
1. カスタムタブストップを定義します。
1. テキストには #$TAB プレースホルダーを使用してください。
1. PDF にテキストを追加します。
1. PDF を保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def custom_tab_stops(output_file_name):
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Define tab stops
    tab_stops = ap.text.TabStops()

    tab_stop1 = tab_stops.add(100)
    tab_stop1.alignment_type = ap.text.TabAlignmentType.RIGHT
    tab_stop1.leader_type = ap.text.TabLeaderType.SOLID

    tab_stop2 = tab_stops.add(200)
    tab_stop2.alignment_type = ap.text.TabAlignmentType.CENTER
    tab_stop2.leader_type = ap.text.TabLeaderType.DASH

    tab_stop3 = tab_stops.add(300)
    tab_stop3.alignment_type = ap.text.TabAlignmentType.LEFT
    tab_stop3.leader_type = ap.text.TabLeaderType.DOT

    # Create TextFragments with tab placeholders
    header = ap.text.TextFragment(
        "This is an example of forming table with TAB stops", tab_stops
    )
    text0 = ap.text.TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", tab_stops)
    text1 = ap.text.TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", tab_stops)

    text2 = ap.text.TextFragment("#$TABdata21 ", tab_stops)
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data22 "))
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data23"))

    # Add text fragments to page
    page.paragraphs.add(header)
    page.paragraphs.add(text0)
    page.paragraphs.add(text1)
    page.paragraphs.add(text2)

    # Save PDF document
    document.save(output_file_name)
```

### 関連テキストトピック

- [Python を使用して PDF 内のテキストを操作する](/pdf/ja/python-net/working-with-text/)
- [PDF へのテキストの追加](/pdf/ja/python-net/add-text-to-pdf-file/)
- [Python を使用して PDF 内のテキストを回転させる](/pdf/ja/python-net/rotate-text-inside-pdf/)
- [Python を使用して PDF 内のテキストを置き換える](/pdf/ja/python-net/replace-text-in-pdf/)

