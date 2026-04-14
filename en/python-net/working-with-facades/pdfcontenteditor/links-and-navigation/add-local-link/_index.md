---
title: Add Local Link
type: docs
weight: 40
url: /python-net/add-local-link/
description: This example binds an input PDF, adds a red-colored local link on page 1 that points to page 1, and saves the modified document.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add a Local Link to a PDF Using PdfContentEditor in Python
Abstract: This example demonstrates how to add a local link to a PDF document using Aspose.PDF for Python via the Facades API. It shows how to create a clickable area that navigates to another page within the same PDF and save the updated document.     
---

Local links in PDFs allow quick navigation between pages within the same document. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), you can define a clickable rectangle that links one page to another, improving document usability and navigation.

1. Create a PdfContentEditor instance.
1. Bind the input PDF document.
1. Define a rectangle for the clickable local link.
1. Specifie the source page and destination page.
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


def add_local_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a local link on page 1 to destination page 1
    content_editor.create_local_link(
        apd.Rectangle(120, 620, 220, 20),
        1,
        1,
        apd.Color.red,
    )
    # Save updated document
    content_editor.save(outfile)
```
