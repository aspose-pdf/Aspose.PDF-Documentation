---
title: Pythonでテキスト生成にFloatingBoxを使用する
linktitle: FloatingBoxの使用
type: docs
weight: 30
url: /ja/python-net/floating-box/
description: このページでは、フローティングボックス内のテキストの書式設定方法を説明します。
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: テキスト生成のためのFloatingBoxツール
Abstract: この記事では、Aspose.PDF for Python の FloatingBox ツールの使用方法について包括的なガイドを提供します。このツールを使用すると、開発者は PDF ページ上にテキストやその他のコンテンツを可動可能でスタイル付けされたコンテナに配置できます。基本的な使用法から高度な使用法までカバーし、フローティングボックスの作成方法、枠線や背景色の適用、マルチカラムレイアウトの制御、段落の位置決め、ボックスの垂直・水平揃えを実演します。また、テキストの切り取り、ページ間でのコンテンツの繰り返し、絶対位置指定、拡張されたレイアウト制御といった主要機能も強調し、PDF コンテンツの精密なカスタマイズを可能にします。実用的なコード例を通じて、読者は FloatingBox コンテナの全機能を活用した視覚的に魅力的で構造的に整った PDF の作成方法を学びます。
---

## FloatingBoxツールの基本的な使用方法

`FloatingBox` ツールは、PDF ページ上にテキストやその他のコンテンツを配置するための特殊なコンテナです。その主な機能は、コンテンツがボックスの境界を超えたときのテキストクリッピングです。Aspose.PDF for Python を使用して、`FloatingBox` を [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) に作成し追加します。`FloatingBox` は可動テキストコンテナとして機能し、通常のテキスト段落に比べてレイアウトの位置決め、枠線、スタイリングをより細かく制御できます。

