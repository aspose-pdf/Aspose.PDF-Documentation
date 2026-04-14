---
title: Add Web Link
type: docs
weight: 60
url: /python-net/add-web-link/
description: This example binds an input PDF, adds a blue web link annotation on page 1 pointing to Aspose’s Python PDF product page, and saves the modified document.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add a Web Link to a PDF Using PdfContentEditor in Python
Abstract: This example demonstrates how to add a web link to a PDF document using Aspose.PDF for Python via the Facades API. It shows how to create a clickable area on a page that opens a specified URL in a web browser and save the updated document.    
---

Web links in PDFs allow users to navigate directly to online resources, websites, or documentation. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), you can define a rectangular area on a PDF page that, when clicked, opens a URL in the default web browser.

1. Create a PdfContentEditor instance.
1. Bind the input PDF document.
1. Define a rectangle for the clickable web link.
1. Specifie the URL, page number, and link color.
1. Save the updated PDF document.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_web_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a web link annotation to page 1
    content_editor.create_web_link(
        apd.Rectangle(100, 650, 200, 20),
        "https://products.aspose.com/pdf/python-net/",
        1,
        apd.Color.blue,
    )
    # Save updated document
    content_editor.save(outfile)
```
