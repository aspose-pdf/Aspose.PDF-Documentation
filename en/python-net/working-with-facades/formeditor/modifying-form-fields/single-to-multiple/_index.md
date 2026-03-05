---
title: Single-Line Field to Multi-Line Field 
type: docs
weight: 80
url: /python-net/single-to-multiple/
description: Convert a single-line text field into a multi-line field in a PDF document using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Convert a Single-Line Text Field to a Multi-Line Field in a PDF Using Python
Abstract: This example demonstrates how to convert a single-line text field into a multi-line field in a PDF document using Aspose.PDF for Python. The code loads an existing PDF form, modifies the specified field to allow multiple lines of text, and saves the updated document.    
---

PDF forms sometimes contain text fields designed for single-line input, which may not be sufficient for certain types of data. With Aspose.PDF for Python, developers can easily convert such fields into multi-line text fields without recreating them.

Using the [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class, developers can modify existing text fields without affecting their position or other properties.

1. Load the existing PDF document.
1. Create a FormEditor instance.
1. Bind the PDF document to the editor.
1. Convert the selected field to multi-line.
1. Save the updated document.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    def single2multiple(infile, outfile):
        # Create FormEditor object
        form_editor = pdf_facades.FormEditor()
        # Bind document to FormEditor
        form_editor.bind_pdf(infile)    
        # Change a single-lined text field to a multiple-lined one
        form_editor.single_2_multiple("City")
        # Save updated document
        form_editor.save(outfile)
```

