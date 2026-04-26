---
title: Get Field Facades
type: docs
weight: 10
url: /python-net/get-field-facades/
description: This example demonstrates how to read the values of specific form fields from a PDF document using Aspose.PDF Facades API.
lastmod: "2026-02-19"
---

PDF forms contain fields where users can enter data, such as text boxes, checkboxes, or radio buttons. To process these forms programmatically, it is often necessary to retrieve the current values of these fields.

1. Create a Form object.
1. Bind the PDF document to the form object.
1. Retrieve Field Values.

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