---
title: Identifying form fields names
type: docs
weight: 10
url: /python-net/identifying-form-fields-names/
description: Aspose.Pdf.Facades allows you identifying form fields names using Form Class.
lastmod: "2025-11-05"
---

[Aspose.PDF for Python via .NET](/pdf/python-net/) provides the capability to create, edit and fill already created Pdf forms. [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades) namespace contains [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) class, which contains the function named [fill_field](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/#methods) and it takes two arguments i.e. Field name and field value. So in-order to fill the form fields, you must be aware of the exact form field name.

In [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades) namespace we have a class named [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) which provides the capability to manipulate PDF forms. Open a pdf form; add a text field beneath every existing form field and save the Pdf form with new name.

Identify form field names and their locations in a PDF document using Aspose.PDF for Python via .NET, and then add new text fields relative to those existing fields.

1. Load the PDF Form.
1. Use FieldNames to get all Form fields.
1. Call GetFieldFacade() to access each field's appearance and bounding box.
1. Save intermediate PDF.
1. Load a second Form for editing.
1. Create a FormEditor object to add new fields.
1. Add text fields.
1. Save final PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as ap
import Aspose.Pdf.Facades as pdf_facades
from System.Drawing import Rectangle

def identify_form_fields_names():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Load the input PDF form
    form = pdf_facades.Form(os.path.join(data_dir, "FilledForm.pdf"))

    # Get all field names
    all_fields = form.FieldNames

    # Create an array to hold field location rectangles
    boxes = [None] * len(all_fields)

    for i, field_name in enumerate(all_fields):
        # Get appearance attributes of each field
        facade = form.GetFieldFacade(field_name)
        # Store the field's location rectangle
        boxes[i] = facade.Box

    # Save PDF document after reading field info
    form.Save(os.path.join(data_dir, "IdentifyFormFields_1_out.pdf"))

    # Open another PDF document
    document = ap.Document(os.path.join(data_dir, "FilledForm - 2.pdf"))

    # Create FormEditor to add new fields
    editor = pdf_facades.FormEditor(document)

    for i, field_name in enumerate(all_fields):
        # Add a text field beneath each existing form field
        editor.AddField(
            pdf_facades.FieldType.Text,
            f"TextField{i}",
            field_name,
            1,
            boxes[i].Left,
            boxes[i].Top,
            boxes[i].Left + 50,
            boxes[i].Top + 10
        )

    # Save updated PDF
    editor.Save(os.path.join(data_dir, "IdentifyFormFields_out.pdf"))

    print("Form fields identified and new text fields added successfully.")
```
