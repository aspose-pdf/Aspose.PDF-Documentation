---
title: Create Rubber Stamp With Appearance File
type: docs
weight: 20
url: /python-net/create-rubber-stamp-with-appearance-file/
description: The example binds an input PDF, creates a rubber stamp on page 1 using an image file as the stamp appearance, and saves the updated PDF.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create a Rubber Stamp with Custom Appearance in a PDF Using PdfContentEditor
Abstract: This example demonstrates how to add a rubber stamp annotation with a custom appearance (image) to a PDF document using Aspose.PDF for Python via the Facades API. Custom stamps allow you to include logos, signatures, or branded visuals as part of the stamp.    
---

Rubber stamp annotations can be customized not only with text but also by using an image file as their appearance. This approach is useful for adding company logos, signature stamps, or any visual indicator to your PDF pages.

1. Create a [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instance.
1. Bind the input PDF document.
1. Define a rectangle for the stamp.
1. Use a custom image file to define the appearance of the rubber stamp.
1. Set the text and color of the stamp.
1. Save the updated PDF document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_rubber_stamp_with_appearance_file(infile, image_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Create rubber stamp using appearance_file overload (image path)
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(100, 400, 200, 60),
        "Stamp with custom appearance",
        apd.Color.dark_green,
        image_file,
    )
    # Save updated document
    content_editor.save(outfile)
```
