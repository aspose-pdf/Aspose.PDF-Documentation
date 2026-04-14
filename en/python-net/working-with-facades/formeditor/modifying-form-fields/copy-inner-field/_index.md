---
title: Copy Inner Field
type: docs
weight: 20
url: /python-net/copy-inner-field/
description: Copy PDF Form Fields to a New Position Using Python using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Copy PDF Form Fields to a New Position Using Python
Abstract: This example demonstrates how to copy an existing form field to a new position in a PDF document using Aspose.PDF for Python. The code opens a PDF, duplicates a field to a specified page and coordinates, and saves the updated document.    
---

PDF forms often require duplicating fields while maintaining the original formatting and behavior. Using Aspose.PDF for Python, developers can copy an existing field to a new position on the same or another page programmatically.

This article explains how to copy a field named 'First Name' to a new field called 'First Name Copy' on page 2 at specific coordinates (x=200, y=600), producing a PDF with the newly positioned field.

1. Open an existing PDF form.
1. Create a FormEditor object.
1. Bind the PDF document to the FormEditor.
1. Copy the 'First Name' field to a new field 'First Name Copy' on page 2 at coordinates (200, 600).
1. Save the updated document.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def copy_inner_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Copies an existing field to a new position specified by both page number and ordinates.
    # A new document will be produced, which contains everything the source document has except for the newly copied field.
    form_editor.copy_inner_field("First Name", "First Name Copy", 2, 200, 600)
    # Save updated document
    form_editor.save(outfile)
```

**Please note:**

The 'copy_inner_field' method signature looks like this:

```python
copy_inner_field(original_field_name, new_field_name, page_number, x, y)
```

- 'original_field_name' – the field you want to duplicate.
- 'new_field_name' – the name of the new field.
- 'page_number' – the page on which the new field will appear.
- x, y – coordinates on that page.

The page_number is expected to be a positive integer corresponding to an existing page in the PDF (1-based indexing).

If you pass a negative parameter, e.g.:

```python
form_editor.copy_inner_field("First Name", "First Name Copy", -1, 200, 600)
```

The program will then reset to the previous parameters.
