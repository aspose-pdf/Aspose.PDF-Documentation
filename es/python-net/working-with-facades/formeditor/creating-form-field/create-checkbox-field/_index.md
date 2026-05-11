---
title: Crear campo CheckBox
type: docs
weight: 10
url: /es/python-net/create-checkbox-field/
description: Aprenda cómo agregar programáticamente un campo de formulario checkbox a un documento PDF usando Aspose.PDF for Python. Esta guía demuestra cómo usar la clase FormEditor para insertar un checkbox interactivo en un archivo PDF existente y guardar el documento actualizado.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crear un campo Checkbox en un PDF usando Aspose.PDF for Python
Abstract: Los campos de formulario interactivos permiten a los usuarios completar e interactuar con documentos PDF de forma digital. En este tutorial, aprenderá cómo agregar un campo checkbox a un PDF usando la API de Aspose.PDF para Python. El ejemplo muestra cómo vincular un documento PDF existente, crear un campo de formulario checkbox en coordenadas especificadas y guardar el archivo modificado.
---

Los formularios PDF se utilizan ampliamente para recopilar la entrada del usuario en documentos como solicitudes, encuestas y acuerdos. Un campo checkbox permite a los usuarios seleccionar o deseleccionar una opción dentro de un formulario.

Usando Aspose.PDF for Python, los desarrolladores pueden manipular formularios PDF programáticamente. The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) La clase proporciona métodos para agregar, editar y gestionar campos de formulario dentro de un documento PDF.

1. Cargar un archivo PDF existente.
1. Llame al método 'add_field()' con el parámetro 'FieldType.CHECK_BOX' para crear la casilla de verificación y especificar su posición.
1. Defina el nombre del campo, el título y la posición.
1. Guarde el documento PDF actualizado.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_checkbox_field(infile, outfile):
    """Create CheckBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add CheckBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.CHECK_BOX,
        "checkbox1",
        "Check Box 1",
        1,
        240,
        498,
        256,
        514,
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
