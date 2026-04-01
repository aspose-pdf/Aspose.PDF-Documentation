---
title: Add PDF Document Link
type: docs
weight: 50
url: /python-net/add-pdf-document-link/
description: This example binds an input PDF, adds a green-colored link to a page in another PDF, and saves the modified document.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add a PDF Document Link Using PdfContentEditor in Python
Abstract: This example demonstrates how to add a link to another PDF document using Aspose.PDF for Python via the Facades API. It shows how to create a clickable area that opens a different PDF and save the updated document.     
---

PDF document links allow users to navigate from one PDF to another seamlessly. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), you can define a clickable rectangle that links to a page in a different PDF file, making your documents interactive and connected.

1. Create a PdfContentEditor instance.
1. Bind the input PDF document.
1. Define a rectangle for the clickable link.
1. Specifie the linked PDF file, source page, and destination page.
1. Set the link color.
1. Save the updated PDF document.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def add_pdf_document_link(infile, linked_pdf, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add link to another PDF document
    content_editor.create_pdf_document_link(
        apd.Rectangle(140, 590, 240, 20),
        linked_pdf,
        1,
        1,
        apd.Color.green,
    )
    # Save updated document
    content_editor.save(outfile)
```