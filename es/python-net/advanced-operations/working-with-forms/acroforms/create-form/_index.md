---
title: Crear AcroForm - Crear PDF rellenable en Python
linktitle: Crear AcroForm
type: docs
weight: 10
url: /es/python-net/create-form/
description: Con Aspose.PDF for Python puedes crear un formulario desde cero en tu archivo PDF
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo crear AcroForm en PDF usando Python
Abstract: El artículo ofrece una guía sobre cómo crear un campo de formulario en un documento PDF usando la biblioteca Aspose.PDF para Python. Presenta la clase `Document`, que contiene una colección `Form` para gestionar los campos de formulario. El proceso para añadir un campo de formulario implica crear el campo deseado y utilizar el método `add` de la colección `Form`. Se proporciona un ejemplo específico para ilustrar la adición de un `TextBoxField` a un documento PDF. El ejemplo incluye código detallado que demuestra la creación de un `TextBoxField`, estableciendo sus propiedades como posición, nombre, valor, borde y color, y posteriormente añadiéndolo al documento. El PDF modificado se guarda con el campo de formulario recién añadido.
---

## Crear formulario desde cero

### Agregar campo de formulario en un documento PDF

El [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) la clase proporciona una colección llamada [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) que le ayuda a administrar campos de formulario en un documento PDF.

Para agregar un campo de formulario:

1. Cree el campo de formulario que desea agregar.
1. Llame a la colección Form [agregar](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/#methods) método.

### Agregar TextBoxField

El ejemplo a continuación muestra cómo agregar un [TextBoxField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).

```python
import aspose.pdf as ap

data_dir = "/path/to/your/pdf/files/"
path_infile = os.path.join(work_dir, infile)
path_outfile = os.path.join(work_dir, outfile)

# Open document
pdfDocument = ap.Document(path_infile)

# Create a field
textBoxField = ap.forms.TextBoxField(
    pdfDocument.pages[1], ap.Rectangle(100, 200, 300, 300, True)
)
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
pdfDocument.save(path_outfile)
```
