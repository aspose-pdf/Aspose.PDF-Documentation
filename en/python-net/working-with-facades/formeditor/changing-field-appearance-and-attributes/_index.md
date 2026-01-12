---
title: Field appearance and attributes
type: docs
weight: 40
url: /python-net/changing-field-appearance-and-attributes/
description: This section explains how you can change field appearance and attributes with FormEditor Class.
lastmod: "2025-11-05"
draft: false
---

{{% alert color="primary" %}}

[FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/FormEditor) class of [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades) allows you to not only change the look and feel of the form field, but also the behavior of the field. In this article, we will see how we can use FormEditor class to change the field appearance, field attributes, and the field limit as well.

{{% /alert %}}

## Implementation details

[set_field_appearance()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/#methods) method is used to the change the appearance of a form field. It takes AnnotationFlag as a parameter. AnnotationFlag is an enumeration which has different members like Hidden or NoRotate etc.

[set_field_appearance()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/#methods) method is used to change the attribute of a form field. A parameter passed to this method is PropertyFlag enumeration which contains members like ReadOnly or Required etc.

[FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/FormEditor) class also provides a method to set the field limit. It tells the field that how much characters it can be filled with. The bellow code snippet shows you how all of these methods can be used.

Add a new text field to a PDF form and configure its attributes. By leveraging the FormEditor class, developers can insert new fields into existing PDF documents, enforce validation rules, and control user input.

1. Open the PDF document.
1. Create a FormEditor object.
1. Use AddField() to insert a new field with specified coordinates.
1. Set field attributes.
1. Set field limits.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades

def add_field_and_set_attributes():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open PDF document
    doc = pdf.Document(os.path.join(data_dir, "FilledForm.pdf"))

    # Create an instance of FormEditor to manipulate form fields
    form_editor = pdf_facades.FormEditor(doc)

    # Add a new text field to the form on page 1 at the specified coordinates
    form_editor.AddField(
        pdf_facades.FieldType.Text,
        "text1",
        1,
        200, 550, 300, 575
    )

    # Set the field attribute to make the text field required
    form_editor.SetFieldAttribute("text1", pdf_facades.PropertyFlag.Required)

    # Set a character limit for the field (maximum 20 characters)
    form_editor.SetFieldLimit("text1", 20)

    # Save the updated PDF document
    form_editor.Save(os.path.join(data_dir, "ChangingFieldAppearance_out.pdf"))

    # Dispose resources
    form_editor.Dispose()
    doc.Dispose()

    print("Text field 'text1' added successfully with required attribute and 20-character limit.")
```
