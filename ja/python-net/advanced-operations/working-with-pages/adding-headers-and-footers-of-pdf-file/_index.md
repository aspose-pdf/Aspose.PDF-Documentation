---
title: Python を使用した PDF のヘッダーとフッターの追加
linktitle: PDF のヘッダーとフッターの追加
type: docs
weight: 50
url: /ja/python-net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for Python via .NET を使用すると、TextStamp クラスを使用して PDF ファイルにヘッダーとフッターを追加できます。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF にヘッダーとフッターを追加する方法
Abstract: この記事では、**Aspose.PDF for Python via .NET** を使用して PDF ファイルにヘッダーとフッターを追加する包括的なガイドを提供します。テキストまたは画像を組み込むことができます。まず、`TextStamp` クラスを使用して PDF 文書のヘッダーにテキストを挿入する方法を詳しく説明します。フォントサイズ、スタイル、色などの主要なプロパティは調整可能で、ヘッダーにテキストを追加する方法は Python のコードスニペットで示されています。記事は同様にフッターにテキストを追加する手順も説明しています。画像を追加する場合は `ImageStamp` クラスを使用し、ヘッダーとフッターの両方に対する手順を Python のコード例と共に紹介しています。また、単一の PDF ファイルに複数のヘッダーを追加する方法についても解説しています。これには、異なる書式設定を持つ複数の `TextStamp` オブジェクトを作成し、異なるページに適用することが含まれます。説明は、この機能を実演する詳細なコードスニペットで補完されています。
---

このページでは、Aspose.PDF for Python via .NET を使用して PDF ドキュメントにヘッダーとフッターを追加する概要を簡潔に紹介します。テキスト、HTML、LaTeX、画像、テーブルベースのアプローチや、動的ページ番号付け、ページごとの複数ヘッダーなどをカバーしています。[`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) オブジェクトの作成とスタイル設定方法（[`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/)、[`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/)、[`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/)、[`Image`](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/)、[`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) などを使用）、正確な配置のための [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) と [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) の調整、そして実用的な Python コード例で結果をページに添付する方法を説明しています。

**Aspose.PDF for Python via .NET** は、既存の [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) にヘッダーとフッターを追加できるようにします。画像やテキストを PDF 文書に追加できます。また、Python を使用して 1 つの PDF ファイルに異なるヘッダーを追加してみてください。

## ヘッダーとフッターをテキストフラグメントとして追加

PDF のすべてのページにシンプルなテキストヘッダーとフッターを追加します。[`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) オブジェクトを作成し、[`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) 要素を挿入し、適切な位置決めのために [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) を設定し、文書の各ページに添付します。その結果、すべてのページで一貫したヘッダーとフッターテキストが表示される PDF が生成されます。

以下のコードスニペットは、Python を使用して PDF にテキストフラグメントとしてヘッダーとフッターを追加する方法を示しています。

1. ヘッダーとフッターのテキストフラグメントを作成します。
1. HeaderFooter オブジェクトを作成し、テキストフラグメントを追加します。
1. ヘッダーとフッターの配置を制御するために余白設定を定義します。
1. 入力ファイルから PDF 文書をロードします。
1. 文書内のすべてのページを反復処理します。
1. 各ページにヘッダーとフッターを割り当てます。
1. 変更した PDF を出力ファイルに保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_text(input_file, output_file):
    """
    Add simple text headers and footers to all pages of a PDF document.

    Creates basic text-based headers and footers that appear on every page
    of the PDF document. Headers show "header" text and footers show "footer" text.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Adds identical headers and footers to all pages
        - Sets margins of 50 units left and 20 units top
        - Uses simple TextFragment elements for content
        - Headers and footers are created separately for each page

    Example:
        >>> add_header_and_footer_as_text("input.pdf", "output.pdf")
        # Adds text headers and footers to all pages
    """
    # Create header text
    header_text = ap.text.TextFragment("Demo header")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Demo footer")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

この方法は、各ページの上下に一貫したタイトル、ページインジケータ、または法的免責事項を追加するのに便利です。画像やページ番号などの動的コンテンツを含めるように拡張することもできます。

## ページ番号付け用のヘッダーとフッターの追加

Aspose.PDF for Python を使用して、PDF 文書のヘッダーとフッターに自動ページ番号付けを追加します。組み込み変数 $p（現在のページ番号）と $P（総ページ数）を使用し、スクリプトは各ページに動的にページ番号を挿入します。ヘッダーは「Page X from Y」の形式で表示され、フッターは「Page X / Y」と表示されます。[`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) は各ページでの適切な配置を保証します。

