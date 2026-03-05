---
title: Set Field Alignment Vertical
type: docs
weight: 40
url: /python-net/set-field-alignment-vertical/
description: This example demonstrates how to set the vertical alignment of a form field in a PDF document using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Set Vertical Alignment for PDF Form Fields Using Python
Abstract: This article explains how to open a PDF, set vertical alignment for a field using the FormEditor class, and save the updated PDF. The example sets the vertical alignment of a field named "First Name" to the bottom of the field area.          
---

PDF form fields can contain text that needs proper vertical alignment for a consistent and professional appearance. Using Aspose.PDF for Python, developers can programmatically modify the vertical alignment of form fields.
Vertical alignment allows developers to control whether the field’s text appears at the top, center, or bottom of the field’s bounding box, improving the layout and readability of form data.

Using the [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class and the [FormFieldFacade](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formfieldfacade/) constants, developers can adjust vertical alignment programmatically to achieve consistent form layout:

1. Open an existing PDF document.
1. Create a FormEditor object.
1. Set the vertical alignment of a field named "First Name" to bottom.
1. Save the modified document.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pydrawing as ap_pydrawing
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    def set_field_alignment_vertical(infile, outfile):
        # Open document
        doc = ap.Document(infile)

        # Create FormEditor object
        form_editor = pdf_facades.FormEditor(doc)

        # Set field vertical alignment to top
        if form_editor.set_field_alignment_v(
            "First Name", pdf_facades.FormFieldFacade.ALIGN_BOTTOM
        ):
            # Save updated document
            form_editor.save(outfile)
        else:
            raise Exception("Failed to set field vertical alignment. Field may not support vertical alignment.")
```
