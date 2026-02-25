---
title: Python を使用した PDF 内のテキストフォーマット
linktitle: PDF 内のテキストフォーマット
type: docs
weight: 70
url: /ja/python-net/text-formatting-inside-pdf/
description: Aspose.PDF を使用して、Python で PDF ファイル内のテキストフォーマットオプションを探求し、カスタマイズされた文書のスタイリングを実現します。
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF のテキストを編集する方法
Abstract: この記事では、Aspose.PDF for Python via .NET を使用した PDF 文書におけるさまざまなテキストフォーマット手法について包括的なガイドを提供します。行のインデント追加、テキスト境界の作成、下線の付与、打ち消し線の追加など、幅広い機能を網羅しています。
---

## 行と文字の間隔

### 行間の使用

#### Python でカスタム行間を使用してテキストをフォーマットする方法 - シンプルなケース

Aspose.PDF for Python は、行間調整によってテキストのレイアウトと可読性を制御するシンプルなアプローチを示します。

このコードスニペットは、PDF ドキュメントで行間を制御する方法を示しています。ファイルからテキストを読み込み（またはフォールバックメッセージを使用）、カスタムフォントサイズと行間を適用し、フォーマットされたテキストを PDF の新しいページに追加します。

1. 新しい PDF ドキュメントを作成します。
1. ソーステキストを読み込みます。
1. TextFragment オブジェクトを初期化し、読み込んだテキストを割り当てます。
1. テキストのフォントと間隔のプロパティを設定します。この値は、テキスト行の間隔がどれだけ密になるか、または緩くなるかを決定します。
- フォントサイズ: 12 ポイント
- 行間: 16 ポイント
1. フォーマットされたテキストフラグメントをページの段落コレクションに挿入します。
1. ドキュメントを保存します。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def specify_line_spacing_simple_case(outfile):
    """
    Specify custom line spacing for text in a PDF document.

    Creates a PDF document with text that has custom line spacing applied.
    Loads text content from an external file and applies 16-point line spacing
    to improve readability and text layout.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Attempts to load text from "lorem.txt" file in DATA_DIR
        - Falls back to default message if file doesn't exist
        - Font size: 12 points
        - Line spacing: 16 points (increased from default for better readability)
        - Demonstrates basic line spacing control in PDF text formatting

    Example:
        >>> specify_line_spacing_simple_case("line_spacing.pdf")
        # Creates a PDF with custom 16-point line spacing
    """

    document = ap.Document()
    page = document.pages.add()

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )

    text_fragment = ap.text.TextFragment(text)
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.line_spacing = 16
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

#### Python でカスタム行間を使用してテキストをフォーマットする方法 - 特定のケース

カスタム TrueType フォント（TTF）を使用して、PDF ドキュメントで異なる行間モードを適用する方法を確認してみましょう。
ファイルからテキストを読み込み、特定のフォントを埋め込み、同じテキストを PDF ページに 2 回描画します—それぞれ異なる行間モードを使用します：

- FONT_SIZE モード: 行間はフォントサイズと同じです。
- FULL_SIZE モード: 行間はフォントの全高さ（上昇部と下降部を含む）を考慮します。

この例は、選択したモードに応じて行間の挙動がどのように変わるかを示しています。

1. 新しい PDF ドキュメントを作成します。
1. カスタムフォントファイルとテキストソースファイルの両方のパスを指定します。
1. テキスト内容を読み込みます。
1. カスタムフォントを開きます。
1. 最初の TextFragment（FONT_SIZE モード）を作成して構成します。line_spacing を 'TextFormattingOptions.LineSpacingMode.FONT_SIZE' に設定し、行間がフォントサイズと同じになることを意味します。
1. 2 番目の TextFragment（FULL_SIZE モード）を作成して構成します。line_spacing を 'TextFormattingOptions.LineSpacingMode.FULL_SIZE' に設定し、フォントの全高さを使用します。
1. 両方のテキストフラグメントを同じ PDF ページに追加します。
1. 完成したドキュメントを指定された出力場所に保存します。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def specify_line_spacing_specific_case(outfile):
    """
    Create a PDF document demonstrating different line spacing modes with custom font.
    This function creates a PDF with two text fragments using the same custom TTF font
    but different line spacing modes to demonstrate the visual differences between
    FONT_SIZE and FULL_SIZE line spacing options.
    Args:
        outfile (str): Path where the output PDF file will be saved.
    Notes:
        - Requires 'HPSimplified.ttf' font file in DATA_DIR
        - Requires 'lorem.txt' text file in DATA_DIR for content
        - Falls back to default text if lorem.txt is not found
        - First fragment uses FONT_SIZE line spacing mode
        - Second fragment uses FULL_SIZE line spacing mode
    Dependencies:
        - aspose.pdf (ap) library
        - os module for file path operations
        - DATA_DIR constant must be defined
    """

    document = ap.Document()
    page = document.pages.add()

    font_file = os.path.join(DATA_DIR, "HPSimplified.ttf")
    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )

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

