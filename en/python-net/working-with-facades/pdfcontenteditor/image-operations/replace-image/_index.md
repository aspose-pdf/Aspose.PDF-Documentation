---
title: Replace Images in PDF
type: docs
weight: 30
url: /python-net/replace-image/
description: This example binds an input PDF, replaces the first image on page 1 with a new image, and saves the modified document.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Replace an Image in a PDF Using PdfContentEditor in Python
Abstract: This example demonstrates how to replace an existing image in a PDF document using Aspose.PDF for Python via the Facades API. It shows how to target a specific image on a page and replace it with a new image, then save the updated PDF.   
---

PDFs often contain images that may need to be updated or replaced, such as logos, diagrams, or photos. With [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), you can replace a specific image on a given page by providing the page number, image index, and new image file path.

1. Create a PdfContentEditor instance.
1. Bind the input PDF document.
1. Replace a specific image on a given page.
1. Save the updated PDF document.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_image(infile, image_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace image on page 1
    content_editor.replace_image(1, 1, image_file)
    # Save updated document
    content_editor.save(outfile)
```
