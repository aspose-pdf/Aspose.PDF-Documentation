---
title: Add Application Link
type: docs
weight: 10
url: /python-net/add-application-link/
description: This example binds an input PDF, adds an application launch link on the first page, and saves the modified document.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add an Application Launch Link to a PDF Using PdfContentEditor in Python
Abstract: This example demonstrates how to add an application launch link to a PDF document using Aspose.PDF for Python via the Facades API. It shows how to create a clickable area that opens a specified application when clicked, and save the updated PDF.  
---

PDF can include interactive elements such as links that launch external applications. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), you can define a rectangular region on a page that, when clicked, opens a specific executable file.

1. Create a PdfContentEditor instance.
1. Bind the input PDF document.
1. Define a rectangle area for the clickable link.
1. Specifie the application path to launch.
1. Set the link color.
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


def add_application_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add application launch link
    content_editor.create_application_link(
        apd.Rectangle(180, 530, 260, 20),
        "notepad.exe",
        1,
        apd.Color.purple,
    )
    # Save updated document
    content_editor.save(outfile)
```
