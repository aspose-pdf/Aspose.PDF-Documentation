---
title: Remove Open Action
type: docs
weight: 30
url: /python-net/remove-open-action/
description: This example loads an existing PDF, removes the open action, and saves the cleaned document.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remove Document Open Action from a PDF Using Python
Abstract: This example demonstrates how to remove a document open action from a PDF using Aspose.PDF for Python via the Facades API. It shows how to bind a PDF, clear the open action, and save the updated document.    
---

PDF documents may contain actions that execute automatically when the file is opened, such as JavaScript alerts, navigation commands, or other behaviors. In some scenarios, you may need to remove these actions for security, compliance, or user experience reasons.

Using PdfContentEditor, you can easily remove the document open action and ensure the PDF opens without executing any automatic behavior.

1. Create the PdfContentEditor object.
1. Bind the input PDF.
1. Remove the Document Open Action.
1. Save the updated Document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_open_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Remove open action from the document
    content_editor.remove_document_open_action()
    # Save updated document
    content_editor.save(outfile)
```
