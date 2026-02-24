---
title: Python を使用して PDF 内のテキストを回転
linktitle: PDF 内のテキスト回転
type: docs
weight: 50
url: /ja/python-net/rotate-text-inside-pdf/
description: Aspose.PDF for Python を使用して、Python で PDF ドキュメント内のテキストを回転させ、柔軟な文書フォーマットを実現する方法を探ります。
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF のテキストを回転させる方法
Abstract: この記事では、.NET 経由で Python 用 Aspose.PDF ライブラリを使用して PDF ドキュメント内のテキストを回転させる方法について詳しく解説します。`TextFragment` クラスの `Rotation` プロパティを利用して、さまざまな角度でテキストを回転させる方法を説明し、複数の文書生成シナリオで役立ちます。指定した回転角度でテキストフラグメントを作成し、`TextBuilder` を使用して PDF ページに追加する方法をデモンストレーションします。回転したテキストフラグメントを `TextParagraph` に追加し、段落を PDF ページに配置する方法を示します。ページの段落コレクションに直接回転テキストフラグメントを追加する方法を示します。複数のテキストフラグメントを含む段落全体の回転についても解説します。
---

Aspose.PDF for Python via .NET を使用して PDF ドキュメント内のテキストフラグメントを回転させます。'TextFragment'、'TextState'、'TextBuilder' クラスを組み合わせて、個々のテキスト要素の位置と回転を正確に制御する方法を示します。各テキストフラグメントの回転角度を調整することで、対角線ヘッダー、垂直ラベル、回転注釈など、視覚的にダイナミックなレイアウトを作成できます。

## PDF で TextBuilder を使用したテキストフラグメントの回転

水平に配置された 3 つのテキストフラグメントを含む rotated_fragments.pdf という PDF ファイルを作成します:

- 最初のテキストは回転していません
- 2 番目のテキストは 45° 回転しています
- 3 番目のテキストは 90° 回転しています

