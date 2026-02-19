---
title: Fill Text Fields
type: docs
weight: 10
url: /python-net/fill-text-fields/
description: This example demonstrates how to automatically fill text fields in a PDF form using Aspose.PDF for Python via .NET. It shows how to load a PDF document, populate specific form fields by name, and save the updated file.
lastmod: "2026-02-19"
---

Programmatically filling text fields allows applications to reuse PDF templates and insert dynamic content without manual editing. In this example, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade from [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) is used to bind a PDF form and update multiple fields such as name, address, and email. After assigning values, the modified PDF is saved as a new document.

1. Initialize 'pdf_facades.Form()' to manage form field operations.
1. Use 'bind_pdf()' to attach the input PDF containing text fields.
1. Call 'fill_field()' to insert data into fields like name, address, and email.
1. Save the updated PDF.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    # Fill Text Fields
    def fill_text_fields(infile, outfile):
        """Fill text fields in PDF form."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Fill text fields by name
        pdf_form.fill_field("name", "John Doe")
        pdf_form.fill_field("address", "123 Main St, Anytown, USA")
        pdf_form.fill_field("email", "john.doe@example.com")

        # Save updated PDF
        pdf_form.save(outfile)
```