---
title: Move Field
type: docs
weight: 50
url: /python-net/move-field/
description: Move an existing form field to a different position in a PDF document.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Move a PDF Form Field to a New Position Using Python
Abstract: This example demonstrates how to move an existing form field to a different position in a PDF document using Aspose.PDF for Python. The code opens an existing PDF, relocates the specified form field to new coordinates, and saves the updated document.    
---

PDF forms often require layout adjustments after creation. Using Aspose.PDF for Python, developers can move existing form fields to a new position without recreating them.

This example shows how to reposition the "Country" field by specifying new coordinates for its placement within the page. The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class provides the move_field method to relocate fields within a PDF page.

1. Open the existing PDF form.
1. Create a FormEditor object.
1. Bind the PDF document to the FormEditor.
1. Move the 'Country' field to a new position using coordinates.
1. Save the modified document.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    def move_field(infile, outfile):
        # Create FormEditor object
        form_editor = pdf_facades.FormEditor()
        # Bind document to FormEditor
        form_editor.bind_pdf(infile)
        # Move field to new page
        form_editor.move_field("Country", 200, 600, 280, 620)
        # Save updated document
        form_editor.save(outfile)
```