![行間をカスタム設定したテキストを表示する PDF ドキュメント（読みやすさとレイアウトの向上のために 16 ポイントの行間）](line_spacing.png)

### 文字間隔の使用

#### TextFragment クラスを使用して PDF テキストの文字間隔を制御する方法

文字間隔は、テキスト行内の各文字間の距離を決定します—テキストの外観を微調整したり、特定のタイポグラフィ効果を実現するのに役立ちます。

1. 新しい Document オブジェクトを初期化し、テキスト配置用の空白ページを追加します。
1. フラグメントジェネレータを定義します。ヘルパー関数 make_fragment(spacing): を実装します。
- サンプルテキストで TextFragment を作成します。
- フォントを設定します。
1. 異なる間隔値でテキストフラグメントを追加します。
1. Document を保存します。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def character_spacing_using_text_fragment(outfile):
    """
    Demonstrate character spacing control using TextFragment objects.

    Creates a PDF document showing different character spacing values applied
    to text fragments. Each line demonstrates progressively increased character
    spacing to illustrate the visual effect on text appearance.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Creates multiple TextFragment objects with varying character spacing
        - Character spacing values: 0, 1, 2, 3, and 4 points
        - Font: Times Roman, 12 points
        - Each fragment is positioned on a new line for comparison
        - Character spacing affects only horizontal letter spacing
        - Higher values create more space between individual characters

    Example:
        >>> character_spacing_using_text_fragment("char_spacing_fragment.pdf")
        # Creates a PDF showing progressive character spacing effects
    """
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

![PDFドキュメントは、文字間隔が段階的に狭くなる様子を示す、同一テキスト「Sample Text」の3行を表示したもので、上部の行は文字間が広く、途中の行は中程度、下部の行は最も狭い文字間隔で、PDFテキストフォーマットにおける異なる文字間隔値の視覚効果を示しています](character_spacing_simple.png)

#### TextParagraph と TextBuilder を使用した PDF テキストの文字間隔の制御方法

Aspose.PDF は、TextParagraph と TextBuilder を使用して PDF ドキュメントにテキストを追加する際に、カスタム文字間隔を適用することができます。
ページ上に特定の領域を定義し、テキストの折り返しを設定し、文字間隔が調整されたテキストフラグメントをレンダリングします。

正確なテキスト配置とレイアウトの制御が必要な場合、たとえば構造化されたテキストブロックや複数列のテキストブロックを作成する際には、TextParagraph の使用が理想的です。

1. 新しい PDF ドキュメントを作成します。
1. ページ用に TextBuilder インスタンスを初期化します。
1. TextParagraph を作成し、設定します。
- 単語単位の折り返しモードを 'TextFormattingOptions.WordWrapMode.BY_WORDS' に設定します。
1. カスタム文字間隔を持つ TextFragment を作成します。
- 新しい TextFragment を作成し、そのテキストを設定します（例: "Sample Text with character spacing"）。
- Arial などのフォント属性とフォントサイズ 14 pt を指定します。
- 文字間隔 = 2.0 を適用します。これにより文字間が広がります。
1. TextFragment を TextParagraph に追加します。
1. TextParagraph をページに追加します。
1. PDF ドキュメントを保存します。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def character_spacing_using_text_paragraph(outfile):
    """
    Demonstrate character spacing control using TextParagraph objects.

    Creates a PDF document with text paragraph that has custom character spacing
    applied. Shows how to set character spacing at the paragraph level and
    demonstrates the visual effect on text layout.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses TextParagraph for paragraph-level formatting
        - Character spacing: 2.0 points
        - Font: Times Roman, 12 points
        - Demonstrates paragraph-based character spacing control
        - Character spacing applies to all text within the paragraph
        - Alternative approach to fragment-based character spacing

    Example:
        >>> character_spacing_using_text_paragraph("char_spacing_paragraph.pdf")
        # Creates a PDF with paragraph-level character spacing
    """
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

