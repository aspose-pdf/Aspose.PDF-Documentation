---
title: Copy Outer Field
type: docs
weight: 30
url: /python-net/copy-outer-field/
description: This example demonstrates how to copy a form field from one PDF document to another using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Copy PDF Form Fields from Another Document Using Python
Abstract: This article explains how to create a new PDF document, copy the "First Name" field from a source PDF to page 1 at coordinates (200, 600), and save the updated target document.   
---

Sometimes, PDF forms require reusing fields from one document in another. Using Aspose.PDF for Python, developers can programmatically copy form fields from a source PDF to a target PDF.

The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class provides the 'copy_outer_field' method, which copies a field from a source document to a target document at a specified page and coordinates.

The code creates a new PDF (target), adds a page, and then copies a field from an existing PDF (source) to the target document at specified coordinates.

1. Create a new target PDF document.
1. Add at least one page to the target PDF.
1. Save the empty target document.
1. Create a FormEditor object and bind it to the target PDF.
1. Copy the 'First Name' field from the source PDF to page 1 at (200, 600).
1. Save the updated target PDF.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    def copy_outer_field(infile, outfile):
        # Since copy_outer_field() method needs to copy field from source document to target document, we need to create a new document as target document first.
        doc = ap.Document()
        doc.pages.add()
        doc.save(outfile)

        # Create FormEditor object
        form_editor = pdf_facades.FormEditor()
        # Bind document to FormEditor
        form_editor.bind_pdf(outfile)
        # Copies an existing field to a new position specified by both page number and ordinates. 
        # A new document will be produced, which contains everything the source document has except for the newly copied field.
        form_editor.copy_outer_field(infile, "First Name", 1, 200, 600)
        # Save updated document
        form_editor.save(outfile)
```

**Please note:**

The 'copy_outer_field' method signature looks like this:

```python

    copy_outer_field(original_field_name, new_field_name, page_number, x, y)
```

- 'original_field_name' – the field you want to duplicate.
- 'new_field_name' – the name of the new field.
- 'page_number' – the page on which the new field will appear.
- x, y – coordinates on that page.

The page_number is expected to be a positive integer corresponding to an existing page in the PDF (1-based indexing).

If you pass a negative parameter, e.g.:

```python

    form_editor.copy_outer_field("First Name", "First Name Copy", 1, -200, 600)
```

The program will then reset to the previous parameters.