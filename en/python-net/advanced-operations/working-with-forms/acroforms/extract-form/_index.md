---
title: Extract AcroForm - Extract Form Data from PDF in Python
linktitle: Extract AcroForm
type: docs
weight: 30
url: /python-net/extract-form/
description: Extract values from AcroForm fields in PDF documents by using Aspose.PDF for Python via .NET.
lastmod: "2026-04-28"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to get Form Data from PDF using Python
Abstract: This article shows how to extract data from AcroForm fields in PDF documents by using Aspose.PDF for Python via .NET. The example iterates through form field names, reads values by using the Form facade, and returns a dictionary for downstream processing. This workflow is useful for reporting, validation, and integration with external systems.
---

## Extract Data from Form

### Get Values from All Fields in a PDF Document

To read values from all fields in a PDF document, iterate through the form field names and retrieve each value from the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade.

Use the following steps:

1. Bind the input PDF to a `Form` object.
1. Iterate through `field_names`.
1. Read each value with `get_field()`.
1. Store values in a dictionary.
1. Return or process the extracted values.

The following Python code snippet shows this approach.

```python
import aspose.pdf as ap


def get_values_from_all_fields(input_file_name):
    form = ap.facades.Form(input_file_name)

    form_values = {}
    for field_name in form.field_names:
        form_values[field_name] = form.get_field(field_name)

    print(form_values)
    return form_values
```

## Related Topics

- [Create AcroForm](/pdf/python-net/create-form/)
- [Fill AcroForm](/pdf/python-net/fill-form/)
- [Import and Export Form Data](/pdf/python-net/import-export-form-data/)
- [Modifying AcroForm](/pdf/python-net/modifying-form/)