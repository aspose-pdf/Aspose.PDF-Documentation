---
title: PDFにテキストを追加
linktitle: PDFにテキストを追加
type: docs
weight: 10
url: /ja/python-net/add-text-to-pdf-file/
description: この記事では、Aspose.PDFでテキストを扱うさまざまな側面を説明します。PDFへのテキストの追加、HTML フラグメントの追加、カスタム OTF フォントの使用方法を学びます。
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用した PDF へのテキスト追加
Abstract: この記事は、Python 用 Aspose.PDF ライブラリを使用して PDF ドキュメントを操作するための包括的なガイドを提供します。フォントサイズ、種類、色、位置などのテキストプロパティを設定することを含む、テキストの追加と書式設定に関するさまざまな手法をカバーしています。
---

このガイドでは、Aspose.PDF for Python via .NET を使用して PDF ドキュメントにテキストコンテンツを追加する方法を説明します。シンプルなテキストフラグメントを特定の位置に配置する方法から、フォント、サイズ、色、スタイルでの装飾、右から左 (RTL) 言語の取り扱い、ハイパーリンクの埋め込み、段落レイアウト、リスト、透明効果の扱いまで、テキスト挿入の基本技術を学びます。また、HTML や LaTeX フラグメントの使用、カスタムフォント、行間や文字間隔といったテキスト書式設定オプションなど、上級シナリオも取り上げています。

シンプルな注釈の作成からリッチなタイポグラフィレイアウトまで、このリソースは Aspose.PDF を使用した PDF のテキスト操作に必要な基本的な構成要素を提供します。

## 基本的なテキスト挿入

Aspose.PDF for Python via .NET は、PDF ファイル内のテキストを処理するための強力かつ柔軟な API を提供します。
シンプルな静的ラベル、リッチなフォーマットコンテンツ、多言語テキスト、インタラクティブなハイパーリンクが必要な場合でも、ツールキットを使えば簡潔な Python コードで実現できます。

### テキスト追加（シンプルケース）

Aspose.PDF for Python via .NET は、ページ上の特定の位置にシンプルなテキストフラグメントを追加する方法を示します。新しい PDF ドキュメントの作成、ページの追加、指定座標へのテキスト挿入、そして結果ファイルの保存方法を学びます。

1. 新しい[ドキュメント](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)オブジェクトを作成します。
1. `document.pages.add()` を使用して、新しい空白の[ページ](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)を作成します。
1. テキストコンテンツで[`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) を作成します。
1. [`Position`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/position/) クラスを使用してテキスト位置を設定します。`Position` を指定すると、テキストは左から右へ配置され、下方向にシフトします。
1. テキストの外観をカスタマイズします。フォントサイズ、色、フォントスタイルなどは [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) を介して設定できます。
`TextFragment` を `page.paragraphs.add(text_fragment)` でページの段落コレクションに追加します。
1. ドキュメントを保存します。

以下のコードスニペットは、既存の PDF ファイルにテキストを追加する方法を示しています：

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_simple_case(outfile):
    """
    Add simple text to a PDF document.
    Creates a new PDF document with a single page and adds a text fragment
    "Hello, Aspose!" at position (100, 600) on the page.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        >>> add_text_simple_case("output.pdf")
        # Creates a PDF file named "output.pdf" with "Hello, Aspose!" text
    """

    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 600)

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

このコード例は TextFragment を使用していますが、TextParagraph を使用して PDF ページにテキストを追加することもできます。その違いを見てみましょう。
**[TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)** は単一のテキスト片です。TextFragment はテキストの単位を表し、独立して配置、スタイル設定、位置指定が可能です。少量のシンプルなテキストを追加したい場合に最適です。

**[TextParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/)** は TextFragment の集合です。複数行のテキストを追加できます。TextParagraph は 1 つ以上の TextFragment オブジェクトのコンテナまたはコレクションであり、複数のフラグメントをまとめてブロックテキスト（複数行、単語、書式付き要素など）を作成したい場合に最適です。
TextParagraph はテキストの整列、行間、ページ上での自動レイアウトも管理します。赤線の使用は TextParagraph でのみ可能です。

テキスト操作に関する詳細は、[PDF 内のテキスト書式設定](/pdf/python-net/text-formatting-inside-pdf/) と [Python を使用した PDF からのテキスト抽出](/pdf/python-net/extract-text-from-pdf/) のドキュメントセクションをご確認ください。

### TextParagraph を使用したテキスト追加

Aspose.PDF for Python via .NET は、[`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) と [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) を使用して、折り返しオプション付きで段落テキストを追加できます。

