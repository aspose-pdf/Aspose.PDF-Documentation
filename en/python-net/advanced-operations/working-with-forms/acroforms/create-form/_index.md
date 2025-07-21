---
title: Create AcroForm - Create Fillable PDF in Python
linktitle: Create AcroForm
type: docs
weight: 10
url: /python-net/create-form/
description: With Aspose.PDF for Python you may create a form from scratch in your PDF file
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to create AcroForm in PDF using Python
Abstract: The article provides a guide on how to create a form field in a PDF document using the Aspose.PDF library for Python. It introduces the `Document` class, which contains a `Form` collection for managing form fields. The process to add a form field involves creating the desired field and utilizing the `add` method from the `Form` collection. A specific example is provided to illustrate adding a `TextBoxField` to a PDF document. The example includes detailed code demonstrating the creation of a `TextBoxField`, setting its properties such as position, name, value, border, and color, and subsequently adding it to the document. The modified PDF is then saved with the newly added form field.
---

## Create form from scratch

### Add Form Field in a PDF Document

The [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class provides a collection named [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) which helps you manage form fields in a PDF document.

To add a form field:

1. Create the form field you want to add.
1. Call the Form collection's [add](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/#methods) method.

### Adding TextBoxField

Below example shows how to add a [TextBoxField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).

```python

    import aspose.pdf as ap

    # Open document
    pdfDocument = ap.Document(input_file)

    # Create a field
    textBoxField = ap.forms.TextBoxField(pdfDocument.pages[1], ap.Rectangle(100, 200, 300, 300, True))
    textBoxField.partial_name = "textbox1"
    textBoxField.value = "Text Box"

    border = ap.annotations.Border(textBoxField)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    textBoxField.border = border

    textBoxField.color = ap.Color.green

    # Add field to the document
    pdfDocument.form.add(textBoxField, 1)

    # Save modified PDF
    pdfDocument.save(output_pdf)
```

