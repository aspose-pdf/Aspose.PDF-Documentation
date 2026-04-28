---
title: Posting Forms in PDF via Python
linktitle: Posting Forms
type: docs
weight: 75
url: /python-net/posting-form/
description: Add submit buttons and submission actions to PDF AcroForms by using Aspose.PDF for Python via .NET.
lastmod: "2026-04-28"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to Add Submit Buttons and Form Submission Actions to a PDF Using Python
Abstract: This article shows two approaches to add submit functionality to PDF forms by using Aspose.PDF for Python via .NET. You can add a ready-made submit button through FormEditor or create a custom button field with SubmitFormAction for advanced control. These patterns help integrate PDF forms with server-side form processing endpoints.
---

## Add Submit Button with FormEditor

The following code snippet demonstrates how to add a submit button to a PDF form using the FormEditor class in Aspose.PDF for Python via .NET. The button is configured to submit form data to a specified URL when clicked.

1. Create a `FormEditor` object.
1. Add a submit button to the target page.
1. Set the submission URL and button coordinates.
1. Save the updated PDF.

```python
import aspose.pdf as ap

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
1. Create a submit action.
1. Set the target URL and submission flags.
1. Create a button field and bind its click action.
1. Add the button to the form.
1. Save the updated PDF.

```python
import aspose.pdf as ap

def add_submit_action(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    submit_action = ap.annotations.SubmitFormAction()
    submit_action.url = ap.FileSpecification("http://localhost:3000/submit")
    submit_action.flags = (
        ap.annotations.SubmitFormAction.EXPORT_FORMAT
        | ap.annotations.SubmitFormAction.SUBMIT_COORDINATES
    )

    rect = ap.Rectangle(10, 10, 100, 40)
    submit_button = ap.forms.ButtonField(document.pages[1], rect)
    submit_button.partial_name = "SubmitButton"
    submit_button.value = "Submit"
    submit_button.actions.on_release_mouse_btn = submit_action

    document.form.add(submit_button, 1)
    document.save(output_file_name)
```

## Related Topics

- [Create AcroForm](/pdf/python-net/create-form/)
- [Fill AcroForm](/pdf/python-net/fill-form/)
- [Modifying AcroForm](/pdf/python-net/modifying-form/)
- [Import and Export Form Data](/pdf/python-net/import-export-form-data/)