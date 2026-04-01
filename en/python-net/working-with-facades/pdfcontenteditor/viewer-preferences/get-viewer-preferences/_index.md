---
title: Get PDF Viewer Preferences
type: docs
weight: 20
url: /python-net/get-viewer-preferences/
description: How to read and modify PDF viewer preferences programmatically using Aspose.PDF for Python
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Manage PDF Viewer Preferences with Aspose.PDF in Python
Abstract: This guide demonstrates how to read and modify PDF viewer preferences programmatically using Aspose.PDF for Python. Viewer preferences control how a PDF is displayed when opened in a PDF viewer, such as opening with outlines, hiding toolbars, or using single-page layout.      
---

Aspose.PDF provides tools to access and update PDF viewer preferences. These preferences define the initial layout and presentation behavior of a PDF document in PDF readers. This includes options such as enabling outline view, hiding menu bars, or specifying page layout modes. Using PdfContentEditor, you can retrieve existing preferences, check specific flags, and update them as needed.

1. Define ViewerPreference Flags.
1. Initialize [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) and Bind PDF.
1. Get Current Viewer Preferences.
1. Check Specific Flags.
1. Display Current Preferences.

```python
import aspose.pdf.facades as pdf_facades
import sys
from enum import IntFlag
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def get_viewer_preferences(infile):
	# Create PdfContentEditor object
	content_editor = pdf_facades.PdfContentEditor()
	# Bind document to PdfContentEditor
	content_editor.bind_pdf(infile)
	# Read current viewer preference flags
	viewer_preference = ViewerPreference(content_editor.get_viewer_preference())
	if viewer_preference & ViewerPreference.PAGE_MODE_USE_OUTLINES:
		print("PageModeUseOutlines is enabled")
	print(f"Current viewer preference: {viewer_preference}")
```