PDF ファイルを扱う際、箇条書きや番号付きリスト、HTML や LaTeX でフォーマットされたリストなど、構造化された情報を表示する必要がある場合があります。
Aspose.PDF for Python via .NET は、PDF ドキュメント内でリストを直接作成およびフォーマットする柔軟な方法をいくつか提供し、レイアウト、フォント、スタイルを完全に制御できます。

この記事では、プレーンテキストのフォーマットから高度な HTML や LaTeX のレンダリングまで、PDF でリストを作成する複数のアプローチを示します。各手法は、正確なプログラム的制御を好む場合や、便利なマークアップベースのスタイリングを好む場合など、特定のユースケースに対応しています。

この記事の最後までに、以下を理解できるようになります：

- TextParagraph と TextBuilder を使用してカスタムの箇条書きリストと番号付きリストを作成する。

- HTML フラグメント（HtmlFragment）を使用して、PDF 内で '<ul>' と '<ol>' リストを簡単にレンダリングする。

- LaTeX フラグメント（TeXFragment）を活用して、数式や科学的なリストのフォーマットを行う。

- ページ内でテキストの折り返し、フォントスタイル、レイアウト位置を制御する。

- 手動によるリスト構築とマークアップ駆動アプローチの違いを理解する。

### 箇条書きリストの作成

HTML や LaTeX のフォーマットに依存せず、TextParagraph と TextBuilder を使用して PDF にカスタム箇条書きリストを作成します。
各リスト項目は箇条書き文字 (•) が前置され、個別の TextFragment として追加されます。

1. Document オブジェクトを初期化し、空白ページを追加します。
1. 箇条書きに変換する文字列の Python リストを定義します。
1. TextBuilder と TextParagraph を作成します。
1. 'TextBuilder' を使用して、設定した段落をページに追加します。
1. PDF ドキュメントを保存します。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list(outfile):
    """
    Create a PDF document with a bullet list using plain text formatting.
    This function generates a PDF document containing a bullet list with predefined items.
    The list is formatted with bullet points, uses Times New Roman font, and includes
    text wrapping behavior for longer items.
    Args:
        outfile (str): The file path where the PDF document will be saved.
    Returns:
        None: The function saves the document to the specified file path.
    Note:
        The bullet list is positioned within a rectangle at coordinates (80, 200, 400, 800)
        and uses word wrapping mode for text formatting.
    """

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

### 番号付きリストの作成

HTML や LaTeX のフォーマットに依存せず、TextParagraph と TextBuilder を使用して PDF にカスタム番号付き（順序付き）リストを作成します。
各リスト項目はその番号（例: 1., 2.）が前置され、個別の TextFragment として追加されます。

1. Document オブジェクトを初期化し、空白ページを追加します。
1. 番号付きリスト項目に変換する文字列の Python リストを定義します。
1. TextBuilder と TextParagraph を作成します。
1. 各項目を番号付きの TextFragment として追加します。
1. TextBuilder を使用して、設定した段落をページに追加します。
1. PDF ドキュメントを保存します。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list(outfile):
    """
    Create a numbered list in a PDF document using plain text formatting.
    This function generates a PDF document containing a numbered list with predefined
    items. The list is formatted with Times New Roman font and includes text wrapping
    by words within a specified rectangular area on the page.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified file path but does
              not return any value.
    Note:
        - Uses Aspose.PDF library (imported as 'ap')
        - List items are hardcoded within the function
        - Font: Times New Roman, size 12
        - Text wrapping: BY_WORDS mode
        - Rectangle bounds: (80, 200, 400, 800)
    """

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

### 箇条書きリストの HTML バージョン作成

当ライブラリでは、HTML フラグメントを使用して PDF ドキュメントに箇条書き（順序なし）リストを作成する方法を示します。Python の文字列リストを HTML `<ul>` 要素に変換し、HtmlFragment として PDF ページに挿入します。HTML フラグメントを使用すると、リストや太字、斜体などの HTML フォーマット機能を PDF 内で直接活用できます。

