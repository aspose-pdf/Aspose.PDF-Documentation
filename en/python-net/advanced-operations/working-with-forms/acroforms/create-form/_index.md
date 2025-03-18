---
title: Create AcroForm - Create Fillable PDF in Python
linktitle: Create AcroForm
type: docs
weight: 10
url: /python-net/create-form/
description: With Aspose.PDF for Python you may create a form from scratch in your PDF file
lastmod: "2025-02-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Guide to generating forms within PDF documents using Python
Abstract: The article titled "Create AcroForm in Python", published by Aspose.PDF Doc Team, serves as a beginner's guide to generating forms within PDF documents using Python. The article focuses on leveraging the Aspose.PDF for Python library to create AcroForm fields from scratch. It specifically details the process of adding a `TextBoxField` to a PDF document, illustrating this with a Python code example. The guide begins by explaining the use of the `Document` class and its `Form` collection, which facilitates form field management in a PDF. Subsequently, it demonstrates how to create a `TextBoxField`, configure its properties such as size, position, border, and color, and finally add it to the document. The modified document is then saved, completing the form creation process. This tutorial provides a practical introduction for those interested in PDF document generation using Python, supported by the Aspose.PDF library.
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

