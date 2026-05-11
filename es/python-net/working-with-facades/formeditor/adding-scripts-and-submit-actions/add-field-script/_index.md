---
title: Agregar script de campo
linktitle: Agregar script de campo
type: docs
weight: 10
url: /es/python-net/add-field-script/
description: Los formularios PDF interactivos pueden incluir JavaScript para automatizar acciones cuando los usuarios interactúan con los campos del formulario. Usando Aspose.PDF for Python, los desarrolladores pueden adjuntar fácilmente scripts a los elementos del formulario, como botones o campos de texto.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar acciones JavaScript a los campos de formulario PDF usando Python
Abstract: Este artículo explica cómo abrir un formulario PDF, asignar código JavaScript a un campo de formulario específico, agregar acciones de script adicionales y guardar el documento actualizado. El ejemplo usa la clase FormEditor de la API Aspose.PDF Facades para manipular el comportamiento del formulario programáticamente.
---

## Agregar acciones JavaScript a los campos de formulario PDF usando Python

Este fragmento de código le permite agregar acciones JavaScript a un campo de formulario PDF existente usando la biblioteca Aspose.PDF for Python. Abre un documento PDF, asigna una acción JavaScript a un campo de formulario y agrega un script que se ejecuta cuando se activa el campo. Finalmente, el PDF actualizado se guarda como un nuevo archivo.
Usando el [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) clase de la [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) módulo, puede adjuntar programáticamente JavaScript a los campos de formulario existentes:

1. Abra un formulario PDF existente.
1. Establezca una acción JavaScript para un campo específico.
1. Añade otra acción JavaScript al mismo campo.
1. Guarda el documento PDF modificado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set JavaScript action for the field
    form_editor.set_field_script(
        "Script_Demo_Button", "app.alert('Script 1 has been executed');"
    )

    # Add JavaScript action to the field
    form_editor.add_field_script(
        "Script_Demo_Button", "app.alert('Script 2 has been executed');"
    )

    # Save output PDF file
    form_editor.save(output_file_name)
```
