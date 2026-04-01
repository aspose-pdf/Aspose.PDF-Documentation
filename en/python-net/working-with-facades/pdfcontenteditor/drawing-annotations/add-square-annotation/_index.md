---
title: Add Square Annotation
type: docs
weight: 60
url: /python-net/add-square-annotation/
description: This example binds an input PDF, adds a filled blue square annotation on the first page, and saves the modified document.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Square Annotation to a PDF Using PdfContentEditor in Python
Abstract: This example demonstrates how to add a square annotation to a PDF document using Aspose.PDF for Python via the Facades API. It shows how to define the annotation rectangle, text content, color, fill options, and save the updated document.   
---

Square annotations are commonly used to highlight areas of interest, mark important sections, or provide visual cues in a PDF document. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), you can create square (or circular) annotations by specifying the bounding rectangle, content text, border color, fill option, page number, and border width.

1. Create the PdfContentEditor object.
1. Bind the input PDF.
1. Define the Square annotation.
1. Add the Square annotation.
1. Save the updated Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def add_square_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)
    
    # Create SquareAnnotation object
    rect = apd.Rectangle(100, 300, 200, 400)
    contents = "This is square annotation"
    content_editor.create_square_circle(rect, contents, apd.Color.blue, True, 1, 3)
    
    # Save output PDF file
    content_editor.save(outfile)
```