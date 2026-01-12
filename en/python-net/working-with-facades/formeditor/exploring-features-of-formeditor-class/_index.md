---
title: Exploring features of FormEditor class
type: docs
weight: 20
url: /python-net/exploring-features-of-formeditor-class/
description: You can learn details of exploring features of FormEditor class with Aspose. PDF for Python via .NET library
lastmod: "2025-11-05"
---

{{% alert color="primary" %}}

PDF documents sometimes contain interactive form, which are known as AcroForm. It is just like a form used in the web pages. These forms contain different types of controls i.e. Text boxes, Check boxes, and Buttons etc. A developer working with PDF files might sometimes have to edit these forms. In this article, we’ll look into the details how [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades) enables us to do that.

{{% /alert %}}

## Implementation details

Developers can use [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades) not only to add new forms and form fields in a PDF document, but also allow you to edit existing fields. The scope of this article is limited to the features of [Aspose.PDF for Python via .NET](/pdf/python-net/) which deal with the form editing.

[FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor) is the class which contains most of the methods and properties which allow the developers to edit form fields. You can not only add new fields, but also remove existing fields, move one field to another position, change field name, or attributes etc. The list of the features provided by this class is quite comprehensive, and it is very easy to work with the form fields using this class.

Explore and apply multiple form editing features in a PDF using Aspose.PDF for Python via .NET. The FormEditor class provides a wide range of methods to manipulate form fields, including adding, modifying, styling, and removing them.

1. Open the PDF document.
1. Create a FormEditor object.
1. Insert text fields, list boxes, and buttons with AddField() and AddSubmitBtn().
1. Add or delete list items, move fields, rename fields, and remove fields.
1. Reset visual attributes, set alignment, appearance, and field attributes (e.g., ReadOnly).
1. Set character limits for text fields.
1. Save the updated PDF.

```python

import os
import clr

# Add references to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades
from Aspose.Pdf.Annotations import AnnotationFlags

def exploring_form_editor_features():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open PDF document
    document = pdf.Document(os.path.join(data_dir, "inFile.pdf"))

    # Create instance of FormEditor
    editor = pdf_facades.FormEditor(document)

    # Add a text field
    editor.AddField(pdf_facades.FieldType.Text, "field1", 1, 300, 500, 350, 525)

    # Add a list box field
    editor.AddField(pdf_facades.FieldType.ListBox, "field2", 1, 300, 200, 350, 225)

    # Add list items
    editor.AddListItem("field2", "item 1")
    editor.AddListItem("field2", "item 2")

    # Add a submit button
    editor.AddSubmitBtn("submitbutton", 1, "Submit Form", "http://Testwebsite.com/testpage", 200, 200, 250, 225)

    # Delete a list item
    editor.DelListItem("field2", "item 1")

    # Move field to new position
    editor.MoveField("field1", 10, 10, 50, 50)

    # Remove existing field
    editor.RemoveField("field1")

    # Rename field
    editor.RenameField("field1", "newfieldname")

    # Reset all visual attributes
    editor.ResetFacade()

    # Set alignment style of a text field
    editor.SetFieldAlignment("field1", pdf_facades.FormFieldFacade.AlignLeft)

    # Set appearance of the field
    editor.SetFieldAppearance("field1", AnnotationFlags.NoRotate)

    # Set field attribute (e.g., ReadOnly)
    editor.SetFieldAttribute("field1", pdf_facades.PropertyFlag.ReadOnly)

    # Set field character limit
    editor.SetFieldLimit("field1", 25)

    # Save modifications
    editor.Save(os.path.join(data_dir, "FormEditorFeatures2_out.pdf"))

    # Dispose resources
    editor.Dispose()
    document.Dispose()

    print("FormEditor features demonstrated successfully.")
```