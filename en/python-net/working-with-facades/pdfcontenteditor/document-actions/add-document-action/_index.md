---
title: Add Document Action
type: docs
weight: 20
url: /python-net/add-document-action/
description: This example adds a JavaScript alert that appears when the PDF is opened. The script is attached to the document open event and executed automatically in supported PDF viewers. 
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Document Open JavaScript Action to a PDF Using Python
Abstract: This example demonstrates how to add a document-level JavaScript action that triggers when a PDF is opened. Using Aspose.PDF for Python via the Facades API, the sample shows how to bind a document, assign an open event action, and save the updated PDF.     
---

Document-level actions allow you to define behaviors that execute automatically when certain events occur, such as opening a PDF. With [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), you can attach JavaScript code to these events. This can be used for notifications, validation logic, or interactive workflows.

1. Create the PdfContentEditor object.
1. Bind the input PDF.
1. Add Document-Level action.
1. Save the updated Document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def add_document_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add JavaScript action for document open event
    content_editor.add_document_additional_action(
        content_editor.DOCUMENT_OPEN,
        "app.alert('Document opened with PdfContentEditor action');",
    )
    # Save updated document
    content_editor.save(outfile)
```