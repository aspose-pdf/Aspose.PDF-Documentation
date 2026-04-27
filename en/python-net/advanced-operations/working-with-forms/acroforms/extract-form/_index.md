---
title: Extract AcroForm - Extract Form Data from PDF in Python
linktitle: Extract AcroForm
type: docs
weight: 30
url: /python-net/extract-form/
description: Extract form from your PDF document with Aspose.PDF for Python library. Get value from an individual field of PDF file.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to get Form Data from PDF using Python
Abstract: This article provides a guide on extracting data from form fields within a PDF document using Python. It describes how to navigate through all the fields using the Aspose.PDF library, specifically by accessing the `Form` collection and utilizing the `Field` type and its `value` property. A sample Python code snippet is included, demonstrating how to open a PDF document, iterate through its form fields, and print each field's name and value. This method is useful for programmatically retrieving form data from PDF files.
---

## Extract data from form

### Get Values from all the Fields of PDF Document

To get values from all the fields in a PDF document, you need to navigate through all the form fields and then get the value using the Value property. Get each field from the Form collection, in the base field type called [Field](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/) and access its [value](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/#properties) property.

The following Python code snippets show how to get the values of all the fields from a PDF document.

```python
import aspose.pdf as ap
import sys
from os import path

def get_values_from_all_fields(input_file_name):
    form = ap.facades.Form(input_file_name)

    form_values = {}
    for field_name in form.field_names:
        form_values[field_name] = form.get_field(field_name)

    print(form_values)
    return form_values
```
