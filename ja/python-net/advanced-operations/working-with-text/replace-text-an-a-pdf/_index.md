---
title: Python を使用した PDF のテキスト置換
linktitle: PDF のテキスト置換
type: docs
weight: 40
url: /ja/python-net/replace-text-in-pdf/
description: Aspose.PDF for Python via .NET ライブラリを使用して、テキストの置換や削除のさまざまな方法について詳しく学びます。
lastmod: "2025-10-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
aliases: 
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Python を使用して PDF のテキストを置換する方法
Abstract: この記事では、Aspose.PDF for Python via .NET を使用した PDF 文書内のさまざまなテキスト操作手法について包括的なガイドを提供します。すべてのページでのテキスト置換、特定のページ領域内での置換、正規表現を使用した置換など、複数のテキスト置換戦略を取り上げます。また、PDF 内のフォントを置換し未使用フォントを削除する方法や、テキスト置換に伴いページ内容を自動的に再配置する管理方法についても説明します。さらに、PDF 作成時に置換可能なシンボルをレンダリングする方法（ヘッダー/フッター領域での使用を含む）について掘り下げ、ドキュメントのカスタマイズを向上させます。最後に、PDF 文書からすべてのテキストを削除する方法を詳述し、完全なテキスト削除が必要なシナリオでの操作を最適化します。各セクションには、Python およびその他の対応言語のコードスニペットが付属し、実装例を示します。
---

これらの例は、既存の PDF でテキストを **変更または削除** する方法を示しています。

## 既存のテキストを置換

### PDF 文書のすべてのページでテキストを置換

{{% alert color="primary" %}}

