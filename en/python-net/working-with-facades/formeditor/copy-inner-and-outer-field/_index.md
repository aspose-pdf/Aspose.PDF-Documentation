---
title: Copy Inner and Outer Field
type: docs
weight: 60
url: /python-net/copy-inner-and-outer-field/
description: This section explains how to copy Inner and Outer Field with Aspose.PDF Facades using FormEditor Class.
lastmod: "2025-11-05"
---

## Copy an existing Form Field from one page of a PDF to another

[copy_inner_field()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/#methods) method allows you to copy a field in the same file, at the same coordinates, on the specified page. This method requires the field name which you want to copy, the new field name, and the page number at which the field needs to be copied. [FormEditor](https://reference.aspose.com/html/python-net/aspose.html.forms/formeditor) class provides this method. The following code snippet shows you how to copy the field at the same location in the same file.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades

def copy_inner_field():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open PDF document
    document = pdf.Document(os.path.join(data_dir, "Sample-Form-01.pdf"))

    # Add a new blank page to the document
    document.Pages.Add()

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Bind PDF document
    form_editor.BindPdf(document)

    # Copy the field "Last Name" from the first page to "Last Name 2" on the second page
    form_editor.CopyInnerField("Last Name", "Last Name 2", 2)

    # Save modified PDF document
    form_editor.Save(os.path.join(data_dir, "Sample-Form-01-mod.pdf"))

    # Dispose resources
    form_editor.Dispose()
    document.Dispose()

    print("Field 'Last Name' copied successfully to page 2 as 'Last Name 2'.")
```

## Copy Outer Field in an Existing PDF File

[copy_outer_field](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/#methods) method allows you to copy a form field from an external PDF file and then add it to the input PDF file at the same location and the specified page number. This method requires the PDF file from which the field needs to be copied, the field name, and the page number at which the field needs to be copied. This method is provided by [FormEditor](https://reference.aspose.com/html/python-net/aspose.html.forms/formeditor) class.The following code snippet shows you how to copy a field from an external PDF file.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades

def copy_outer_field():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create empty PDF document
    document = pdf.Document()

    # Add a new blank page
    document.Pages.Add()

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Bind the new PDF document
    form_editor.BindPdf(document)

    # Copy the outer field "First Name" from the original document to the new document
    form_editor.CopyOuterField(os.path.join(data_dir, "Sample-Form-01.pdf"), "First Name", 1)

    # Copy the outer field "Last Name" from the original document to the new document
    form_editor.CopyOuterField(os.path.join(data_dir, "Sample-Form-01.pdf"), "Last Name", 1)

    # Save the modified PDF document
    form_editor.Save(os.path.join(data_dir, "Sample-Form-02-mod.pdf"))

    # Dispose resources
    form_editor.Dispose()
    document.Dispose()

    print("Outer fields 'First Name' and 'Last Name' copied successfully into new PDF.")
```


