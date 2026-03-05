---
title: Set Field Script
type: docs
weight: 30
url: /python-net/set-field-script/
description: This code snippet shows how to assign a JavaScript action to a form field in a PDF document using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Set JavaScript Actions for PDF Form Fields Using Python
Abstract: This article explains how to open a PDF document, assign JavaScript code to a form field, update the script using the FormEditor class, and save the modified file. The example demonstrates how existing scripts can be overridden to modify the behavior of form fields.  
---

Interactive PDF forms often rely on JavaScript to perform tasks such as displaying alerts, validating input, or triggering dynamic form behavior. With Aspose.PDF for Python, developers can programmatically manage these scripts.

The example first adds a JavaScript action to the field and then replaces it with another script using the 'set_field_script' method. This approach allows developers to control or update the interactive behavior of PDF form elements such as buttons or input fields.

The form field used in this example is named 'Script_Demo_Button', which typically represents a button that executes the assigned script when triggered.

Using the [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class from the [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) module, developers can programmatically manage JavaScript actions associated with form fields:

1. Open an existing PDF form document.
1. Add a JavaScript action to a form field.
1. Set (replace) the JavaScript action with a new script.
1. Save the modified PDF document.

```python

    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades
    import sys
    from os import path

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    def set_field_script(input_file_name, output_file_name):
        # Create FormEditor object
        form_editor = pdf_facades.FormEditor()

        # Open input PDF file
        form_editor.bind_pdf(input_file_name)

        # Add JavaScript action to the field
        form_editor.add_field_script("Script_Demo_Button", "app.alert('Script 1 has been executed');")

        # Set JavaScript action for the field
        form_editor.set_field_script("Script_Demo_Button", "app.alert('Script 2 has been executed');")

        # Save output PDF file
        form_editor.save(output_file_name)
```
