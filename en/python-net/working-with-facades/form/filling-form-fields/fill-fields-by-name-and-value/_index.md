---
title: Fill Fields by Name and Value
type: docs
weight: 60
url: /python-net/fill-fields-by-name-and-value/
description: This article demonstrates how to dynamically fill multiple PDF form fields by name and value using Aspose.PDF for Python via .NET. Instead of setting each field individually, it uses a dictionary structure to map field names to values and populates them in a loop.
lastmod: "2026-02-19"
---

Filling form fields using a name–value collection allows developers to create scalable and flexible solutions for PDF form automation. In this example, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade from [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) is used to bind a PDF document and iterate through a dictionary of field data. Each entry is applied using the 'fill_field method', enabling efficient bulk updates to form fields.

1. Initialize 'pdf_facades.Form()' to work with interactive form fields.
1. Use 'bind_pdf()' to attach the source PDF document.
1. Create a dictionary containing field names and the values you want to insert.
1. Iterate through the dictionary and call 'fill_field()' for each entry.
1. Save the updated Document.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    # Fill Fields by Name and Value
    def fill_fields_by_name_and_value(infile, outfile):
        """Fill PDF form fields by name and value."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Fill fields by name and value
        fields = {
            "name": "Jane Smith",
            "address": "456 Elm St, Othertown, USA",
            "email": "jane.smith@example.com"
        }
        for field_name, value in fields.items():
            pdf_form.fill_field(field_name, value)

        # Save updated PDF
        pdf_form.save()  
```