---
title: Move Stamp By Index
type: docs
weight: 90
url: /python-net/move-stamp-by-index/
description: How to reposition rubber stamp annotations in a PDF by using their index on a page with Aspose.PDF for Python
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Move Rubber Stamps in a PDF Using Index-Based Positioning
Abstract: This example demonstrates how to reposition rubber stamp annotations in a PDF by using their index on a page with Aspose.PDF for Python via the Facades API. It highlights creating multiple stamps and preparing them for movement operations.    
---

In PDF editing, it may be necessary to adjust the position of existing rubber stamps. This code snippet shows how to:

- Add multiple stamps on the same page
- Prepare them for repositioning using their index
- Optionally move a stamp by specifying its page, index, and new coordinates

The 'move_stamp(page_number, stamp_index, new_x, new_y)' method can reposition stamps precisely.

1. Create a [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) object.
1. Bind the PDF to the editor.
1. Add multiple rubber stamps to a page.
1. Save the document before performing movement operations.
1. Move a specific stamp by its index.
1. Save the updated PDF.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_stamp_by_index(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        2,
        apd.Rectangle(200, 380, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )

    content_editor.create_rubber_stamp(
        2,
        apd.Rectangle(200, 480, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )
    content_editor.save(outfile)

    # Move first stamp on page 1 by index
    # content_editor.move_stamp(1, 1, 10, 10)
    # Save updated document
    content_editor.save(outfile)
```    
