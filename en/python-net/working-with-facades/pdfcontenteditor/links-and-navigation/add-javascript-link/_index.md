---
title: Add JavaScript Link
type: docs
weight: 30
url: /python-net/add-javascript-link/
description: This example binds an input PDF, adds a JavaScript link that triggers an alert on click, and saves the modified document.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add a JavaScript Link to a PDF Using PdfContentEditor in Python
Abstract: This example demonstrates how to add a JavaScript link to a PDF document using Aspose.PDF for Python via the Facades API. It shows how to create a clickable area that executes JavaScript code when clicked, and save the updated PDF.     
---

JavaScript links in PDFs allow interactive functionality such as displaying alerts, performing calculations, or dynamically modifying document content. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), you can define a clickable rectangle on a page and associate it with custom JavaScript code.

1. Create a PdfContentEditor instance.
1. Bind the input PDF document.
1. Define a rectangle for the clickable JavaScript link.
1. Specifie the page number and link color.
1. Assign JavaScript code to execute when clicked.
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


def add_javascript_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add JavaScript link action
    content_editor.create_java_script_link(
        "app.alert('PdfContentEditor JavaScript link');",
        apd.Rectangle(160, 560, 260, 20),
        1,
        apd.Color.orange,
    )
    # Save updated document
    content_editor.save(outfile)
```
