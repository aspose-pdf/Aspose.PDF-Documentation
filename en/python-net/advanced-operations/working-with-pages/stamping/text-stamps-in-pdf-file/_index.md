---
title: Adding Text stamps in PDF via Python
linktitle: Text stamps in PDF File
type: docs
weight: 20
url: /python-net/text-stamps-in-the-pdf-file/
description: Add a text stamp to a PDF document using the TextStamp class with  Aspose.PDF for Python library.
lastmod: "2025-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to add Text stamps in PDF using Python
Abstract: This article provides a comprehensive guide on adding text stamps to PDF files using the Aspose.PDF library for Python. It outlines the use of the `TextStamp` class to create customizable text stamps with properties such as font size, style, color, and alignment. The article includes code snippets demonstrating how to add a simple text stamp, configure text alignment, and apply advanced rendering modes like fill stroke text. The first section explains the creation of a `Document` and `TextStamp` object, setting text properties, and adding the stamp to a specific page. The second section introduces the `text_alignment` property to align text horizontally and vertically, providing a code example of centering text on a PDF page. The final section discusses rendering modes, demonstrating how to add fill stroke text using a `TextState` object to set stroke color and rendering mode before binding to a stamp. Each section is accompanied by practical examples to facilitate understanding and implementation.
---

## Adding Text Stamp with Python

You can use [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) class to add a text stamp in a PDF file. [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) class provides properties necessary to create a text based stamp like font size, font style, and font color etc. In order to add text stamp, you need to create a Document object and a TextStamp object using required properties. After that, you can call [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) method of the Page to add the stamp in the PDF. The following code snippet shows you how to add text stamp in the PDF file. This is useful for adding annotations, watermarks, or labels to PDF pages.

1. Open the PDF document.
1. Create a TextStamp object.
1. Set stamp background behavior.
1. Position the stamp on the page.
1. Rotate the stamp if needed.
1. Set text properties.
1. Add the stamp to a page.
1. Save the modified PDF document.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_stamp(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    # Create text stamp
    text_stamp = ap.TextStamp("Sample Stamp")
    # Set whether stamp is background
    text_stamp.background = True
    # Set origin
    text_stamp.x_indent = 100
    text_stamp.y_indent = 100
    # Rotate stamp
    text_stamp.rotate = ap.Rotation.ON90
    # Set text properties
    text_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_stamp.text_state.font_size = 14.0
    text_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    text_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    text_stamp.text_state.foreground_color = ap.Color.dark_green
    # Add stamp to particular page
    document.pages[1].add_stamp(text_stamp)

    document.save(output_file_name)
```
