---
title: Crear campo RadioButton
type: docs
weight: 40
url: /es/python-net/create-radiobutton-field/
description: Aprenda cómo agregar programáticamente un campo de formulario de botón de opción a un documento PDF utilizando Aspose.PDF for Python. Este ejemplo muestra cómo crear un grupo de botones de opción, definir opciones seleccionables y guardar el archivo PDF actualizado.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crear un campo de botón de opción en un PDF usando Aspose.PDF for Python
Abstract: Los botones de opción se utilizan comúnmente en formularios PDF para permitir a los usuarios seleccionar una opción de un grupo predefinido de elecciones. En este tutorial, aprenderá cómo crear un campo de botón de opción en un PDF usando la clase FormEditor en Aspose.PDF for Python. El ejemplo muestra cómo definir los elementos del botón de opción, establecer una selección predeterminada y guardar el documento actualizado.
---

Los formularios PDF interactivos permiten a los usuarios proporcionar entradas estructuradas directamente dentro de un documento. Un campo de botón de opción es útil cuando los usuarios deben elegir solo una opción entre varias, como seleccionar un país, género o preferencia.

El [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) La clase proporciona métodos para crear diferentes tipos de campos, incluidos cuadros de texto, casillas de verificación, cuadros combinados, listas desplegables y botones de opción

1. Cargar un documento PDF existente.
1. Definir una lista de opciones de botones de radio.
1. Agregar un campo de botón de radio a una página específica.
1. Establecer un valor seleccionado predeterminado.
1. Guarda el documento PDF modificado.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_radiobutton_field(infile, outfile):
    """Create RadioButton field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add RadioButton field to PDF form
    pdf_form_editor.items = ["Australia", "New Zealand", "Malaysia"]
    pdf_form_editor.add_field(
        pdf_facades.FieldType.RADIO, "radiobutton1", "Malaysia", 1, 240, 498, 256, 514
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
