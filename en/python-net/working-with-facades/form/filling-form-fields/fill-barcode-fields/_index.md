---
title: Fill Barcode Fields
type: docs
weight: 50
url: /python-net/fill-barcode-fields/
description: This example demonstrates how to programmatically fill barcode fields in a PDF form using Aspose.PDF for Python via .NET. It shows how to bind a PDF document, assign a value to a barcode field, and save the updated file.
lastmod: "2026-02-19"
---

Barcode fields in PDF forms allow encoded information to be stored and displayed visually as barcodes. In this example, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade from the [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) module is used to access form fields and assign a barcode value. Once the data is filled, the PDF is saved with the updated barcode content.

1. Initialize 'pdf_facades.Form()' to manage PDF form interactions.
1. Call 'bind_pdf()' to attach the PDF containing barcode fields.
1. Use 'fill_field()' to assign a barcode value.
1. Save the updated Document.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    # Fill Barcode Fields
    def fill_barcode_fields(infile, outfile):
        """Fill barcode fields in PDF form."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Fill barcode fields by name
        pdf_form.fill_field("product_barcode", "123456789012")

        # Save updated PDF
        pdf_form.save(outfile)
```

