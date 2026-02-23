---
title: Get Field Values
type: docs
weight: 50
url: /python-net/get-field-values/
description: Retrieving Field Values from a PDF Form with Aspose.PDF Facades using Form Class.
lastmod: "2026-02-19"
---

This code snippet shows how to retrieve the current values of form fields from a PDF document using Aspose.PDF Facades API. The [get_field()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/#methods) method allows you to programmatically access data entered into text fields, checkboxes, radio buttons, and other AcroForm elements.

1. Bind the PDF to a Form object.
1. Specify the field names you want to read.
1. Retrieve each field's value using get_field().

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir


    # Get field values
    def get_field_values(infile):
        """Get field values from a PDF document."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Get field values by their names
        field_names = ["First Name", "Last Name"]
        for field_name in field_names:
            value = pdf_form.get_field(field_name)
            print(f"Value of '{field_name}': {value}")
```