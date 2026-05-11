---
title: Crear campo ListBox
linktitle: Crear campo ListBox
type: docs
weight: 30
url: /es/python-net/create-listbox-field/
description: Aprenda cómo agregar programáticamente un campo de formulario ListBox a un documento PDF usando Aspose.PDF for Python. Esta guía muestra cómo insertar un campo ListBox, definir los elementos seleccionables y guardar el archivo PDF actualizado.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crear un campo ListBox en un PDF usando Aspose.PDF for Python
Abstract: Los formularios PDF permiten a los usuarios interactuar con los documentos seleccionando opciones, ingresando datos y enviando información de forma digital. Un campo ListBox permite a los usuarios elegir uno o varios valores de una lista visible de opciones. En este tutorial, aprenderá cómo crear un campo ListBox en un PDF utilizando la clase FormEditor en Aspose.PDF for Python y rellenarlo con elementos predefinidos.
---

Los formularios PDF se utilizan comúnmente para solicitudes, encuestas y documentos de registro. Un campo ListBox muestra múltiples opciones simultáneamente, facilitando a los usuarios revisar y seleccionar elementos de una lista.

El [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) La clase proporciona funcionalidad para agregar diferentes tipos de campos interactivos, incluidos los elementos ListBox.

1. Cargar un documento PDF existente.
1. Definir una lista de opciones seleccionables.
1. Agregar un campo ListBox a una página específica.
1. Establecer un valor seleccionado predeterminado.
1. Guarde el documento PDF actualizado.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_listbox_field(infile, outfile):
    """Create ListBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add ListBox field to PDF form
    pdf_form_editor.items = ["Australia", "New Zealand", "Malaysia"]
    pdf_form_editor.add_field(
        pdf_facades.FieldType.LIST_BOX, "listbox1", "Australia", 1, 230, 398, 350, 514
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
