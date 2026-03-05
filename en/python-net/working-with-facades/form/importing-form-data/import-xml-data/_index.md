---
title: Import XML Data
type: docs
weight: 40
url: /python-net/import-xml-data/
description: This example demonstrates how to import form data from an XML file into PDF form fields using Aspose.PDF for Python via .NET. It shows how to bind a PDF document, read structured XML data through a file stream, and populate corresponding form fields automatically.
lastmod: "2026-02-19"
---

XML is commonly used to store structured form data, making it a practical format for transferring values between systems. In this example, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade from [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) is used to load a PDF form and apply field values directly from an XML file. After importing the data, the updated PDF is saved as a new document.

1. Initialize pdf_facades.Form() to interact with PDF form fields.
1. Call 'bind_pdf()' to attach the PDF form template.
1. Use 'FileIO()' to access the XML file containing form data.
1. Call 'import_xml()' to populate PDF fields with values from the XML file.
1. Save the updated PDF.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    # Import data from XML
    def import_xml_to_pdf_fields(infile, datafile, outfile):
        """Import form data from XML file into PDF form fields."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Open XML file as stream
        with FileIO(datafile, 'r') as xml_input_stream:
            # Import data from XML into PDF form fields
            pdf_form.import_xml(xml_input_stream)

        # Save updated PDF
        pdf_form.save(outfile)
```