---
title: Delete All Images from PDF
type: docs
weight: 10
url: /python-net/delete-all-images/
description: Delete all images from a PDF document using Aspose.PDF for Python via the Facades API.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remove All Images from a PDF Using PdfContentEditor in Python
Abstract: This example demonstrates how to delete all images from a PDF document using Aspose.PDF for Python via the Facades API. It shows how to bind a PDF, remove all embedded images, and save the updated document.    
---

PDF documents often contain images for illustrations, branding, or decoration. There may be cases where you need to remove all images from a PDF, such as reducing file size, protecting sensitive visuals, or preparing a text-only version.

Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), you can programmatically remove all images from a PDF, ensuring the document only contains textual content. This example binds an input PDF, deletes all images, and saves the modified file.

1. Create the PdfContentEditor object.
1. Bind the input PDF.
1. Delete All images.
1. Save the updated Document.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def delete_all_image(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Delete all images from the document
    content_editor.delete_image()
    # Save updated document
    content_editor.save(outfile)
```