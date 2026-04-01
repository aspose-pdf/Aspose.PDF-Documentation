---
title: Delete Images from PDF
type: docs
weight: 20
url: /python-net/delete-images/
description: 
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Delete Specific Images from a PDF Page Using PdfContentEditor in Python
Abstract: This example demonstrates how to delete specific images from a PDF document using Aspose.PDF for Python via the Facades API. It shows how to target images on a specific page and save the updated document.    
---

Sometimes, you may want to remove only certain images from a PDF rather than clearing all visuals. With [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), you can delete selected images by specifying the page number and the image index.

This code snippet binds an input PDF, deletes the second image on page 1, and saves the modified PDF, leaving other images intact.

1. Create a PdfContentEditor instance.
1. Bind the input PDF document.
1. Delete specific images from a designated page.
1. Save the updated PDF document.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def delete_images(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Delete image on page 1
    content_editor.delete_image(1, [2])
    # Save updated document
    content_editor.save(outfile)
```