---
title: Export to JSON
type: docs
weight: 30
url: /python-net/export-to-json/
description: This example demonstrates how to export PDF form field values to a JSON file using Aspose.PDF for Python via .NET. It explains how to load a PDF form, access its fields through the Form facade, and save the extracted data in a structured JSON format
lastmod: "2026-02-19"
---

JSON is a widely used data format that enables seamless exchange between applications and services. In this example, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) object from the [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) module is used to bind a PDF file and export its form field values into a readable JSON structure.

1. Initialize pdf_facades.Form() to work with form fields.
1. Use 'bind_pdf()' to attach the source PDF document.
1. Create a writable stream using 'FileIO()'.
1. Call 'export_json()' to extract form field values and save them in formatted JSON.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    # Export Data to JSON
    def export_form_to_json(infile, outfile):
        """Export PDF form field values to JSON file."""
        # Create Form object
        form = pdf_facades.Form()

        # Bind PDF document
        form.bind_pdf(infile)

        # Create JSON file stream
        with FileIO(outfile, 'w') as json_stream:
            # Export form field values to JSON
            form.export_json(json_stream, indented=True)
```