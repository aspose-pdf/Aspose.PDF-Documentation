---
title: Crear campo ComboBox
type: docs
weight: 20
url: /es/python-net/create-combobox-field/
description: Verifique cómo agregar programáticamente un campo ComboBox (lista desplegable) a un documento PDF usando Aspose.PDF for Python. Este ejemplo muestra cómo insertar un campo de formulario ComboBox, añadir elementos seleccionables y guardar el archivo PDF actualizado.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crear un campo ComboBox en un PDF usando Aspose.PDF for Python
Abstract: Los campos de formulario interactivos hacen que los PDFs sean más dinámicos y fáciles de usar. Un campo ComboBox permite a los usuarios seleccionar una opción de una lista desplegable predefinida. En este tutorial, aprenderá cómo crear un ComboBox en un PDF usando la clase FormEditor en Aspose.PDF for Python, poblarlo con opciones y guardar el documento modificado.
---

Los formularios PDF se utilizan ampliamente para recopilar información estructurada en documentos digitales como solicitudes, encuestas y formularios de registro. Un campo ComboBox ofrece una manera conveniente para que los usuarios elijan de una lista de valores predefinidos mientras se mantiene el formulario compacto y organizado.

El [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) La clase permite crear y gestionar diferentes tipos de campos, incluidos los cuadros de texto, casillas de verificación, botones de radio y listas desplegables.

1. Cargar un documento PDF existente.
1. Agregar un campo ComboBox con el método 'add_field()' y el parámetro 'FieldType.COMBO_BOX'.
1. Utilizar el método 'add_list_item()' para insertar opciones seleccionables en la lista desplegable.
1. Guarde el documento PDF actualizado.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_combobox_field(infile, outfile):
    """Create ComboBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add ComboBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.COMBO_BOX, "combobox1", "Australia", 1, 230, 498, 350, 514
    )
    pdf_form_editor.add_list_item("combobox1", ["Australia", "Australia"])
    pdf_form_editor.add_list_item("combobox1", ["New Zealand", "New Zealand"])

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
