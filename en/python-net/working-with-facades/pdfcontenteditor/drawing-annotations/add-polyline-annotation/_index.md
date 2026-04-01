---
title: Add Polyline Annotation
type: docs
weight: 50
url: /python-net/add-polyline-annotation/
description: The example binds an input PDF, creates a solid polyline on the first page, and saves the modified document with an annotation.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Polyline Annotation to a PDF Using PdfContentEditor in Python
Abstract: This example demonstrates how to add a polyline annotation to a PDF document using Aspose.PDF for Python via the Facades API. It shows how to define a sequence of vertices, border style, annotation rectangle, text, and save the updated document.    
---

Polyline annotations allow you to highlight a series of connected line segments in a PDF. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), you can draw a polyline by specifying vertices coordinates, border style, page number, and annotation bounds. This is useful for visually representing paths, trends, or connections in diagrams and documents.

1. Create the PdfContentEditor object.
1. Bind the input PDF.
1. Configure Polyline properties.
1. Add the Polyline annotation.
1. Save the updated Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def add_polyline_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 0 # 0 - Solid
    line_info.vertice_coordinate = [120, 420, 180, 460, 230, 430, 290, 470]
    content_editor.create_poly_line(
        line_info,
        1,
        apd.Rectangle(110, 410, 200, 90),
        "This is polyline annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```