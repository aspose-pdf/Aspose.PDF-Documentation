---
title: Rename Form Fields
type: docs
weight: 30
url: /python-net/rename-form-fields/
description: This example demonstrates how to rename form fields in a PDF document using Aspose.PDF for Python via .NET. It shows how to bind a PDF form, update existing field names programmatically, and save the modified file. Renaming fields helps standardize form structures, improve data mapping, and simplify integration with automated workflows or external systems.
lastmod: "2026-02-19"
---

Renaming form fields is useful when aligning PDF forms with internal naming conventions or preparing documents for structured data processing. In this example, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade from the [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) module is used to bind the source PDF and apply a mapping that replaces old field names with new ones. After updating the field identifiers, the document is saved with the changes applied.

1. Initialize pdf_facades.Form() to interact with PDF form fields.
1. Call 'bind_pdf()' to attach the PDF document.
1. Create a list of tuples containing old field names and their corresponding new names.
1. Iterate through the mapping and call 'rename_field()' for each entry.
1. Save the updated Document.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    # Rename form fields
    def rename_form_fields(infile, outfile):
        """Rename form fields in a PDF document."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Rename form fields by providing a mapping of old names to new names
        field_renaming_map = [
            ("First Name", "NewFirstName"),
            ("Last Name", "NewLastName")
        ]
        for old_name, new_name in field_renaming_map:
            pdf_form.rename_field(old_name, new_name)

        # Save updated PDF
        pdf_form.save(outfile)
```