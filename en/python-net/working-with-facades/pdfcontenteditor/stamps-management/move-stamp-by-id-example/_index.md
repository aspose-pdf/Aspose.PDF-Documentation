---
title: Move Stamp By ID
type: docs
weight: 80
url: /python-net/move-stamp-by-id-example/
description: In this example, a rubber stamp is added to page 1 and then moved to a new position using its ID before saving the updated document.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Move a Rubber Stamp by ID in a PDF Using PdfContentEditor in Python
Abstract: This example demonstrates how to reposition an existing rubber stamp annotation in a PDF using Aspose.PDF for Python via the Facades API. It shows how to create a stamp and then move it programmatically using its ID.    
---

After adding a rubber stamp annotation to a PDF, you may need to adjust its position. The 'move_stamp_by_id()' method allows you to relocate a stamp based on its identifier, without recreating it. This is useful in automated workflows where stamp placement must be dynamically adjusted.

1. Create a [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instance.
1. Bind the input PDF document.
1. Add a rubber stamp annotation.
1. Move the stamp using its ID.
1. Save the updated PDF document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_stamp_by_id_example(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(300, 420, 180, 60),
        "Approved",
        "Move this stamp by ID",
        apd.Color.green,
    )

    # Move stamp by ID overload
    content_editor.move_stamp_by_id(1, 1, 240, 360)

    # Save updated document
    content_editor.save(outfile)
```    
