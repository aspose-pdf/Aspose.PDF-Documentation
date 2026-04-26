---
title: Create Submit Button
type: docs
weight: 50
url: /python-net/create-submit-button/
description: Learn how to add a Submit Button to a PDF document programmatically using Aspose.PDF for Python. This tutorial demonstrates how to create a button that submits form data to a specified URL and save the updated PDF.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Create a Submit Button in a PDF Using Aspose.PDF for Python
Abstract: Submit buttons in PDF forms allow users to send form data directly to a server or endpoint. In this guide, you will learn how to add a Submit Button field to a PDF using the FormEditor class in Aspose.PDF for Python. The example shows how to configure the button’s name, label, target URL, and position, then save the updated PDF document.
---

Interactive PDF forms often require users to submit their input for processing, such as sending survey results, application forms, or feedback data. A Submit Button field provides this functionality by linking the button to a web endpoint.

The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class allows adding buttons, checkboxes, radio buttons, text fields, and other form controls.

1. Load an existing PDF document.
1. Add a Submit Button field to a specific page.
1. Set the button label and target submission URL.
1. Save the updated PDF with the new button.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_submit_button(infile, outfile):
    """Create Submit Button in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add Submit Button to PDF form
    pdf_form_editor.add_submit_btn(
        "submitbtn1",
        1,
        "Submit Button",
        "http://example.com/submit",
        100,
        450,
        200,
        470,
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
