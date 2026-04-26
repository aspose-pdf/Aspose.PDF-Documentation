---
title: Create TextBox Field
type: docs
weight: 60
url: /python-net/create-textbox-field/
description: Learn how to programmatically add TextBox fields to a PDF document using Aspose.PDF for Python. This tutorial shows how to insert multiple text fields, set default values, and save the updated PDF document.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Create TextBox Fields in a PDF Using Aspose.PDF for Python
Abstract: TextBox fields in PDF forms allow users to enter and edit text, making documents interactive and user-friendly. In this tutorial, you will learn how to create TextBox form fields in a PDF using the FormEditor class in Aspose.PDF for Python. The example demonstrates adding multiple fields, specifying default values, and saving the modified PDF.
---

PDF forms often require text input from users, such as names, addresses, or comments. TextBox fields enable this functionality by providing editable fields directly within the PDF document.

The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class allows adding text fields, checkboxes, radio buttons, list boxes, combo boxes, and buttons, making it easy to build interactive PDFs.

1. Load an existing PDF document.
1. Add multiple TextBox fields for user input.
1. Set default values for each field.
1. Save the updated PDF document.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_textbox_field(infile, outfile):
    """Create TextBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add TextBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.TEXT, "first_name", "Alexander", 1, 50, 570, 150, 590
    )
    pdf_form_editor.add_field(
        pdf_facades.FieldType.TEXT, "last_name", "Smith", 1, 235, 570, 330, 590
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
