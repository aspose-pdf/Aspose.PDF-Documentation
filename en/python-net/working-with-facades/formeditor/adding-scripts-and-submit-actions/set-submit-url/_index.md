---
title: Set Submit Url
type: docs
weight: 40
url: /python-net/set-submit-url/
description: This example demonstrates how to configure a submit action for a button field in a PDF form using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Set a Submit URL for a PDF Form Button Using Python
Abstract: This article explains how to open an existing PDF form, define a submission URL for a button field using the FormEditor class, verify that the operation succeeds, and save the updated PDF document.   
---

PDF forms can be designed to submit their data to a web server when a user clicks a submit button. Using Aspose.PDF for Python, developers can programmatically configure a submit action for form fields.
By setting a submit URL, the form can send user-entered data to a server when the button is clicked. This functionality is useful for workflows where PDF forms must submit information to web applications, databases, or processing services.

Using the [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class from the [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) module, developers can programmatically assign a submit URL to a button field in an existing PDF form.

1. Open an existing PDF form.
1. Locate a button field named Script_Demo_Button.
1. Assign a URL where the form data will be submitted.
1. Verify that the action was successfully applied.
1. Save the updated PDF document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_submit_url(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Set license
    set_license()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set submit URL for the button
    if not form_editor.set_submit_url(
        "Script_Demo_Button", "http://www.example.com/submit"
    ):
        raise Exception("Failed to set submit URL")

    # Save output PDF file
    form_editor.save(output_file_name)
```
