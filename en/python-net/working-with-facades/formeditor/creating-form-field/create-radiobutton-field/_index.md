---
title: Create RadioButton Field
type: docs
weight: 40
url: /python-net/create-radiobutton-field/
description: Learn how to programmatically add a radio button form field to a PDF document using Aspose.PDF for Python. This example demonstrates how to create a radio button group, define selectable options, and save the updated PDF file.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Create a Radio Button Field in a PDF Using Aspose.PDF for Python
Abstract: Radio buttons are commonly used in PDF forms to allow users to select one option from a predefined group of choices. In this tutorial, you will learn how to create a radio button field in a PDF using the FormEditor class in Aspose.PDF for Python. The example shows how to define radio button items, set a default selection, and save the updated document.
---

Interactive PDF forms enable users to provide structured input directly within a document. A radio button field is useful when users must choose only one option from multiple choices, such as selecting a country, gender, or preference.

The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class provides methods to create different types of fields, including text boxes, checkboxes, combo boxes, list boxes, and radio buttons.

1. Load an existing PDF document.
1. Define a list of radio button options.
1. Add a radio button field to a specific page.
1. Set a default selected value.
1. Save the modified PDF document.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_radiobutton_field(infile, outfile):
    """Create RadioButton field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add RadioButton field to PDF form
    pdf_form_editor.items = ["Australia", "New Zealand", "Malaysia"]
    pdf_form_editor.add_field(
        pdf_facades.FieldType.RADIO, "radiobutton1", "Malaysia", 1, 240, 498, 256, 514
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
