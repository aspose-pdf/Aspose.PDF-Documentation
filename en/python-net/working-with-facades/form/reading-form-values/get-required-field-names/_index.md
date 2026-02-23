---
title: Get Required Field Names
type: docs
weight: 30
url: /python-net/get-required-field-names/
description: This example demonstrates how to identify and retrieve the names of required form fields in a PDF document using Aspose.PDF Facades API.
lastmod: "2026-02-19"
---

PDF forms may contain mandatory fields that users must complete before submission. These fields are typically marked as required in the form's properties.

1. Create a Form Object.
1. Bind the PDF Document.
1. Access all field names using 'pdf_form.field_names'.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    # Get required field names
    def get_required_field_names(infile):
        """Get required field names from a PDF document."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Get required field names
        for field in pdf_form.field_names:
            if pdf_form.is_required_field(field):
                print(f"Required field: {field}")
```