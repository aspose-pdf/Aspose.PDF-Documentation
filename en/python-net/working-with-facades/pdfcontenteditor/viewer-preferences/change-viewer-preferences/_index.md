---
title: Change PDF Viewer Preferences
type: docs
weight: 10
url: /python-net/change-viewer-preferences/
description: This module demonstrates how to adjust a PDF document’s viewer settings using Aspose.PDF for Python. 
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Customize PDF Viewer Experience with Python
Abstract: Control how your PDF document appears when opened by modifying viewer preferences programmatically. This functionality allows you to tailor the user interface and layout, ensuring a consistent viewing experience.    
---

PDF files have built-in viewer preferences that control aspects like page layout, toolbar visibility, and window behavior. Using this script, you can:

- Inspect the current viewer preferences of a PDF.
- Modify layout options (e.g., single-page, one-column, two-column).
- Toggle UI elements such as toolbar, menu bar, or title display.
- Save the PDF with the updated preferences for a controlled viewing experience.

1. Define ViewerPreference Flags.
1. Get Current Viewer Preferences.
1. Modify Preferences.
1. Apply Updated Preferences.
1. Save the PDF.

```python
import aspose.pdf.facades as pdf_facades
import sys
from enum import IntFlag
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

# Define ViewerPreference flags
class ViewerPreference(IntFlag):
    HIDE_TOOLBAR = 1
    HIDE_MENUBAR = 2
    HIDE_WINDOW_UI = 4
    FIT_WINDOW = 8
    CENTER_WINDOW = 16
    DISPLAY_DOC_TITLE = 32
    NON_FULL_SCREEN_PAGE_MODE_USE_NONE = 64
    NON_FULL_SCREEN_PAGE_MODE_USE_OUTLINES = 128
    NON_FULL_SCREEN_PAGE_MODE_USE_THUMBS = 256
    NON_FULL_SCREEN_PAGE_MODE_USE_OC = 512
    DIRECTION_L2R = 1024
    DISPLAY_DOC_TITLE_IN_TITLE_BAR = 2048
    PAGE_LAYOUT_SINGLE_PAGE = 4096
    PAGE_LAYOUT_ONE_COLUMN = 8192
    PAGE_LAYOUT_TWO_COLUMN_LEFT = 16384
    PAGE_LAYOUT_TWO_COLUMN_RIGHT = 32768
    PAGE_LAYOUT_TWO_PAGE_LEFT = 65536
    PAGE_LAYOUT_TWO_PAGE_RIGHT = 131072

def change_viewer_preferences(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Get current viewer preference and toggle single-page layout
    current_preference = ViewerPreference(content_editor.get_viewer_preference())
    updated_preference = current_preference | ViewerPreference.PAGE_LAYOUT_SINGLE_PAGE
    content_editor.change_viewer_preference(int(updated_preference))

    # Save updated document
    content_editor.save(outfile)
```