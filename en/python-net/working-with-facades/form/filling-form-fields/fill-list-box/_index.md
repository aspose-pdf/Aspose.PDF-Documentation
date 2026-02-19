---
title: Fill List Box
type: docs
weight: 40
url: /python-net/fill-list-box/
description: This example demonstrates how to programmatically fill list box and multi-select fields in a PDF form using Aspose.PDF for Python via .NET. It shows how to bind a PDF document, select values within a list-based form field, and save the updated file.
lastmod: "2026-02-19"
---

List box and multi-select fields allow users to choose one or multiple values from a predefined set of options. In this example, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade from [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) is used to access the PDF form and assign a selected value to the favorite_colors field. Once the desired option is selected, the updated document is saved.

1. Initialize 'pdf_facades.Form()' to manage and update form fields.
1. Call 'bind_pdf()' to attach the source PDF containing list box or multi-select fields.
1. Use 'fill_field()' to select a value from the available options.
1. Save the updated Document.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    # Fill List Box / Multi-Select Fields
    def fill_list_box_fields(infile, outfile):
        """Fill list box and multi-select fields in PDF form."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Fill list box / multi-select fields by name
        pdf_form.fill_field("favorite_colors", "Red")
        
        # Save updated PDF
        pdf_form.save(outfile)
```