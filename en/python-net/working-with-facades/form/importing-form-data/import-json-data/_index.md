---
title: Import JSON Data
type: docs
weight: 30
url: /python-net/import-json-data/
description: This example demonstrates how to import form field data from a JSON file into a PDF form using Aspose.PDF for Python via .NET. It shows how to bind a PDF document, read structured JSON data through a file stream, and automatically populate matching form fields.
lastmod: "2026-02-19"
---

JSON is widely used for storing and transferring structured data between systems. In this example, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade from the [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) module is used to bind a PDF form and import field values from an external JSON file. After the import process, the updated document is saved as a new PDF.

1. Initialize pdf_facades.Form() to interact with PDF form fields.
1. Call 'bind_pdf()' to attach the PDF form template.
1. Use 'FileIO()' to read the JSON file containing form values.
1. Call 'import_json()' to populate PDF fields using JSON key–value pairs.
1. Save the updated PDF.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    # Import from JSON
    def import_json_to_pdf_form(infile, datafile, outfile):
        """Import form data from JSON file into PDF form fields."""
        # Create Form object
        form = pdf_facades.Form()

        # Bind PDF document
        form.bind_pdf(infile)

        # Open JSON file as stream
        with FileIO(datafile, 'r') as json_stream:
            # Import data from JSON into PDF form fields
            form.import_json(json_stream)

        # Save updated PDF
        form.save(outfile)
```