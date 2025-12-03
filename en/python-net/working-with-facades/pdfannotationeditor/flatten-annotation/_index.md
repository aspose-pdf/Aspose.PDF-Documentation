---
title: Flatten Annotation from PDF to XFDF 
type: docs
weight: 40
url: /python-net/flatten-annotation/
description: This section explains how to export annotations from PDF file to XFDF with Aspose.PDF Facades.
lastmod: "2025-11-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Flattening annotations means converting interactive elements (like comments, highlights, buttons, or redactions) into static content so they can no longer be edited or interacted with.

1. Create PdfAnnotationEditor.
1. Attach the input PDF file with BindPdf().
1. Configure options such as:
    - Apply redaction annotations permanently.
    - Disable event triggers.
    - Hide interactive buttons.
    - Refresh annotation appearances before flattening.
1. Use FlatteningAnnotations() with the defined settings.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades
from Aspose.Pdf.Forms import Form

def flatten_annotation_from_pdf():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create PdfAnnotationEditor
    annotation_editor = pdf_facades.PdfAnnotationEditor()

    # Bind PDF document
    annotation_editor.BindPdf(os.path.join(data_dir, "AnnotationsInput.pdf"))

    # Create FlattenSettings
    flatten_settings = Form.FlattenSettings()
    flatten_settings.ApplyRedactions = True
    flatten_settings.CallEvents = False
    flatten_settings.HideButtons = True
    flatten_settings.UpdateAppearances = True

    # Flatten annotations with the specified settings
    annotation_editor.FlatteningAnnotations(flatten_settings)

    # Save updated PDF document
    annotation_editor.Save(os.path.join(data_dir, "FlattenAnnotation_out.pdf"))

    # Dispose resources
    annotation_editor.Dispose()

    print("Annotations flattened successfully into the PDF.")
```
