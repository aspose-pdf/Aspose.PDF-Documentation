---
title: Posting Forms in PDF via Python
linktitle: Posting Forms
type: docs
weight: 75
url: /python-net/posting-form/
description: Add submit functionality to a PDF form using Python and Aspose.PDF
lastmod: "2026-04-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to Add Submit Buttons and Form Submission Actions to a PDF Using Python
Abstract: This article demonstrates two ways to add submit functionality to a PDF form using Python and Aspose.PDF. It shows how to create a ready-made submit button with FormEditor and how to build a custom button field that sends form data to a server URL when clicked.
---

## Add Submit Button with FormEditor

The following code snippet demonstrates how to add a submit button to a PDF form using the FormEditor class in Aspose.PDF for Python via .NET. The button is configured to submit form data to a specified URL when clicked.

1. Open FormEditor.
1. Create Submit Button.
1. Assign Submission URL.
1. Set Button Coordinates.
1. Save Updated PDF.

```python
import aspose.pdf as ap
from aspose.pdf import Rectangle, FileSpecification
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import SubmitFormAction
from os import path
import sys

def add_submit_button(input_file_name, output_file_name):
    editor = ap.facades.FormEditor(input_file_name, output_file_name)
    editor.add_submit_btn(
        "submitbutton", 1, "Submit", "http://localhost/testing/show", 100, 450, 150, 475
    )
    editor.save()
```

## Add Custom Submit Action

The following code snippet explains how to create a custom submit button in a PDF form using Aspose.PDF for Python via .NET. The button is configured to send form data to a specified URL when clicked.

1. Open the PDF with ap.Document().
1. Create Submit Action.
1. Set Target URL.
1. Configure Submission Flags.
1. Create Button Area.
1. Create Button Field.
1. Assign Click Action.
1. Add Button to Form.
1. Save PDF.

```python
import aspose.pdf as ap
from aspose.pdf import Rectangle, FileSpecification
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import SubmitFormAction
from os import path
import sys

def add_submit_action(input_file_name, output_file_name):
    try:
        document = ap.Document(input_file_name)

        submit_action = ap.SubmitFormAction()
        submit_action.url = FileSpecification("http://localhost:3000/submit")
        submit_action.flags = (
            SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES
        )

        rect = Rectangle(10, 10, 100, 40)
        submit_button = ButtonField(document.pages[1], rect)
        submit_button.partial_name = "SubmitButton"
        submit_button.value = "Submit"
        submit_button.actions.on_release_mouse_btn = submit_action

        document.form.add(submit_button, 1)
        document.save(output_file_name)

    except Exception as e:
        print(f"Error adding submit button: {e}")
```