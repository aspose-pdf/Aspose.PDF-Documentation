---
title: PDF ページからテキストを検索して取得
linktitle: テキストの検索と取得
type: docs
weight: 60
url: /ja/python-net/search-and-get-text-from-pdf/
description: Aspose.PDF を使用した Python での PDF 文書の検索とテキスト抽出方法を学びます。
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF ページからテキストを検索して取得する方法
Abstract: この記事では、Aspose.PDF for Python via .NET ライブラリを使用した PDF ドキュメント内のテキスト抽出および操作機能を詳しく解説します。TextFragmentAbsorber クラスを紹介し、開発者が文書全体または特定のページで指定フレーズや正規表現パターンを検索できるようにします。本ページでは、テキストコンテンツの取得、位置（座標やインデント値を含む）の特定、フォント名・サイズ・埋め込み状態・色といったフォント属性の抽出など、マッチしたテキストフラグメントに対するさまざまな実用シナリオを示します。詳細なコード例がステップバイステップでプロセスを示すため、開発者がアプリケーションにテキスト検索機能を統合しやすくなります。
---

## PDFからテキストを検索

TextAbsorber クラスを使用して、PDF ドキュメント内の定義された矩形領域からテキストを検索および抽出します。純粋なテキスト形式モードを使用してクリーンでフォーマットされていないテキスト出力を行うため、ヘッダー、フッター、テーブル領域などの構造化された領域からのコンテンツ抽出に最適です。TextExtractionOptions と TextSearchOptions を矩形制約と組み合わせることで、ドキュメント内のテキスト抽出位置と方法を細かく制御できます。

1. 'ap.Document' を使用して PDF ファイルを読み込む。
1. テキスト抽出オプションを構成する。
1. 矩形制約で検索領域を定義する。
1. TextAbsorber を作成し構成する。
1. ドキュメントのすべてのページを処理する。
1. 抽出したテキストを取得して表示する。

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_absorber_search(input_file_path):
    """
    Search and extract text from PDF using TextAbsorber with area constraints.

    Demonstrates basic text extraction from a PDF document using TextAbsorber
    with pure text formatting mode and rectangular boundary constraints.
    Extracts text from all pages within the specified rectangular area.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints extracted text to console.

    Note:
        - Uses PURE text formatting mode for clean text extraction
        - Constrains search to rectangle (0, 0, 842, 250)
        - Processes all pages in the document
        - TextAbsorber provides high-level text extraction capabilities
        - Good for extracting text content without detailed positioning

    Example:
        >>> text_absorber_search("document.pdf")
        # Prints all text found in the specified rectangular area across all pages
    """
    # Open PDF document
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Process all pages
    document.pages.accept(absorber)

    print(f"Text fragments found: {absorber.text}")
```

## 特定の PDF ページからテキストを検索

Aspose.PDF の TextAbsorber を使用して、PDF の特定ページと領域からテキストを検索および抽出します。文書のページ 2 を対象とし、定義された矩形領域内に見つかったテキストのみを抽出します。
TextExtractionOptions（書式制御用）と TextSearchOptions（領域限定用）を組み合わせることで、正確なページ単位のテキスト抽出を効率的に実行できます。

1. PDF ドキュメントを読み込む。
1. テキスト抽出オプションを設定する。
1. ページ上の特定の矩形領域にテキスト抽出を制限する。
1. TextAbsorber を作成し構成する。
1. 特定のページを処理する。
1. 抽出したテキストを取得して表示する。

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_absorber_search_page(input_file_path):
    """
    Search and extract text from a specific PDF page using TextAbsorber.

    Demonstrates targeted text extraction from a single page (page 2) using
    TextAbsorber with area constraints. Shows how to limit search scope to
    specific pages and rectangular regions.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints extracted text from page 2 to console.

    Note:
        - Targets only page 2 of the document (document.pages[2])
        - Uses PURE text formatting mode for clean extraction
        - Constrains search to rectangle (0, 0, 842, 250)
        - Useful for page-specific text extraction
        - More efficient than processing entire document when targeting specific pages

    Example:
        >>> text_absorber_search_page("document.pdf")
        # Prints text found in the specified area on page 2 only
    """
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Only page 2
    document.pages[2].accept(absorber)

    print(f"Text fragments found: {absorber.text}")

```

