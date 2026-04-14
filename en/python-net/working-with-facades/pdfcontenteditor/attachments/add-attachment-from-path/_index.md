---
title: Add Attachment From Path
type: docs
weight: 20
url: /python-net/add-attachment-from-path/
description: This example binds an input PDF, attaches an external file using its file path, and saves the modified PDF with the embedded attachment.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Attach Files to a PDF Using File Path Overload in Python
Abstract: This example demonstrates how to attach external files to a PDF document using the file-path overload of 'add_document_attachment()' in Aspose.PDF for Python via the Facades API. It simplifies adding attachments without manually opening a file stream.
---

PDF can include embedded files such as documents, spreadsheets, or images for reference or distribution. The file-path overload of 'add_document_attachment()' allows you to add attachments directly from a file path, eliminating the need to open the file manually.

1. Create the [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) object.
1. Bind the input PDF.
1. Add the Attachment Using File Path.
1. Save the updated Document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_attachment_from_path(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add attachment using file-path overload
    content_editor.add_document_attachment(
        attachment_file,
        "Attachment added using file path overload.",
    )
    # Save updated document
    content_editor.save(outfile)
```
