---
title: Add Bookmark Action
type: docs
weight: 10
url: /python-net/add-bookmark-action/
description: This example binds an input PDF, creates a bookmark labeled "PdfContentEditor Bookmark" that navigates to page 1, and saves the updated document. 
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create a Bookmark with Navigation Action in a PDF Using Python
Abstract: This example demonstrates how to add a bookmark with a navigation action to a PDF document using Aspose.PDF for Python via the Facades API. It shows how to configure bookmark text, appearance, and an action that directs users to a specific page.  
---

Bookmarks provide quick navigation within PDF documents. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), you can programmatically create bookmarks and assign actions such as navigating to a page. You can also customize the bookmark appearance, including color and style options like bold or italic.

1. Create the PdfContentEditor object.
1. Bind the input PDF.
1. Define Bookmark properties.
1. Assign Bookmark action.
1. Save the updated Document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_bookmark_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a bookmark action to navigate to page 1
    content_editor.create_bookmarks_action(
        "PdfContentEditor Bookmark",
        apd.Color.blue,
        True,
        False,
        "",
        "GoTo",
        "1",
    )
    # Save updated document
    content_editor.save(outfile)
```