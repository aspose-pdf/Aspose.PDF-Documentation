---
title: Get Field Appearance
type: docs
weight: 20
url: /python-net/get-field-appearance/
description: This article explains how to open a PDF, access a form field, retrieve its appearance settings, and display them. The example demonstrates retrieving the appearance of a field named "Last Name".
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Retrieve PDF Form Field Appearance Using Python
Abstract: This example demonstrates how to retrieve the visual appearance properties of a form field in a PDF document using Aspose.PDF for Python. The code opens an existing PDF, accesses a specific form field, and prints its appearance details, including background color, text color, border color, and alignment.         
---

Form fields in PDF documents have visual properties such as background color, text color, border color, and alignment. With Aspose.PDF for Python, developers can programmatically inspect these appearance settings using the [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class.

1. Open an existing PDF document.
1. Create a FormEditor object.
1. Retrieve the appearance information of a specific field.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pydrawing as ap_pydrawing
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    def get_field_appearance(infile, outfile):
        # Open document
        doc = ap.Document(infile)

        # Create FormEditor object
        form_editor = pdf_facades.FormEditor(doc)

        # Get field appearance
        appearance = form_editor.get_field_appearance("Last Name")
        print("Field Appearance: " + str(appearance))
```