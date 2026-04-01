---
title: Add Polygon Annotation
type: docs
weight: 40
url: /python-net/add-polygon-annotation/
description: This example binds an input PDF, draws a solid polygon on the first page, and saves the modified document with an annotation.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Polygon Annotation to a PDF Using PdfContentEditor in Python
Abstract: This example demonstrates how to add a polygon annotation to a PDF document using Aspose.PDF for Python via the Facades API. It shows how to define polygon vertices, border style, annotation bounds, descriptive text, and save the updated document.    
---

Polygon annotations are used to highlight irregular areas or shapes in a PDF, providing visual emphasis or marking specific regions. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), you can create polygons by specifying the vertices coordinates, border style, page number, and annotation rectangle.

1. Create the PdfContentEditor object.
1. Bind the input PDF.
1. Configure Polygon properties.
1. Add the Polygon annotation.
1. Save the updated Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def add_polygon_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 0 # 0 - Solid
    line_info.vertice_coordinate = [100, 200, 150, 260, 220, 220, 200, 160]
    content_editor.create_polygon(
        line_info,
        1,
        apd.Rectangle(90, 150, 150, 120),
        "This is polygon annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```