## PDF から詳細なテキストフラグメントプロパティを分析・抽出

生テキストを抽出する TextAbsorber とは異なり、TextFragmentAbsorber は各テキストフラグメントの位置、フォント属性、色、埋め込み情報など、詳細な低レベル情報を提供します。

1. PDF ドキュメントを読み込む。
1. TextFragmentAbsorber を初期化する。
1. ドキュメントのすべてのページを処理する。
1. 抽出されたテキストフラグメントを反復処理する。
1. 基本的なテキスト情報を出力する。
1. フォントと書式設定の詳細を出力する。

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search(input_file_path):
    """
    Search and analyze all text fragments in a PDF with detailed properties.

    Demonstrates comprehensive text fragment analysis using TextFragmentAbsorber
    to extract all text with detailed positioning, font, and formatting information.
    Provides low-level access to text properties for detailed analysis.

    Args:
        input_file_path (str): Path to the input PDF file to analyze.

    Returns:
        None: Prints detailed text fragment information to console.

    Note:
        - Extracts all text fragments from all pages
        - Provides detailed properties: position, font info, colors, sizes
        - Shows font accessibility, embedding, and subset information
        - Useful for detailed text analysis and formatting inspection
        - TextFragmentAbsorber offers more granular control than TextAbsorber

    Example:
        >>> text_fragment_absorber_search("document.pdf")
        # Prints comprehensive details about every text fragment in the document
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    document.pages.accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
        print("XIndent:", fragment.position.x_indent)
        print("YIndent:", fragment.position.y_indent)
        print("Font - Name:", fragment.text_state.font.font_name)
        print("Font - IsAccessible:", fragment.text_state.font.is_accessible)
        print("Font - IsEmbedded:", fragment.text_state.font.is_embedded)
        print("Font - IsSubset:", fragment.text_state.font.is_subset)
        print("Font Size:", fragment.text_state.font_size)
        print("Foreground Color:", fragment.text_state.foreground_color)
```

## 単一 PDF ページで特定のテキストフレーズを検索

TextFragmentAbsorber を使用して PDF 文書のページ内で特定のテキストフレーズを検索します。文書全体を検索するのとは異なり、この手法は検索対象を1ページに限定するため、ヘッダー、フッター、特定のコンテンツセクションなどの対象領域にテキストが存在するかとその位置を確認するのに効率的です。

1. PDF ドキュメントを読み込む。
1. 検索フレーズを指定して TextFragmentAbsorber を初期化する。
1. 特定のページに Absorber を適用する。
1. 見つかったフラグメントを反復処理する。

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_page(input_file_path):
    """
    Search for specific text phrase on a particular PDF page.

    Demonstrates targeted text search for a specific phrase ("whale") on
    a single page. Shows how to combine phrase searching with page-specific
    scope for efficient and focused text location.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints matching text fragments and their positions to console.

    Note:
        - Searches for the phrase "whale" on page 2 only
        - Returns text fragments with position information
        - More efficient than document-wide search when targeting specific pages
        - Useful for validating content presence in specific document sections
        - Provides exact positioning coordinates for found text

    Example:
        >>> text_fragment_absorber_search_page("document.pdf")
        # Prints all instances of "whale" found on page 2 with their positions
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale")
    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## 累積結果によるページごとの連続テキスト検索

Aspose.PDF の TextFragmentAbsorber を使用して、PDF 文書の複数ページにわたりテキストを段階的に検索します。
単一ページまたは文書全体の検索とは異なり、この手法ではページを順次処理し、結果を段階的に収集し、ページ固有のコンテキストでテキストフラグメントを分析できます。この方法は大規模文書や段階的処理ワークフローに最適です。

