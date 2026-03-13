---
title: Create ListBox Field
type: docs
weight: 30
url: /python-net/create-listbox-field/
description: Learn how to programmatically add a ListBox form field to a PDF document using Aspose.PDF for Python. This guide shows how to insert a ListBox field, define selectable items, and save the updated PDF file.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Create a ListBox Field in a PDF Using Aspose.PDF for Python
Abstract: PDF forms allow users to interact with documents by selecting options, entering data, and submitting information digitally. A ListBox field lets users choose one or multiple values from a visible list of options. In this tutorial, you will learn how to create a ListBox field in a PDF using the FormEditor class in Aspose.PDF for Python and populate it with predefined items.
---

PDF forms are commonly used for applications, surveys, and registration documents. A ListBox field displays multiple options simultaneously, making it easier for users to review and select items from a list.

The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class provides functionality for adding different types of interactive fields, including ListBox elements.

1. Load an existing PDF document.
1. Define a list of selectable options.
1. Add a ListBox field to a specific page.
1. Set a default selected value.
1. Save the updated PDF document.

```python

    import sys
    from os import path
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    def create_listbox_field(infile, outfile):
        """Create ListBox field in PDF document."""
        pdf_form_editor = pdf_facades.FormEditor()
        pdf_form_editor.bind_pdf(infile)

        # Add ListBox field to PDF form
        pdf_form_editor.items = ["Australia", "New Zealand", "Malaysia"];
        pdf_form_editor.add_field(pdf_facades.FieldType.LIST_BOX, "listbox1", "Australia", 1, 230, 398, 350, 514)

        # Save updated PDF document with form fields
        pdf_form_editor.save(outfile)
```