---
title: Manage Stamp By ID
type: docs
weight: 95
url: /python-net/manage-stamp-by-id/
description: How to manipulate rubber stamp annotations in a PDF by their unique IDs using Aspose.PDF for Python
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Manage Rubber Stamps by ID in a PDF Using PdfContentEditor in Python
Abstract: This example demonstrates how to manipulate rubber stamp annotations in a PDF by their unique IDs using Aspose.PDF for Python via the Facades API. You can hide or show specific stamps on certain pages without affecting other stamps.    
---

In PDFs with multiple rubber stamps, it can be useful to control individual stamps based on their ID. The 'hide_stamp_by_id()' and 'show_stamp_by_id()' methods allow selective visibility control. This example shows how to:

- Add multiple stamps with unique IDs
- Hide a stamp on a specific page
- Show a stamp on another page

By using ID-based operations, you avoid tracking stamps by page position or other attributes.

1. Create a [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instance.
1. Bind the input PDF document.
1. Add rubber stamps with specific IDs.
1. Hide and shows stamps based on their IDs and page numbers.
1. Save the updated PDF document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def manage_stamp_by_id(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        1,
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

    # Apply ID-based stamp operations
    content_editor.hide_stamp_by_id(1, 1)
    content_editor.show_stamp_by_id(1, 2)

    # Save updated document
    content_editor.save(outfile)
```
