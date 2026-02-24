---
title: 使用 FloatingBox 进行 Python 文本生成
linktitle: 使用 FloatingBox
type: docs
weight: 30
url: /zh/python-net/floating-box/
description: 本页解释了如何在浮动框内格式化文本。
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: 用于文本生成的 FloatingBox 工具
Abstract: 本文提供了在 Aspose.PDF for Python 中使用 FloatingBox 工具的全面指南，该工具允许开发者在 PDF 页面上将文本和其他内容放置在可移动、样式化的容器中。文章涵盖了基础和高级用法，演示如何创建浮动框、应用边框和背景颜色、控制多列布局、管理段落定位，以及垂直和水平对齐容器。文章还强调了关键特性，如文本裁剪、跨页重复内容、绝对定位和增强的布局控制，从而实现对 PDF 内容的精确自定义。通过实用的代码示例，读者可以学习如何创建视觉上吸引人且结构良好的 PDF，充分利用 FloatingBox 容器的全部功能。
---

## 使用 FloatingBox 工具的基础

The [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) 工具是一个用于在 PDF 页面上放置文本和其他内容的专用容器。其主要特性是在内容超出框边界时进行文本裁剪。使用 Aspose.PDF for Python 创建并将 `FloatingBox` 添加到 [`文档`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。`FloatingBox` 充当可移动的文本容器，与普通文本段落相比，能够提供对布局定位、边框和样式的更多控制。

1. 创建一个新的 [`文档`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。
1. 向文档中添加一个 [`页面`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)。
1. 创建一个 [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/)。
1. 使用 [`边框信息`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) 和 [`边框侧`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderside/) 设置框的边框。
1. 使用 [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) 属性控制框的重复。
1. 使用 [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) 添加文本内容。
1. 将 `FloatingBox` 添加到 [`页面`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)。
1. 使用 [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 保存最终的 PDF 文档。

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

在上面的示例中，我们创建了一个宽度为 400 pt、高度为 30 pt 的 FloatingBox。
此外，在此示例中，故意创建的文本超过了给定尺寸的容纳范围。
结果，文本被截断。

![Image 1](image01.png)

属性 [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) 设置为 `False` 时，将文本限制在单页。

如果将此属性设置为 `True`，文本将以相同位置在后续页面重新流动。

![Image 2](image02.png)

## FloatingBox 的高级功能

### 多列支持

#### 多列布局（简单案例）

`FloatingBox` 支持多列布局。要创建此类布局，必须定义 [`ColumnInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/columninfo/) 属性的值。

* `column_widths` 是以 pt 为单位的宽度枚举字符串。
* `column_spacing` 是列间间距宽度的字符串。
* `column_count` 是列数。

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

我们在上述示例中使用了额外的库 LoremNET，并创建了 20 个段落。这些段落被划分为三列，并填充到以下页面，直至文本用尽。

#### 强制列起始的多列布局

我们将使用以下示例进行相同操作，与之前的不同之处在于我们创建了 3 个段落。我们可以强制 FloatingBox 在新列中渲染每个段落。为此，需要在向 FloatingBox 对象添加文本时设置 `is_first_paragraph_in_column`。

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

### 背景支持

使用 Aspose.PDF for Python via .NET 为 PDF 文档中的 FloatingBox 应用背景颜色。
`FloatingBox` 是用于文本或其他元素的容器，通过分配 [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) 作为背景颜色，可以使内容在视觉上突出——这对于标题、重点或样式化的章节非常有用。

此代码片段展示了如何创建一个带有示例内容的浅绿色文本框。

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

### 定位支持

生成页面上 FloatingBox 的位置由 `positioning_mode`、`left`、`top` 属性决定。
当 `positioning_mode` 值为

* [`ParagraphPositioningMode.DEFAULT`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/)（默认值）

位置由之前放置的元素决定；添加元素会影响后续元素的位置。如果 [`Left`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) 或 [`Top`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) 的值非零，它们也会被考虑，但组合逻辑可能并不直观。

* [`ParagraphPositioningMode.ABSOLUTE`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/)

位置由 `Left` 和 `Top` 值指定；它不依赖于之前的元素，也不影响后续元素的位置。

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

### 在 PDF 中使用垂直和水平对齐对齐浮动框

在 PDF 页面中使用不同的 [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/) 和 [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) 选项，对 `FloatingBox` 元素进行对齐，适用于 Aspose.PDF for Python via .NET。它展示了如何控制布局定位（顶部、居中、底部、左侧、右侧），以实现浮动容器的精确视觉对齐。每个浮动框被分配了不同的位置，以展示在页面布局、页眉/页脚放置或侧边注释中的对齐灵活性。

1. 创建一个新 PDF 文档。
1. 向文档添加页面。
1. 创建第一个 FloatingBox（右下对齐）。
1. 创建第二个 FloatingBox（右侧居中对齐）。
1. 创建第三个 FloatingBox（右上对齐）。
1. 保存文档。

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
