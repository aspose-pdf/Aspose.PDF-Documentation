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


    path_infile = self.data_dir + "DynamicXFAToAcroForm.pdf.pdf"
    path_outfile = self.data_dir + "StandardAcroForm_out.pdf"

    # Load dynamic XFA form
    with ap.Document(path_infile) as document:
        # Set the form fields type as standard AcroForm
        document.form.type = ap.forms.FormType.STANDARD
        # Save PDF document
        document.save(path_outfile)
```

## Use of IgnoreNeedsRendering

This example demonstrates how to convert a dynamic XFA form to a standard AcroForm using Aspose.PDF for Python. The code checks if the input PDF contains an XFA form and overrides rendering if necessary. It then sets the form type to STANDARD and saves the updated PDF.

```python

    import aspose.pdf as ap


    path_infile = self.data_dir + "DynamicXFAToAcroForm.pdf.pdf"
    path_outfile = self.data_dir + "StandardAcroForm_out.pdf"

    # Load dynamic XFA form
    with ap.Document(path_infile) as document:
        # check if XFA is present & if rendering should be overwritten
        if not document.form.needs_rendering and document.form.has_xfa:
            document.form.ignore_needs_rendering = True
        # Set the form fields type as standard AcroForm
        document.form.type = ap.forms.FormType.STANDARD
        # Save the resultant PDF
        document.save(path_outfile)
```