1. 新しい PDF ドキュメントを作成し、ページを追加します。
1. リスト項目を準備します。
1. リストを HTML の順序なしリストに変換します。
- `<ul>` タグを使用して、順序なし（箇条書き）リストを作成します。
- リスト内包表記を使用して、各項目を 'li' タグでラップします。
1. HtmlFragment を作成します。HTML 文字列を PDF ページに追加できる HtmlFragment オブジェクトに変換します。
1. HtmlFragment をページの段落コレクションに挿入します。
1. PDF ドキュメントを保存します。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list_html_version(outfile):
    """
    Create a bulleted list using HTML formatting in a PDF document.

    Generates a PDF with an unordered (bulleted) list created using HTML markup.
    Demonstrates how to use HtmlFragment to embed HTML list structures directly
    into PDF documents with proper formatting and styling.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses HTML <ul> and <li> tags for list structure
        - Items are predefined with sample content
        - HtmlFragment automatically handles HTML rendering
        - Lists maintain proper bullet formatting and indentation
        - Simpler alternative to manual list creation with TextFragments
        - Supports nested lists and HTML styling if needed

    Example:
        >>> create_bullet_list_html_version("bullet_list_html.pdf")
        # Creates a PDF with HTML-formatted bulleted list
    """

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

![PDF ドキュメントに表示された箇条書きリストで、4つの項目が示されています：リストの最初の項目、折り返し動作を示すためにテキストが多い2番目の項目、3番目の項目、4番目の項目。各項目は標準の箇条点で始まり、HTML 形式のリストが PDF 構造内で適切なインデントと間隔でレンダリングされることを示しています](bullet_list_html.png)

### 番号付きリストの HTML バージョンを作成

HTML フラグメントを使用して PDF ドキュメントに番号付き（順序付け）リストを作成します。Python の文字列リストを HTML の `<ol>` 要素に変換し、HtmlFragment として PDF ページに挿入します。

HTML フラグメントを使用すると、番号付きリスト、太字、斜体などの HTML ベースの書式設定機能を PDF に直接組み込むことができます。

1. 新しい PDF ドキュメントを作成し、ページを追加します。
1. リスト項目を準備します。
1. リストを HTML の順序付きリストに変換します。
- 番号付きリストには `<ol>` タグを使用します。
- リスト内包表記を使用して各項目を 'li' タグでラップします。
1. HTML 文字列を PDF ページに追加できる HtmlFragment オブジェクトに変換します。
1. HtmlFragment をページの段落コレクションに挿入します。
1. PDF ドキュメントを保存します。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list_html_version(outfile):
    """
    Create a numbered list using HTML formatting in a PDF document.

    Generates a PDF with an ordered (numbered) list created using HTML markup.
    Demonstrates how to use HtmlFragment to embed HTML ordered list structures
    directly into PDF documents with automatic numbering and formatting.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses HTML <ol> and <li> tags for ordered list structure
        - Items are predefined with sample content
        - HtmlFragment automatically handles HTML rendering and numbering
        - Lists maintain proper numeric formatting and indentation
        - Numbers are automatically generated (1, 2, 3, etc.)
        - Supports nested lists and custom numbering styles if needed

    Example:
        >>> create_numbered_list_html_version("numbered_list_html.pdf")
        # Creates a PDF with HTML-formatted numbered list
    """

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

![PDF ドキュメントに表示された番号付きリストで、4つの自動番号付けされた項目が示されています：1. リストの最初の項目、2. 折り返し動作を示すためにテキストが多い2番目の項目、3. 3番目の項目、4. 4番目の項目。リストは PDF 構造内で HTML 形式の順序付きリストが適切な数値順序、インデント、項目間の間隔でレンダリングされることを示しています](numbered_list_html.png)

### 箇条書きリスト LaTeX バージョンの作成

LaTeX フラグメント（TeXFragment）を使用して PDF に箇条書き（順不同）リストを作成します。Python の文字列リストを LaTeX の itemize 環境に変換し、PDF ページに挿入します。数式、シンボル、または正確な書式設定が必要な構造化リストをレンダリングしたい場合、LaTeX フラグメントの使用が最適です。

