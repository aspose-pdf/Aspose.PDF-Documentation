---
title: Eliminar acción de campo
type: docs
weight: 20
url: /es/python-net/remove-field-action/
description: Eliminar JavaScript de los campos de formulario puede ser útil al modificar formularios PDF interactivos, desactivar acciones asignadas previamente o limpiar documentos que contienen scripts innecesarios.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar acciones de JavaScript de los campos de formulario PDF usando Python
Abstract: Con Aspose.PDF for Python, los desarrolladores pueden eliminar programáticamente las acciones de JavaScript adjuntas a los campos de formulario. Este artículo explica cómo abrir un formulario PDF existente, eliminar el script asociado a un campo específico utilizando la clase FormEditor, verificar la operación y guardar el documento modificado.
---

Los formularios PDF a menudo contienen acciones de JavaScript que se ejecutan cuando los usuarios interactúan con elementos del formulario, como botones o campos de entrada. En algunos casos, estos scripts deben eliminarse para simplificar el comportamiento del formulario, mejorar la seguridad o actualizar la lógica del formulario. Elimine una acción de JavaScript de un campo de formulario en un documento PDF usando Aspose.PDF for Python. El código abre un formulario PDF existente, localiza un campo específico, elimina su acción de JavaScript asociada y guarda el documento actualizado como un nuevo archivo PDF.

Usando el [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) clase de la [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/), puede eliminar acciones de JavaScript de campos específicos en un formulario PDF existente:

1. Abra un formulario PDF existente.
1. Ubique un campo de formulario llamado 'Script_Demo_Button'.
1. Elimine la acción JavaScript asociada a ese campo.
1. Verifique si la eliminación fue exitosa.
1. Guarde el documento PDF actualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Remove JavaScript action from the field
    if not form_editor.remove_field_action("Script_Demo_Button"):
        raise Exception("Failed to remove field script")

    # Save output PDF file
    form_editor.save(output_file_name)
```
