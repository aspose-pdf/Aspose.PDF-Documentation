---
title: Create CheckBox Field
type: docs
weight: 10
url: /python-net/create-checkbox-field/
description: Learn how to programmatically add a checkbox form field to a PDF document using Aspose.PDF for Python. This guide demonstrates how to use the FormEditor class to insert an interactive checkbox into an existing PDF file and save the updated document.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Create a Checkbox Field in a PDF Using Aspose.PDF for Python
Abstract: Interactive form fields allow users to fill out and interact with PDF documents digitally. In this tutorial, you will learn how to add a checkbox field to a PDF using the Aspose.PDF Python API. The example shows how to bind an existing PDF document, create a checkbox form field at specified coordinates, and save the modified file.
---

PDF forms are widely used for collecting user input in documents such as applications, surveys, and agreements. A checkbox field enables users to select or deselect an option within a form.

Using Aspose.PDF for Python, developers can manipulate PDF forms programmatically. The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class provides methods to add, edit, and manage form fields within a PDF document.

1. Load an existing PDF file.
1. Call the 'add_field()' method with the 'FieldType.CHECK_BOX' parameter to create the checkbox and specify its position.
1. Define the field name, caption, and position.
1. Save the updated PDF document.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_checkbox_field(infile, outfile):
    """Create CheckBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add CheckBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.CHECK_BOX,
        "checkbox1",
        "Check Box 1",
        1,
        240,
        498,
        256,
        514,
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
