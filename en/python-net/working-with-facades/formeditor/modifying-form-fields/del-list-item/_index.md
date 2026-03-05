---
title: Delete List Item
type: docs
weight: 40
url: /python-net/del-list-item/
description: 
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Remove Items from PDF List Box Fields Using Python
Abstract: This example demonstrates how to remove an item from a list box form field in a PDF document using Aspose.PDF for Python. The code opens an existing PDF, deletes a specific item from a list box field, and saves the updated document.   
---

List box fields in PDFs allow users to select one or multiple predefined options. Using Aspose.PDF for Python, developers can programmatically remove items from these fields.

This article explains how to delete the 'UK' item from a list box field named 'Country', ensuring the field only contains the desired options.

The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class provides the 'del_list_item' method to remove a specific item from a list box field.

1. Open an existing PDF form.
1. Create a FormEditor object.
1. Bind the PDF document to the FormEditor.
1. Delete the "UK" item from the "Country" list box field.
1. Save the updated document.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    def del_list_item(infile, outfile):
        # Create FormEditor object
        form_editor = pdf_facades.FormEditor()
        # Bind document to FormEditor
        form_editor.bind_pdf(infile)
        # Delete list item from list box field
        form_editor.del_list_item("Country", "UK")
        # Save updated document
        form_editor.save(outfile)
```

