---
title: Justify Text in a Textbox Field
type: docs
weight: 20
url: /python-net/justify-text-in-a-textbox-field/
description: This article shows you how to Justify Text in a Textbox Field using Form Class.
lastmod: "2025-11-05"
---

## Implementation details

Fill a text field in a PDF form and justify its alignment. The workflow first fills a text field with content, saves the PDF into a memory stream, and then uses the FormEditor class to apply justified alignment to the text field. Finally, the updated PDF is saved to disk.

1. Open the PDF document.
1. Initialize the PDF form handler.
1. Bind the PDF document.
1. Use FillField() to insert text into the target field.
1. Save to memory stream.
1. Initialize the editor to modify field properties.
1. Load the updated PDF into the editor.
1. Apply FormFieldFacade.AlignJustified to the field.
1. Call DecorateField() and save the final PDF to disk.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades
from System.IO import FileStream, FileMode, MemoryStream, SeekOrigin

def justify_text_in_textbox_field():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open PDF document as stream
    source = FileStream(os.path.join(data_dir, "JustifyText.pdf"), FileMode.Open)

    # Create a memory stream to hold intermediate PDF
    ms = MemoryStream()

    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.BindPdf(source)

    # Fill text field
    form.FillField("Text1", "Thank you for using Aspose")

    # Save PDF document into memory stream
    form.Save(ms)
    ms.Seek(0, SeekOrigin.Begin)

    # Create destination file stream
    dest = FileStream(os.path.join(data_dir, "JustifyText_out.pdf"), FileMode.Create)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open PDF from memory stream
    form_editor.BindPdf(ms)

    # Set text alignment to Justified
    form_editor.Facade.Alignment = pdf_facades.FormFieldFacade.AlignJustified

    # Decorate the form field
    form_editor.DecorateField()

    # Save updated PDF
    form_editor.Save(dest)

    # Dispose resources
    source.Close()
    ms.Close()
    dest.Close()
    form.Dispose()
    form_editor.Dispose()

    print("Text field filled and justified successfully.")
```