1. ヘッダー用に "Page $p from $P" を使用して TextFragment を作成し、現在のページと総ページ数を表示します。
1. HeaderFooter オブジェクトを作成し、ヘッダー文字列を追加します。
1. フッター用に "Page $p / $P" を使用して TextFragment を作成し、代替の番号付けスタイルを設定します。
1. Footer オブジェクトを作成し、フッター文字列を追加します。
1. 余白設定（左 = 50、上 = 20）を定義し、ヘッダーとフッターの両方に適用します。
1. 入力ファイルから PDF 文書を開きます。
1. すべてのページをループし、各ページにヘッダーとフッターを割り当てます。
1. 更新した PDF を出力パスに保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def using_header_and_footer_for_page_numbering(input_file, output_file):
    """
    Add page numbering headers and footers to all pages of a PDF document.

    Creates headers and footers with dynamic page numbering using special variables.
    The $p variable represents the current page number and $P represents the total
    number of pages in the document.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses $p for current page number and $P for total pages
        - Header shows "Page X from Y" format
        - Footer shows "Page X / Y" format
        - Variables are automatically replaced by Aspose.PDF
        - Sets margins of 50 units left and 20 units top
        - Page numbering updates dynamically for each page

    Example:
        >>> using_header_and_footer_for_page_numbering("input.pdf", "output.pdf")
        # Adds page numbering headers and footers to all pages
    """
    # Create header text
    header_text = ap.text.TextFragment("Page $p from $P")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Page $p / $P")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Create margins
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20

    # Set header margin
    header.margin = margin
    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## ヘッダーとフッターを HTML フラグメントとして追加

Aspose.PDF for Python を使用して、PDF 文書の各ページに HTML 形式のヘッダーとフッターを適用します。[`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/) を使用することで、太字や斜体などのリッチテキストスタイルをヘッダーとフッターに表示できます。適切な配置のために [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) を適用し、同じ書式設定された要素を文書の各ページに添付します。

以下のコードスニペットは、Python を使用して PDF に HTML フラグメントとしてヘッダーとフッターを追加する方法を示しています。

1. HtmlFragment を使用して HTML ヘッダーのスニペットを作成します。'<strong>' などのスタイル付きテキストを含めます。
1. HeaderFooter オブジェクトを作成し、HTML ヘッダーを追加します。
1. '<i>' を使用してイタリックスタイルの HTML フッタースニペットを作成します。
1. Footer オブジェクトを作成し、フッターの HTML を追加します。
1. 余白（左 = 50、上 = 20）を設定し、ヘッダーとフッターの両方に割り当てます。
1. 'ap.Document()' を使用して PDF 文書をロードします。
1. すべてのページをループし、各ページにヘッダーとフッターを割り当てます。
1. 変更した PDF を指定された出力パスに保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_html(input_file, output_file):
    """
    Add HTML-formatted headers and footers to all pages of a PDF document.

    Creates rich HTML-based headers and footers with formatting like bold
    and italic text. Demonstrates how to use HtmlFragment for styled content.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses HtmlFragment for rich text formatting
        - Header includes HTML with <strong> tag for bold text
        - Footer includes HTML with <i> tag for italic text
        - Sets margins of 50 units left and 20 units top
        - HTML tags are rendered properly in the PDF

    Example:
        >>> add_header_and_footer_as_html("input.pdf", "output.pdf")
        # Adds HTML-formatted headers and footers to all pages
    """
    # Create header HTML
    header_html = ap.HtmlFragment("This is an HTML <strong>Header</strong>")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_html)

    # Create footer HTML
    footer_html = ap.HtmlFragment("Powered by <i>Aspose.PDF</i>")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_html)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

HtmlFragment を使用すると、インラインスタイルや HTML マークアップによるリッチなフォーマットが可能になり、プレーンテキストに比べてデザインの柔軟性が向上します。

## ヘッダーとフッターを画像として追加

Aspose.PDF for Python を使用して、PDF 文書の各ページに画像ベースのヘッダーとフッターを追加します。同じ画像ファイルが各ページのヘッダーとフッターの両方に使用されます。[`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) が画像の位置を決定し、画像はヘッダー/フッター領域に合わせて自動的に調整されます。

