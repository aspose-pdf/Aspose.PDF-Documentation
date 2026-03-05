---
title: Export to XML
type: docs
weight: 40
url: /python-net/export-to-xml/
description: This example demonstrates how to export PDF form data to an XML file using Aspose.PDF for Python via .NET. It shows how to load a PDF document, access its form fields through the Form facade, and save the extracted data as structured XML using Form Class.
lastmod: "2026-02-19"
---

Exporting form data allows developers to reuse information stored in PDF AcroForms without manually copying field values. In this example, a [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) object is created from the aspose.pdf. In the facades module, the source PDF is bound to it, and the form data is written to an XML stream.

1. Create a Form Object. Initialize pdf_facades.Form() to access and manage form fields.
1. Use 'bind_pdf()' to attach the source PDF document to the Form instance.
1. Create a writable file stream using 'FileIO()'.
1. Call 'export_xml()' to extract all form field values and write them into the XML file.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    # Export Data to XML
    def export_pdf_form_data_to_xml(infile, datafile):
        """Export PDF form data to XML file."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Open XML file as stream
        with FileIO(datafile, 'w') as xml_output_stream:
            # Export data from PDF form fields to XML
            pdf_form.export_xml(xml_output_stream)
```