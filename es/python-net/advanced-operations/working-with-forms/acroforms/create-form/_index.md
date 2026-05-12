---
title: Crear AcroForm - Crear PDF rellenable en Python
linktitle: Crear AcroForm
type: docs
weight: 10
url: /es/python-net/create-form/
description: Crear campos AcroForm desde cero en documentos PDF utilizando Aspose.PDF for Python via .NET.
lastmod: "2026-04-28"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo crear AcroForm en PDF utilizando Python
Abstract: Este artículo explica cómo crear campos AcroForm en documentos PDF utilizando Aspose.PDF for Python via .NET. Cubre la creación básica de campos con TextBoxField, la personalización de la apariencia de cajas de texto multi‑widget y tipos de campos adicionales como botones de opción, cuadros combinados, casillas de verificación, listas desplegables, campos de firma y campos de código de barras. Estos ejemplos le ayudan a crear formularios PDF interactivos para la recopilación de datos y flujos de trabajo de automatización de documentos.
---

## Crear Formulario desde cero

### Agregar campo de formulario en un documento PDF

El [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) la clase proporciona una colección llamada [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) que le ayuda a gestionar los campos de formulario en un documento PDF.

Para agregar un campo de formulario:

1. Crea el campo de formulario que deseas agregar.
1. Llamar a la colección Form [agregar](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/#methods) método.

### Agregar TextBoxField

El siguiente ejemplo muestra cómo agregar un [Campo de cuadro de texto](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).

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

### Campo de cuadro de texto Multi-Widget en PDF

Crea un campo de formulario de cuadro de texto con múltiples apariencias de widget en un PDF usando Python y Aspose.PDF. Coloca varias áreas de entrada de texto en una página, aplica diferentes fuentes y colores a cada widget, personaliza los bordes y establece estilos de fondo para un formulario PDF interactivo.

1. Crear nuevo documento PDF.
1. Definir posiciones de los campos de texto.
1. Crear diferentes apariencias predeterminadas.
1. Crear campo de cuadro de texto.
1. Aplicar apariencia a cada widget.
1. Personalizar estilo de borde.
1. Agregar campo al formulario.
1. Guardar archivo PDF.

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

## Agregar Other Form Fields

Los siguientes fragmentos de código muestran cómo agregar varios tipos de campos, como botones de opción, cuadros combinados, casillas de verificación, listas desplegables, campos de firma y campos de código de barras. Cada función crea un nuevo documento PDF, agrega un campo objetivo con las opciones seleccionadas y guarda el archivo actualizado.

1. Agregar campo de botón de opción
1. Agregar campo de cuadro combinado
1. Agregar campo de casilla de verificación
1. Agregar campo de lista
1. Agregar campo de firma
1. Agregar campo de código de barras

### Agregar campo de botón de opción

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

### Agregar campo de cuadro combinado

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

### Agregar campo de casilla de verificación

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

### Agregar campo de lista

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

### Agregar campo de firma

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

### Agregar campo de código de barras

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

## Temas relacionados

- [Rellenar AcroForm](/pdf/es/python-net/fill-form/)
- [Extraer AcroForm](/pdf/es/python-net/extract-form/)
- [Modificando AcroForm](/pdf/es/python-net/modifying-form/)
- [Importar y Exportar datos de Form](/pdf/es/python-net/import-export-form-data/)