以下のコードスニペットは、Python を使用してヘッダーとフッターを画像として PDF に追加する方法を示しています。

1. 画像を 'ap.Image' オブジェクトにロードし、ヘッダーとして使用できるように準備します。
1. HeaderFooter オブジェクトを作成し、ヘッダー画像を添付します。
1. 同じ画像を再度ロードし、フッターとして使用します。
1. Footer オブジェクトを作成し、フッター画像を追加します。
1. 'ap.Document()' を使用して入力 PDF ドキュメントをロードします。
1. ドキュメントのすべてのページを反復処理します。
1. マージン（左 = 50）を適用してヘッダーとフッターの位置を決定します。
1. ヘッダーとフッターを PDF の各ページに割り当てます。
1. 更新された PDF を指定された出力ファイルに保存します。

この手法は、ヘッダー/フッター領域にロゴや透かしを配置して文書にブランディングするのに最適です。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_image(input_file, image_file, output_file):
    """
    Add image-based headers and footers to all pages of a PDF document.

    Creates headers and footers using image files. The same image is used
    for both header and footer positioning on each page.

    Args:
        input_file (str): Path to the input PDF file.
        image_file (str): Path to the image file to use for headers and footers.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses the same image file for both header and footer
        - Creates separate Image objects for header and footer
        - Sets margin of 50 units left for positioning
        - Image files should be in supported formats (PNG, JPG, etc.)
        - Images are automatically sized to fit header/footer areas

    Example:
        >>> add_header_and_footer_as_image("input.pdf", "logo.png", "output.pdf")
        # Adds image headers and footers using logo.png
    """

    # Create header image
    header_image = ap.Image()
    header_image.file = image_file
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_image)

    # Create footer image
    footer_image = ap.Image()
    footer_image.file = image_file

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_image)

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Set header margin
            margin = ap.MarginInfo()
            margin.left = 50
            header.margin = margin

            # Set footer margin
            footer.margin = margin

            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## テーブルとしてヘッダーとフッターを追加

Aspose.PDF for Python を使用して、PDF ドキュメントのすべてのページに構造化されたテーブルベースのヘッダーとフッターを追加します。[`テーブル`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) オブジェクトは、複雑なヘッダーとフッターに対して、レイアウト制御、配置、そして一貫したフォーマットを向上させます。ヘッダーのテキストは中央揃え、フッターのテキストは左揃えで、どちらも Arial 12pt フォントを使用します。列幅はページ寸法に基づいて動的に計算され、適切な配置が保証されます。

このコードスニペットは、Aspose.PDF for Python を .NET 経由で使用し、テーブルを用いて PDF ドキュメントの各ページにヘッダーとフッターを追加します。