Aspose.PDF を使用して文書内のテキストを検索・置換し、オンラインで結果を確認するには、この [リンク](https://products.aspose.app/pdf/redaction) をお試しください。

{{% /alert %}}

テキスト置換は、既存の PDF 文書の内容を更新または修正する際によくある要件です。たとえば、製品名の変更、誤字の修正、複数ページにわたる用語の更新などがあります。

Aspose.PDF for Python via .NET は、[TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) クラスを使用して、プログラムでテキストを検索・置換するための強力かつ効率的な方法を提供します。

この例では、特定のフレーズ（この場合は「Black cat」）のすべての出現箇所を見つけ、PDF 文書全体で新しいフレーズ（「White dog」）に置換する方法を示します。

1. 検索フレーズと置換フレーズを指定します。検索したいテキストと置換先のテキストを設定します。
1. PDF 文書をロードします。
1. テキスト吸収器を作成します。TextFragmentAbsorber を検索フレーズで初期化し、文書内の該当フレーズのすべてのインスタンスをスキャンします。
1. 吸収器をすべてのページに適用します。すべてのページを反復し、フレーズに一致するテキストフラグメントを収集します。
1. 見つかった各フラグメントを置換します。「Black cat」のすべてのインスタンスを「White dog」に変更します。
1. 更新された PDF を保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_on_all_pages(infile, outfile):
    """
    Replace text on all pages of a PDF document.

    Searches for a specific text phrase throughout all pages of a PDF document
    and replaces all occurrences with a new phrase. This function demonstrates
    global text replacement using TextFragmentAbsorber.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Replaces "Black cat" with "White dog" as demonstration
        - Searches across all pages in the document
        - Preserves original formatting and layout
        - Uses TextFragmentAbsorber for efficient text search

    Example:
        >>> replace_text_on_all_pages("input.pdf", "output.pdf")
        # Replaces all instances of "Black cat" with "White dog"
    """
    search_phrase = "Black cat"
    replace_phrase = "White dog"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### 特定のページ領域でテキストを置換

場合によっては、PDF ページ全体を検索する代わりに、特定の領域内のテキストのみを置換する必要があることがあります。たとえば、既知の位置にあるヘッダー、フッター、または表のセルを更新する場合です。

Aspose.PDF for Python via .NET ライブラリは、[TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) と領域ベースのテキスト検索を組み合わせることで、この機能を実現します。

この例では、特定のページ上の定義された矩形領域内でターゲットフレーズのすべての出現箇所を見つけて置換する方法を示します。

1. 検索フレーズと置換フレーズを指定します。
1. PDF 文書をロードします。
1. 検索用のテキスト吸収器を作成します。目的のテキストを見つけるために TextFragmentAbsorber を初期化します。
1. 検索領域を制限します。矩形でページ上の x と y の座標範囲を指定します。
1. 吸収器を特定のページに適用します。指定された領域内で検索を実行し、一致するテキストフラグメントを収集します。
1. 見つかったテキストを置換します。定義された領域内の 'doc' のすべての出現が 'DOC' に変わります。
1. 更新された PDF を保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_in_particular_page_region(infile, outfile):
    """
    Replace text in a particular region of a page.

    Performs targeted text replacement within a specific rectangular region
    on the first page of a PDF document. This allows for precise control
    over which text gets replaced based on its location.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Replaces "doc" with "DOC" within the specified region
        - Only affects text within coordinates (300, 442, 500, 742)
        - Uses limit_to_page_bounds for precise region control
        - Only processes the first page (pages[1])

    Example:
        >>> replace_text_in_particular_page_region("input.pdf", "output.pdf")
        # Replaces "doc" with "DOC" only in the specified rectangular area
    """
    search_phrase = "doc"
    replace_phrase = "DOC"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        absorber.text_search_options.limit_to_page_bounds = True
        absorber.text_search_options.rectangle = ap.Rectangle(300, 442, 500, 742, True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### フォントサイズを変更せずにテキストのサイズ変更とシフト

PDF のテキストを置換する際、フォントサイズを変更せずに新しいテキストを特定の領域に合わせて調整したり、位置を変更したりしたいことがあります。
Aspose.PDF for Python via .NET は、元のフォントサイズを維持しながらテキストのレイアウトや間隔を調整するオプションを提供します。

1. PDF 文書をロードします。
1. 'TextFragmentAbsorber' を使用してページ上のすべてのテキストフラグメントを収集します。
1. 修正するフラグメントを選択します。
1. テキストの矩形をシフトし、サイズ変更します。
1. テキスト間隔を調整します。変更された矩形内にテキストを収めるために間隔調整を有効にします。
1. フラグメントのテキストを置換します。
1. 更新された PDF を保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_shift_without_changing_font_size(infile, outfile):
    """
    Resize and shift text without changing the font size.

    Demonstrates how to replace text content while adjusting its position
    and width within a modified rectangular area. The font size remains
    unchanged, but spacing is adjusted to fit the new content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Targets the second text fragment on the first page
        - Narrows the text rectangle by 50 units on each side
        - Duplicates the original text content
        - Uses ADJUST_SPACE_WIDTH for proper spacing
        - Maintains original font size and style

    Example:
        >>> replace_text_and_resize_and_shift_without_changing_font_size("input.pdf", "output.pdf")
        # Duplicates text in a narrower space with adjusted spacing
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = fragment.rectangle
        rect.llx += 50
        rect.urx -= 50
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### PDFで段落をリサイズしてシフトする

PDFを扱う際、ページレイアウトと視覚的に整合させたまま段落を置き換えたり拡張したりする必要があることがあります。Aspose.PDF を使用すると、段落の境界矩形のサイズを変更し、間隔を調整して新しいテキストに合わせることができ、フォントサイズを変更せずに行えます。

1. PDF ドキュメントを読み込む。
1. 'TextFragmentAbsorber' を使用してページ上のすべてのテキスト フラグメントを収集する。
1. 修正するフラグメントを選択する。
1. 段落をリサイズしてシフトする。ページのメディアボックスを使用して境界を決定し、矩形を調整する。
1. スペースを調整する。これはフォントサイズを変更する代わりに単語/文字間の間隔を調整します。
1. フラグメントのテキストを置き換える。
1. 変更された PDF を保存する。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_shift_paragraph(infile, outfile):
    """
    Resize and shift a paragraph in the document.

    Demonstrates paragraph-level text replacement with automatic resizing
    to fit within the page's media box boundaries. Adjusts the text area
    to provide margins while duplicating content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses page media box as base rectangle
        - Adds 20-unit margins on left, right, and top
        - Targets the second text fragment on the first page
        - Duplicates original text content
        - Automatically adjusts space width for proper fit

    Example:
        >>> replace_text_and_resize_and_shift_paragraph("input.pdf", "output.pdf")
        # Resizes paragraph to fit within page margins with duplicated text
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = document.pages[1].media_box
        rect.llx += 20
        rect.urx -= 20
        rect.ury -= 20
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### テキストを置き換え、フォントを自動的に拡大して対象領域を埋める

PDF のテキストを置き換え、フォントを自動的にリサイズおよび拡大して特定の矩形領域を埋めます。Aspose.PDF for Python via .NET ライブラリを使用すると、コードはフォントサイズと間隔を動的に調整し、新しいテキスト コンテンツが定義されたバウンディングボックス内に完全に収まるようにします — 手動でフォント計算を行う必要はありません。

1. PDF を読み込む。
1. テキスト フラグメントを取得する。
1. 特定のフラグメントを選択する。
1. 対象矩形を定義する。
1. テキスト調整オプションを有効にする。
1. テキストを置き換える。
1. ドキュメントを保存する。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_expand_font(infile, outfile):
    """
    Resize and expand font to fill target area.

    Demonstrates automatic font scaling to fill a specified rectangular area.
    The font size is dynamically adjusted to make the text content fit
    perfectly within the defined target rectangle.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Defines target rectangle at coordinates (100, 300, 512, 692)
        - Uses SCALE_TO_FILL for automatic font size adjustment
        - Duplicates original text content
        - Adjusts space width for optimal text distribution
        - Font size scales up or down to fill the entire rectangle

    Example:
        >>> replace_text_and_resize_and_expand_font("input.pdf", "output.pdf")
        # Scales font to completely fill the specified rectangular area
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = ap.Rectangle(100, 300, 512, 692, True)
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SCALE_TO_FILL
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)

```

### テキストを置き換えて矩形内に収める

PDF ドキュメントのテキストを置き換え、新しいコンテンツが元のテキストの矩形領域内に収まるように、必要に応じてフォントサイズを自動的に縮小して適合させます。

Aspose.PDF for Python via .NET ライブラリを使用して、この機能はテキストレイアウトとフォントサイズの両方を動的に調整し、文書構造を保持しながらオーバーフローを防止します。

1. TextFragmentAbsorber オブジェクトを作成し、最初のページからすべてのテキスト フラグメントを抽出する。
1. 特定のテキスト フラグメントにアクセスする。
1. 置換領域を設定する。
1. テキスト調整オプションを構成する。2 つの主要な置換オプションを設定する：
- フォントサイズ調整 - 新しいテキストが長すぎる場合、'SHRINK_TO_FIT' が自動的にフォントサイズを縮小します。
- スペース調整 - 'ADJUST_SPACE_WIDTH' は間隔を比例的に保ちます。
1. テキストを置き換える。
1. 修正された PDF を保存する。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_fit_text_into_rectangle(infile, outfile):
    """
    Fit text into a rectangle by adjusting font size.

    Demonstrates how to ensure text content fits within its original
    rectangle by automatically shrinking the font size when the new
    content is longer than the original.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses original text fragment rectangle as target area
        - Employs SHRINK_TO_FIT to reduce font size if needed
        - Duplicates original text content (making it longer)
        - Adjusts space width for proper text distribution
        - Prevents text overflow by automatic font scaling

    Example:
        >>> replace_text_and_fit_text_into_rectangle("input.pdf", "output.pdf")
        # Shrinks font size to fit doubled text content in original space
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = fragment.rectangle
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SHRINK_TO_FIT
        )
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH

        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### プレースホルダー テキストを自動的に置き換え、PDF レイアウトを再配置する

PDF 内のプレースホルダー テキスト（テンプレートやフォームなど）を、名前や会社情報などの実際のデータに置き換える。
カスタム書式設定（フォント、色、サイズ）を適用しながら、新しいテキストに合わせてページレイアウトを自動的に調整します。

1. PDF をインポートして読み込む。
1. プレースホルダー用の Text Absorber を作成する。
1. 吸収器をすべてのページに適用する。
1. 見つかったテキスト フラグメントをループ処理する。
1. カスタムテキスト書式設定を適用する。
1. 更新されたドキュメントを保存する。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def automatically_rearrange_page_contents(input_file, output_file):
    """
    Replace placeholder text in PDF with actual content.

    Demonstrates how to replace long placeholder text with actual content
    and automatically rearrange page layout. Shows dynamic content replacement
    with custom formatting applied to the new text.

    Args:
        input_file (str): Path to the input PDF file containing placeholders.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Searches for "[Long_placeholder_Long_placeholder]" placeholders
        - Replaces with either "John Smith" or extended version with studio info
        - Applies Calibri font, size 12, navy blue color
        - Automatically adjusts page layout to accommodate content changes
        - Demonstrates real-world template filling scenarios

    Example:
        >>> automatically_rearrange_page_contents("template.pdf", "filled.pdf")
        # Replaces placeholders with formatted actual content
    """
    document = ap.Document(input_file)

    absorber = ap.text.TextFragmentAbsorber("[Long_placeholder_Long_placeholder]")
    document.pages.accept(absorber)

    for text_fragment in absorber.text_fragments:
        # text_fragment.text = "John Smith"
        text_fragment.text = "John Smith, South Development Studio"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Calibri")
        text_fragment.text_state.font_size = 12
        text_fragment.text_state.foreground_color = ap.Color.navy

    # Save PDF document
    document.save(output_file)
```

### 正規表現に基づいてテキストを置き換える

PDF ドキュメントを扱う際、特定のフレーズではなくパターンに従うテキストを置き換える必要がある場合があります。たとえば電話番号、コード、日付形式などです。

Aspose.PDF for Python via .NET を使用すると、TextFragmentAbsorber クラスで正規表現（regex）を使った置換が可能です。

この例では、テキスト パターン（この場合は ####-#### の形式、例: 1234-5678）を見つけ、フォーマットされた文字列 'ABC1-2XZY' に置き換える方法を示します。また、置換されたテキストのフォント、色、サイズをカスタマイズする方法も示しています。

以下のコードスニペットは、正規表現に基づいてテキストを置き換える方法を示しています。

1. PDF ドキュメントを読み込む。
1. 正規表現ベースの Text Absorber を作成する。正規表現パターンで TextFragmentAbsorber を初期化する。
1. 正規表現モードを有効にする。'True' パラメータは正規表現検索モードを有効にします。
1. 吸収器をページに適用する。これにより、定義された正規表現パターンに一致するすべてのテキスト フラグメントをページ上でスキャンします。
1. 各一致を新しいテキストに置き換え、カスタムスタイルを適用する。
1. 修正されたドキュメントを保存する。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_based_on_regex(infile, outfile):
    """
    Replace text based on a regular expression pattern.

    Demonstrates pattern-based text replacement using regular expressions
    to find and replace text that matches specific formats. Also shows
    how to apply formatting changes to the replaced text.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses regex pattern r"\\d{4}-\\d{4}" to find 4-digit-4-digit patterns
        - Replaces matched patterns with "ABC1-2XZY"
        - Applies custom formatting: Verdana font, size 12, blue text
        - Sets light green background color for replaced text
        - Enables regex mode with TextSearchOptions(True)

    Example:
        >>> replace_text_based_on_regex("input.pdf", "output.pdf")
        # Replaces patterns like "1234-5678" with formatted "ABC1-2XZY"
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(r"\d{4}-\d{4}")
        absorber.text_search_options = ap.text.TextSearchOptions(True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = "ABC1-2XZY"
            fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
            fragment.text_state.font_size = 12
            fragment.text_state.foreground_color = ap.Color.blue
            fragment.text_state.background_color = ap.Color.light_green

        document.save(outfile)
```

## フォントを置き換えるまたは未使用フォントを削除する

### 既存のPDFファイルのフォントを置換する

たまに、PDF全体のフォントを標準化または更新する必要があります。たとえば、時代遅れまたは専有フォントを、より汎用的なフォントに置き換えることです。Aspose.PDF for Python via .NET ライブラリを使用すると、プログラムでフォントを検出し置換でき、タイポグラフィの一貫性と文書の互換性を確保します。

この例では、特定のフォント（例: 'Arial-BoldMT'）のすべてのインスタンスを別のフォント（例: 'Verdana'）に置き換える方法をPDF文書全体で示します。

以下のコードスニペットは、PDF文書内のフォントを置換する方法を示しています。

1. PDF文書を開く。
1. TextFragmentAbsorberを初期化する。
1. Absorberを使用して、文書のすべてのページからテキストフラグメントを抽出する。
1. フォントを識別し置換する。スクリプトはフラグメントの現在のフォントが 'Arial-BoldMT' かどうかをチェックし、該当する場合は FontRepository.find_font() メソッドを使用して 'Verdana' フォントに置き換えます。
1. 変更された文書を保存する。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_fonts(infile, outfile):
    """
    Replace specific fonts in a PDF document.

    Demonstrates how to find and replace specific fonts throughout a PDF
    document. Searches for text using a particular font and changes it
    to a different font while preserving the text content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Searches for text using "Arial-BoldMT" font
        - Replaces font with "Verdana" while keeping text content
        - Processes all text fragments across all pages
        - Maintains original text size and formatting properties
        - Useful for font standardization across documents

    Example:
        >>> replace_fonts("input.pdf", "output.pdf")
        # Changes all Arial-BoldMT text to use Verdana font instead
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            if fragment.text_state.font.font_name == "Arial-BoldMT":
                fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")

        document.save(outfile)
```

### 未使用フォントの削除

時間が経つにつれて、PDF文書には使用されていない埋め込みフォントが蓄積し、ファイルサイズが増加し処理が遅くなることがあります。テキストの編集や置換後でも、特に大規模または複雑なPDFでは、未使用フォントが残ることがあります。

Aspose.PDF for Python via .NET ライブラリは、TextEditOptions クラスを使用してこのような冗長なフォントを削除する効率的な方法を提供します。これにより文書が最適化され、可視テキストに実際に適用されているフォントのみが使用されるようになります。

'remove_unused_fonts()' メソッドは、冗長なフォントデータを削除してPDFファイルを最適化するシンプルながら強力な方法です。

この例では、以下の方法を示します。

- PDFから未使用フォントをスキャンする。
- 安全に削除する。
- アクティブなテキストフラグメントを一貫したフォント（例: Times New Roman）に再割り当てする。

1. PDF文書を開く。
1. テキスト編集オプションを設定する。これにより、エンジンは可視テキストで現在使用されていない埋め込みフォントをすべて除去します。
1. オプション付きのテキスト吸収器を作成する。TextFragmentAbsorber は、編集のために文書からテキストフラグメントを抽出します。
1. 標準フォントを再割り当てする。吸収器がすべてのフラグメントを収集したら、それらを反復し一貫したフォントを適用します。
1. クリーニングされたPDFを保存する。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_unused_fonts(input_file, output_file):
    """
    Remove unused fonts from a PDF document.

    Optimizes PDF file size by removing fonts that are embedded but not
    actually used in the document. Also demonstrates how to standardize
    all text to use a specific font family.

    Args:
        input_file (str): Path to the input PDF file to optimize.
        output_file (str): Path where the optimized PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses REMOVE_UNUSED_FONTS option for optimization
        - Changes all text to use TimesNewRoman font
        - Processes all text fragments across the document
        - Reduces file size by eliminating unnecessary font data
        - Useful for PDF optimization and standardization

    Example:
        >>> remove_unused_fonts("input.pdf", "optimized.pdf")
        # Removes unused fonts and standardizes text to TimesNewRoman
    """

    # Open PDF document
    document = ap.Document(input_file)

    # Initialize text edit options to remove unused fonts
    options = ap.text.TextEditOptions(ap.text.TextEditOptions.FontReplace.REMOVE_UNUSED_FONTS)

    # Create a TextFragmentAbsorber with the specified options
    absorber = ap.text.TextFragmentAbsorber(options)
    document.pages.accept(absorber)

    # Iterate through all TextFragments
    for text_fragment in absorber.text_fragments:
        text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")

    # Save the updated PDF document
    document.save(output_file)
```

## すべてのテキストを削除する

### PDFからテキストを削除する

画像、形状、レイアウト構造はそのままに、PDFファイルからすべてのテキストコンテンツを削除します。
TextFragmentAbsorber を使用することで、コードは文書全体を効率的にスキャンし、各ページで見つかったすべてのテキストフラグメントを削除します。

1. PDF文書をロードする。
1. PDF内のテキストフラグメントを検出・処理するために TextFragmentAbsorber オブジェクトを作成する。
1. すべてのテキストコンテンツを削除する。'absorber.remove_all_text()' メソッドは、ロードされた文書からすべてのテキスト要素を削除し、非テキスト要素はそのまま残します。
1. 更新された文書を保存する。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber1(infile, outfile):
    """
    Remove all text from a PDF using TextFragmentAbsorber.

    Demonstrates complete text removal from an entire PDF document,
    leaving only non-text elements like images, shapes, and layout
    structures intact.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the text-free PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes all text content from the entire document
        - Preserves images, graphics, and page structure
        - Uses document-level text removal for complete cleanup
        - Useful for creating templates or removing sensitive text
        - Maintains page layout and non-text elements

    Example:
        >>> remove_all_text_using_absorber1("input.pdf", "no_text.pdf")
        # Creates a PDF with all text removed but graphics preserved
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document)
        document.save(outfile)
