---
title: Use FloatingBox for PDF Text Layout in Python
linktitle: Using FloatingBox
type: docs
weight: 30
url: /python-net/floating-box/
description: Learn how to use FloatingBox for text layout and styled content containers in PDF documents in Python.
lastmod: "2026-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Create styled floating text containers in PDF files with Python
Abstract: This article explains how to use FloatingBox in Aspose.PDF for Python via .NET. Learn how to place text and other content in styled floating containers, control layout, borders, alignment, and clipping, and build more structured PDF page designs in Python.
---

## Basics of using the FloatingBox tool

The [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) tool is a specialized container for placing text and other content on a PDF page. Its main feature is text clipping when content exceeds the box bounds. Create and add a `FloatingBox` to a [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) using Aspose.PDF for Python. A `FloatingBox` acts as a movable text container, allowing more control over layout positioning, borders, and styling compared to regular text paragraphs.

1. Create a new [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Add a [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) to the document.
1. Create a [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/).
1. Set the box border using [`BorderInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) and [`BorderSide`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderside/).
1. Control box repetition with the [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) property.
1. Add text content using [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/).
1. Add the `FloatingBox` to the [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Save the final PDF document using [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python
import sys
import aspose.pdf as ap
from os import path

def create_and_add_floating_box(outfile):
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

In the example above, we are creating a FloatingBox with a width of 400 pt and a height of 30 pt.
Also, in this example, more text was intentionally created than could fit in the given size.
As a result, the text was cut off.

![Image 1](image01.png)

Property [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) with `False` value limits text to a single page.

If we set this property to `True` the text will reflow to subsequent pages in the same position.

![Image 2](image02.png)

## Advanced features of FloatingBox

### Multi-column support

#### Multi-column layout (simple case)

`FloatingBox` supports multi-column layout. To create such a layout, you must define the values of the [`ColumnInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/columninfo/) properties.

* `column_widths` is a string with enumeration of width in pt.
* `column_spacing` is a string with width of the gap between columns.
* `column_count` is a number of columns.

```python
import sys
import aspose.pdf as ap
from os import path

def multi_column_layout(outfile):
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

We used the additional library LoremNET in the above example and created 20 paragraphs. These paragraphs were divided into three columns and filled the following pages until the text ran out.

#### Multi-column layout with forced column start

We will do the same with the following example as the previous one. The difference is that we created 3 paragraphs. We can force FloatingBox to render each paragraph in the new column. To do that we need to set `is_first_paragraph_in_column` when we adding text to the FloatingBox object.

```python
import sys
import aspose.pdf as ap
from os import path

def multi_column_layout_2(outfile):
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

### Background support

Apply a background color to a FloatingBox in a PDF document using Aspose.PDF for Python via .NET.
A `FloatingBox` is a container for text or other elements, and by assigning a [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) as the background color, you can make the content stand out visually — useful for headers, highlights, or styled sections.

This code snippet shows how to create a simple light green text box with sample content.

```python
import sys
import aspose.pdf as ap
from os import path

def background_support(outfile):
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

### Positioning support

The location of the FloatingBox on the generated page is determined by the `positioning_mode`, `left`, `top` properties.
When the `positioning_mode` value is

 * [`ParagraphPositioningMode.DEFAULT`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/) (default value)

The location is determined by previously placed elements; adding an element affects the location of subsequent elements. If [`Left`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) or [`Top`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) are non-zero, they are considered too, but the combined logic can be non-obvious.

 * [`ParagraphPositioningMode.ABSOLUTE`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/)

The location is specified by the `Left` and `Top` values; it does not depend on previous elements and does not affect the location of subsequent ones.

```python
import sys
import aspose.pdf as ap
from os import path

def offset_support(outfile):
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

### Align Floating Boxes with Vertical and Horizontal Alignment in PDF

Align `FloatingBox` elements within a PDF page using different [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/) and [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) options in Aspose.PDF for Python via .NET. It shows how to control layout positioning (top, center, bottom, left, right) to achieve precise visual alignment of floating containers. Each floating box is assigned a distinct position to showcase alignment flexibility for page layout, header/footer placement, or side annotations.

1. Create a New PDF Document.
1. Add a Page to the Document.
1. Create the First FloatingBox (Bottom-Right Alignment).
1. Create the Second FloatingBox (Center-Right Alignment).
1. Create the Third FloatingBox (Top-Right Alignment).
1. Save the Document.

```python
import sys
import aspose.pdf as ap
from os import path

def align_text_to_float(outfile):
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

## Related Text Topics

- [Work with text in PDF using Python](/pdf/python-net/working-with-text/)
- [Adding text to PDF](/pdf/python-net/add-text-to-pdf-file/)
- [Format PDF text in Python](/pdf/python-net/text-formatting-inside-pdf/)
- [Add tooltips to PDF text in Python](/pdf/python-net/pdf-tooltip/)