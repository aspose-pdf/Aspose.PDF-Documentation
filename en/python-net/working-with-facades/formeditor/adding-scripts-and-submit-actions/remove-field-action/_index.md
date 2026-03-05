---
title: Remove Field Action
type: docs
weight: 20
url: /python-net/remove-field-action/
description: Removing JavaScript from form fields can be useful when modifying interactive PDF forms, disabling previously assigned actions, or cleaning documents that contain unnecessary scripts.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Remove JavaScript Actions from PDF Form Fields Using Python
Abstract: Using Aspose.PDF for Python, developers can programmatically remove JavaScript actions attached to form fields. This article explains how to open an existing PDF form, remove the script associated with a specific field using the FormEditor class, verify the operation, and save the modified document.
---

PDF forms often contain JavaScript actions that execute when users interact with form elements such as buttons or input fields. In some cases, these scripts must be removed to simplify form behavior, improve security, or update the form logic. Remove a JavaScript action from a form field in a PDF document using Aspose.PDF for Python. The code opens an existing PDF form, locates a specific field, removes its associated JavaScript action, and saves the updated document as a new PDF file.

Using the [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class from the [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/), you can remove JavaScript actions from specific fields in an existing PDF form:

1. Open an existing PDF form.
1. Locate a form field named 'Script_Demo_Button'.
1. Remove the JavaScript action associated with that field.
1. Check whether the removal was successful.
1. Save the updated PDF document.

```python

    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades
    import sys
    from os import path

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    def remove_field_script(input_file_name, output_file_name):
        # Create FormEditor object
        form_editor = pdf_facades.FormEditor()

        # Open input PDF file
        form_editor.bind_pdf(input_file_name)

        # Remove JavaScript action from the field
        if not form_editor.remove_field_action("Script_Demo_Button"):
            raise Exception("Failed to remove field script")        

        # Save output PDF file
        form_editor.save(output_file_name)
```
