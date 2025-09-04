---
title: Fill AcroForm - Fill PDF Form using Python
linktitle: Fill AcroForm
type: docs
weight: 20
url: /python-net/fill-form/
description: You can fill forms in your PDF document  with Aspose.PDF for Python library.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to fill form field in PDF using Python
Abstract: The article provides a guide on how to fill a form field in a PDF document using the Aspose.PDF library for Python. It explains the process of accessing a form field from the document's form collection and setting its value via the field's value property. The example code demonstrates how to open a PDF document, iterate through its form fields to find a specific field by its partial name (in this case, "Field 1"), and modify the value of a TextBoxField to "777". Finally, the updated document is saved to an output file. Links to the relevant Aspose documentation are provided for further reference.
---

## Fill Form Field in a PDF Document

The next example fills PDF form fields with new values using Aspose.PDF for Python via .NET and saves the updated document. Supports updating multiple fields by specifying a dictionary of field names and values.

```python

    import aspose.pdf as ap

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    # Define the new field values
    new_field_values = {
        "First Name": "Alexander_New",
        "Last Name": "Greenfield_New",
        "City": "Yellowtown_New",
        "Country": "Redland_New"
    }

    # Create a Form object from the input PDF file
    form = ap.facades.Form(path_infile)

    # Fill out the form fields with the new values
    for formField in form.field_names:
        if formField in new_field_values:
            form.fill_field(formField, new_field_values[formField])

    # Save the modified form to the output PDF file
    form.save(path_outfile)
```