1. ヘッダーとフッターのテキストスタイル（フォント、サイズ、配置）を定義するために、[`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) を使用します。
1. ヘッダーとフッターのために [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) オブジェクトを作成します。
1. ヘッダー用に、単一の行とヘッダーテキストを含むセルを持つ[`テーブル`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) を構築します。
1. フッター用に、単一の行とフッターテキストを含むセルを持つ[`テーブル`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) を構築します。
1. テーブルを対応する[`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) オブジェクトに追加します。
1. フッターの水平位置を適切に設定するために、[`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) を設定します。
1. 適切な方法で[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を開きます。
1. すべてのページを反復処理し、テーブルベースのヘッダーとフッターを各ページに割り当てます。
1. 変更された[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を出力ファイルに保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_table(input_file, output_file):
    """
    Add table-based headers and footers to all pages of a PDF document.

    Creates headers and footers using table structures for better layout
    control and alignment. Demonstrates advanced formatting with text states.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses Table objects for structured layout
        - Header table has centered Arial 12pt text
        - Footer table has left-aligned Arial 12pt text
        - Column width calculated based on page width minus margins
        - Provides more precise control over text positioning

    Example:
        >>> add_header_and_footer_as_table("input.pdf", "output.pdf")
        # Adds table-structured headers and footers to all pages
    """
    text_state_header = ap.text.TextState()
    text_state_header.font = ap.text.FontRepository.find_font("Arial")
    text_state_header.font_size = 12
    text_state_header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    text_state_footer = ap.text.TextState()
    text_state_footer.font = ap.text.FontRepository.find_font("Arial")
    text_state_footer.font_size = 12
    text_state_footer.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # Create header
    header = ap.HeaderFooter()
    # Create footer
    footer = ap.HeaderFooter()
    # Create header Table
    table_header = ap.Table()
    table_header.column_widths = str(594 - header.margin.left - header.margin.right)
    header_row = table_header.rows.add()
    header_row.cells.add("This is a Table Header", text_state_header)
    # Create footer Table
    table = ap.Table()
    table.column_widths = str(594 - footer.margin.left - footer.margin.right)
    table.rows.add().cells.add("Powered by Aspose.PDF", text_state_footer)
    header.paragraphs.add(table_header)
    footer.paragraphs.add(table)
    # Set footer margin
    footer.margin.left = 150

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## LaTeX としてヘッダーとフッターを追加

Aspose.PDF for Python を使用して、PDF ドキュメントのすべてのページに LaTeX 形式のコンテンツを含むヘッダーとフッターを追加します。LaTeX を使用すると、数式記号、日付、著作権マーク、その他の高度な書式設定をレンダリングできます。ヘッダーには動的な日付が含まれ、フッターには現在のページ番号と総ページ数とともに著作権記号が表示されます。

以下のコードスニペットは、Aspose.PDF for Python を .NET 経由で使用し、PDF のヘッダーおよびフッターで [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) を利用する方法を示しています。

1. 適切な方法で[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を開きます。
1. 動的フッターで使用するために総ページ数を取得します。
1. ドキュメントのすべてのページを反復処理します。
1. ヘッダー用に[`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) オブジェクトを作成します。
1. ヘッダーのテキストに LaTeX コマンド（例: `\\today\\`）を含む [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) を作成します。
1. フッター用に[`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) オブジェクトを作成します。
1. フッターテキストに LaTeX 記号とページ番号を含む [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) を作成します。
1. 対応するヘッダー/フッターオブジェクトに[`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) を追加します。
1. 現在のページにヘッダーとフッターをバインドします。
1. 変更された[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を出力ファイルに保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_latex(input_file, output_file):
    """
    Add LaTeX-formatted headers and footers to all pages of a PDF document.

    Creates headers and footers using LaTeX markup for mathematical expressions,
    symbols, and advanced formatting. Demonstrates TeXFragment usage.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses TeXFragment for LaTeX rendering
        - Header includes LaTeX date command (\\today\\)
        - Footer includes copyright symbol and page numbering
        - LaTeX commands are processed and rendered properly
        - Page count is dynamically calculated and inserted

    Example:
        >>> add_header_and_footer_as_latex("input.pdf", "output.pdf")
        # Adds LaTeX-formatted headers and footers with symbols and page numbers
    """
    # Open PDF document
    with ap.Document(input_file) as document:
        page_count = len(document.pages)
        for i in range(1, page_count + 1):
            # Create header
            header = ap.HeaderFooter()
            h_latex_text = "This is a LaTex Header. \\today\\"
            h_l_text = ap.TeXFragment(h_latex_text, True)
            # Create footer
            footer = ap.HeaderFooter()
            f_latex_text = f"\\copyright\\ 2025 My Company -- Page \\thepage\\ is {page_count}"
            f_l_text = ap.TeXFragment(f_latex_text, True)

            header.paragraphs.add(h_l_text)
            footer.paragraphs.add(f_l_text)
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```
