---
title: Add Curve Annotation
type: docs
weight: 20
url: /python-net/add-curve-annotation/
description: This example binds an input PDF, draws a dashed curve on the first page, and saves the modified document.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Curve Annotation to a PDF Using PdfContentEditor in Python
Abstract: This example demonstrates how to add a curve annotation to a PDF document using Aspose.PDF for Python via the Facades API. It shows how to define curve vertices, border style, annotation bounds, text content, and save the updated document.    
---

Curve annotations are used to highlight irregular paths or shapes in a PDF, providing visual emphasis or marking important areas. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), you can draw curves by specifying a sequence of vertices, border style, visibility, annotation rectangle, and descriptive text.

1. Create the PdfContentEditor object.
1. Bind the onput PDF.
1. Configure the Curve properties.
1. Draw the Curve annotation.
1. Save the updated Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_curve_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 1  # 1 - Dashed
    line_info.vertice_coordinate = [120, 520, 160, 560, 220, 540, 280, 580]
    line_info.visibility = True
    content_editor.draw_curve(
        line_info,
        1,
        apd.Rectangle(110, 510, 220, 100),
        "This is curve annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```
