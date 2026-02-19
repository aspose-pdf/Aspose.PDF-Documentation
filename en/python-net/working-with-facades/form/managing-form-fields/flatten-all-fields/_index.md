---
title: Flatten All Fields
type: docs
weight: 10
url: /python-net/flatten-all-fields/
description: This example demonstrates how to flatten all form fields in a PDF using Aspose.PDF for Python via .NET. It shows how to bind a PDF document, convert every interactive form element into static page content, and save the finalized file.
lastmod: "2026-02-19"
---

Flattening removes interactivity from PDF forms by merging field values directly into the document layout. In this example, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade from [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) is used to bind the source PDF and apply the flatten_all_fields() method, which converts all fields into non-editable content.

1. Initialize pdf_facades.Form() to interact with PDF form fields.
1. Call 'bind_pdf()' to attach the source document.
1. Call 'flatten_all_fields()' to convert all interactive fields into static content.
1. Save the updated Document.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    # Flatten all fields
    def flatten_all_fields(infile, outfile):
        """Flatten all fields in a PDF document."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Flatten all fields in the PDF document
        pdf_form.flatten_all_fields()

        # Save updated PDF
        pdf_form.save(outfile)
```