```

### 特定のページからすべてのテキストを削除する

Aspose.PDF の TextFragmentAbsorber クラスを使用して、PDFドキュメントの単一ページからすべてのテキストを削除します。
全体文書の削除とは異なり、このメソッドはページレベルのテキストクリーンアップを実行し、選択したページのみからテキストを削除し、他のすべてのページはそのままにします。

1. PDFファイルをロードする。
1. TextFragmentAbsorber のインスタンスを作成する。
1. 最初のページからすべてのテキストを削除する。
1. 変更されたPDFを保存する。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber2(infile, outfile):
    """
    Remove all text from page using TextFragmentAbsorber.

    Demonstrates text removal from a specific page while leaving text
    on other pages intact. Useful for selective text cleanup or
    creating mixed-content documents.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes text only from the first page (pages[1])
        - Preserves text content on all other pages
        - Maintains page structure and non-text elements
        - Useful for page-specific text removal operations
        - Images and graphics on the target page remain intact

    Example:
        >>> remove_all_text_using_absorber2("input.pdf", "first_page_clean.pdf")
        # Removes all text from first page only
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1])
        document.save(outfile)
```

### PDFページの特定領域からすべてのテキストを削除する

Aspose.PDF の TextFragmentAbsorber を使用して、ページ上の特定の矩形領域からすべてのテキストを削除します。
ページ全体をクリアする代わりに、このメソッドは対象を絞ったテキスト削除を行い、ページのどの部分が影響を受けるかを正確に制御できます。

