---
title: Adding multi line watermark 
type: docs
weight: 10
url: /python-net/adding-multi-line-watermark-to-existing-pdf/
description: This section explains how to add multi line watermark to existing PDF using FormattedText Class.
lastmod: "2026-01-05"
---

This example demonstrates how to create a multi-line text watermark (stamp) for an existing PDF document using Aspose.PDF for Python via .NET. The approach mirrors the .NET Facades API and is commonly used for adding watermarks, headers, or background text to PDF files.

1. Create a Stamp object. A Stamp acts as a container for the content that will be placed onto the PDF pages.

1. The FormattedText class is used to define the appearance of the text, including:

   - Text content
   - Color and transparency (using ARGB)
   - Font style (e.g., Times Italic)
   - Text encoding
   - Font size

    Additional lines can be appended using 'add_new_line_text()', allowing you to create multi-line watermarks such as titles with subtitles or messages spanning multiple rows.

1. Bind the text to the stamp. The formatted text is attached to the stamp using 'bind_logo()'. At this stage, the stamp is fully defined but not yet applied to a document.

1. Apply the stamp to a PDF. The configured stamp is usually added to an existing PDF using PdfFileStamp, which applies the watermark to one or more pages and saves the result.

```python

import aspose.pdf as pdf
import System
from System.Drawing import Color

def add_text_stamp_to_pdf():
    # Instantiate a Stamp object
    logo_stamp = pdf.facades.Stamp()

    # Create a FormattedText object (first line)
    formatted_text = pdf.facades.FormattedText(
        "Hello World!",
        Color.FromArgb(180, 0, 0),                 # Semi-transparent red
        pdf.facades.FontStyle.TimesItalic,         # Font style
        pdf.facades.EncodingType.Winansi,          # Encoding
        False,                                     # Embedded font
        50                                         # Font size
    )

    # Add another line to the stamp
    formatted_text.add_new_line_text("Good Luck")

    # Bind formatted text to the stamp
    logo_stamp.bind_logo(formatted_text)

    return logo_stamp
```
