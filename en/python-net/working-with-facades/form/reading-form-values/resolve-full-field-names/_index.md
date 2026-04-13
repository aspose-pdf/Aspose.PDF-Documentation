---
title: Resolve Full Field Names
type: docs
weight: 60
url: /python-net/resolve-full-field-names/
description: This example demonstrates how to retrieve the fully qualified names of form fields in a PDF document using Aspose.PDF Facades API.
lastmod: "2026-02-19"
---

In PDF forms, fields can be organized hierarchically, especially when subforms are used. Each field has a short name and a fully qualified name. The fully qualified name represents the complete path of the field within the form hierarchy and is required by many API methods that manipulate or read form data.

1. Create a Form Object.
1. Bind the PDF Document.
1. Access all form field names.
1. Each field's fully qualified name is resolved using get_full_field_name().

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Resolve full field names
def resolve_full_field_names(infile):
    """Resolve full field names in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Resolve full field names
    for field in pdf_form.field_names:
        name = pdf_form.get_full_field_name(field)
        print(f"Full field name: {name}")
```
