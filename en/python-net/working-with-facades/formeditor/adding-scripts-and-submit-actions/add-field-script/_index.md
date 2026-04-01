---
title: Add Field Script
type: docs
weight: 10
url: /python-net/add-field-script/
description: Interactive PDF forms can include JavaScript to automate actions when users interact with form fields. Using Aspose.PDF for Python, developers can easily attach scripts to form elements such as buttons or text fields. 
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Add JavaScript Actions to PDF Form Fields Using Python
Abstract: This article explains how to open a PDF form, assign JavaScript code to a specific form field, append additional script actions, and save the updated document. The example uses the FormEditor class from the Aspose.PDF Facades API to manipulate form behavior programmatically.   
---

## Add JavaScript Actions to PDF Form Fields Using Python

This code snippet enables you to add JavaScript actions to an existing PDF form field using the Aspose.PDF for Python library. It opens a PDF document, assigns a JavaScript action to a form field, and adds a script that runs when the field is triggered. Finally, the updated PDF is saved as a new file.
Using the [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class from the [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) module, you can programmatically attach JavaScript to existing form fields:

1. Open an existing PDF form.
1. Set a JavaScript action for a specific field.
1. Append another JavaScript action to the same field.
1. Save the modified PDF document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def add_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set JavaScript action for the field
    form_editor.set_field_script("Script_Demo_Button", "app.alert('Script 1 has been executed');")

    # Add JavaScript action to the field
    form_editor.add_field_script("Script_Demo_Button", "app.alert('Script 2 has been executed');")

    # Save output PDF file
    form_editor.save(output_file_name)
```
