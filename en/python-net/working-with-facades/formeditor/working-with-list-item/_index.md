---
title: Working with List Item
type: docs
weight: 50
url: /python-net/working-with-list-item/
description: This section explains how to work with List Item with Aspose.PDF Facades using FormEditor Class.
lastmod: "2025-11-05"
---

## Add List Item in an Existing PDF File

Add a ListBox field and populate it with items in a PDF form. The FormEditor class allows developers to insert interactive fields and configure their options programmatically.

1. Create a FormEditor object.
1. Attach the input PDF file with BindPdf().
1. Use AddField() to insert a ListBox at specified coordinates.
1. Use AddListItem() to populate the ListBox with selectable options (e.g., USA, Canada, France, Spain).
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def add_list_item():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create an instance of FormEditor to manipulate form fields
    form_editor = pdf_facades.FormEditor()

    # Bind PDF document
    form_editor.BindPdf(os.path.join(data_dir, "Sample-Form-01.pdf"))

    # Add a ListBox field for selecting country, placed at the specified coordinates on page 1
    form_editor.AddField(
        pdf_facades.FieldType.ListBox,
        "Country",
        1,
        232.56, 476.75, 352.28, 514.03
    )

    # Add list items to the 'Country' ListBox field
    form_editor.AddListItem("Country", "USA")
    form_editor.AddListItem("Country", "Canada")
    form_editor.AddListItem("Country", "France")
    form_editor.AddListItem("Country", "Spain")

    # Save modified PDF document
    form_editor.Save(os.path.join(data_dir, "Sample-Form-01-mod.pdf"))

    # Dispose resources
    form_editor.Dispose()

    print("ListBox 'Country' added successfully with items: USA, Canada, France, Spain.")
```

## Delete List Item from an Existing PDF File

Remove a specific item from a ListBox field in a PDF form. The FormEditor class provides methods to manipulate form fields, including adding, deleting, and updating list items.

1. Create a FormEditor object.
1. Attach the input PDF file with BindPdf().
1. Use DelListItem() to remove the specified option (e.g., "France") from the ListBox field ("Country").
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def del_list_item():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create an instance of FormEditor to manipulate form fields
    form_editor = pdf_facades.FormEditor()

    # Bind PDF document
    form_editor.BindPdf(os.path.join(data_dir, "Sample-Form-04.pdf"))

    # Delete the list item "France" from the 'Country' ListBox field
    form_editor.DelListItem("Country", "France")

    # Save modified PDF document
    form_editor.Save(os.path.join(data_dir, "Sample-Form-04-mod.pdf"))

    # Dispose resources
    form_editor.Dispose()

    print("List item 'France' removed successfully from the 'Country' ListBox field.")
```