1. PDF ドキュメントを読み込む。
1. TextFragmentAbsorber を初期化し、検索フレーズを設定する。
1. 最初のページを処理する。ページ 1 のみを検索し、テキスト、ページ番号、位置を出力します。明確さのために、ページ単位の独立した結果を提供します。
1. 次のページを順次処理します。ページ2に移動し、必要に応じて文書の残りを続行します。'absorber.visit()' は、訪問したすべてのページからの結果の蓄積を保証します。累積検索結果を出力し、テキストと位置の両方を表示します。

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_sequential_search(input_file_path):
    """
    Demonstrate sequential page-by-page text search with cumulative results.

    Shows how to perform incremental text searches across multiple pages,
    accumulating results from each page. Demonstrates both individual page
    processing and document-wide search continuation.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints text fragments from sequential page searches to console.

    Note:
        - Searches for "whale" on page 1, then continues to page 2
        - Uses absorber.visit(document) to process remaining pages
        - Demonstrates incremental search accumulation
        - Shows page numbers for found fragments
        - Useful for progressive document processing and result accumulation

    Example:
        >>> text_fragment_absorber_sequential_search("document.pdf")
        # Prints "whale" instances from page 1, then from all remaining pages
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.phrase = "whale"

    # First page
    document.pages[1].accept(absorber)
    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)

    print("--")

    # Continue to next page
    document.pages[2].accept(absorber)
    absorber.visit(document)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)
```

## 四角形エリア内の対象フレーズ検索

PDF内で特定のフレーズを検索し、単一ページの特定の四角形エリアに検索範囲を制限します。
フレーズ検索と空間的制約を組み合わせることで、ページ全体や文書全体をスキャンすることなく、指定された領域でコンテンツを正確に特定できます。これは、フォーム、ヘッダー、フッター、または構造化レポートのように、コンテンツが予測可能な位置に現れる場合に特に有用です。

1. PDFドキュメントを読み込む。
1. フレーズと矩形制約を使用して TextFragmentAbsorber を初期化する
1. Absorber をページ2に適用する。処理をページ2に限定し、不要な計算を削減します。検索がページ固有であることを保証します。
1. 見つかったフラグメントを反復処理し、出力する

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_phrase(input_file_path):
    """
    Search for specific phrase within a rectangular area constraint.

    Demonstrates targeted phrase searching with both text matching and
    spatial constraints. Combines phrase search with rectangular boundary
    limitations for precise content location.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints matching text fragments and positions to console.

    Note:
        - Searches for "elephant" phrase on page 2
        - Constrains search to rectangle (0, 0, 842, 250)
        - Combines text matching with spatial filtering
        - Useful for finding content in specific document regions
        - More precise than page-wide or document-wide searches

    Example:
        >>> text_fragment_absorber_search_phrase("document.pdf")
        # Prints "elephant" instances found within the specified rectangular area on page 2
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        "elephant", ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## 正規表現を使用した PDF のテキストパターン検索

正規表現を使用して PDF のテキストパターンを検索します。TextFragmentAbsorber の正規表現モードを有効にすることで、数字、日付、価格、座標、またはカスタムテキスト形式などの複雑なパターンを検出できます。この機能は検索を特定のページに限定し、構造化データのターゲット抽出を効率化します。

1. PDFドキュメントを読み込む。
1. 正規表現パターンで TextFragmentAbsorber を初期化する。
1. Absorber をページ2に適用する。効率と精度のために検索をページ2に限定します。このページのテキストのみが分析されます。
1. 見つかったフラグメントを反復処理する。マッチしたテキストフラグメントとその座標を出力します。抽出されたパターンの正確な位置情報を提供します。

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_regex(input_file_path):
    """
    Search for text patterns using regular expressions.

    Demonstrates advanced text searching using regular expression patterns
    to find complex text structures like numbers, dates, or custom formats.
    Shows how to enable regex mode in TextFragmentAbsorber.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints matching text fragments and positions to console.

    Note:
        - Uses regex pattern r"\\d+\\.\\d+" to find decimal numbers
        - Enables regex mode with is_regular_expression_used=True
        - Searches on page 2 only
        - Powerful for finding formatted data like prices, coordinates, dates
        - Regular expressions provide flexible pattern matching capabilities

    Example:
        >>> text_fragment_absorber_search_regex("document.pdf")
        # Prints all decimal numbers (e.g., "12.34", "0.99") found on page 2
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(r"\d+\.\d+", ap.text.TextSearchOptions(is_regular_expression_used=True))

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## TextFragmentAbsorber を使用して PDF のテキストマッチをハイパーリンクに変換する

PDF 内の特定のテキストフレーズを検索し、クリック可能なハイパーリンクに変換します。正規表現パターンを使用した TextFragmentAbsorber により、対象の語句を検出し、視覚的スタイリング（色と下線）とインタラクティブなリンクを適用します。

1. PDFドキュメントを読み込む。
1. 正規表現パターンで TextFragmentAbsorber を初期化する。
1. Absorber をページ1に適用する。
1. マッチにスタイルを適用し、ハイパーリンクを追加する。
1. 変更された PDF を保存する。

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_and_add_hyperlink(input_file_path):
    """
    Search for text and convert matches to hyperlinks with styling.

    Demonstrates advanced text processing by finding specific words and
    converting them into clickable hyperlinks with visual styling. Shows
    how to combine text search with document modification.

    Args:
        input_file_path (str): Path to the input PDF file to process.

    Returns:
        None: Saves modified PDF with hyperlinks to output file.

    Note:
        - Searches for "whale|elephant" using regex pattern on page 1
        - Converts found text to Wikipedia hyperlinks
        - Applies blue color and underline styling to hyperlinks
        - Creates new output file with "_out.pdf" suffix
        - Demonstrates practical text enhancement and interactivity
        - Combines search, styling, and hyperlinking in one operation

    Example:
        >>> text_fragment_absorber_search_and_add_hyperlink("document_in.pdf")
        # Creates "document_out.pdf" with "whale" and "elephant" as clickable Wikipedia links
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale|elephant")
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        fragment.text_state.foreground_color = ap.Color.blue
        fragment.text_state.underline = True
        fragment.hyperlink = ap.WebHyperlink(
            f"https://en.wikipedia.org/wiki/{fragment.text}"
        )

    output = input_file_path.replace("in.pdf", "out.pdf")
    document.save(output)
