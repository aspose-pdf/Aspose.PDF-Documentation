---
title: Get Radio Button Options
type: docs
weight: 20
url: /python-net/get-radio-button-options/
description: This article demonstrates how to retrieve the currently selected value of a radio button field in a PDF document using Aspose.PDF Facades API.
lastmod: "2026-02-19"
---

Radio button fields in PDF forms are grouped controls where only one option can be selected at a time. Each group has a field name, and each option has a corresponding value.

1. Create a Form Object.
1. Bind the PDF Document.
1. Retrieve the Selected Radio Button Option.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    # Get radio button options
    def get_radio_button_options(infile):
        """Get radio button options from a PDF document."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Get radio button options by their names
        field_names = ["WorkType"]
        for field_name in field_names:
            options = pdf_form.get_button_option_current_value(field_name)
            print(f"Options for '{field_name}': {options}")
```