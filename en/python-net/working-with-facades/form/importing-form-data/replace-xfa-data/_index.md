---
title: Replace XFA Data
type: docs
weight: 50
url: /python-net/replace-xfa-data/
description: This example demonstrates how to replace existing XFA form data in a PDF using Aspose.PDF for Python via .NET. It shows how to bind an XFA-based PDF document, load new data from an external XFA file, and update the form content programmatically.
lastmod: "2026-02-19"
---

XFA (XML Forms Architecture) forms store their data in XML format within the PDF structure. In this example, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade from the [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) module is used to bind a PDF and replace its existing XFA dataset using an external XML stream. After applying the new data, the updated PDF is saved as a separate file.

1. Initialize pdf_facades.Form() to manage XFA form data.
1. Call 'bind_pdf()' to attach the PDF containing XFA forms.
1. Use 'FileIO()' to read the XFA XML file.
1. Call 'set_xfa_data()' to update the PDF with new XFA content.
1. Save the updated Document.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    # Replace from XFA data
    def replace_xfa_data(infile, datafile, outfile):
        """Import form data from XFA file into PDF form fields."""
        # Create Form object
        form = pdf_facades.Form()

        # Bind PDF document
        form.bind_pdf(infile)

        # Open XFA file as stream
        with FileIO(datafile, 'r') as xfa_stream:
            # Import data from XFA into PDF form fields
            form.set_xfa_data(xfa_stream)

        # Save updated PDF
        form.save(outfile)
```