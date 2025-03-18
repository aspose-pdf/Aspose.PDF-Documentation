---
title: Extract AcroForm - Extract Form Data from PDF in Python
linktitle: Extract AcroForm
type: docs
weight: 30
url: /python-net/extract-form/
description: Extract form from your PDF document with Aspose.PDF for Python library. Get value from an individual field of PDF file.
lastmod: "2025-02-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Guide on extracting AcroForm data from PDF documents using Python
Abstract: The article, authored and published by the Aspose.PDF Doc Team, provides a beginner-level guide on extracting AcroForm data from PDF documents using Python. It focuses on utilizing the Aspose.PDF for Python library to navigate through form fields and retrieve their values. The article includes a practical code snippet demonstrating the process of accessing and printing the names and values of all fields in a PDF document. This guide is part of the broader topic of PDF document generation and manipulation, and it highlights the functionality of the Aspose.PDF for Python library, which is available for various operating systems and can be downloaded from the provided link.
---

## Extract data from form

### Get Values from all the Fields of PDF Document

To get values from all the fields in a PDF document, you need to navigate through all the form fields and then get the value using the Value property. Get each field from the Form collection, in the base field type called [Field](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/) and access its [value](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/#properties) property.

The following Python code snippets show how to get the values of all the fields from a PDF document.

```python

    import aspose.pdf as ap

    # Open document
    pdfDocument = ap.Document(input_file)

    # Get values from all fields
    for formField in pdfDocument.form.fields:
        # Analyze names and values if need
        print("Field Name : " + formField.partial_name)
        print("Value : " + str(formField.value))
```

