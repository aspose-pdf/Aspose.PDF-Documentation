---
title: Get Button Option Value
type: docs
weight: 40
url: /python-net/get-button-option-value/
description: This section explains how to get Button Option Value with Aspose.PDF Facades using Form Class.
lastmod: "2025-11-05"
---

## Get Button Option Values from an Existing PDF File

Retrieve option values from a button field, such as a radio button group, in a PDF form using Aspose.PDF for Python via .NET. By binding a PDF document to the Form class and calling GetButtonOptionValues(), developers can access the available choices for a specific field. Iterating through the returned collection allows you to examine each option’s key and value, making it easy to validate form design or process user selections dynamically.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def get_button_options():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.BindPdf(os.path.join(data_dir, "FormField.pdf"))

    # Get button option values for the "Gender" field
    option_values = pdf_form.GetButtonOptionValues("Gender")

    # Iterate through option values
    enumerator = option_values.GetEnumerator()
    while enumerator.MoveNext():
        print(f"Key : {enumerator.Key}, Value : {enumerator.Value}")

    # Dispose form object
    pdf_form.Dispose()

# Example usage
get_button_options()
```

## Get Current Button Option Value from an Existing PDF File

Retrieve the currently selected option value from a button field (such as a radio button group) in a PDF form. By binding a PDF document to the Form class and calling [get_button_option_current_value()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/#methods), developers can determine which option is active for a given field. This is useful for validating user input, processing form submissions, or dynamically reading form data.

1. Create a Form object.
1. Bind the target PDF form with BindPdf().
1. Call GetButtonOptionCurrentValue("Gender") to retrieve the selected option.
1. Print or process the retrieved value.
1. Dispose of the form object to release resources.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def get_current_button_option_value():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.BindPdf(os.path.join(data_dir, "FormField.pdf"))

    # Get current value of the "Gender" button field
    option_value = pdf_form.GetButtonOptionCurrentValue("Gender")

    # Display result
    print(f"Current Value : {option_value}")

    # Dispose form object
    pdf_form.Dispose()

# Example usage
get_current_button_option_value()
```