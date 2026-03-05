---
title: Export to FDF
type: docs
weight: 10
url: /python-net/export-to-fdf/
description: This example explains how to export PDF form field data to an FDF (Forms Data Format) file using Aspose.PDF for Python via .NET. It demonstrates how to access interactive form data through the Form facade, bind a source PDF document, and save the extracted values into an FDF stream.
lastmod: "2026-02-19"
---

FDF is a lightweight format designed specifically for storing and transferring PDF form data without embedding the entire document. In this example, a [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) object is initialized from the [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) module, allowing developers to interact with AcroForm fields and export their values.

1. Create an instance of pdf_facades.Form() to work with PDF form fields.
1. Call 'bind_pdf()' to attach the PDF document containing the form.
1. Use 'open(')' to create a writable binary stream for the FDF file.
1. Export Form Data. Call 'export_fdf()' to extract and save all form field values.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    # Export Data to FDF
    def export_form_data_to_fdf(infile, outfile):
        """Export PDF form data to FDF file."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Create FDF file stream
        with open(outfile, 'wb') as fdf_output_stream:
            # Export form data to FDF file
            pdf_form.export_fdf(fdf_output_stream)
```