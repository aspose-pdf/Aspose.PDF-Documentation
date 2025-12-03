---
title: Get Viewer Preference of PDF File
type: docs
weight: 70
url: /python-net/get-viewer-preference-of-an-existing-pdf-file/
description: This section shows how to get viewer preference of an existing PDF file using PdfContentEditor Class.
lastmod: "2025-11-05"
---

## Get Viewer Preference of an existing PDF File

Viewer Preferences in a PDF define how the document behaves when opened in a PDF viewer—such as whether the window is centered, if toolbars are hidden, if the document opens in full-screen mode, and more. Using Aspose.PDF for Python via .NET, you can easily access and evaluate these preferences programmatically.

1. Open the PDF document.
1. Create an instance of PdfContentEditor to manage viewer preferences.
1. Call GetViewerPreference() to obtain the preference flags.
1. Check specific preferences:
    - CenterWindow
    - HideMenubar
    - PageModeFullScreen
1. Print the active preferences to the console.

```python

import os
import clr

# Add reference to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades

def get_viewer_preference():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open PDF document
    document = pdf.Document(os.path.join(data_dir, "SetViewerPreference.pdf"))

    # Instantiate PdfContentEditor object
    editor = pdf_facades.PdfContentEditor(document)

    # Get Viewer Preferences
    preferences = editor.GetViewerPreference()

    # Check specific preferences
    if (preferences & pdf_facades.ViewerPreference.CenterWindow) != 0:
        print("CenterWindow")

    if (preferences & pdf_facades.ViewerPreference.HideMenubar) != 0:
        print("Menu bar hidden")

    if (preferences & pdf_facades.ViewerPreference.PageModeFullScreen) != 0:
        print("Page Mode Full Screen")

    # Dispose resources
    editor.Dispose()
    document.Dispose()

    print("Viewer preferences retrieved successfully.")
```