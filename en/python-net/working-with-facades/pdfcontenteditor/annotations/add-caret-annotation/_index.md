---
title: Add Caret Annotation
type: docs
weight: 10
url: /python-net/add-caret-annotation/
description: This example loads an existing PDF, adds a caret annotation to the first page, and saves the modified document. The annotation includes a red caret symbol and descriptive comment text.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Add Caret Annotation to a PDF Using Python
Abstract: This example demonstrates how to add a caret annotation to a PDF document using Aspose.PDF for Python via the Facades API. The sample shows how to bind a PDF file, define annotation placement using rectangles, configure caret properties, and save the updated document.    
---

Caret annotations are commonly used to indicate text insertions or editorial comments in a document. With PdfContentEditor, you can programmatically add caret annotations by specifying the page number, annotation bounds, callout area, symbol, note text, and color.

1. Create the [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) object.
1. Bind the input PDF.
1. Define Caret Annotation parameters:
  - Page number where annotation will be added
  - Caret rectangle (annotation position)
  - Callout rectangle (text area)
  - Symbol (for example "P")
  - Annotation text
  - Annotation color
1. Add the Caret Annotation.
1. Save the updated Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def add_caret_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add caret annotation to page 1
    content_editor.create_caret(1, 
                                apd.Rectangle(350, 400, 10, 10), 
                                apd.Rectangle(300, 380, 115, 15), 
                                "P", "This is a caret annotation",
                                apd.Color.red)
    # Save updated document
    content_editor.save(outfile)
```