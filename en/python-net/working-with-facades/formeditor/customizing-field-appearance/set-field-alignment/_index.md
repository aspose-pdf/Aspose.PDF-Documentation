---
title: Set Field Alignment
type: docs
weight: 30
url: /python-net/set-field-alignment/
description: This example demonstrates how to set the text alignment of a form field in a PDF document using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Set Text Alignment for PDF Form Fields Using Python
Abstract: This article explains how to open a PDF document, set the alignment of a specific field using the FormEditor class, and save the updated PDF. The example sets the text alignment of a field named "First Name" to center.         
---

PDF form fields often require customized text alignment to maintain a consistent and professional layout. Using Aspose.PDF for Python, developers can programmatically set the alignment of a form field’s text content.

The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class, in combination with the [FormFieldFacade](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formfieldfacade/) constants, allows developers to modify the alignment of existing form fields programmatically.

1. Open an existing PDF document.
1. Create a FormEditor object.
1. Set the alignment of a field named "First Name" to center.
1. Save the modified document.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_alignment(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field alignment to center
    if form_editor.set_field_alignment(
        "First Name", pdf_facades.FormFieldFacade.ALIGN_CENTER
    ):
        # Save updated document
        form_editor.save(outfile)
    else:
        raise Exception(
            "Failed to set field alignment. Field may not support alignment."
        )
```
