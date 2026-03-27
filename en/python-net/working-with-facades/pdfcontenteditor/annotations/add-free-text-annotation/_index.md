---
title: Add Free Text Annotations
type: docs
weight: 20
url: /python-net/add-free-text-annotation/
description: This example loads an existing PDF file, adds a free text annotation to the first page at a defined position, and saves the modified document.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Add Free Text Annotation to a PDF Using Python
Abstract: This example demonstrates how to insert a free text annotation into a PDF document using Aspose.PDF for Python via the Facades API. It shows how to bind a PDF, define annotation placement, add custom text, and save the updated document.
---

Free text annotations allow you to place visible text directly onto a PDF page without requiring pop-up comments. Using PdfContentEditor, you can specify the annotation rectangle, the displayed text, and the target page.

1. Create the [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) object.
1. Bind the input PDF.
1. Define the Annotation position.
1. Add the Free Text Annotation.
1. Save the updated Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def add_free_text_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add free text annotation to page 1
    content_editor.create_free_text(apd.Rectangle(200, 480, 150, 25), "This is a free text annotation", 1)
    # Save updated document
    content_editor.save(outfile)
```