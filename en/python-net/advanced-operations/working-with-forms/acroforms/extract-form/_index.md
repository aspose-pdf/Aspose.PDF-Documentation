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

    # Construct the full path to the input PDF file
    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)

    # Create a Form object from the PDF file
    form = ap.facades.Form(path_infile)

    # Initialize an empty dictionary to store form values
    form_values = {}

    # Iterate through all form fields in the PDF
    for formField in form.field_names:
        # Retrieve the value for each form field and store in the dictionary
        form_values[formField] = form.get_field(formField)

    # Print and return the extracted form values
    print(form_values)
```

