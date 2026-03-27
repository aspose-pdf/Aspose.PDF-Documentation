---
title: Add Markup Annotations
type: docs
weight: 30
url: /python-net/add-markup-annotation/
description: This example binds an input PDF, adds four different markup annotations to the first page, and saves the updated document. Each annotation demonstrates a different markup style and color.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Add Highlight, Underline, Strikeout, and Squiggly Markup Annotations in a PDF Using Python
Abstract: This example demonstrates how to add multiple markup annotations—highlight, underline, strikeout, and squiggly—to a PDF document using Aspose.PDF for Python via the Facades API. The sample shows how to define annotation areas, specify markup types, apply colors, and save the modified document.   
---

Markup annotations are used to emphasize or review text within a PDF. With PdfContentEditor, you can programmatically apply different markup styles by specifying a rectangle area, comment text, markup type, page number, and color.

1. Create the [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) object.
1. Bind the input PDF.
1. Define Annotation rectangles.
1. Add Markup Annotations.
1. Save the updated Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def add_markup_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add markup annotation to page 1
    content_editor.create_markup(apd.Rectangle(120, 440, 200, 20), "This is a highlight annotation", 0, 1, apd.Color.yellow)
    content_editor.create_markup(apd.Rectangle(110, 542, 200, 20), "This is a underline annotation", 1, 1, apd.Color.yellow)
    content_editor.create_markup(apd.Rectangle(120, 568, 200, 20), "This is a strikeout annotation", 2, 1, apd.Color.orange_red)
    content_editor.create_markup(apd.Rectangle(110, 598, 200, 20), "This is a squiggly annotation", 3, 1, apd.Color.dark_blue)
    # Save updated document
    content_editor.save(outfile)
```