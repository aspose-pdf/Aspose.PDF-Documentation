---
title: Set Field Limit
type: docs
weight: 80
url: /python-net/set-field-limit/
description: This example shows how to set a maximum character limit for a form field in a PDF document using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Set Maximum Character Limit for PDF Form Fields Using Python
Abstract: This example demonstrates setting the character limit for a field named "Last Name" to 10 characters, ensuring that users cannot enter more than the specified limit.        
---

Form fields in PDF documents may require input restrictions to maintain proper formatting. Using Aspose.PDF for Python, developers can programmatically set a maximum number of characters for a field.

The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class provides the 'set_field_limit' method to define the maximum input length for a field.

1. Open an existing PDF form.
1. Create a FormEditor object.
1. Set the maximum character limit for the field "Last Name".
1. Save the updated PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_limit(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field limit to 10
    if not form_editor.set_field_limit("Last Name", 10):
        raise Exception(
            "Failed to set field limit. Field may not support specified limit."
        )

    # Save updated document
    form_editor.save(outfile)
```
