---
title: Create ComboBox Field
type: docs
weight: 20
url: /python-net/create-combobox-field/
description: Check how to programmatically add a ComboBox (drop-down list) field to a PDF document using Aspose.PDF for Python. This example demonstrates how to insert a ComboBox form field, add selectable items, and save the updated PDF file.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Create a ComboBox Field in a PDF Using Aspose.PDF for Python
Abstract: Interactive form fields make PDFs more dynamic and user-friendly. A ComboBox field allows users to select an option from a predefined drop-down list. In this tutorial, you will learn how to create a ComboBox in a PDF using the FormEditor class in Aspose.PDF for Python, populate it with options, and save the modified document.
---

PDF forms are widely used for collecting structured information in digital documents such as applications, surveys, and registration forms. A ComboBox field provides a convenient way for users to choose from a list of predefined values while keeping the form compact and organized.

The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class allows you to create and manage different types of fields, including text boxes, checkboxes, radio buttons, and drop-down lists.

1. Load an existing PDF document.
1. Add a ComboBox field with 'add_field()' method and 'FieldType.COMBO_BOX' parameter.
1. Use the 'add_list_item()' method to insert selectable options into the drop-down list.
1. Save the updated PDF document.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_combobox_field(infile, outfile):
    """Create ComboBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add ComboBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.COMBO_BOX, "combobox1", "Australia", 1, 230, 498, 350, 514
    )
    pdf_form_editor.add_list_item("combobox1", ["Australia", "Australia"])
    pdf_form_editor.add_list_item("combobox1", ["New Zealand", "New Zealand"])

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
