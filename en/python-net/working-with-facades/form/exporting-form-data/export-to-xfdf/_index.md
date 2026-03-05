---
title: Export to XFDF
type: docs
weight: 20
url: /python-net/export-to-xfdf/
description: This example shows how to export PDF form field data to an XFDF (XML Forms Data Format) file using Aspose.PDF for Python via .NET. It demonstrates how to load a PDF form, access its fields through the Form facade, and save the extracted values into an XFDF stream.
lastmod: "2026-02-19"
---

XFDF is an XML representation of PDF form data that allows developers to transfer form field values independently from the original document. In this example, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) object from [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) is used to bind the source PDF and export its data into a structured XFDF file.

1. Initialize pdf_facades.Form() to manage PDF form data.
1. Call 'bind_pdf()' to attach the source PDF document.
1. Use 'open()' to create a writable binary stream.
1. Export Form Data. Call 'export_xfdf()' to extract and save form field values in XFDF format.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    # Export Data to XFDF
    def export_pdf_form_to_xfdf(infile, outfile):
        """Export PDF form data to XFDF file."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Create XFDF file stream
        with open(outfile, "wb") as xfdf_output_stream:
            # Export form data to XFDF file
            pdf_form.export_xfdf(xfdf_output_stream)
```