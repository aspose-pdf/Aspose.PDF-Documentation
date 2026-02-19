---
title: Extract XFA Data
type: docs
weight: 50
url: /python-net/extract-xfa-data/
description: This example explains how to extract XFA form data from a PDF file using Aspose.PDF for Python via .NET. It demonstrates how to bind an XFA-based PDF document to the Form facade and export its internal data structure into a file stream.
lastmod: "2026-02-19"
---

XFA (XML Forms Architecture) forms differ from traditional AcroForms because their data is stored as XML within the PDF. In this example, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) object from the [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) module is used to bind the PDF and extract its XFA data directly into a file.

1. Create an instance of pdf_facades.Form() to manage form data.
1. Call 'bind_pdf()' to attach the source PDF containing XFA forms.
1. Use 'FileIO()' to create a writable file stream.
1. Call 'extract_xfa_data()' to export the embedded XFA XML data.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    # Extract XFA Data
    def export_xfa_data(infile, outfile):
        """Export XFA form data."""
        # Create Form object
        form = pdf_facades.Form()

        # Bind PDF document
        form.bind_pdf(infile)
        
        with FileIO(outfile, 'w') as stream:
            # Export form field values to JSON
            form.extract_xfa_data(stream)
```