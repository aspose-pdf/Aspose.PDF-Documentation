---
title: Set Submit Flag
type: docs
weight: 50
url: /python-net/set-submit-flag/
description: Learn how to programmatically set a submit flag for a PDF form button using Aspose.PDF for Python. This allows the button to submit form data in a specific format, such as XFDF, when clicked by a user.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Set Submit Flag for a PDF Form Button Using Aspose.PDF for Python
Abstract: PDF forms can be configured to submit form data to a server or endpoint in different formats. By setting a submit flag on a button field, developers can define how the data is sent. This tutorial demonstrates how to use the FormEditor class to set a submit flag for an existing submit button in a PDF document and save the updated file.  
---

PDF forms often include Submit Buttons to send user input to a server. The submit flag determines the data format sent (e.g., XFDF, FDF, HTML).

1. Bind a PDF document.
1. Access an existing submit button.
1. Set the submit flag for the desired format.
1. Save the updated PDF document.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_submit_flag(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set submit flag for the form
    form_editor.set_submit_flag("Script_Demo_Button", ap.facades.SubmitFormFlag.XFDF)

    # Save output PDF file
    form_editor.save(output_file_name)
```
