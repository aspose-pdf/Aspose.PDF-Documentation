---
title: Add Popup Annotations
type: docs
weight: 40
url: /python-net/add-popup-annotation/
description: This example loads a PDF, adds a popup annotation to the first page, and saves the modified document. The popup is set to be visible by default and displays the specified comment text.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Add Popup Annotations to a PDF Using Python
Abstract: This example demonstrates how to insert a popup annotation into a PDF document using Aspose.PDF for Python via the Facades API. It explains how to define the popup area, set the annotation text, control visibility, and save the updated document.
---

Popup annotations are useful for adding comments, explanations, or interactive notes in PDF files. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), you can create popup annotations programmatically by specifying the location, content, visibility, and page number.

1. Create the PdfContentEditor object.
1. Bind the input PDF.
1. Define the Popup Annotation rectangle.
1. Add the Popup Annotation.
1. Save the updated Document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def add_popup_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add popup annotation to page 1
    content_editor.create_popup(
        apd.Rectangle(220, 520, 180, 80),
        "This is a popup annotation",
        True,
        1,
    )
    # Save updated document
    content_editor.save(outfile)
```