1. `document.pages.add()` を使用して新しい[ドキュメント](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)と空白の[ページ](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)を作成します。
1. ファイルからテキストを読み込むか、デフォルトテキストを使用します。
1. レイアウトと折り返し制御付きの段落レベルコンテンツを追加するために、[`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) を作成します。
1. [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) を作成し、折り返しモードを設定します（例では `DISCRETIONARY_HYPHENATION` を使用）。
1. [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) を作成し、スタイルを適用してフラグメントを段落に追加します。
1. `TextBuilder` を使用して段落をページに追加します。
1. ドキュメントを保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_paragraph(outfile):
    """
    Add formatted text paragraph with indentation and wrapping to a PDF document.

    Creates a PDF document with a text paragraph that demonstrates advanced text
    formatting including first line indentation, text wrapping with discretionary
    hyphenation, and loading text content from an external file.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Attempts to load text from "lorem.txt" file in DATA_DIR
        - Falls back to default message if file doesn't exist
        - Uses Times New Roman font at 12pt size
        - First line indent: 20 points
        - Rectangle bounds: (80, 800, 400, 200)
        - Text wrapping: DISCRETIONARY_HYPHENATION mode for better line breaks

    Example:
        >>> add_text_paragraph("paragraph_text.pdf")
        # Creates a PDF with formatted paragraph text
    """
    document = ap.Document()
    page = document.pages.add()

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    if os.path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as file:
            text = file.read()
    else:
        text = "Lorem ipsum sample text not found."

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.first_line_indent = 20
    paragraph.rectangle = ap.Rectangle(80, 800, 400, 200, True)
    # paragraph.formatting_options.wrap_mode = TextFormattingOptions.WordWrapMode.BY_WORDS
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.DISCRETIONARY_HYPHENATION
    )

    fragment = ap.text.TextFragment(text)
    fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment.text_state.font_size = 12

    paragraph.append_line(fragment)
    builder.append_paragraph(paragraph)

    document.save(outfile)
```

![TextParagraph を使用したテキスト追加](text_paragraph.png)

### PDF でインデント付き段落を追加

以下のコードスニペットは、新しい PDF ドキュメントを作成し、異なるインデントスタイルを持つ 2 つの段落テキストを追加する方法を示しています：

- 最初の段落は最初の行インデント（最初の行だけがインデント）を示しています。

- 2 番目の段落は以降の行インデント（最初の行以外のすべての行がインデント）を示しています。

これは Aspose.PDF の 'TextParagraph'、'TextBuilder'、'TextFragment' クラスを使用して、レイアウトと書式設定を正確に制御します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_paragraphs_indents(output_file_name):
    """Add text with indents to a PDF document.
    Creates a PDF document with two text paragraphs demonstrating different
    indent styles. The first paragraph uses first line indent, while the
    second paragraph uses subsequent lines indent. Text content is loaded
    from a lorem.txt file if available, otherwise uses a fallback message.
    Args:
        output_file_name (str): The file path where the PDF document will be saved.
    Returns:
        None: The function saves the PDF document to the specified output file.
    Note:
        - Uses Times New Roman font at 12pt size
        - Text wrapping is set to wrap by words
        - First paragraph: 20pt first line indent, positioned at (80, 800, 300, 50)
        - Second paragraph: 20pt subsequent lines indent, positioned at (320, 800, 500, 50)
    """

    document = ap.Document()
    page = document.pages.add()

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    if os.path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as file:
            text = file.read()
    else:
        text = "Lorem ipsum sample text not found."

    fragment = ap.text.TextFragment(text)
    fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment.text_state.font_size = 12

    builder = ap.text.TextBuilder(page)
    paragraph1 = ap.text.TextParagraph()
    paragraph1.first_line_indent = 20
    paragraph1.rectangle = ap.Rectangle(80, 800, 300, 50, True)
    paragraph1.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    paragraph1.append_line(fragment)
    builder.append_paragraph(paragraph1)

    paragraph2 = ap.text.TextParagraph()
    paragraph2.subsequent_lines_indent = 20
    paragraph2.rectangle = ap.Rectangle(320, 800, 500, 50, True)
    paragraph2.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    paragraph2.append_line(fragment)
    builder.append_paragraph(paragraph2)
    document.save(output_file_name)
```

### PDF に新しいテキスト行を追加

Aspose.PDF for Python via .NET は、TextFragment、TextParagraph、TextBuilder クラスを使用して、PDF ドキュメントに複数行テキストを挿入することを可能にします。

1. 新しいドキュメントを作成します。
1. 改行文字を含む TextFragment を定義します。
1. テキストのスタイルを設定します。
1. フラグメントを段落に追加します。
1. 段落の位置を設定します。
1. ページ上に段落を描画します。
1. ドキュメントを保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_new_line(output_file):
    """Add a new line of text to a PDF document."""
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Initialize new TextFragment with text containing required newline markers
    text_fragment = ap.text.TextFragment("Applicant Name: " + os.linesep + " Joe Smoe")

    # Set text fragment properties if necessary
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red

    # Create TextParagraph object
    par = ap.text.TextParagraph()

    # Add new TextFragment to paragraph
    par.append_line(text_fragment)

    # Set paragraph position
    par.position = ap.text.Position(100, 600)

    # Create TextBuilder object
    text_builder = ap.text.TextBuilder(page)

    # Add the TextParagraph using TextBuilder
    text_builder.append_paragraph(par)

    # Save PDF document
    document.save(output_file)
```

### PDFで改行を判定し通知をログに記録する

PDF ドキュメントに複数のテキストフラグメントを含め、レイアウトイベント（改行やテキストの折り返しなど）をレンダリング中に監視するために Aspose.PDF の通知ロギングを有効にする方法を示しています。

1. 新しい PDF ドキュメントを作成します。
1. 通知ロギングを有効にします。
1. document.pages.add() を使用して最初のページを作成します。
1. 複数のテキストフラグメントを追加します。
1. page.paragraphs.add(text) を使用して各テキストフラグメントを描画します。
1. ドキュメントを保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def determine_line_break(output_file):
    """Create a PDF document with multiple text fragments and log notifications."""
    # Create PDF document
    document = ap.Document()

    # Enable notification logging
    document.enable_notification_logging = True

    page = document.pages.add()

    for i in range(4):
        text = ap.text.TextFragment(
            "Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, "
            "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
            "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
            "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
            "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
            "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
            "culpa qui officia deserunt mollit anim id est laborum."
        )
        text.text_state.font_size = 20
        page.paragraphs.add(text)

    # Save PDF document
    document.save(output_file)

    notifications = document.pages[1].get_notifications()
    print(notifications)
```

### PDFでテキスト幅を動的に測定する

特定のフォントで文字や文字列の幅を動的に測定する方法を Aspose.PDF for Python via .NET で示します。'Font.measure_string()' と 'TextState.measure_string()' メソッドを使用して、測定された文字列幅が一貫して正確であることを検証します。

1. 'FontRepository.find_font()' を使用してリポジトリから Arial フォントオブジェクトを取得します。
1. フォントプロパティを管理する TextState オブジェクトを作成します。
1. 個々の文字を測定します。
1. 'A' から 'z' までのすべての文字について、両方のメソッドの結果を比較します。
1. 両方の測定手法が同じ結果を出すことを確認します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_text_width_dynamically(output_file):

    font = ap.text.FontRepository.find_font("Arial")
    ts = ap.text.TextState()
    ts.font = font
    ts.font_size = 14

    if math.fabs(font.measure_string("A", 14) - 9.337) > 0.001:
        print("Unexpected font string measure!")

    if math.fabs(ts.measure_string("z") - 7.0) > 0.001:
        print("Unexpected font string measure!")

    c_code = ord("A")
    while c_code <= ord("z"):
        c = chr(c_code)

        fn_measure = font.measure_string(str(c), 14)
        ts_measure = ts.measure_string(str(c))

        if math.fabs(fn_measure - ts_measure) > 0.001:
            print("Font and state string measuring doesn't match!")

        c_code += 1
```

### ハイパーリンク付きテキストの追加

Aspose.PDF for Python via .NET を使用して PDF 内のテキストにクリック可能なハイパーリンクを追加します。当ライブラリは、単一の TextFragment 内に複数のテキストセグメントを追加し、特定のセグメントにハイパーリンクを適用し、テキストセグメントを個別にスタイル設定（例：色、斜体フォント）する方法を示します。

1. 'Document()' と 'document.pages.add()' を使用して新しいドキュメントとページを作成し、空白のページを追加します。
1. TextFragment を作成します。
1. �数の TextSegment オブジェクトを追加します。各セグメントは独自のコンテンツとスタイルを持つことができます。例えば、プレーンテキストやハイパーリンクテキストなどです。
1. セグメントにハイパーリンクを適用します。desired URL を使用して WebHyperlink オブジェクトを作成します。
1. セグメントのスタイルを設定します。text_state を使用して色、フォントスタイル、サイズなどをカスタマイズします。
1. 'page.paragraphs.add()' を使用してフラグメントをページに追加します。
1. PDF を保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_with_hyperlink(outfile):
    """
    Add text with embedded hyperlinks to a PDF document.

    Creates a PDF document with a text fragment containing multiple segments,
    including one with a hyperlink to Aspose. Demonstrates how to create
    clickable links within PDF text content with different formatting.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Creates 4 text segments within a single text fragment
        - One segment contains a hyperlink to "https://products.aspose.com/pdf"
        - Hyperlinked text is styled in blue italic font
        - Other segments are regular text without links

    Example:
        >>> add_text_with_hyperlink("hyperlink_text.pdf")
        # Creates a PDF with clickable Aspose link in the text
    """

    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment(
        "Sample Text Fragment"
    )

    segment = ap.text.TextSegment(" ... Text Segment 1...")
    fragment.segments.append(segment)

    segment = ap.text.TextSegment("Link to Aspose")
    fragment.segments.append(segment)
    segment.hyperlink = ap.WebHyperlink("https://products.aspose.com/pdf")
    segment.text_state.foreground_color = ap.Color.blue
    segment.text_state.font_style = ap.text.FontStyles.ITALIC

    segment = ap.text.TextSegment("TextSegment without hyperlink")
    fragment.segments.append(segment)

    page.paragraphs.add(fragment)
    document.save(outfile)
```

![PDFに表示されたテキストフラグメントで、Sample Text Fragment の後に Text Segment 1、次に青いハイパーリンクテキスト「Link to Aspose」（https://products.aspose.com/pdf にリンク）が続き、最後にハイパーリンクなしの黒いテキストで TextSegment が続く混合コンテンツ](hyperlink_text.png)

### PDFドキュメントに右から左 (RTL) テキストを追加する

RTL（右から左へ）は、テキストの書き方向を示すプロパティで、テキストが右から左へ書かれます。
Aspose.PDF for Python via .NET は、アラビア語やヘブライ語などの右から左へ (RTL) テキストを PDF ドキュメントに追加する方法を示します。

1. 'Document()' と 'document.pages.add()' を使用して新しいドキュメントとページを作成し、空白ページを追加します。
1. RTL コンテンツを持つ TextFragment を作成します。フラグメントの内容としてアラビア語、ヘブライ語、またはその他の RTL 言語のテキストを挿入します。
フォントとスタイリングを設定します。RTL スクリプトをサポートするフォント（例：Tahoma、Arial Unicode MS）を選択します。必要に応じて font_size と foreground_color を設定します。
1. 'text_fragment.horizontal_alignment' を使用して水平揃えを右に設定します。
1. テキストフラグメントをページに追加します。
1. PDF ドキュメントを保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_with_rtl_text(outfile):
    """
    Add right-to-left (RTL) text to a PDF document.

    Creates a PDF document with Arabic text that demonstrates right-to-left text
    rendering and alignment. The text uses the Tahoma font which supports Arabic
    characters and is aligned to the right side of the page.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses Tahoma font at 14pt size for proper Arabic character support
        - Text color is set to blue
        - Horizontal alignment is set to RIGHT for proper RTL display
        - The Arabic text describes Nasreddin Hodja, a folklore character

    Example:
        >>> add_text_with_rtl_text("arabic_text.pdf")
        # Creates a PDF with right-to-left Arabic text
    """

    document = ap.Document()
    page = document.pages.add()
    # Styled text fragment
    text_fragment = ap.text.TextFragment(
        "يعتبر خوجا نصر الدين شخصية فولكلورية من الشرق الإسلامي وبعض شعوب البحر الأبيض المتوسط ​​والبلقان، وهو بطل القصص والحكايات القصيرة الفكاهية والساخرة، وأحيانًا الحكايات اليومية."
    )
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Tahoma")
    text_fragment.text_state.font_size = 14
    text_fragment.text_state.foreground_color = ap.Color.blue
    text_fragment.horizontal_alignment = ap.HorizontalAlignment.RIGHT

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

![右から左へのテキスト](rtl_text.png)

## テキストのスタイリング

### フォントスタイル付きテキストの追加

これは、テキストスタイリング、フォントのカスタマイズ、混合フォーマットテキスト（下付きテキストセグメントの使用）を示す高度な例です。Aspose.PDF は、フォントファミリー、サイズ、色、太字、斜体、下線などのフォントプロパティをテキストフラグメントに適用する方法を説明します。
さらに、このコードスニペットは、単一のフラグメント内で複数のテキストセグメントを使用して複雑なテキスト表現を作成する方法を示します。たとえば、数式や科学的表記でしばしば必要とされる下付きや上付き文字を含めることができます。

1. 'Document()' と 'document.pages.add()' を使用して新しいドキュメントとページを作成し、空白のページを追加します。
1. シンプルなスタイルテキスト用の TextFragment を作成します。
1. テキストコンテンツを定義します。
1. Position(x, y) 座標を使用して位置を設定します。
1. 'text_state'プロパティを使用してスタイリングを適用します - フォント、font_size、foreground_color、font_style、underline。
1. 複数の TextSegment オブジェクトを使用して複合式を作成します。各 TextSegment は独自のスタイルを持つテキストの一部を表します。これにより、数式や化学式などの式を構築できます。
1. 複数の TextState オブジェクトを定義します。メインテキスト用 (text_state_letters) と、下付きまたは上付きテキスト用 (text_state_index) の2つです。
1. テキストセグメントを結合します。各セグメントを 'segments.append()' を使用して 'TextFragment' に追加します。
1. 両方のテキストオブジェクトをページに追加します。'page.paragraphs.add()' を使用してドキュメントに配置します。
1. 最終的なドキュメントを保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_with_font_styling(outfile):
    """
    Add styled text fragments to a PDF document.
    Creates a new PDF document with a single page and adds a styled text fragment
    "Hello, Aspose!" at position (100, 600) and a formula with styled segments at position (100, 500).
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        >>> add_text_with_font_styling("styled_text.pdf")
        # Creates a PDF file named "styled_text.pdf" with styled text and a formula
    """

    document = ap.Document()
    page = document.pages.add()

    # Initialize an empty TextFragment to build a formula using segments
    formula = ap.text.TextFragment()
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.text_state.foreground_color = ap.Color.blue
    text_fragment.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    text_fragment.text_state.underline = True
    text_fragment.horizontal_alignment = ap.HorizontalAlignment.LEFT

    text_state_letters = ap.text.TextState()
    text_state_letters.font = ap.text.FontRepository.find_font("Arial")
    text_state_letters.font_size = 14
    text_state_letters.foreground_color = ap.Color.blue
    text_state_letters.font_style = ap.text.FontStyles.BOLD

    text_state_index = ap.text.TextState()
    text_state_index.font = ap.text.FontRepository.find_font("Arial")
    text_state_index.font_size = 14
    text_state_index.foreground_color = ap.Color.dark_red
    # text_state_index.superscript = True
    text_state_index.subscript = True

    position = ap.text.Position(100, 500)

    # Helper function to add segments
    def add_segment(text, state):
        seg = ap.text.TextSegment(text)
        seg.text_state = state
        seg.position = position
        formula.segments.append(seg)

    add_segment("S = a", text_state_letters)
    add_segment("2n", text_state_index)
    add_segment(" + a", text_state_letters)
    add_segment("2n+1", text_state_index)
    add_segment(" + a", text_state_letters)
    add_segment("2n+2", text_state_index)
    formula.horizontal_alignment = ap.HorizontalAlignment.LEFT

    page.paragraphs.add(text_fragment)
    page.paragraphs.add(formula)
    document.save(outfile)
```

![青いイタリック体Arialフォントで「Hello, Aspose!」というテキストが表示され、その後に青い本文テキストと赤い下付き文字で S = a₂ₙ + a₂ₙ+₁ + a₂ₙ+₂ の数式が続くテキストフラグメントです](styled_text.png)

## テキストを透明に追加

Aspose.PDF for Python を使用して、PDFドキュメントに半透明の形状とテキストを追加します。
部分的な不透明度を持つカラー矩形を作成し、透明な前景色の TextFragment を重ね合わせます。

1. Document オブジェクトを初期化し、描画用の空白ページを追加します。
1. 'ap.drawing.Graph' を使用して、図形を描画できるキャンバスを作成します。
1. 半透明の塗りつぶしを持つ矩形を追加します。
1. キャンバスの位置シフトを防止します。
1. キャンバスをページに追加します。ページの段落コレクションにグラフィック形状を挿入します。
1. 透明なテキストフラグメントを作成します。
1. テキストフラグメントをページの段落コレクションに挿入します。
1. PDFドキュメントを保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_transparent(outfile):
    """
    Add transparent text over a semi-transparent background to a PDF document.

    Creates a PDF document with a semi-transparent filled rectangle as background
    and transparent green text overlaid on top. This demonstrates how to create
    transparency effects in PDF documents using ARGB color values.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Background rectangle: 128 alpha, light purple color (0xC5, 0xB5, 0xFF)
        - Text transparency: 30 alpha, green color (0, 255, 0)
        - The canvas is set to not change position to prevent layout shifts

    Example:
        >>> add_text_transparent("transparent_output.pdf")
        # Creates a PDF with transparent text effects
    """

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create Graph object
    canvas = ap.drawing.Graph(100.0, 400.0)

    # Create rectangle with semi-transparent fill
    rect = ap.drawing.Rectangle(100, 100, 400, 400)
    rect.graph_info.fill_color = ap.Color.from_argb(128, 0xC5, 0xB5, 0xFF)
    canvas.shapes.add(rect)

    # Prevent position shift
    canvas.is_change_position = False
    page.paragraphs.add(canvas)

    # Create transparent text
    text = ap.text.TextFragment(
        "This is the transparent text. "
        "This is the transparent text. "
        "This is the transparent text."
    )
    text.text_state.foreground_color = ap.Color.from_argb(30, 0, 255, 0)
    page.paragraphs.add(text)

    document.save(outfile)
```

### PDFに不可視テキストを追加

この例では、可視テキストと不可視テキストの両方を含む PDF ドキュメントの作成方法を示します。不可視テキストはドキュメント構造の一部として残りますが、表示されないため、レイアウトに影響を与えずにメタデータ、アクセシビリティタグ、検索可能なコンテンツを埋め込むのに役立ちます。

1. PDF ドキュメントとページを作成します。
1. 繰り返し表示されるコンテンツを持つテキストフラグメントを作成します。
1. 2つ目のテキストフラグメントを追加し、不可視としてマークします。
1. ドキュメントを保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_invisible(outfile):
    """
    Creates a PDF document with both visible and invisible text.
    This function generates a PDF file containing two text fragments:
    one visible text that will be displayed normally, and one invisible
    text that will be hidden from view but still present in the document.
    Args:
        outfile (str): The file path where the PDF document will be saved.
    Returns:
        None: The function saves the PDF to the specified file path.
    Example:
        add_text_invisible("output.pdf")
    """

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Add visible text
    text1 = ap.text.TextFragment(
        "This is the visible text. "
        "This is the visible text. "
        "This is the visible text."
    )
    page.paragraphs.add(text1)

    # Create transparent text
    text2 = ap.text.TextFragment(
        "This is the invisible text. "
        "This is the invisible text. "
        "This is the invisible text."
    )
    text2.text_state.invisible = True
    page.paragraphs.add(text2)

    document.save(outfile)
```

### PDFで枠線スタイリング付きテキストを追加

Aspose.PDF ライブラリは、可視の枠線を持つスタイル化されたテキストフラグメントを含む PDF ドキュメントの作成方法を示しています。この手法では、背景色と前景色、フォント設定、およびテキスト矩形の周囲にストローク（枠線）を適用して視覚的な強調を高めます。

1. PDF ドキュメントとページを作成します。
1. テキストフラグメントを作成し配置します。メッセージを含むテキストフラグメントを追加し、位置を設定します。
1. テキストのスタイリングを適用します。フォントを Times New Roman、サイズ 12 に設定し、薄いグレーの背景と赤の前景（テキスト）色を適用します。
1. 枠線のスタイリングを構成します。
1. ページにテキストを追加します。TextBuilder を使用してスタイル化されたテキストをページに追加します。
1. ドキュメントを保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_border(output_file_name):
    """
    Add text with border styling to a PDF document.

    Creates a PDF document with a text fragment that has border styling applied.
    The text includes background color, foreground color, and a configurable
    border (stroke) around the text rectangle.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "This is sample text with border."
        - Font: Times New Roman, 12pt
        - Background: Light gray
        - Foreground: Red text
        - Border: Dark red stroke around text rectangle
        - Position: (10, 700)
        - Border is only visible when draw_text_rectangle_border is True

    Example:
        >>> add_text_border("bordered_text.pdf")
        # Creates a PDF with bordered text styling
    """
    # Create PDF document
    document = ap.Document()
    # Get particular page
    page = document.pages.add()
    # Create text fragment
    text_fragment = ap.text.TextFragment("This is sample text with border.")
    text_fragment.position = ap.text.Position(10, 700)

    # Set text properties
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red
    # Set StrokingColor property for drawing border (stroking) around text rectangle.
    # Note: This only affects the border if draw_text_rectangle_border is set to True.
    text_fragment.text_state.stroking_color = ap.Color.dark_red
    # Enable drawing of the text rectangle border
    text_fragment.text_state.draw_text_rectangle_border = True

    text_builder = ap.text.TextBuilder(page)
    text_builder.append_text(text_fragment)

    # Save PDF document
    document.save(output_file_name)
```

### PDFに取り消し線テキストを追加

PDF ドキュメントのテキストフラグメントに取り消し線（ストライクスルー）フォーマットを追加します。取り消し線テキストは、削除や修正、強調を示すのに役立ちます。

1. 'Document()' を使用して新しいドキュメントとページを作成し、'document.pages.add()' で空白ページを追加します。
1. テキストフラグメントを作成してスタイル設定します。
1. 色と取り消し線のフォーマットを適用します。背景を薄いグレー、テキスト色を赤に設定し、取り消し線を有効にします。
1. テキストの位置を設定します。
1. 'TextBuilder' を使用してスタイル化されたテキストをページに追加します。
1. ドキュメントを保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_strikeout_text(output_file_name):
    """
    Add text with strikeout (strikethrough) formatting to a PDF document.

    Creates a PDF document with a text fragment that has strikeout formatting applied.
    The text appears with a line through it, along with additional styling including
    background color, foreground color, and bold font style.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "This is sample strikeout text."
        - Font: Times New Roman, 12pt, Bold
        - Background: Light gray
        - Foreground: Red text
        - Strikeout: Enabled (line through text)
        - Position: (100, 600)

    Example:
        >>> add_strikeout_text("strikeout_text.pdf")
        # Creates a PDF with strikethrough text formatting
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create text fragment
    text_fragment = ap.text.TextFragment("This is sample strikeout text.")
    # Set text properties
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red
    text_fragment.text_state.strike_out = True
    text_fragment.text_state.font_style = ap.text.FontStyles.BOLD
    text_fragment.position = ap.text.Position(100, 600)

    # Create TextBuilder object
    text_builder = ap.text.TextBuilder(page)
    text_builder.append_text(text_fragment)

    # Save PDF document
    document.save(output_file_name)
```

## 高度なカラーエフェクト

### PDFのテキストに軸方向グラデーションを適用する

Aspose.PDF for Python via .NET は、PDF ドキュメントのテキストに線形グラデーション効果を適用する方法を示しています。軸方向グラデーションはテキスト全体で赤から青へ滑らかに変化し、視覚的に際立った見出しを作成します。この手法は、スタイリッシュなタイトル、ブランディング、または PDF レイアウトの装飾要素に最適です。

1. 新しいドキュメントを初期化し、空白ページを追加します。
1. テキストフラグメントを作成してスタイル設定します。タイトルを追加し、位置、フォント、サイズを設定します。
1. 'GradientAxialShading' を使用して軸方向グラデーションシェーディングを適用します。前景色を赤から青への GradientAxialShading で設定します。
1. 下線のスタイルを追加します。
1. スタイル化されたテキストフラグメントをページに挿入します。
1. ドキュメントを保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def apply_gradient_axial_shading_to_text(output_file_name):
    """
    Apply axial gradient shading to text in a PDF document.

    Creates a PDF document with large title text that has an axial (linear) gradient
    effect applied. The gradient transitions from red to blue in a linear fashion
    across the text. This demonstrates advanced text styling with gradient effects.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "PDF TITLE"
        - Font: Arial Bold, 36pt
        - Position: (100, 600)
        - Gradient: Linear gradient from red to blue
        - Additional styling: Underlined text
        - Uses GradientAxialShading for linear gradient effect

    Example:
        >>> apply_gradient_axial_shading_to_text("gradient_axial.pdf")
        # Creates a PDF with linear gradient text effect
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("PDF TITLE")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font_size = 36
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial Bold")

    text_fragment.text_state.foreground_color = ap.Color()
    text_fragment.text_state.foreground_color.pattern_color_space = (
        ap.drawing.GradientAxialShading(ap.Color.red, ap.Color.blue)
    )
    text_fragment.text_state.underline = True

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

### PDFのテキストに放射状グラデーションを適用する

放射状グラデーションは、テキストの中心から外側へ放射する円形の色変化を作り出し、タイトル、ヘッダー、装飾要素などに視覚的にダイナミックなスタイリングオプションを提供します。

1. 新しいドキュメントを初期化し、空白ページを追加します。
1. テキストフラグメントを作成してスタイル設定します。タイトルを追加し、位置、フォント、サイズを設定します。
1. 'GradientRadialShading' を使用して放射状グラデーションを適用します。前景色を赤から青への GradientRadialShading で設定します。
1. 下線スタイルを追加します。
1. スタイル付けされたテキストフラグメントをページに挿入します。
1. ドキュメントを保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def apply_gradient_radial_shading_to_text(output_file_name):
    """
    Apply radial gradient shading to text in a PDF document.

    Creates a PDF document with large title text that has a radial (circular) gradient
    effect applied. The gradient radiates from the center outward, transitioning from
    red to blue. This demonstrates advanced text styling with radial gradient effects.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "PDF TITLE"
        - Font: Arial Bold, 36pt
        - Position: (100, 600)
        - Gradient: Radial gradient from red to blue
        - Additional styling: Underlined text
        - Uses GradientRadialShading for circular gradient effect

    Example:
        >>> apply_gradient_radial_shading_to_text("gradient_radial.pdf")
        # Creates a PDF with radial gradient text effect
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("PDF TITLE")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font_size = 36
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial Bold")

    # Apply radial gradient shading (red to blue)
    text_fragment.text_state.foreground_color = ap.Color()
    text_fragment.text_state.foreground_color.pattern_color_space = (
        ap.drawing.GradientRadialShading(ap.Color.red, ap.Color.blue)
    )
    text_fragment.text_state.underline = True

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![放射状グラデーションシェーディングを適用](gradient_radial_shading.png)

## HTML と LaTeX フラグメント

### PDF ドキュメントに HTML テキストを追加

Aspose.PDF for Python via .NET ライブラリを使用すると、HtmlFragment クラスを使って HTML 形式のコンテンツを PDF ドキュメントに挿入できます。HTML タグを使用することで、スタイル付き、構造化された、または数式のようなテキストを PDF に直接レンダリングできます。

1. 'Document()' を使用して新しいドキュメントとページを作成し、'document.pages.add()' で空白ページを追加します。
1. HtmlFragment クラスのインスタンスを作成し、HTML 文字列をパラメータとして渡します。
1. 'page.paragraphs.add()' を使用してフラグメントをページに追加し、HTML コンテンツを挿入します。
1. PDF を保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_html_fragment(outfile):
    """
    Add HTML fragment with mathematical notation to a PDF document.

    Creates a PDF document containing an HTML fragment that displays mathematical
    notation using HTML tags including subscript and superscript elements.
    This demonstrates how to embed formatted HTML content directly into PDF.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses HTML <pre> tags to preserve formatting
        - Includes <sub> for subscript (2n) and <sup> for superscript (2)
        - Formula displayed: S=a₂ₙ+a²
        - HTML is rendered as formatted content within the PDF

    Example:
        >>> add_text_html_fragment("html_math.pdf")
        # Creates a PDF with HTML mathematical notation
    """

    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.HtmlFragment("<pre>S=a<sub>2n</sub>+a<sup>2</sup><pre>")

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

![PDF ドキュメントに HTML テキストを追加](html_fragment.png)

### PDF ドキュメントにさまざまな書式設定を持つスタイル付き HTML フラグメントを追加

HTML フラグメントを定義し、HTML タグで直接テキストスタイルを設定できます。スタイル付き HTML コンテンツを PDF ドキュメントに埋め込みます。このコードスニペットは新しい PDF ファイルを作成し、ページを追加し、見出し、段落、リンク、インラインスタイルなどさまざまな書式要素を含む HTML フラグメントを挿入し、指定されたパスに結果を保存します。

1. PDF を表す新しい Document オブジェクトを初期化します。
1. HTML コンテンツが配置される空白ページをドキュメントに追加します。
1. HTML コンテンツを準備します。HTML 文字列には h1 見出し、緑色の段落（太字、斜体、下線付きテキスト）と、フォントサイズが大きく設定されたウェブサイトへのハイパーリンクが含まれています。
1. HTML フラグメントを作成します。HTML 文字列を HtmlFragment オブジェクトでラップします。
1. HTML をページに挿入します。HTML フラグメントをページの段落コレクションに追加し、HTML をネイティブ PDF コンテンツとしてレンダリングします。
1. ドキュメントを保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_html_fragment(outfile):
    """
    Add styled HTML fragment with various formatting to a PDF document.

    Creates a PDF document containing rich HTML content including headings,
    paragraphs with inline formatting, colored text, and hyperlinks.
    Demonstrates comprehensive HTML rendering capabilities in PDF.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Includes HTML heading (h1) with blue color styling
        - Contains paragraph with bold, italic, and underlined text
        - Features green-colored paragraph text
        - Includes styled hyperlink to Aspose website
        - All HTML styling is preserved in the PDF output

    Example:
        >>> add_html_fragment("rich_html.pdf")
        # Creates a PDF with various HTML formatting elements
    """

    document = ap.Document()
    page = document.pages.add()
    html_content = """
        <h1 style='color:blue;'>Hello, Aspose!</h1>
        <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
        <p style='color:green;'>This paragraph is green.</p>
        <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
    """
    html_fragment = ap.HtmlFragment(html_content)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![PDF ドキュメントに HTML コンテンツを追加](html_content.png)

### テキスト状態を上書きした HTML フラグメントを追加

前の例で見たように、HTML コード内で直接スタイルを設定することが可能です。これには利点がありますが、欠点もあります。顧客の HTML を扱っていて、出力の外観を統一したいとします。
この場合、以下の例に示すように、独自の TextState を使用して顧客のスタイルを上書きすることができます。

1. 'Document()' を使用して新しいドキュメントとページを作成し、'document.pages.add()' で空白ページを追加します。
1. HTML コンテンツを準備します。HTML 文字列には Verdana フォントの h1 見出し、緑色の段落（太字、斜体、下線付きテキスト）と、フォントサイズが大きく設定されたウェブサイトへのハイパーリンクが含まれています。
1. HTML フラグメントを作成します。HTML 文字列を HtmlFragment オブジェクトでラップします。
1. テキスト書式を上書きします。TextState オブジェクトを作成し、フォント、フォントサイズ、テキストカラーを設定します。
1. HTML フラグメントをページの段落コレクションに追加します。
1. ドキュメントを保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_html_fragment_override_text_state(outfile):
    """
    Add HTML fragment with overridden text styling to a PDF document.

    Creates a PDF document with HTML content where the default text styling
    is overridden using TextState properties. This demonstrates how to apply
    global text formatting that supersedes HTML styling for consistent appearance.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - HTML includes heading, paragraphs, and links with original styling
        - TextState override applies: Arial font, 14pt size, red color
        - Override styling takes precedence over HTML inline styles
        - Useful for enforcing consistent document-wide text appearance
        - Original HTML styling is replaced by the TextState properties

    Example:
        >>> add_html_fragment_override_text_state("html_override.pdf")
        # Creates a PDF where HTML styling is overridden with red Arial text
    """

    document = ap.Document()
    page = document.pages.add()
    html_content = """
        <h1 style='color:blue;font-family:Verdana'>Hello, Aspose!</h1>
        <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
        <p style='color:green;'>This paragraph is green.</p>
        <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
    """
    html_fragment = ap.HtmlFragment(html_content)
    html_fragment.text_state = ap.text.TextState()
    html_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    html_fragment.text_state.font_size = 14
    html_fragment.text_state.foreground_color = ap.Color.red

    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![HTML フラグメントでテキスト状態を上書き](html_override.png)

### PDF ドキュメントに LaTeX テキストを追加

Aspose.PDF for Python via .NET の TeXFragment クラスを使用して、LaTeX 形式の数式を PDF ドキュメントに追加します。
LaTeX は科学・数学文書の作成に広く用いられる強力な組版システムです。TeXFragment を使用すると、LaTeX の数式表記や記号を PDF ページ内に直接レンダリングできます。

1. 'Document()' を使用して新しいドキュメントとページを作成し、'document.pages.add()' で空白ページを追加します。
1. TeXFragment クラスを使用して LaTeX 構文を直接レンダリングします。
1. 'page.paragraphs.add()' で LaTeX コンテンツを PDF レイアウトに追加します。
1. PDF を保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_latex_fragment(outfile):
    """
    Add LaTeX mathematical expression to a PDF document.

    Creates a PDF document containing a complex mathematical expression rendered
    from LaTeX markup. This demonstrates advanced mathematical typesetting
    capabilities using LaTeX syntax within PDF documents.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses LaTeX TeXFragment for mathematical expression rendering
        - Expression includes overbrace and underbrace notation
        - Formula: (a+b)⁶ · (c+d)⁷ with braces and labels = 42
        - LaTeX commands: \\overbrace, \\underbrace, \\text, \\cdot
        - Provides professional mathematical typography

    Example:
        >>> add_text_latex_fragment("latex_math.pdf")
        # Creates a PDF with complex LaTeX mathematical expression
    """

    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.TeXFragment(
        "\\underbrace{\\overbrace{a+b}^6 \\cdot \\overbrace{c+d}^7}_\\text{example of text} = 42"
    )

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

![PDF に表示された複雑な数式。LaTeX の (a+b)⁶ の上に overbrace、全体式 (a+b)⁶·(c+d)⁷ の下に underbrace を用いた数式で、テキスト例としてラベル付けされ、結果は 42 です。LaTeX のレンダリング特有の適切な間隔と括弧スタイルを示す高度な数式組版です。](latex_fragment.png)

## カスタムフォント

### ファイルからカスタムフォントを使用

この例では、Aspose.PDF for Python via .NET でカスタム OpenType フォントを使用して PDF ファイルにテキストを追加する方法を示します。新しい PDF ドキュメントの作成、ページ上へのテキストの正確な配置、フォントタイプ、サイズ、カラー、斜体などのカスタム書式設定の適用方法がわかります。

1. 新しい PDF ドキュメントを作成し、ページを追加します。
1. PDF に追加したいテキストコンテンツを定義します。
1. テキストの位置を設定します。
1. TextFragment をページに追加します。
1. PDFドキュメントを保存します。

この機能はOTFだけでなくTTFフォントでも動作します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def use_custom_font_from_file(outfile):
    """
    Creates a PDF document with text using a custom font loaded from a file.
    This function demonstrates how to load a custom OpenType font (.otf) from the file system
    and apply it to text in a PDF document. The text is styled with blue color, italic style,
    and positioned at specific coordinates on the page.
    Args:
        outfile (str): The output file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file path.
    Note:
        - Requires the "BriosoPro Italic.otf" font file to be present in the DATA_DIR directory
        - Uses Aspose.PDF library for PDF generation and text manipulation
        - The text fragment is positioned at coordinates (100, 600) on the page
        - Font size is set to 24 points with blue foreground color and italic style
    """

    font_path = os.path.join(DATA_DIR, "BriosoPro Italic.otf")
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("Hello, Aspose!")
    fragment.position = ap.text.Position(100, 600)
    fragment.text_state.font = ap.text.FontRepository.open_font(font_path)
    fragment.text_state.font_size = 24
    fragment.text_state.foreground_color = ap.Color.blue
    fragment.text_state.font_style = ap.text.FontStyles.ITALIC

    page.paragraphs.add(fragment)
    document.save(outfile)
```

![PDFドキュメントに表示されたテキストフラグメントで、Hello, Aspose! が青いイタリック体のBriosoProフォントで描画され、カスタムOpenTypeフォントの統合とスタイリング機能をPDFテキストフォーマット内で示しています](custom_font.png)

### ストリームからカスタムフォントを使用する

このコードスニペットは、Aspose.PDF for Python via .NET を使用して、カスタム埋め込み OpenType (OTF) フォントで PDF ドキュメントにテキストを追加する方法を示しています。フォントファイルをストリームとして開き、PDF に埋め込んで異なるシステム間でフォントの利用可能性を確保し、フォントサイズ、色、イタリックスタイルなどのテキスト書式設定を適用する手順を示します。このアプローチは、インストールされたフォントがなくても、共有や閲覧時にタイポグラフィを保持した視覚的に一貫した PDF を作成するのに最適です。

1. フォントファイルをバイナリストリームとしてロードします。
1. 'FontRepository.open_font' を使用してフォントを開き、埋め込みます。
1. 新しい PDF ドキュメントを作成し、ページを追加します。
1. 次の設定でスタイル付きテキストフラグメントを追加します。
- 埋め込みカスタムフォント。
- イタリック体スタイルと青色。
- 特定のフォントサイズと位置。
1. 最終ドキュメントを指定された出力パスに保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def use_custom_font_from_stream(outfile):
    """Use custom font from stream."""

    font_path = os.path.join(DATA_DIR, "BriosoPro Italic.otf")
    with open(font_path, "rb") as font_stream:
        font = ap.text.FontRepository.open_font(font_stream, ap.text.FontTypes.OTF)
        font.is_embedded = True

        document = ap.Document()
        page = document.pages.add()

        fragment = ap.text.TextFragment("Hello, Aspose!")
        fragment.position = ap.text.Position(100, 600)
        fragment.text_state.font = font
        fragment.text_state.font_size = 14
        fragment.text_state.foreground_color = ap.Color.blue
        fragment.text_state.font_style = ap.text.FontStyles.ITALIC

        page.paragraphs.add(fragment)
        document.save(outfile)
```

フォントを埋め込むことで、プラットフォーム間で一貫したレンダリングが保証されるため、このアプローチはブランディング、デザインの忠実度、マルチ言語サポートに最適です。

