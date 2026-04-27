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
import aspose.pydrawing as drawing

def add_text_box_field(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    rectangle = ap.Rectangle(10, 600, 110, 620, True)
    text_box_field = ap.forms.TextBoxField(page, rectangle)
    text_box_field.partial_name = "textbox1"
    text_box_field.value = "Text Box"

    text_box_field.default_appearance = ap.annotations.DefaultAppearance(
        "Arial", 10, drawing.Color.dark_blue
    )

    border = ap.annotations.Border(text_box_field)
    border.width = 1
    border.style = ap.annotations.BorderStyle.DASHED
    border.dash = ap.annotations.Dash(3, 3)
    text_box_field.border = border

    text_box_field.characteristics.border = ap.Color.red.to_rgb()
    text_box_field.characteristics.background = ap.Color.yellow.to_rgb()

    document.form.add(text_box_field, 1)
    document.save(output_file_name)
```

### Multi-Widget Text Box Field in PDF

Create a text box form field with multiple widget appearances in a PDF using Python and Aspose.PDF. It places several text input areas on a page, applies different fonts and colors to each widget, customizes borders, and sets background styling for an interactive PDF form.

1. Create New PDF Document.
1. Define Text Field Positions.
1. Create Different Default Appearances.
1. Create Text Box Field.
1. Apply Appearance to Each Widget.
1. Customize Border Style.
1. Add Field to Form.
1. Save PDF File.

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_text_box_field_nt(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    rects = [
        ap.Rectangle(10, 600, 110, 620, normalize_coordinates=True),
        ap.Rectangle(10, 630, 110, 650, normalize_coordinates=True),
        ap.Rectangle(10, 660, 110, 680, normalize_coordinates=True),
    ]

    default_appearances = [
        ap.annotations.DefaultAppearance("Arial", 10, drawing.Color.dark_blue),
        ap.annotations.DefaultAppearance("Helvetica", 12, drawing.Color.dark_green),
        ap.annotations.DefaultAppearance(
            ap.text.FontRepository.find_font("Calibri"), 14, drawing.Color.dark_magenta
        ),
    ]

    text_box_field = ap.forms.TextBoxField(page, rects)
    text_box_field.partial_name = "textbox1"
    text_box_field.value = "Some text"

    for i, widget in enumerate(text_box_field):
        widget.default_appearance = default_appearances[i]

    border = ap.annotations.Border(text_box_field)
    border.width = 1
    border.style = ap.annotations.BorderStyle.DASHED
    border.dash = ap.annotations.Dash(3, 3)
    text_box_field.border = border

    text_box_field.characteristics.border = ap.Color.red.to_rgb()
    text_box_field.characteristics.background = ap.Color.yellow.to_rgb()

    document.form.add(text_box_field)
    document.save(output_file_name)
```

## Adding Other Form Fields

The following code snippets shows how to add various types of form fields, such as radio buttons, combo boxes, checkboxes, list boxes, signature fields, and barcode fields, to a PDF document using the Aspose.PDF library for Python. Each function creates a new PDF document, adds a specific form field with defined properties and options, and saves the modified document with the new form field included.

1. Add Radio Button Field
1. Add Combo Box Field
1. Add Checkbox Field
1. Add List Box Field
1. Add Signature Field
1. Add Barcode Field

### Add Radio Button Field

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_radio_button(output_file_name):
    document = ap.Document()
    document.pages.add()

    radio = ap.forms.RadioButtonField(document.pages[1])
    radio.add_option(
        "Option 1", ap.Rectangle(100, 640, 120, 680, normalize_coordinates=True)
    )
    radio.add_option(
        "Option 2", ap.Rectangle(140, 640, 160, 680, normalize_coordinates=True)
    )

    document.form.add(radio)
    document.save(output_file_name)
```

### Add Combo Box Field

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_combo_box(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    combo = ap.forms.ComboBoxField(
        page, ap.Rectangle(100, 640, 150, 656, normalize_coordinates=True)
    )
    combo.add_option("Red")
    combo.add_option("Yellow")
    combo.add_option("Green")
    combo.add_option("Blue")
    combo.selected = 3

    document.form.add(combo)
    document.save(output_file_name)
```

### Add Checkbox Field

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_checkbox_field_to_pdf(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    checkbox = ap.forms.CheckboxField(
        page, ap.Rectangle(50, 620, 100, 650, normalize_coordinates=True)
    )
    checkbox.characteristics.background = ap.Color.aqua.to_rgb()
    checkbox.style = ap.forms.BoxStyle.CIRCLE

    document.form.add(checkbox)
    document.save(output_file_name)
```

### Add List Box Field

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_list_box_field_to_pdf(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    list_box = ap.forms.ListBoxField(
        page, ap.Rectangle(50, 650, 100, 700, normalize_coordinates=True)
    )
    list_box.partial_name = "list"
    list_box.add_option("Red")
    list_box.add_option("Green")
    list_box.add_option("Blue")

    document.form.add(list_box)
    document.save(output_file_name)
```

### Add Signature Field

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_signature_field(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    signature_field = ap.forms.SignatureField(
        page, ap.Rectangle(100, 700, 200, 800, True)
    )
    signature_field.partial_name = "Signature1"
    document.form.add(signature_field)
    document.save(output_file_name)
```

### Add Barcode Field

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_barcode_field(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    barcode = ap.forms.BarcodeField(page, ap.Rectangle(100, 700, 200, 740, True))
    barcode.partial_name = "Barcode1"
    barcode.add_barcode("1234567890")
    document.form.add(barcode)
    document.save(output_file_name)
```
