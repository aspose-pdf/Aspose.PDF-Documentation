---
title: Rename Field
type: docs
weight: 70
url: /python-net/rename-field/
description: Rename an existing form field in a PDF document using Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Rename a PDF Form Field Using Python
Abstract: This example demonstrates how to rename an existing form field in a PDF document using Aspose.PDF for Python. The code opens an input PDF, changes the name of a specified form field using the FormEditor class, and saves the updated document.    
---

PDF forms often rely on field names for scripting, automation, and data processing. Using Aspose.PDF for Python, developers can rename existing fields without recreating them or altering the form layout.

The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class provides the 'rename_field' method, which allows developers to change the name of an existing field while preserving its position, value, and appearance.

1. Load the existing PDF form.
1. Create a FormEditor instance.
1. Bind the PDF document to the editor.
1. Rename the target field.
1. Save the updated PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def rename_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Rename field in document
    form_editor.rename_field("City", "Town")
    # Save updated document
    form_editor.save(outfile)
```

