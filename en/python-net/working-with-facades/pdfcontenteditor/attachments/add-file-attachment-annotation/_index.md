---
title: Add File Attachment Annotation
type: docs
weight: 30
url: /python-net/add-file-attachment-annotation/
description: The example binds an input PDF, adds a file attachment annotation to the first page using the file path, and saves the updated document.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add File Attachment Annotations to a PDF Using Python
Abstract: This example demonstrates how to create a file attachment annotation in a PDF using a file path with Aspose.PDF for Python via the Facades API. It shows how to define annotation placement, set description text, choose an icon type, and save the modified document.  
---

File attachment annotations allow you to embed external files as interactive icons on a PDF page. Using the file-path overload, you can attach files directly from disk without manually opening streams. This method also lets you customize the annotation icon and provide a description for users.

1. Create the [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) object.
1. Bind the input PDF.
1. Define the Annotation Rectangle.
1. Add the File Attachment Annotation.
1. Save the updated Document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def add_file_attachment_annotation(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Create file attachment annotation on page 1
    content_editor.create_file_attachment(
        apd.Rectangle(100, 520, 20, 20),
        "Attachment annotation contents",
        attachment_file,
        1,
        "PushPin",
    )
    # Save updated document
    content_editor.save(outfile)
```