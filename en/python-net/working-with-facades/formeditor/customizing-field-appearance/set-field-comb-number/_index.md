---
title: Set Field Comb Number
type: docs
weight: 70
url: /python-net/set-field-comb-number/
description: This example demonstrates how to set a comb number for a PDF form field using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Set Comb Number for PDF Form Fields Using Python
Abstract: Using Aspose.PDF for Python, developers can programmatically set the number of boxes (comb number) for a form field to enforce a fixed-length input. This article demonstrates setting the comb number for a field named "PIN".         
---

The comb number defines how the field's content is split into equally spaced boxes, often used for PIN codes, serial numbers, or other fixed-length input fields. The code opens an existing PDF, sets the comb number for a field, and saves the modified document.

The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class provides the 'set_field_comb_number' method to define the number of boxes (characters) in a form field.

1. Open an existing PDF form.
1. Creates a FormEditor object.
1. Set the comb number of a field named "PIN" to 5.
1. Save the updated document.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pydrawing as ap_pydrawing
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    def set_field_comb_number(infile, outfile):
        # Open document
        doc = ap.Document(infile)

        # Create FormEditor object
        form_editor = pdf_facades.FormEditor(doc)

        # Set field comb number to 5
        form_editor.set_field_comb_number("PIN", 5)
        
        # Save updated document
        form_editor.save(outfile)
```