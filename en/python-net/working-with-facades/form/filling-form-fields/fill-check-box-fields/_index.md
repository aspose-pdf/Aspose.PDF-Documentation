---
title: Fill Check Box Fields
type: docs
weight: 20
url: /python-net/fill-check-box-fields/
description: This example demonstrates how to programmatically fill check box fields in a PDF form using Aspose.PDF for Python via .NET. It shows how to bind a PDF document, update check box values by field name, and save the modified file.
lastmod: "2026-02-19"
---

The check box is commonly used in PDF forms to represent binary choices such as subscriptions or agreement confirmations. In this example, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade from [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) is used to access form fields and set their values to a selected state. After updating the check boxes, the filled PDF is saved as a new document.

1. Initialize 'pdf_facades.Form()' to manage form field interactions.
1. Use 'bind_pdf()' to attach the source PDF containing check box fields.
1. Call 'fill_field()' to mark fields like 'subscribe_newsletter' and 'accept_terms' as selected.
1. Save the updated Document.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    # Fill Check Box Fields
    def fill_check_box_fields(infile, outfile):
        """Fill check box fields in PDF form."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Fill check box fields by name
        pdf_form.fill_field("subscribe_newsletter", "Yes")
        pdf_form.fill_field("accept_terms", "Yes")

        # Save updated PDF
        pdf_form.save(outfile)
```