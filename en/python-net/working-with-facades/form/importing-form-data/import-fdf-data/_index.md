---
title: Import FDF Data
type: docs
weight: 10
url: /python-net/import-fdf-data/
description: This example demonstrates how to import form data from an FDF file into a PDF form using Aspose.PDF for Python via .NET. It shows how to bind a PDF document, read form field values from an FDF stream, and automatically populate the corresponding fields.
lastmod: "2026-02-19"
---

FDF (Forms Data Format) is a lightweight format used to store and transfer PDF form field values without including the entire document. In this example, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade from [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) is used to load a PDF form and import field data from an external FDF file. After the import process, the updated PDF is saved as a new file.

1. Initialize pdf_facades.Form() to work with interactive PDF form fields.
1. Call 'bind_pdf()' to attach the PDF form template.
1. Use 'open()' to read the FDF file in binary mode.
1. Call 'import_fdf()' to populate PDF fields with data from the FDF file.
1. Save the updated PDF.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    # Import Data from FDF
    def import_fdf_to_pdf_form(infile, datafile, outfile):
        """Import form data from FDF file into PDF form fields."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Open FDF file as stream
        with open(datafile, 'rb') as fdf_input_stream:
            pdf_form.import_fdf(fdf_input_stream)

        # Save updated PDF
        pdf_form.save(outfile)
```