1. 新しい PDF ドキュメントを作成し、ページを追加します。
1. LaTeX の itemize 環境で箇条点になる Python の文字列リストを定義します。
1. リストを LaTeX の itemize 環境に変換します：
- アイテムを \begin{itemize} と \end{itemize} で囲みます。
- 各項目はリスト内包表記を使用して \item で前置されます。
1. LaTeX 文字列を PDF にレンダリングできる TeXFragment オブジェクトに変換します。
1. LaTeX フラグメントをページに追加します。
1. PDF ドキュメントを保存します。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list_latex_version(outfile):
    """
    Create a bulleted list using LaTeX formatting in a PDF document.

    Generates a PDF with an unordered list created using LaTeX markup.
    Demonstrates how to use TeXFragment to embed LaTeX itemize environments
    directly into PDF documents with proper mathematical and scientific formatting.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses LaTeX \\begin{itemize} and \\item commands
        - TeXFragment handles LaTeX compilation and rendering
        - Supports mathematical expressions and scientific notation
        - Lists maintain proper bullet formatting and indentation
        - More powerful than HTML for mathematical content
        - Can include LaTeX math modes and special symbols

    Example:
        >>> create_bullet_list_latex_version("bullet_list_latex.pdf")
        # Creates a PDF with LaTeX-formatted bulleted list
    """

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

![PDF に表示された箇条書きリストで、LaTeX でレンダリングされた書式設定とテキストが示されています。テキスト「Lists are easy to create:」の後に、4つの箇条点項目：最初の項目、折り返し動作を示すテキストが多い2番目の項目、3番目の項目、4番目の項目。リストは、適切な箇条点書式、一定の間隔、テキスト折り返し機能を備えたプロフェッショナルな LaTeX タイポグラフィが、クリーンな PDF 文書レイアウト内でデモンストレーションされています](bullet_list_latex.png)

### 番号付きリスト LaTeX バージョンの作成

LaTeX フラグメント（TeXFragment）を使用して PDF に番号付き（順序付け）リストを作成します。Python の文字列リストを LaTeX の enumerate 環境に変換し、PDF ページに挿入します。正確な書式設定、構造化リスト、または数式を PDF に組み込みたい場合、LaTeX フラグメントの使用が理想的です。

1. 新しい PDF ドキュメントを作成し、ページを追加します。
1. LaTeX の enumerate 環境で番号付き項目になる Python の文字列リストを定義します。
1. リストを LaTeX の enumerate 環境に変換します。
1. LaTeX 文字列を PDF にレンダリングできる TeXFragment オブジェクトに変換します。
1. LaTeX フラグメントをページに追加します。
1. PDF ドキュメントを保存します。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list_latex_version(outfile):
    """Create a numbered list using LaTeX."""

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

![PDF に表示された番号付きリストで、LaTeX でレンダリングされた書式設定と項目が示されています：1. 最初の項目、2. 折り返し動作を示すテキストが多い2番目の項目、3. 3番目の項目、4. 4番目の項目。テキスト「Lists are easy to create」に続く形で表示されています](numbered_list_latex.png)

## フットノートとエンドノート

### フットノートの追加

フットノートは、文書本文内で関連するテキストの横に連続した上付き数字を配置して、注記を参照するために使用されます。これらの数字は、通常インデントされ、同ページの下部に配置された詳細な注記に対応し、追加の文脈、引用、またはコメントを提供します。

Aspose.PDF for Python via .NET を使用して、PDF ドキュメントのテキストフラグメントにフットノートを追加します。フットノートは、本文の内容を乱さずに補足情報、引用、または注釈を提供するのに便利です。この方法により、フットノートが PDF レイアウトに視覚的かつ構造的に統合されます。

1. 新しいドキュメントを作成します。
1. 主なコンテンツを含む TextFragment を作成します。
1. インラインテキストを追加します。同じ段落で続く別の TextFragment を作成します。
1. ドキュメントを保存します。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote(outfile):
    """Add footnote to a PDF document."""

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

### カスタムスタイルのフットノートを PDF に追加

1. 新しい PDF ドキュメントを初期化し、空白ページを追加します。
1. メインテキストフラグメントを作成します。
1. フットノートを作成し、スタイル設定（フォント、サイズ、色、スタイル）を行います。
1. スタイル設定されたテキストフラグメント（フットノート付き）をページに挿入します。
1. フットノートなしの別のテキストフラグメントを追加します。
1. ドキュメントを保存します。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_custom_text_style(outfile):
    """Add footnote with custom text style."""

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

### PDFでカスタム記号を使用した脚注の追加

Aspose.PDF for Python via .NET を使用して PDF ドキュメントのテキストフラグメントに脚注を追加し、脚注マーカー記号をカスタマイズできるようにします。

