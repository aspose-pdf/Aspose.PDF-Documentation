---
title: Add PDF Form Fields
type: docs
weight: 10
url: /python-net/add-form-fields/
description: This topic explains how to work with Form Fields with Aspose.PDF Facades using FormEditor Class.
lastmod: "2025-11-05"
---

## Add Form Field in an Existing PDF file

Aspose.PDF for Python via .NET shows how to add a new text field to a PDF form. By leveraging the FormEditor class, developers can insert new fields into existing PDF documents, configure their properties, and save the updated file.

1. Create a FormEditor object.
1. Attach the input PDF file with BindPdf().
1. Use AddField() to insert a new field with specified coordinates.
1. Set field properties.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def add_field():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create an instance of FormEditor to manipulate form fields
    editor = pdf_facades.FormEditor()

    # Bind PDF document
    editor.BindPdf(os.path.join(data_dir, "Sample-Form-01.pdf"))

    # Add a text field named "Country" to the first page of the PDF
    # Coordinates: left, bottom, right, top
    editor.AddField(
        pdf_facades.FieldType.Text,
        "Country",
        1,
        232.56, 496.75, 352.28, 514.03
    )

    # Set a character limit for the "Country" field to 20 characters
    editor.SetFieldLimit("Country", 20)

    # Save modified PDF document
    editor.Save(os.path.join(data_dir, "Sample-Form-01-mod.pdf"))

    # Dispose resources
    editor.Dispose()

    print("Text field 'Country' added successfully with a 20-character limit.")
```

## Add Submit Button URL in an Existing PDF File

Add a submit button to a PDF form using Aspose.PDF for Python via .NET. A submit button allows users to send form data to a specified URL when clicked. By using the FormEditor class, developers can insert interactive buttons into existing PDF documents and configure their properties.

1. Create a FormEditor object.
1. Attach the input PDF file with BindPdf().
1. Use AddSubmitBtn() to insert a button with text, target URL, and coordinates.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def add_submit_btn():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create an instance of FormEditor to manipulate form fields
    editor = pdf_facades.FormEditor()

    # Bind PDF document
    editor.BindPdf(os.path.join(data_dir, "Sample-Form-01.pdf"))

    # Add a submit button named "Submit" to the first page of the PDF
    # Parameters: field name, page number, button text, submit URL, coordinates (left, bottom, right, top)
    editor.AddSubmitBtn(
        "Submit", 
        1, 
        "Submit", 
        "http://localhost:3000", 
        232.56, 466.75, 352.28, 484.03
    )

    # Save modified PDF document
    editor.Save(os.path.join(data_dir, "Sample-Form-01-mod.pdf"))

    # Dispose resources
    editor.Dispose()

    print("Submit button added successfully to the PDF form.")
```

## Add JavaScript for Push Button

Attach a JavaScript action to a PDF form field. By leveraging the FormEditor class, developers can embed scripts into form fields to enhance interactivity. In this case, a script is added to the "Last Name" field that displays an alert message when triggered.

1. Create a FormEditor object.
1. Attach the input PDF file with BindPdf().
1. Use AddFieldScript() to insert JavaScript into the specified field.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def add_field_script():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create an instance of FormEditor to manipulate form fields
    editor = pdf_facades.FormEditor()

    # Bind PDF document
    editor.BindPdf(os.path.join(data_dir, "Sample-Form-01.pdf"))

    # Add a JavaScript action to the field named "Last Name"
    # The script displays an alert box with the message "Only one last name"
    editor.AddFieldScript("Last Name", "app.alert(\"Only one last name\",3);")

    # Save modified PDF document
    editor.Save(os.path.join(data_dir, "Sample-Form-01-mod.pdf"))

    # Dispose resources
    editor.Dispose()

    print("JavaScript action added successfully to the 'Last Name' field.")
```