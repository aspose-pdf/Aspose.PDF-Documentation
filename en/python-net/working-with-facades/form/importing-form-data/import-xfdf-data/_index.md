---
title: Import XFDF Data
type: docs
weight: 20
url: /python-net/import-xfdf-data/
description: This example demonstrates how to import form data from an XFDF file into a PDF form using Aspose.PDF for Python via .NET. It shows how to bind a PDF document, read XML-based XFDF data through a file stream, and automatically populate matching form fields. Importing XFDF data enables efficient form data exchange and supports automated document workflows that rely on structured XML formats.
lastmod: "2026-02-19"
---

XFDF (XML Forms Data Format) is an XML representation of PDF form data designed for interoperability and data exchange. In this example, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade from the [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) module is used to bind a PDF form and import field values from an external XFDF file. After importing the data, the updated PDF is saved as a new document.

1. Initialize pdf_facades.Form() to interact with PDF form fields.
1. Call 'bind_pdf()' to attach the PDF form template.
1. Use 'open()' to read the XFDF file.
1. Call 'import_xfdf()' to populate PDF fields with values from the XFDF file.
1. Save the updated Document.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    # Import Data from XFDF
    def import_data_from_xfdf(infile, datafile, outfile):
        """Import form data from XFDF file into PDF form fields."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Open XFDF file as stream
        with open(datafile, 'rb') as xfdf_input_stream:
            # Import data from XFDF into PDF form fields
            pdf_form.import_xfdf(xfdf_input_stream)

        # Save updated PDF
        pdf_form.save(outfile)
```