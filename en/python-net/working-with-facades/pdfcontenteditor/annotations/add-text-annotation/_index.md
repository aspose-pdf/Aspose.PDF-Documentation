---
title: Add Text Annotations
type: docs
weight: 50
url: /python-net/add-text-annotation/
description: Add text annotations to a PDF document using the PdfContentEditor class in Aspose.PDF for Python via .NET.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Text Annotations in Python
Abstract: Learn how to add text annotations to a PDF document using the PdfContentEditor class in Aspose.PDF for Python via .NET. This example shows how to place a text annotation at a specific position, define its title and contents, and save the updated PDF file.
---

This article shows how to add a text annotation to a PDF document using the [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) class in Aspose.PDF.

Text annotations let you attach comments, notes, or extra information to specific parts of a PDF page. These annotations can appear as icons and be expanded by users when viewing the document.

In this example:

- A PDF document is loaded into the PdfContentEditor.
- A text annotation is added at a specific position on the page.
- The annotation includes a title, content, icon type, and visibility settings.
- The modified document is saved to a new file.

1. Create a PdfContentEditor object.
1. Bind the input PDF Document.
1. Define annotation position.
1. Add Text annotation.
1. Save the updated PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def add_text_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add text annotation to page 1
    content_editor.create_text(apd.Rectangle(100, 400, 50, 50), "Text Annotation", "This is a text annotation", True, "Insert", 1)
    # Save updated document
    content_editor.save(outfile)
```
