---
title: Add Attachment
type: docs
weight: 10
url: /python-net/add-attachment/
description: This example binds an input PDF, attaches an external file to the first page, and saves the modified PDF with the embedded attachment.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add File Attachments to a PDF Using Python
Abstract: This example demonstrates how to attach external files to a PDF document using Aspose.PDF for Python via the Facades API. It shows how to bind a PDF, add attachments with descriptions, and save the updated document.
---

File attachments in PDFs allow you to include supplementary documents, images, or other resources directly within the PDF. With [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), you can programmatically attach files to specific pages, set the attachment name, and provide a description.

1. Create the PdfContentEditor object.
1. Bind the input PDF.
1. Open the Attachment file.
1. Add the Attachment to the PDF.
1. Save the updated Document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_attachment(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add attachment to page 1
    with open(attachment_file, "rb") as attachment_stream:
        content_editor.add_document_attachment(
            attachment_stream,
            path.basename(attachment_file),
            "This is a sample attachment for demonstration purposes.",
        )
    # Save updated document
    content_editor.save(outfile)
```