1. PDF ドキュメントとページを作成します。
1. カスタム脚注記号付きの最初のテキストフラグメントを追加します。
1. 脚注なしで段落を続ける別のテキストフラグメントを追加します。
1. デフォルト脚注付きの2番目のテキストフラグメントを追加します。
1. ドキュメントを保存します。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_custom_text(outfile):
    """
    Add footnote with custom text marker to a PDF document.
    Creates a PDF document with text fragments that include footnotes with custom
    styling. The function demonstrates how to add footnotes with custom text markers
    and standard footnotes to different text fragments within the same document.
    Args:
        outfile (str): The output file path where the PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        add_footnote_custom_text("output_with_footnotes.pdf")
    Note:
        The document will contain:
        - Text with a custom footnote marker ("*")
        - Text without footnotes
        - Text with a standard footnote
    """

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

### PDFでカスタムラインスタイルを使用した脚注の追加

Python ライブラリを使用して PDF ドキュメントの脚注ラインの視覚的外観をカスタマイズします。脚注ラインをカスタマイズすると、視覚的な明瞭さが向上し、レポート、学術論文、注釈付き出版物などの文書でスタイルの一貫性が保たれます。

1. 新しい PDF ドキュメントを作成し、ページを追加します。
1. 脚注コネクタ用にカスタムラインスタイル（色、幅、破線パターン）を定義します。
1. 複数の脚注付きテキストフラグメントを追加します。
1. 最終ドキュメントを保存します。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_with_custom_line_style(outfile):
    """
    Add footnotes with custom line style to a PDF document.
    Creates a PDF document with text fragments that have footnotes and applies
    a custom line style for the footnote separator line. The custom style includes
    red color, increased line width, and dashed pattern.
    Args:
        outfile (str): Path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        >>> add_footnote_with_custom_line_style("output.pdf")
        # Creates a PDF with footnoted text and custom separator line styling
    """

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

### PDFで画像と表を使用した脚注の追加

Aspose.PDF for Python via .NET を使用して画像、スタイル付きテキスト、表を埋め込むことで、PDF ドキュメントの脚注を強化する方法は？

1. 新しい PDF ドキュメントを作成し、ページを追加します。
1. 添付脚注付きのテキストフラグメントを追加します。
1. 脚注内に画像、スタイル付きテキスト、表を埋め込みます。
1. ドキュメントを保存します。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_with_image_and_table(outfile):
    """
    Add a footnote containing an image and table to a PDF document.
    Creates a new PDF document with sample text that includes a footnote. The footnote
    contains three elements: an image (logo.jpg), descriptive text, and a simple table
    with two cells. The image is resized to 20x20 pixels and the footnote text uses
    a 20pt font size.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Note:
        - Requires the logo.jpg file to be present in the DATA_DIR directory
        - Uses the Aspose.PDF library (imported as 'ap')
        - The footnote is attached to the main text fragment on the page
    """

    document = ap.Document()
    page = document.pages.add()

    text = ap.text.TextFragment("This is a sample text with a footnote.")
    page.paragraphs.add(text)

    note = ap.Note()

    # Add image
    image_note = ap.Image()
    image_note.file = os.path.join(DATA_DIR, "logo.jpg")
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

### PDF ドキュメントへの文末脚注の追加

文末脚注は、引用文やパラフレーズされた考え、要約された内容の完全な参照情報を文書の最後の指定されたセクションに示すための引用タイプです。文末脚注を使用する際には、参照された資料のすぐ後に上付き番号が配置され、読者は文書の末尾にある対応する脚注へと誘導されます。

このコードスニペットは、PDF ドキュメントのテキストフラグメントに文末脚注を追加する方法を示しています。脚注が参照テキストの近くに表示されるのとは異なり、文末脚注は通常、文書やセクションの最後に配置されます。このメソッドは、文末脚注が長文コンテンツでどのように動作するかを示すために、長い文書をシミュレートする例も含んでいます。

