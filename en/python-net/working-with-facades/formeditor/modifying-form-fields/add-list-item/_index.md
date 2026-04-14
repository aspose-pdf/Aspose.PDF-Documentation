---
title: Add List Item
type: docs
weight: 10
url: /python-net/add-list-item/
description: This example demonstrates how to add items to a list box form field in a PDF document using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Add Items to PDF List Box Fields Using Python
Abstract: This article shows how to open a PDF document, append items to a list box field named "Country", and save the updated document.    
---

List box fields in PDFs allow users to select one or multiple options from a predefined set. Using Aspose.PDF for Python, developers can programmatically add new items to these fields. The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class provides the 'add_list_item' method to append items to an existing list box field.

1. Open an existing PDF form.
1. Create a FormEditor object.
1. Bind the PDF to the FormEditor.
1. Add items to the list box field "Country".
1. Save the updated document.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_list_item(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Add list item to list box field
    form_editor.add_list_item("Country", ["New Zealand", "New Zealand"])
    # Save updated document
    form_editor.save(outfile)
```
