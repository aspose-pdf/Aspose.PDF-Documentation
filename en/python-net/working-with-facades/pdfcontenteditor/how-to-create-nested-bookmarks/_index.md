---
title: Adding Bookmarks to PDF file
type: docs
weight: 20
url: /python-net/how-to-create-nested-bookmarks/
description: This section explains how to create Nested Bookmarks with PdfContentEditor Class.
lastmod: "2025-11-05"
---

Bookmarks give you the option to keep track/link to specific page inside the PDF document. [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/PdfContentEditor) class in [aspose.pdf.facades namespace](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) provides a feature which allows you to create your own bookmark in a sophisticated yet intuitive way within an existing PDF file, at a given page or all pages.

## Implementation details

Bookmarks in a PDF help users quickly navigate through the document. With Aspose.PDF for Python via .NET, you can programmatically create bookmarks and assign actions to them—such as jumping to a specific page when clicked.

Other than the creation of simple bookmarks, sometimes you have a requirement to create a bookmark in the form of chapters where you nest the individual bookmarks inside of the chapter bookmarks so that when you click on the + sign for a chapter you would see the pages inside when the bookmarks expands, as shown in the picture below.

1. Load the input PDF using the Document class.
1. Create an instance of PdfContentEditor to manage bookmarks and actions.
1. Call CreateBookmarksAction(title, color, bold, italic, destination, actionType, pageNumber).
1. Save the updated PDF.

```python

import os
import clr

# Add references to Aspose.PDF and System.Drawing
clr.AddReference("Aspose.PDF")
clr.AddReference("System.Drawing")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades
from System.Drawing import Color

def add_bookmarks_action():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open PDF document
    document = pdf.Document(os.path.join(data_dir, "Sample.pdf"))

    # Instantiate PdfContentEditor object
    editor = pdf_facades.PdfContentEditor(document)

    # Create a bookmark with action
    editor.CreateBookmarksAction(
        "Bookmark 1",     # Bookmark title
        Color.Green,      # Bookmark color
        True,             # Bold
        False,            # Italic
        "",               # Destination (empty string for default)
        "GoTo",           # Action type
        "2"               # Destination page number
    )

    # Save updated PDF document
    editor.Save(os.path.join(data_dir, "PdfContentEditorDemo_Bookmark_out.pdf"))

    # Dispose resources
    editor.Dispose()
    document.Dispose()

    print("Bookmark with action added successfully.")
```
