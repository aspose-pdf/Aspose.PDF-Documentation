---
title: Remove Field
type: docs
weight: 60
url: /python-net/remove-field/
description: This example shows how to delete the 'Country' field from a PDF form using the 'remove_field' method of the 'FormEditor' class.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Remove a Form Field from a PDF Document Using Python
Abstract: This example demonstrates how to remove an existing form field from a PDF document using Aspose.PDF for Python. The code loads a PDF file, deletes the specified field using the FormEditor class, and saves the updated document.    
---

PDF forms may contain fields that are no longer needed due to design changes or workflow updates. With Aspose.PDF for Python, developers can easily remove specific form fields programmatically.

The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class in Aspose.PDF provides the 'remove_field' method, which allows developers to delete a form field by its name.

1. Load the PDF document.
1. Create a FormEditor object.
1. Bind the PDF to the FormEditor.
1. Remove the specified form field.
1. Save the updated document.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Remove field from document
    form_editor.remove_field("Country")
    # Save updated document
    form_editor.save(outfile)
```
