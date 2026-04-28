---
title: Modifying AcroForm
linktitle: Modifying AcroForm
type: docs
weight: 45
url: /python-net/modifying-form/
description: Modify AcroForm fields in PDF documents by using Aspose.PDF for Python via .NET, including clearing text, setting limits, styling fields, and removing fields.
lastmod: "2026-04-28"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Managing and Customizing PDF Form Fields
Abstract: This article presents practical examples for modifying AcroForm fields by using Aspose.PDF for Python via .NET. It covers clearing text from Typewriter form content, setting and reading text field character limits, applying custom font appearance, and removing fields by name. These workflows support common form maintenance tasks in automated PDF processing pipelines.
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

## Set Field Limit

Use `set_field_limit(field, limit)` from `FormEditor` to define the maximum number of characters allowed in a text field.

1. Create a `FormEditor` object.
1. Bind the input PDF.
1. Set the field limit for a target field.
1. Save the updated PDF.

```python
import aspose.pdf as ap


def set_field_limit(input_file_name, output_file_name):
    form = ap.facades.FormEditor()
    form.bind_pdf(input_file_name)
    form.set_field_limit("First Name", 15)
    form.save(output_file_name)
```

## Get Field Limit

You can also read the character limit from a text field.

1. Load the PDF document.
1. Access the target form field.
1. Ensure the field is a `TextBoxField`.
1. Read and print `max_len`.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable


def get_field_limit(input_file_name):
    document = ap.Document(input_file_name)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        text_box_field = cast(ap.forms.TextBoxField, document.form[1])
        print(f"Limit: {text_box_field.max_len}")
```

## Set Custom Font for the Form Field

This example sets a custom default appearance for a text box field, including font, size, and color.

1. Load the PDF document.
1. Access the target field and verify its type.
1. Find the font in `FontRepository`.
1. Apply a new `DefaultAppearance`.
1. Save the updated PDF.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable


def set_form_field_font(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        text_box_field = cast(ap.forms.TextBoxField, document.form[1])
        font = ap.text.FontRepository.find_font("Calibri")
        text_box_field.default_appearance = ap.annotations.DefaultAppearance(
            font, 10, ap.Color.black.to_rgb()
        )

    document.save(output_file_name)
```

## Remove Fields in an Existing Form

This code removes a specific form field (by its name) from a PDF document and saves the updated file using Aspose.PDF for Python via .NET.

1. Load the PDF document.
1. Delete a form field by name.
1. Save the updated PDF.

```python
import aspose.pdf as ap


def delete_form_field(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    document.form.delete("First Name")
    document.save(output_file_name)
```

## Related Topics

- [Create AcroForm](/pdf/python-net/create-form/)
- [Fill AcroForm](/pdf/python-net/fill-form/)
- [Extract AcroForm](/pdf/python-net/extract-form/)
- [Import and Export Form Data](/pdf/python-net/import-export-form-data/)