1. 新しい PDF ドキュメントを作成します。
1. 回転したテキストを配置する新しいページを挿入します。
1. 最初のテキストフラグメントを作成します - 回転なし。
1. 2 番目のテキストフラグメントを作成します - 45° 回転。
1. 3 番目のテキストフラグメントを作成します - 90° 回転。
1. TextBuilder を使用してテキストフラグメントを追加します。
1. ドキュメントを保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_1(outfile):
    """
    Implement text rotation using TextFragment and TextBuilder.

    Demonstrates basic text rotation techniques by creating multiple text
    fragments with different rotation angles. Shows how to position and
    rotate individual text elements using TextBuilder for precise control.

    Args:
        outfile (str): Path where the PDF with rotated text will be saved.

    Returns:
        None: The function creates and saves a PDF file with rotated text fragments.

    Note:
        - Creates three text fragments with 0°, 45°, and 90° rotations
        - Uses Position class for precise text placement
        - Applies TimesNewRoman font with 12pt size
        - TextBuilder provides low-level control over text placement
        - Demonstrates individual fragment rotation capabilities

    Example:
        >>> rotate_text_inside_pdf_1("rotated_fragments.pdf")
        # Creates a PDF with text fragments at different rotation angles
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        text_fragment_1.position = ap.text.Position(100, 600)
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create rotated text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        text_fragment_2.position = ap.text.Position(200, 600)
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        text_fragment_2.text_state.rotation = 45
        # Create rotated text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        text_fragment_3.position = ap.text.Position(300, 600)
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        text_fragment_3.text_state.rotation = 90
        # create TextBuilder object
        builder = ap.text.TextBuilder(page)
        # Append the text fragment to the PDF page
        builder.append_text(text_fragment_1)
        builder.append_text(text_fragment_2)
        builder.append_text(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## PDF の段落内で個々のテキストフラグメントを回転させる

段落内の個々のテキストフラグメントを回転させます。複数のフラグメント (TextFragment) を含む複数行の段落 (TextParagraph) を構築し、各フラグメントに独自の回転角度を設定する方法を示します。この手法は、水平と斜めのテキストを組み合わせた視覚的にリッチな文書を作成するのに役立ちます — 例として、装飾的なヘッダー、図、注釈ラベルなどがあります。

3 行のテキストがそれぞれ異なる角度で回転した段落を含む rotated_paragraph_fragments.pdf という PDF を作成します:

- 最初の行は 45° 回転しています
- 2 行目は水平のままです (0°)
- 3 行目は -45° 回転しています

1. 新しい PDF ドキュメントを作成します。
1. 回転したテキストが表示される空白ページを追加します。
1. TextParagraph を作成します。
1. 最初のテキストフラグメントを作成および設定します - 45° 回転。
1. 2 番目のテキストフラグメントを作成します - 回転なし。
1. 3 番目のテキストフラグメントを作成します - 45° 回転。
1. テキストフラグメントを段落に追加します。
1. TextBuilder を使用して段落をページに追加します。
1. ドキュメントを保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_2(outfile):
    """
    Implement text rotation using TextParagraph and TextBuilder with rotated fragments.

    Demonstrates how to create multi-line paragraphs containing individually
    rotated text fragments. Shows the combination of paragraph structure
    with fragment-level rotation control.

    Args:
        outfile (str): Path where the PDF with rotated paragraph fragments will be saved.

    Returns:
        None: The function creates and saves a PDF file with a paragraph containing rotated fragments.

    Note:
        - Creates a TextParagraph containing multiple text fragments
        - Individual fragments have different rotations: 45°, 0°, and -45°
        - Uses append_line to structure fragments within the paragraph
        - Demonstrates mixed rotation within a single paragraph
        - TextBuilder handles paragraph-level placement and rendering

    Example:
        >>> rotate_text_inside_pdf_2("rotated_paragraph_fragments.pdf")
        # Creates a PDF with a paragraph containing individually rotated text fragments
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        paragraph = ap.text.TextParagraph()
        paragraph.position = ap.text.Position(200, 600)
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_1.text_state.rotation = 45
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("another rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_3.text_state.rotation = -45
        # Append the text fragments to the paragraph
        paragraph.append_line(text_fragment_1)
        paragraph.append_line(text_fragment_2)
        paragraph.append_line(text_fragment_3)
        # Create TextBuilder object
        text_builder = ap.text.TextBuilder(page)
        # Append the text paragraph to the PDF page
        text_builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```

## PDF のページ段落を使用したテキストの回転

Aspose.PDF for Python via .NET を使用して PDF 内のテキストを回転させる簡易的な方法です。
TextBuilder や TextParagraph を使用した低レベルなアプローチとは異なり、この方法は回転したテキストフラグメントをページの段落コレクション (page.paragraphs) に直接追加します。基本的なテキスト回転が必要で、精密な位置指定や段落構造が不要なケースに最適です。このアプローチはレイアウト作成を簡素化し、ページ上のテキスト配置を自動的に処理しながら、個々のテキスト回転制御も可能にします。

simple_rotated_text.pdf というファイルを生成し、以下を含みます:

- メインの水平テキストフラグメント（0° 回転）
- 315° 回転したフラグメント
- 270° 回転したフラグメント

1. 新しい PDF ドキュメントを初期化します。
1. 回転したテキストを配置するページを作成します。
1. 最初のテキストフラグメントを作成 - 回転なし。
1. 2番目のテキストフラグメントを作成 - 315° 回転。
1. 3番目のテキストフラグメントを作成 - 270° 回転。
1. テキストフラグメントをページの段落に直接追加。
1. PDFドキュメントを保存。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_3(outfile):
    """
    Implement text rotation using TextFragment and Page.Paragraphs.

    Demonstrates a simplified approach to text rotation by adding rotated
    text fragments directly to the page's paragraph collection. Shows
    high-level text placement without TextBuilder complexity.

    Args:
        outfile (str): Path where the PDF with rotated text will be saved.

    Returns:
        None: The function creates and saves a PDF file with rotated text using page paragraphs.

    Note:
        - Uses Page.Paragraphs for direct text fragment addition
        - Creates fragments with 0°, 315°, and 270° rotations
        - Simpler approach compared to TextBuilder method
        - Demonstrates automatic layout with rotated text elements
        - Good for basic rotation without precise positioning needs

    Example:
        >>> rotate_text_inside_pdf_3("simple_rotated_text.pdf")
        # Creates a PDF with rotated text using the simplified page paragraphs approach
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_2.text_state.rotation = 315
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_3.text_state.rotation = 270
        page.paragraphs.add(text_fragment_1)
        page.paragraphs.add(text_fragment_2)
        page.paragraphs.add(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## PDF内の段落全体を回転

当ライブラリは、PDF内で段落レベルの高度なテキスト回転を示します。フラグメント単位の回転（各テキスト要素を個別に回転させる）とは異なり、この方法では段落全体を統一されたブロックとしてさまざまな角度で回転させます。
各段落は複数のスタイル付きテキストフラグメントを含み、全体の段落が特定の角度で回転します — 複雑で一貫したレイアウト変換が可能です。
これは、アーティスティックなレイアウトや透かし、デザイン重視のPDFで、テキスト全体のセクションをさまざまな方向に配置する必要がある場合に最適です。

『rotated_paragraphs.pdf』を作成し、4つの完全にスタイル付けされ回転した段落を含みます:

- 各段落がユニークな角度で回転（45°, 135°, 225°, 315°）
- 各段落は、カラー背景、下線、統一されたスタイルの3行のテキストを持ちます

1. 新しいPDFドキュメントを作成。
1. 回転した段落を収める空白ページを追加。
1. 複数の段落を作成するために繰り返し処理。
1. 段落を作成し配置。
1. 書式設定付きのテキストフラグメントを作成。
1. テキスト書式を適用。
1. テキストフラグメントを段落に追加。
1. TextBuilder を使用して段落をページに追加。
1. 4つの回転すべてに対して繰り返し。
1. PDFドキュメントを保存。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_4(outfile):
    """
    Implement whole paragraph rotation using TextParagraph and TextBuilder.

    Demonstrates advanced text rotation by rotating entire paragraphs at
    different angles. Creates multiple styled paragraphs with comprehensive
    formatting and rotates each paragraph as a complete unit.

    Args:
        outfile (str): Path where the PDF with rotated paragraphs will be saved.

    Returns:
        None: The function creates and saves a PDF file with fully rotated paragraphs.

    Note:
        - Creates 4 paragraphs rotated at 45°, 135°, 225°, and 315°
        - Each paragraph contains multiple formatted text fragments
        - Applies comprehensive styling: colors, backgrounds, underlines
        - Demonstrates paragraph-level rotation vs. fragment-level rotation
        - Shows complex multi-line content with consistent rotation
        - Uses loop to create systematic rotation pattern

    Example:
        >>> rotate_text_inside_pdf_4("rotated_paragraphs.pdf")
        # Creates a PDF with complete paragraphs rotated at different angles
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        for i in range(4):
            paragraph = ap.text.TextParagraph()
            paragraph.position = ap.text.Position(200, 600)
            # Specify rotation
            paragraph.rotation = i * 90 + 45
            # Create text fragment
            text_fragment_1 = ap.text.TextFragment("Paragraph Text")
            # Create text fragment
            text_fragment_1.text_state.font_size = 12
            text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_1.text_state.background_color = ap.Color.light_gray
            text_fragment_1.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_2 = ap.text.TextFragment("Second line of text")
            # Set text properties
            text_fragment_2.text_state.font_size = 12
            text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_2.text_state.background_color = ap.Color.light_gray
            text_fragment_2.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_3 = ap.text.TextFragment("And some more text...")
            # Set text properties
            text_fragment_3.text_state.font_size = 12
            text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_3.text_state.background_color = ap.Color.light_gray
            text_fragment_3.text_state.foreground_color = ap.Color.blue
            text_fragment_3.text_state.underline = True
            paragraph.append_line(text_fragment_1)
            paragraph.append_line(text_fragment_2)
            paragraph.append_line(text_fragment_3)
            # Create TextBuilder object
            builder = ap.text.TextBuilder(page)
            # Append the text fragment to the PDF page
            builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```