1. PDF ドキュメントとページを作成します。
1. 文末脚注付きのテキストフラグメントを追加します。
1. 外部テキストコンテンツを読み込みます。
1. 長文ドキュメントをシミュレートします。読み込んだテキストを複数回追加して、より長い文書を模倣します。
1. ドキュメントを保存します。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_endnote(outfile):
    """Add endnote to a PDF document.
    Creates a new PDF document with a text fragment containing an endnote,
    followed by additional lorem ipsum content to simulate a longer document.
    The endnote is attached to the first text fragment and will be displayed
    according to the PDF viewer's endnote handling.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file path.
    Note:
        This function requires the aspose-pdf library and assumes the existence
        of a DATA_DIR variable pointing to a directory containing 'lorem.txt'.
        If the lorem.txt file is not found, fallback text will be used.
    """

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    page.paragraphs.add(text_fragment)

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text_content = (
        open(lorem_path, encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum sample text not found."
    )

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

### PDFでカスタムマーカー文字を使用した文末脚注の追加

PDF ドキュメントのテキストフラグメントに文末脚注を追加し、カスタムマーカー記号（例: "***"）を使用します。文末脚注は通常、文書やセクションの最後に配置され、追加のコンテキストや引用、コメントを提供するのに役立ちます。

1. PDF ドキュメントとページを作成します。
1. スタイル付きテキストフラグメントに文末脚注を追加します。
1. 文末脚注のマーカー文字をカスタマイズします。
1. .txt ファイルから外部コンテンツを読み込みます。
1. 文末脚注の配置を示すために長文コンテンツをシミュレートします。
1. PDF ドキュメントを保存します。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_endnote_custom_text(outfile):
    """
    Add endnote with custom text marker to a PDF document.
    Creates a PDF document with a text fragment that contains an endnote with
    a custom marker ("***"). The document is populated with sample text content
    from a lorem.txt file, repeated multiple times to simulate a longer document.
    Args:
        outfile (str): Path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file path.
    Note:
        - Requires lorem.txt file in DATA_DIR for sample content
        - Falls back to default text if lorem.txt is not found
        - Uses Arial font with 14pt size for all text elements
        - The endnote marker is set to "***" instead of default numbering
    """

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    text_fragment.end_note.text = "***"
    page.paragraphs.add(text_fragment)

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text_content = (
        open(lorem_path, encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum sample text not found."
    )

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

## レイアウトとページ制御

### PDFでテーブルを新しいページで開始させる

Aspose.PDF for Python via .NET を使用して、PDF ドキュメント内で特定のコンテンツを新しいページから開始させます。
プロパティ 'is_in_new_page' を設定することで、ページレイアウトと構造を正確に制御でき、テーブルやレポート、サマリーなどの特定のセクションが常に新しいページから開始するように保証します。これは、文書のフォーマット、印刷用レポート、または整理された出力生成に最適です。

1. テーブルを作成し、構成します。
1. テーブルにデータを追加します。
1. テーブルの新しいページへの開始を強制します。これにより、現在のページに既存のコンテンツがある場合でも、テーブルが新しいページの上部から開始します。
1. テーブルをページに追加します。'page.paragraphs.add()' を使用してテーブルを PDF レイアウトに組み込みます。
1. ドキュメントを保存します。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def force_new_page(output_file_name):
    """
    Create a PDF document demonstrating forced page breaks with tables.

    Creates a PDF document with a table that is forced to start on a new page
    using the is_in_new_page property. This is useful for controlling page layout
    and ensuring specific content starts on fresh pages.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Creates a 3-column table with 5 rows of sample data
        - Table uses uniform column widths of 150 units each
        - All cells have borders for clear visual separation
        - is_in_new_page=True forces the table to start on a new page
        - Useful for reports, documents with sections, or content organization

    Example:
        >>> force_new_page("new_page_table.pdf")
        # Creates a PDF with a table that starts on a new page
    """
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

### PDFでインライン段落プロパティを使用する

当ライブラリでは、PDF 内のテキストと画像間のインラインフローを制御するために、'is_in_line_paragraph' プロパティを使用できます。
通常、新しい要素（テキストフラグメントや画像など）を追加すると、各要素は新しい行または新しい段落から開始します。
'is_in_line_paragraph = True' を設定することで、要素を同じ行または同じ段落内に表示させ、スムーズなインラインレイアウトを作成できます。これは、ロゴやアイコン、シンボルを文章内に挿入するなど、テキストと画像をインラインで組み合わせるのに最適です。

最初のテキストフラグメント、画像、2 番目のテキストフラグメントが同じ行に表示され、連続したインライン段落を形成します。
3番目のテキストフラグメントは新しい段落を開始し、デフォルトの改行動作を示しています。

1. 新しいPDFドキュメントを作成します。
1. 最初のテキストフラグメントを追加します。
1. インライン画像を挿入します。
1. さらにインラインテキストを追加します。
1. 新しい段落を追加します。
1. PDFを保存します。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def using_inline_paragraph_property(output_file_name):
    """
    Demonstrate inline paragraph behavior in PDF document layout.

    Creates a PDF document showing how the is_in_line_paragraph property affects
    the flow of text and images. Elements with this property continue the flow
    of the previous paragraph instead of starting a new one.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - First text fragment starts a new paragraph
        - Image with is_in_line_paragraph=True continues the same line
        - Second text fragment also continues the same paragraph line
        - Third text fragment starts a new paragraph (default behavior)
        - Demonstrates inline flow control for mixed content (text + images)
        - Image is resized to 30x30 pixels and flows inline with text

    Example:
        >>> using_inline_paragraph_property("inline_paragraph.pdf")
        # Creates a PDF demonstrating inline paragraph flow
    """
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
    image.file = os.path.join(DATA_DIR, "logo.jpg")
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

### マルチカラムPDFを作成

Aspose.PDF for Python via .NET を使用して、PDFでマルチカラムの新聞スタイルレイアウトを作成します。
FloatingBox 内でテキスト、HTML 書式設定、グラフィックを組み合わせる方法を示し、マルチカラムの雑誌やニュースレターのデザインに似た高度なレイアウト制御を可能にします。

1. PDFドキュメントを初期化します。
1. 上部に水平セパレータラインを追加します。
1. スタイル付けされたHTML見出しを追加します。
1. レイアウト制御のために FloatingBox を作成します。
1. マルチカラムレイアウトを構成します。
1. 著者情報を追加します。
1. 別の内部水平線を描画します。
1. 記事テキストを追加します。
1. 最終的なPDFを保存します。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_multi_column_pdf(output_file_name):
    """
    Create a PDF document with multi-column layout using FloatingBox.

    Creates a professional-looking PDF with a multi-column newspaper-style layout.
    Demonstrates advanced layout techniques including floating boxes, column
    configuration, and mixed content with graphics and text.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Document margins: 40 points left and right
        - Top horizontal line for visual separation
        - HTML-formatted heading with custom styling
        - FloatingBox with 2-column layout (105 units wide each)
        - Column spacing: 5 units between columns
        - Includes author attribution with italic styling
        - Internal horizontal line within the floating box
        - Long text content automatically flows between columns
        - Demonstrates professional document layout techniques

    Example:
        >>> create_multi_column_pdf("multi_column_layout.pdf")
        # Creates a PDF with newspaper-style multi-column layout
    """
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
    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    lorem_text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )
    text2 = ap.text.TextFragment(lorem_text * 5)
    box.paragraphs.add(text2)

    page.paragraphs.add(box)

    # Save PDF
    document.save(output_file_name)
```

### PDFでのテキスト配置のためのカスタムタブストップ

テーブル構造に依存せず、カスタムタブストップを使用してPDFでテーブルのようなテキストレイアウトを作成します。
タブストップの位置、配置、リーダースタイルを定義することで、列全体でテキストを正確に揃えることができます。これは請求書、レポート、または構造化されたテキストデータに便利です。

1. 新しいPDFドキュメントを作成します。
1. カスタムタブストップを定義します。
1. テキストで #$TAB プレースホルダーを使用します。
1. テキストをPDFに追加します。
1. PDFを保存します。

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def custom_tab_stops(output_file_name):
    """
    Create a PDF document demonstrating custom tab stops for table-like formatting.

    Creates a PDF document that uses custom tab stops to format text in a table-like
    structure without using actual table elements. This demonstrates advanced text
    formatting with precise positioning and leader styles.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Tab stop 1: Position 100, right-aligned, solid leader line
        - Tab stop 2: Position 200, center-aligned, dashed leader line
        - Tab stop 3: Position 300, left-aligned, dotted leader line
        - Uses #$TAB placeholder for tab positions in text
        - Creates table-like structure with headers and data rows
        - Demonstrates mixing TextFragment and TextSegment approaches
        - Leader lines provide visual guides between columns
        - Alternative to HTML tables for precise text positioning

    Example:
        >>> custom_tab_stops("custom_tabs.pdf")
        # Creates a PDF with custom tab stop formatting
    """
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
