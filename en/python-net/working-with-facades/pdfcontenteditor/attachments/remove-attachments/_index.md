---
title: Remove Attachments
type: docs
weight: 50
url: /python-net/remove-attachments/
description: This example binds an input PDF, deletes all attachments, and saves the modified PDF without any embedded files.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remove All Attachments from a PDF Using Python
Abstract: This example demonstrates how to remove all file attachments from a PDF document using Aspose.PDF for Python via the Facades API. It shows how to bind a PDF, delete embedded attachments, and save the updated document.  
---

PDFs may contain attachments such as documents, images, or other files. There are scenarios where you need to clean a PDF of all attachments for security, privacy, or distribution purposes. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), you can programmatically remove all embedded attachments in a document.

1. Create the PdfContentEditor object. 
1. Bind the input PDF.
1. Delete All Attachments.
1. Save the updated Document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def remove_attachments(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Remove all attachments from document
    content_editor.delete_attachments()
    # Save updated document
    content_editor.save(outfile)
```