---
title: Add Line Annotation
type: docs
weight: 30
url: /python-net/add-line-annotation/
description: This example binds an input PDF, draws a red line annotation with square line endings, and saves the modified PDF.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Line Annotation to a PDF Using PdfContentEditor in Python
Abstract: This example demonstrates how to add a line annotation to a PDF document using Aspose.PDF for Python via the Facades API. It explains how to define the line’s start and end points, rectangle bounds, appearance properties, and save the updated document.   
---

Line annotations are useful for emphasizing text, highlighting relationships, or drawing attention to specific areas in a PDF. With [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), you can programmatically create line annotations by specifying the start and end points, bounding rectangle, color, border style, and line endings.

1. Create the PdfContentEditor object.
1. Bind the input PDF.
1. Define Line Annotation properties.
1. Add the Line annotation.
1. Save the updated Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def add_line_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)
    
    # Create LineAnnotation object
    rect = apd.Rectangle(100, 100, 200, 200)
    contents = "This is line annotation"
    content_editor.create_line(rect, contents, 100, 100, 200, 200, 1, 1, apd.Color.red, "Solid", [3,2], ["Square"])
    
    # Save output PDF file
    content_editor.save(outfile)
```