1. 新しい [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を作成します。
1. ドキュメントに [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) を追加します。
1. [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) を作成します。
1. [`BorderInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) と [`BorderSide`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderside/) を使用してボックスの枠線を設定します。
1. [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) プロパティでボックスの繰り返しを制御します。
1. [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) を使用してテキストコンテンツを追加します。
1. `FloatingBox` を [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) に追加します。
1. [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) を使用して最終的な PDF ドキュメントを保存します。

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def create_and_add_floating_box(outfile):
    """
    Create and add a basic floating box to a PDF document.

    Demonstrates the fundamental usage of FloatingBox to create a bordered
    text container with Lorem ipsum content. Shows basic box creation,
    styling, and text content addition.

    Args:
        outfile (str): Path where the PDF with floating box will be saved.

    Returns:
        None: The function creates and saves a PDF file with a floating box.

    Note:
        - Creates a FloatingBox with dimensions 400x30
        - Applies dark green border with 1.5 width
        - Sets is_need_repeating to False for single occurrence
        - Contains Lorem ipsum text fragment
        - Demonstrates basic floating box functionality

    Example:
        >>> create_and_add_floating_box("basic_floating_box.pdf")
        # Creates a PDF with a simple bordered floating text box
    """

    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.border = ap.BorderInfo(ap.BorderSide.ALL, 1.5, ap.Color.dark_green)
        box.is_need_repeating = False
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        box.paragraphs.add(ap.text.TextFragment(phrase))
        # Add box
        page.paragraphs.add(box)
        document.save(outfile)
```  

上の例では、幅400pt、高さ30pt の FloatingBox を作成しています。
また、この例では、意図的に与えられたサイズに収まらないほど多くのテキストを作成しています。
その結果、テキストは切り取られました。

![画像 1](image01.png)

`False` の値を持つプロパティ [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) は、テキストを1ページに限定します。

このプロパティを `True` に設定すると、テキストは同じ位置で次のページに流れます。

![画像 2](image02.png)

## FloatingBox の高度な機能

### マルチカラムサポート

#### マルチカラムレイアウト（シンプルなケース）

`FloatingBox` はマルチカラムレイアウトをサポートします。このようなレイアウトを作成するには、[`ColumnInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/columninfo/) プロパティの値を定義する必要があります。

* `column_widths` は、pt 単位の幅を列挙した文字列です。
* `column_spacing` は、列間の間隔幅を示す文字列です。
* `column_count` は列数を示す数値です。

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def multi_column_layout(outfile):
    """
    Create a multi-column layout using FloatingBox.

    Demonstrates advanced layout capabilities by creating a three-column
    text layout within a floating box. Shows dynamic width calculation
    and column spacing configuration.

    Args:
        outfile (str): Path where the PDF with multi-column layout will be saved.

    Returns:
        None: The function creates and saves a PDF file with multi-column text.

    Note:
        - Creates 3 equal-width columns with 10-unit spacing
        - Calculates column width based on page margins and spacing
        - Uses is_need_repeating for content continuation across columns
        - Adds multiple Lorem ipsum paragraphs for column demonstration
        - Automatically distributes content across columns

    Example:
        >>> multi_column_layout("multi_column.pdf")
        # Creates a PDF with text arranged in three columns
    """
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Set margin settings
        page.page_info.margin = ap.MarginInfo(36, 18, 36, 18)
        column_count = 3
        spacing = 10
        width = (
            page.page_info.width
            - page.page_info.margin.left
            - page.page_info.margin.right
            - (column_count - 1) * spacing
        )
        column_width = width / 3
        # Create FloatingBox
        box = ap.FloatingBox()
        box.is_need_repeating = True
        box.column_info.column_widths = f"{column_width} {column_width} {column_width}"
        box.column_info.column_spacing = f"{spacing}"
        box.column_info.column_count = 3
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        paragraphs = [
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
        ]
        for paragraph in paragraphs:
            box.paragraphs.add(ap.text.TextFragment(paragraph))
        # Add a box to a page
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

上記の例では追加ライブラリ LoremNET を使用し、20 の段落を作成しました。これらの段落は 3 列に分割され、テキストがなくなるまで次のページを埋めました。

#### 強制的に列開始を設定したマルチカラムレイアウト

前の例と同様のことを次の例でも行います。違いは、3 つの段落を作成したことです。FloatingBox に各段落を新しい列でレンダリングさせることができます。そのためには、FloatingBox オブジェクトにテキストを追加する際に `is_first_paragraph_in_column` を設定する必要があります。

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def multi_column_layout_2(outfile):
    """
    Create a multi-column layout with paragraph column control.

    Demonstrates advanced multi-column layout with explicit control over
    paragraph positioning within columns. Uses is_first_paragraph_in_column
    to control text flow and column breaks.

    Args:
        outfile (str): Path where the PDF with controlled multi-column layout will be saved.

    Returns:
        None: The function creates and saves a PDF file with controlled column text.

    Note:
        - Creates 3 equal-width columns with 10-unit spacing
        - Uses is_first_paragraph_in_column for explicit column control
        - Calculates column width dynamically based on page dimensions
        - Demonstrates precise paragraph positioning within columns
        - Shows advanced column layout management techniques

    Example:
        >>> multi_column_layout_2("controlled_columns.pdf")
        # Creates a PDF with precisely controlled multi-column text flow
    """

    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Set margin settings
        page.page_info.margin = ap.MarginInfo(36, 18, 36, 18)
        column_count = 3
        spacing = 10
        width = (
            page.page_info.width
            - page.page_info.margin.left
            - page.page_info.margin.right
            - (column_count - 1) * spacing
        )
        column_width = width / 3
        # Create FloatingBox
        box = ap.FloatingBox()
        box.is_need_repeating = True
        box.column_info.column_widths = f"{column_width} {column_width} {column_width}"
        box.column_info.column_spacing = f"{spacing}"
        box.column_info.column_count = 3
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        paragraphs = [
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
        ]
        for paragraph in paragraphs:
            text = ap.text.TextFragment(paragraph)
            text.is_first_paragraph_in_column = True
            box.paragraphs.add(text)
        # Add a box to a page
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

### 背景サポート

.NET を介した Aspose.PDF for Python を使用して、PDF ドキュメント内の FloatingBox に背景色を適用します。
`FloatingBox` はテキストやその他の要素のコンテナであり、[`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) を背景色として割り当てることで、コンテンツを視覚的に際立たせることができます。ヘッダー、ハイライト、またはスタイルされたセクションに便利です。

このコードスニペットは、サンプルコンテンツを使用したシンプルな淡緑色のテキストボックスの作成方法を示しています。

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def background_support(outfile):
    """
    Demonstrate FloatingBox background color support.

    Shows how to apply background colors to floating boxes to create
    visually distinct text containers. Demonstrates basic styling
    capabilities for enhanced visual presentation.

    Args:
        outfile (str): Path where the PDF with colored background box will be saved.

    Returns:
        None: The function creates and saves a PDF file with a colored floating box.

    Note:
        - Applies light green background color to the floating box
        - Creates a 400x30 box with sample text content
        - Sets is_need_repeating to False for single occurrence
        - Demonstrates visual styling options for floating boxes
        - Shows how background colors enhance text presentation

    Example:
        >>> background_support("colored_background.pdf")
        # Creates a PDF with a light green background floating box
    """

    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.background_color = ap.Color.light_green
        box.is_need_repeating = False
        box.paragraphs.add(ap.text.TextFragment("text example"))
        # Add box
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

### 位置指定サポート

生成されたページ上の FloatingBox の位置は、`positioning_mode`、`left`、`top` プロパティによって決まります。
`positioning_mode` の値が

* [`ParagraphPositioningMode.DEFAULT`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/) （デフォルト値）

位置は以前に配置された要素によって決まり、要素を追加するとその後続の要素の位置に影響します。[`Left`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) または [`Top`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) がゼロでない場合も考慮されますが、組み合わせたロジックは必ずしも明白ではありません。

* [`ParagraphPositioningMode.ABSOLUTE`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/)

位置は `Left` と `Top` の値で指定されます。前の要素に依存せず、後続の要素の位置にも影響しません。

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def offset_support(outfile):
    """
    Demonstrate FloatingBox positioning and offset support.

    Shows how to position floating boxes at specific coordinates using
    absolute positioning mode. Demonstrates integration of floating boxes
    with regular text content and precise layout control.

    Args:
        outfile (str): Path where the PDF with positioned floating box will be saved.

    Returns:
        None: The function creates and saves a PDF file with positioned floating box.

    Note:
        - Uses absolute positioning mode for precise box placement
        - Sets box position to top=45, left=15 coordinates
        - Creates bordered box with dark green border
        - Integrates floating box with regular text paragraphs
        - Demonstrates layered content with mixed positioning

    Example:
        >>> offset_support("positioned_box.pdf")
        # Creates a PDF with a floating box at specific coordinates
    """

    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.top = 45
        box.left = 15
        box.positioning_mode = ap.ParagraphPositioningMode.ABSOLUTE
        box.border = ap.BorderInfo(ap.BorderSide.ALL, 1.5, ap.Color.dark_green)
        box.paragraphs.add(ap.text.TextFragment("text example 1"))
        page.paragraphs.add(ap.text.TextFragment("text example 2"))
        # Add the box to the page
        page.paragraphs.add(box)
        page.paragraphs.add(ap.text.TextFragment("text example 3"))
        document.save(outfile)
```

### PDFで垂直方向と水平方向の配置でフローティングボックスを整列

`FloatingBox` 要素を PDF ページ内で、Aspose.PDF for Python via .NET のさまざまな [`垂直配置`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/) と [`水平配置`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) オプションを使用して整列させます。レイアウト位置（上、中央、下、左、右）を制御し、フローティング コンテナの正確な視覚的配置を実現する方法を示します。各フローティング ボックスには異なる位置が割り当てられ、ページレイアウト、ヘッダー/フッターの配置、またはサイド注釈における配置の柔軟性を示します。

1. 新しい PDF ドキュメントを作成します。
1. ドキュメントにページを追加します。
1. 最初の FloatingBox を作成します（右下揃え）。
1. 2 番目の FloatingBox を作成します（右中央揃え）。
1. 3 番目の FloatingBox を作成します（右上揃え）。
1. ドキュメントを保存します。

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def align_text_to_float(outfile):
    """
    Demonstrate text alignment options for FloatingBox elements.

    Shows different vertical and horizontal alignment options for floating
    boxes. Creates multiple boxes with different alignment settings to
    demonstrate positioning flexibility.

    Args:
        outfile (str): Path where the PDF with aligned floating boxes will be saved.

    Returns:
        None: The function creates and saves a PDF file with variously aligned boxes.

    Note:
        - Creates three 100x100 floating boxes with different alignments
        - First box: bottom-right alignment
        - Second box: center-right alignment
        - Third box: top-right alignment
        - All boxes have blue borders for visual distinction
        - Demonstrates comprehensive alignment control options

    Example:
        >>> align_text_to_float("aligned_boxes.pdf")
        # Creates a PDF with floating boxes in different alignment positions
    """
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()

        # Create float box
        float_box = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box.vertical_alignment = ap.VerticalAlignment.BOTTOM
        float_box.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box.paragraphs.add(ap.text.TextFragment("FloatingBox_bottom"))
        float_box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box)

        # Create float box
        float_box_2 = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box_2.vertical_alignment = ap.VerticalAlignment.CENTER
        float_box_2.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box_2.paragraphs.add(ap.text.TextFragment("FloatingBox_center"))
        float_box_2.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box_2)

        # Create float box
        float_box_3 = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box_3.vertical_alignment = ap.VerticalAlignment.TOP
        float_box_3.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box_3.paragraphs.add(ap.text.TextFragment("FloatingBox_top"))
        float_box_3.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box_3)

        # Save the document
        document.save(outfile)
```