```

## TextFragmentAbsorber を使用して PDF のスタイルテキストを検索・識別する

PDF 内のテキストフラグメントを内容ではなくフォーマット属性に基づいて検索します。TextFragmentAbsorber を使用して、太字テキストなど特定のスタイルを持つテキストを識別します。

1. PDFドキュメントを読み込む。
1. TextFragmentAbsorber を初期化する。
1. Absorber をページ1に適用する。
1. フォーマットに基づいてテキストフラグメントを検査する。太字フォーマットのフォントスタイルを確認します。

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_styled_text(input_file_path):
    """
    Search and identify text based on formatting properties.

    Demonstrates how to find text fragments based on their formatting
    characteristics rather than content. Shows detection of bold text
    and invisible text within the document.

    Args:
        input_file_path (str): Path to the input PDF file to analyze.

    Returns:
        None: Prints formatted text findings to console.

    Note:
        - Searches all text fragments on page 1
        - Identifies text with FontStyles.BOLD formatting
        - Detects invisible/hidden text using text_state.invisible
        - Useful for formatting analysis and hidden content detection
        - Demonstrates text property-based filtering capabilities

    Example:
        >>> text_fragment_absorber_search_styled_text("document.pdf")
        # Prints all bold text and any hidden/invisible text found on page 1
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.font_style == ap.text.FontStyles.BOLD:
            print(f"Bold: {fragment.text}")
```

テキストのフォーマット属性を分析して、PDF 文書内の隠しまたは不可視テキストを検出します：