1. PDF文書をロードする。
1. TextFragmentAbsorber を作成する。
1. 対象領域（矩形）を定義する。
1. 指定領域からテキストを削除する。
1. 文書の残りの部分を保持する。
1. 変更されたPDFを保存する。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber3(infile, outfile):
    """
    Remove all text from particular area on PDF page using TextFragmentAbsorber.

    Demonstrates precise text removal from a specific rectangular region
    on a page. Allows for surgical text removal while preserving text
    outside the target area.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes text only within rectangle (10, 200, 120, 600)
        - Targets the first page only (pages[1])
        - Preserves text outside the specified rectangle
        - Maintains all non-text elements in the region
        - Useful for removing watermarks, headers, or specific sections

    Example:
        >>> remove_all_text_using_absorber3("input.pdf", "region_clean.pdf")
        # Removes text only from the specified rectangular area
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1], ap.Rectangle(10, 200, 120, 600))
        document.save(outfile)
```

### PDF文書からすべての非表示テキストを削除する

Aspose.PDF の TextFragmentAbsorber を使用して、ページ上の特定の矩形領域からすべてのテキストを削除します。
ページ全体をクリアする代わりに、このメソッドは対象を絞ったテキスト削除を行い、ページのどの部分が影響を受けるかを正確に制御できます。

1. PDF文書をロードする。
1. TextFragmentAbsorber を作成します。
1. 対象領域（矩形）を定義します。
1. 指定された領域からテキストを削除します。
1. 文書の残りの部分を保持します。
1. 変更された PDF を保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_hidden_text(infile, outfile):
    """
    Remove all hidden (invisible) text from a PDF document.

    Identifies and removes text that has been marked as invisible while
    preserving all visible text content. Useful for cleaning documents
    that may contain hidden tracking text or metadata.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the cleaned PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Detects text fragments with invisible text state
        - Replaces hidden text with empty strings
        - Uses NONE replacement adjustment to prevent layout shifts
        - Preserves all visible text and document structure
        - Useful for privacy and security document cleanup

    Example:
        >>> remove_hidden_text("input.pdf", "no_hidden_text.pdf")
        # Removes all invisible text while keeping visible content intact
    """
    # Open PDF document
    with ap.Document(infile) as document:
        text_absorber = ap.text.TextFragmentAbsorber()
        # This option can be used to prevent other text fragments from moving after hidden text replacement
        text_absorber.text_replace_options = ap.text.TextReplaceOptions(ap.text.TextReplaceOptions.ReplaceAdjustment.NONE)
        document.pages.accept(text_absorber)
        # Remove hidden text
        for fragment in text_absorber.text_fragments:
            if fragment.text_state.invisible:
                fragment.text = ""
        # Save PDF document
        document.save(outfile)
```
