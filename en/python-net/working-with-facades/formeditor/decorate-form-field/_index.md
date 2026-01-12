---
title: Decorate Form Field in PDF
type: docs
weight: 30
url: /python-net/decorate-form-field/
description: Explore how to decorate form fields in a PDF document, adding visual enhancements like borders, in Python with Aspose.PDF.
lastmod: "2025-11-05"
---

## Decorate a Particular Form Field in an Existing PDF File

Customize the appearance of a PDF form field using Aspose.PDF for Python via .NET. By leveraging the FormEditor and FormFieldFacade classes, developers can apply styling such as font, size, border color, and border width to specific fields in a PDF form.

1. Create a FormEditor object.
1. Attach the input PDF file with BindPdf().
1. Create a FormFieldFacade object.
1. Assign the facade to the editor.
1. Use DecorateField() to apply the styling to the target field (e.g., "City").
1. Save the updated PDF.

This workflow is useful for enhancing the visual presentation of PDF forms, ensuring fields are styled consistently and professionally for end users.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")
clr.AddReference("System.Drawing")  # Needed for colors

import Aspose.Pdf.Facades as pdf_facades
from System.Drawing import Color

def decorate_field():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create an instance of FormEditor to manipulate form fields
    editor = pdf_facades.FormEditor()

    # Bind PDF document
    editor.BindPdf(os.path.join(data_dir, "Sample-Form-01.pdf"))

    # Create a FormFieldFacade object to define decoration properties
    city_decoration = pdf_facades.FormFieldFacade()
    city_decoration.Font = pdf_facades.FontStyle.Courier
    city_decoration.FontSize = 12
    city_decoration.BorderColor = Color.Black
    city_decoration.BorderWidth = 2

    # Assign the decoration facade to the FormEditor
    editor.Facade = city_decoration

    # Apply the decoration to the field named "City"
    editor.DecorateField("City")

    # Save modified PDF document
    editor.Save(os.path.join(data_dir, "Sample-Form-02.pdf"))

    # Dispose resources
    editor.Dispose()

    print("Field 'City' decorated successfully with custom font and border settings.")
```

## Decorate All Fields of a Particular Type in an Existing PDF File

Apply alignment styling to all text fields in a PDF form. By using the FormEditor and FormFieldFacade classes, developers can control the appearance of form fields across the entire document.

1. Create a FormEditor object.
1. Attach the input PDF file with BindPdf().
1. Create a FormFieldFacade object.
1. Assign the facade to the editor.
1. Use DecorateField(FieldType.Text) to apply alignment to every text field.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def decorate_field2():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create an instance of FormEditor to manipulate form fields
    editor = pdf_facades.FormEditor()

    # Bind PDF document
    editor.BindPdf(os.path.join(data_dir, "Sample-Form-01.pdf"))

    # Create a FormFieldFacade object to define alignment properties
    text_field_decoration = pdf_facades.FormFieldFacade()
    text_field_decoration.Alignment = pdf_facades.FormFieldFacade.AlignCenter

    # Assign the decoration facade to the FormEditor
    editor.Facade = text_field_decoration

    # Apply the alignment decoration to all text fields in the PDF
    editor.DecorateField(pdf_facades.FieldType.Text)

    # Save modified PDF document
    editor.Save(os.path.join(data_dir, "Sample-Form-01-align-text.pdf"))

    # Dispose resources
    editor.Dispose()

    print("All text fields aligned to center successfully.")
```