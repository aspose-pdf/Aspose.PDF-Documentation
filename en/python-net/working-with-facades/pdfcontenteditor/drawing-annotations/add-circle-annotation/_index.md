---
title: Add Circle Annotation
type: docs
weight: 10
url: /python-net/add-circle-annotation/
description: This example binds an input PDF, creates a circle annotation on the first page, and saves the modified document.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Circle Annotation to a PDF Using PdfContentEditor in Python
Abstract: This example demonstrates how to add a circle annotation to a PDF document using Aspose.PDF for Python via the Facades API. It shows how to define annotation bounds, set content text, configure color and appearance, and save the updated document.    
---

Circle annotations are useful for highlighting areas of interest in a PDF document. With [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), you can create circular shapes by specifying the rectangle that defines the circle’s bounds, along with annotation text, color, fill options, page number, and border width.

1. Create the PdfContentEditor object.
1. Bind the input PDF.
1. Define the Circle Bounds.
1. Add the Circle annotation.
1. Save the updated Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_circle_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create CircleAnnotation object
    rect = apd.Rectangle(300, 300, 400, 400)
    contents = "This is circle annotation"
    content_editor.create_square_circle(rect, contents, apd.Color.blue, False, 1, 3)

    # Save output PDF file
    content_editor.save(outfile)
```
