---
title: Add Custom Action Link
type: docs
weight: 20
url: /python-net/add-custom-action-link/
description: This example binds an input PDF, adds a custom action link on the first page, and saves the modified document. An empty action list is used for simplicity, but real implementations can include actual actions.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add a Custom Action Link to a PDF Using PdfContentEditor in Python
Abstract: This example demonstrates how to add a custom action link to a PDF document using Aspose.PDF for Python via the Facades API. It shows how to create a clickable area on a page, assign a custom action, and save the updated document.     
---

Custom action links allow you to define interactive areas in a PDF that can trigger specific actions when clicked, such as executing scripts, navigating pages, or running application-specific commands. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), you can create a custom action link by specifying the page, rectangle, color, and actions.

1. Create a PdfContentEditor instance.
1. Bind the input PDF document.
1. Define a rectangle for the clickable link.
1. Specifie the page number and link color.
1. Assign custom actions (empty in this example).
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


def add_custom_action_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add custom action link. Empty action list keeps the sample runnable
    # without requiring additional enum lookups.
    content_editor.create_custom_action_link(
        apd.Rectangle(200, 500, 260, 20),
        1,
        apd.Color.dark_red,
        [],
    )
    # Save updated document
    content_editor.save(outfile)
```
