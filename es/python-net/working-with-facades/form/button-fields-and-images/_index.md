---
title: Campos de botones e imágenes
linktitle: Campos de botones e imágenes
type: docs
weight: 40
url: /es/python-net/button-fields-and-images/
description: Este ejemplo muestra cómo gestionar campos de botones en un formulario PDF utilizando la API Aspose.PDF Facades.
lastmod: "2026-02-19"
TechArticle: true
AlternativeHeadline: Agregar apariencia de imagen a campos de botones & leer banderas de envío
Abstract: Los formularios PDF a menudo incluyen botones interactivos que pueden desencadenar acciones JavaScript o enviar los datos del formulario. Puedes mejorar visualmente los campos de botones añadiendo imágenes como su apariencia y, mediante programación, inspeccionar su comportamiento de envío.
---

## Agregar apariencia de imagen a campos de botones

Este fragmento de código explica cómo agregar una apariencia de imagen a un campo de botón existente en un formulario PDF. La operación mejora la presentación visual de un botón PDF al reemplazar su apariencia predeterminada con una imagen personalizada.

1. Crear un objeto Form.
1. Vincular el archivo PDF al objeto Form.
1. Agregar imagen al campo de botón.

    - Determine la ruta al archivo de imagen asociado con el PDF
    - Abra la imagen en modo binario como image_stream.
    - Llame a fill_image_field() con el nombre de campo de botón totalmente calificado.

1. Guardar el PDF actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add image appearance to button fields
def add_image_appearance_to_button_fields(infile, outfile):
    """Add image appearance to button fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Add image appearance to button fields by providing the field name and image stream
    image_path = infile.replace(".pdf", ".jpg")
    with open(image_path, "rb") as image_stream:
        pdf_form.fill_image_field("Image1_af_image", image_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```

## Obtener banderas de envío

La biblioteca de Python le ayuda a recuperar las banderas de envío de un botón de envío en un formulario PDF utilizando la API Aspose.PDF Facades. Las banderas de envío definen el comportamiento de un botón de envío, como si envía todo el formulario, incluye anotaciones o envía en formato FDF, XFDF, PDF o HTML.

1. Crear un objeto Form.
1. Llame a get_submit_flags() en el objeto form usando el nombre completo del botón de envío.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_submit_flags(infile, outfile):
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)
    flags = pdf_form.get_submit_flags("Submit1_af_submit")

    print(f"Submit flags: {flags}")
```
