---
title: Working with XFA Forms
linktitle: XFA Forms
type: docs
weight: 20
url: /python-net/xfa-forms/
description: Aspose.PDF for Python via .NET API lets you work with XFA and XFA Acroform fields in a PDF document.
lastmod: "2025-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Convert XFA-to-Acroform

{{% alert color="primary" %}}

Try online
You can check the quality of Aspose.PDF conversion and view the results online at this link: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

The next code snippet demonstrates how to convert a dynamic XFA (XML Forms Architecture) form to a standard AcroForm.

**Key steps include:**

1. Loading the input PDF document.
1. Changing the form type to STANDARD.
1. Saving the converted PDF to a new file.

This conversion allows for better compatibility and consistent form handling across different PDF readers and applications.

```python
import aspose.pdf as ap
import sys
from os import path

def convert_dynamic_xfa_to_acroform(infile: str, outfile: str):
    """Convert dynamic XFA form to standard AcroForm."""
    with ap.Document(infile) as document:
        document.form.type = ap.forms.FormType.STANDARD
        document.save(outfile)
```

## Use of IgnoreNeedsRendering

This example demonstrates how to convert a dynamic XFA form to a standard AcroForm using Aspose.PDF for Python. The code checks if the input PDF contains an XFA form and overrides rendering if necessary. It then sets the form type to STANDARD and saves the updated PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def convert_xfa_form_with_ignore_needs_rendering(infile: str, outfile: str):
    """Convert XFA form ignoring needs rendering flag."""
    with ap.Document(infile) as document:
        if not document.form.needs_rendering and document.form.has_xfa:
            document.form.ignore_needs_rendering = True
        document.form.type = ap.forms.FormType.STANDARD
        document.save(outfile)
```
