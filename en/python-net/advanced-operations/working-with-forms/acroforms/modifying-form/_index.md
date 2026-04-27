---
title: Modifying AcroForm
linktitle: Modifying AcroForm
type: docs
weight: 45
url: /python-net/modifying-form/
description: Modifying form in your PDF file with Aspose.PDF for Python via .NET library. You can add or remove fields in existing form, get and set field limit and etc.
lastmod: "2025-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Managing and Customizing PDF Form Fields
Abstract: This collection of examples showcases various techniques for managing and customizing PDF form fields using Aspose.PDF for Python via .NET. It includes methods for clearing text from Typewriter-style form fields using TextFragmentAbsorber, setting and retrieving character limits with FormEditor, applying custom fonts and styling to text box fields, and removing specific form fields by name. These operations enable developers to sanitize, format, and tailor PDF forms for redistribution, branding, or data validation purposes, supporting both aesthetic and functional refinement in automated document workflows.
---

## Clear Text in Form

This example demonstrates how to clear text from Typewriter form fields in a PDF using Aspose.PDF for Python via .NET. It scans the first page of the PDF, identifies Typewriter forms, removes their content, and saves the updated document. This approach is useful for resetting or sanitizing form fields before redistributing a PDF.

1. Load the input PDF document.
1. Access forms on the first page.
1. Iterate over each form and check if it is a `Typewriter` form.
1. Use TextFragmentAbsorber to find text fragments in the form.
1. Clear the text of each fragment.
1. Save the modified PDF to the output file.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import sys
from os import path

def clear_text_in_form(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    forms = document.pages[1].resources.forms

    for form in forms:
        if form.it == "Typewriter" and form.subtype == "Form":
            absorber = ap.text.TextFragmentAbsorber()
            absorber.visit(form)

            for fragment in absorber.text_fragments:
                fragment.text = ""

    document.save(output_file_name)
```

## Get or Set Field Limit

The FormEditor class set_field_limit(field, limit) method allows you to set a field limit, the maximum number of characters that can be entered into a field.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import sys
from os import path

def set_field_limit(input_file_name, output_file_name):
    form = ap.facades.FormEditor()
    form.bind_pdf(input_file_name)
    form.set_field_limit("First Name", 15)
    form.save(output_file_name)
```

Similarly, Aspose.PDF has a method that gets the field limit.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import sys
from os import path

def get_field_limit(input_file_name):
    document = ap.Document(input_file_name)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        textBoxField = cast(ap.forms.TextBoxField, document.form[1])
        print(f"Limit: {textBoxField.max_len}")
```

## Set Custom Font for the Form Field

Form fields in Adobe PDF files can be configured to use specific default fonts. In the early versions of Aspose.PDF, only the 14 default fonts were supported. Later releases allowed developers to apply any font.

This code updates the appearance of a text box field in a PDF form by setting a custom font, size, and color, and then saves the modified document using Aspose.PDF for Python via .NET.

The following code snippet shows how to set the default font for PDF form fields.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import sys
from os import path

def set_form_field_font(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        textBoxField = cast(ap.forms.TextBoxField, document.form[1])
        font = ap.text.FontRepository.find_font("Calibri")
        textBoxField.default_appearance = ap.annotations.DefaultAppearance(
            font, 10, ap.Color.black.to_rgb()
        )

    document.save(output_file_name)
```

## Remove fields in existing form

This code removes a specific form field (by its name) from a PDF document and saves the updated file using Aspose.PDF for Python via .NET.

1. Load the PDF document.
1. Delete a form field by name.
1. Save the updated PDF.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import sys
from os import path

def delete_form_field(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    document.form.delete("First Name")
    document.save(output_file_name)
```
