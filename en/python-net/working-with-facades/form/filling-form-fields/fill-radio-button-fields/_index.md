---
title: Fill Radio Button Fields
type: docs
weight: 30
url: /python-net/fill-radio-button-fields/
description: This example demonstrates how to programmatically fill radio button fields in a PDF form using Aspose.PDF for Python via .NET. It shows how to bind a PDF document, select a radio button option by index, and save the updated file.
lastmod: "2026-02-19"
---

Radio buttons allow users to select a single option from a predefined group, such as gender or preference fields. In this example, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade from the [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) module is used to bind the source PDF and assign a selected option by its index value. Once the desired option is chosen, the modified document is saved.

1. Initialize pdf_facades.Form() to manage PDF form fields.
1. Call 'bind_pdf()' to attach the PDF containing radio button fields.
1. Use 'fill_field()' to select the first option (index 0).
1. Save the updated PDF.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    # Fill Radio Button Fields
    def fill_radio_button_fields(infile, outfile):
        """Fill radio button fields in PDF form."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Fill radio button fields by name
        pdf_form.fill_field("gender", 0) # Select male option (index 0)
        #pdf_form.fill_field("gender", 1) # Select female option (index 1)

        # Save updated PDF
        pdf_form.save(outfile)
```