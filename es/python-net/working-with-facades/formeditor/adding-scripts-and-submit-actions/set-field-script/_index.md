---
title: Establecer script de campo
linktitle: Establecer script de campo
type: docs
weight: 30
url: /es/python-net/set-field-script/
description: Este fragmento de código muestra cómo asignar una acción JavaScript a un campo de formulario en un documento PDF usando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Establecer acciones JavaScript para campos de formulario PDF usando Python
Abstract: Este artículo explica cómo abrir un documento PDF, asignar código JavaScript a un campo de formulario, actualizar el script usando la clase FormEditor y guardar el archivo modificado. El ejemplo demuestra cómo los scripts existentes pueden ser sobrescritos para modificar el comportamiento de los campos de formulario.
---

Los formularios PDF interactivos a menudo dependen de JavaScript para realizar tareas como mostrar alertas, validar la entrada o activar comportamientos dinámicos del formulario. Con Aspose.PDF for Python, los desarrolladores pueden gestionar programáticamente estos scripts.

El ejemplo primero agrega una acción JavaScript al campo y luego la reemplaza con otro script usando el método 'set_field_script'. Este enfoque permite a los desarrolladores controlar o actualizar el comportamiento interactivo de los elementos de formulario PDF, como botones o campos de entrada.

El FormField usado en este ejemplo se llama 'Script_Demo_Button', que típicamente representa un botón que ejecuta el script asignado cuando se activa.

Usando el [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) clase de la [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) Módulo, los desarrolladores pueden gestionar programáticamente acciones JavaScript asociadas con FormFields:

1. Abra un documento de formulario PDF existente.
1. Agregue una acción JavaScript a un FormField.
1. Establezca (reemplace) la acción JavaScript con un script nuevo.
1. Guarda el documento PDF modificado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Add JavaScript action to the field
    form_editor.add_field_script(
        "Script_Demo_Button", "app.alert('Script 1 has been executed');"
    )

    # Set JavaScript action for the field
    form_editor.set_field_script(
        "Script_Demo_Button", "app.alert('Script 2 has been executed');"
    )

    # Save output PDF file
    form_editor.save(output_file_name)
```
