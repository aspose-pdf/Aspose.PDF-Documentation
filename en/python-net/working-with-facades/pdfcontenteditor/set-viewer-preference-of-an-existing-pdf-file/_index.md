---
title: Set Viewer Preference of PDF 
type: docs
weight: 60
url: /python-net/set-viewer-preference-of-an-existing-pdf-file/
description: This section shows how to set viewer preference of an existing PDF file using PdfContentEditor Class.
lastmod: "2025-11-05"
---

## Set Viewer Preference of an existing PDF File

The Python library demonstrates how to configure viewer preferences in a PDF document. Viewer preferences control how a PDF is displayed when opened in a viewer application—for example, whether the window is centered, menus are hidden, or the document opens in full‑screen mode.

1. Load the input PDF using the Document class.
1. Create an instance of PdfContentEditor to manage viewer preferences.
1. Change viewer preferences. Call ChangeViewerPreference() with the desired options:
    - CenterWindow
    - HideMenubar
    - PageModeFullScreen
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades

def set_viewer_preference():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open PDF document
    document = pdf.Document(os.path.join(data_dir, "Sample.pdf"))

    # Instantiate PdfContentEditor object
    editor = pdf_facades.PdfContentEditor(document)

    # Change Viewer Preferences
    editor.ChangeViewerPreference(pdf_facades.ViewerPreference.CenterWindow)
    editor.ChangeViewerPreference(pdf_facades.ViewerPreference.HideMenubar)
    editor.ChangeViewerPreference(pdf_facades.ViewerPreference.PageModeFullScreen)

    # Save updated PDF document
    editor.Save(os.path.join(data_dir, "PdfContentEditorDemo_SetViewerPreference_out.pdf"))

    # Dispose resources
    editor.Dispose()
    document.Dispose()

    print("Viewer preferences set successfully.")
```
