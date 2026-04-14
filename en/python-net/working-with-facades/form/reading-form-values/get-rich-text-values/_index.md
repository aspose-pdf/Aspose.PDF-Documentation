---
title: Get Rich Text Values
type: docs
weight: 40
url: /python-net/get-rich-text-values/
description: This section explains how to retrieve the rich text content of a form field in a PDF document using Aspose.PDF Facades API. Unlike plain text fields, rich text fields can contain formatted content such as bold text, different fonts, colors, and paragraph styling.
lastmod: "2026-02-19"
---

PDF forms may include text fields that support rich text formatting. These fields can store content with styling attributes in addition to plain text values.

1. Create a Form Object.
1. Bind the PDF Document.
1. Retrieve Rich Text Values.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get rich text values
def get_rich_text_values(infile):
    """Get rich text values from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get rich text values by their names
    field_names = ["Summary"]
    for field_name in field_names:
        rich_text_value = pdf_form.get_rich_text(field_name)
        print(f"Rich text value of '{field_name}': {rich_text_value}")
```