1. PDFドキュメントを読み込む。
1. TextFragmentAbsorber を初期化する。
1. Absorber をページ1に適用する。
1. フォーマットに基づいてテキストフラグメントを検査する。隠しテキストについては 'fragment.text_state.invisible' を確認してください。

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_styled_text(input_file_path):
    """
    Search and identify text based on formatting properties.

    Demonstrates how to find text fragments based on their formatting
    characteristics rather than content. Shows detection of bold text
    and invisible text within the document.

    Args:
        input_file_path (str): Path to the input PDF file to analyze.

    Returns:
        None: Prints formatted text findings to console.

    Note:
        - Searches all text fragments on page 1
        - Identifies text with FontStyles.BOLD formatting
        - Detects invisible/hidden text using text_state.invisible
        - Useful for formatting analysis and hidden content detection
        - Demonstrates text property-based filtering capabilities

    Example:
        >>> text_fragment_absorber_search_styled_text("document.pdf")
        # Prints all bold text and any hidden/invisible text found on page 1
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.invisible:
            print(f"Invisible: {fragment.text}")
```

## PDF ページでのビジュアルテキストハイライト

この関数はテキスト認識とレンダリングを単一のワークフローに統合します。テキストを抽出するだけでなく、各ページの PNG 画像上に色分けされた矩形でフラグメント、セグメント、文字をハイライトして可視化します。

この例では、PDF 上で高度なテキスト可視化を次のように実行します：

- 正規表現を使用してすべての可視テキストフラグメントを検索する
- 各 PDF ページを高解像度 PNG 画像にレンダリングする
- テキストフラグメント、テキストセグメント、個々の文字の周囲に色付き矩形を描画する

1. 出力画像解像度を設定する。各 PDF ページは 150 DPI の PNG 画像に変換されます。
1. PDF を開き、Text Absorber を初期化する。
1. 各ページを処理する。Absorber をすべてのページに適用し、検出されたすべてのテキストフラグメントとその幾何位置を収集する。
1. ページを PNG ストリームに変換する。
1. 描画用の Graphics オブジェクトを準備する。
1. 座標変換を適用する。PDF 座標を画像ピクセルに変換する。
1. テキスト要素の矩形を描画する。
1. 結果を保存する。

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_and_highlight(infile):
    """
    Search text and create visual highlighting with PNG output.

    Advanced function that combines text search with visual highlighting.
    Converts PDF pages to PNG images and draws colored rectangles around
    found text fragments, segments, and individual characters.

    Args:
        infile (str): Path to the input PDF file to process.

    Returns:
        None: Saves highlighted PNG images for each page.

    Note:
        - Uses regex pattern r"[\\S]+" to find all non-whitespace sequences
        - Converts each page to 150 DPI PNG image using PngDevice
        - Draws yellow rectangles around text fragments
        - Draws green rectangles around text segments
        - Draws black rectangles around individual characters
        - Creates detailed visual analysis of text structure
        - Output files named with page numbers: "filename1_out.png", etc.
        - Complex coordinate transformation for proper overlay positioning

    Example:
        >>> text_fragment_absorber_search_and_highlight("document_in.pdf")
        # Creates PNG files with visual highlighting of all text elements
    """
    resolution = 150
    png_device = ap.devices.PngDevice(ap.devices.Resolution(resolution, resolution))

    # Open PDF document
    document = ap.Document(infile)
    absorber = ap.text.TextFragmentAbsorber(r"[\S]+")
    absorber.text_search_options.is_regular_expression_used = True

    for page in document.pages:
        page.accept(absorber)
        stream = io.BytesIO()
        png_device.process(page, stream)
        with drawing.Bitmap.from_stream(stream) as bmp:
            with drawing.Graphics.from_image(bmp) as gr:
                scale = resolution / 72
                gr.transform = drawing.drawing2d.Matrix(
                    float(scale),
                    float(0),
                    float(0),
                    float(-scale),
                    float(0),
                    float(bmp.height),
                )
                text_fragment_collection = absorber.text_fragments
                # Loop through the fragments
                for text_fragment in text_fragment_collection:
                    gr.draw_rectangle(
                        drawing.Pens.yellow,
                        float(text_fragment.position.x_indent),
                        float(text_fragment.position.y_indent),
                        float(text_fragment.rectangle.width),
                        float(text_fragment.rectangle.height),
                    )
                    for seg_num in range(1, len(text_fragment.segments) + 1):
                        segment = text_fragment.segments[seg_num]
                        for char_num in range(1, len(segment.characters) + 1):
                            character_info = segment.characters[char_num]
                            rect = page.get_page_rect(True)
                            print(
                                f"TextFragment = {text_fragment.text}"
                                + f" Page URY = {rect.ury}"
                                + f" TextFragment URY = {text_fragment.rectangle.ury}"
                            )
                            gr.draw_rectangle(
                                drawing.Pens.black,
                                float(character_info.rectangle.llx),
                                float(character_info.rectangle.lly),
                                float(character_info.rectangle.width),
                                float(character_info.rectangle.height),
                            )
                        gr.draw_rectangle(
                            drawing.Pens.green,
                            float(segment.rectangle.llx),
                            float(segment.rectangle.lly),
                            float(segment.rectangle.width),
                            float(segment.rectangle.height),
                        )

                # Save result
                bmp.save(
                    infile.replace("_in.pdf", str(page.number) + "_out.png"),
                    drawing.imaging.ImageFormat.png,
                )
```
