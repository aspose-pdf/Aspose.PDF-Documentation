---
title: Fill AcroForm - Fill PDF Form using Python
linktitle: Fill AcroForm
type: docs
weight: 20
url: /python-net/fill-form/
description: Fill AcroForm fields in a PDF document by using Aspose.PDF for Python via .NET.
lastmod: "2026-04-28"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to fill form field in PDF using Python
Abstract: This article explains how to fill AcroForm fields in a PDF document by using Aspose.PDF for Python via .NET. The example uses the Form facade, maps field names to new values in a dictionary, updates matching fields, and saves the output PDF. This approach is useful for automated document completion workflows and bulk form processing.
---

## Fill Form Field in a PDF Document

The following example fills multiple fields in an existing PDF form by using the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade.

Use the following steps:

1. Create a dictionary with field names and values.
1. Bind the input PDF to a Form object.
1. Iterate through available form fields.
1. Fill fields that exist in the dictionary.
1. Save the updated PDF.

```python
import aspose.pdf as ap

def fill_form(input_file_name, output_file_name):
    new_field_values = {
        "First Name": "Alexander_New",
        "Last Name": "Greenfield_New",
        "City": "Yellowtown_New",
        "Country": "Redland_New",
    }

    form = ap.facades.Form(input_file_name)

    for field_name in form.field_names:
        if field_name in new_field_values:
            form.fill_field(field_name, new_field_values[field_name])

    form.save(output_file_name)
```

## Related Topics

- [Create AcroForm](/pdf/python-net/create-form/)
- [Extract AcroForm](/pdf/python-net/extract-form/)
- [Import and Export Form Data](/pdf/python-net/import-export-form-data/)