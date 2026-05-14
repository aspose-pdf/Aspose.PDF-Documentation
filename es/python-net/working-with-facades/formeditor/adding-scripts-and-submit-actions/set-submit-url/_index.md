---
title: Establecer URL de envío
linktitle: Establecer URL de envío
type: docs
weight: 40
url: /es/python-net/set-submit-url/
description: Este ejemplo muestra cómo configurar una acción de envío para un campo de botón en un formulario PDF usando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Establecer una URL de envío para un botón de formulario PDF usando Python
Abstract: Este artículo explica cómo abrir un formulario PDF existente, definir una URL de envío para un campo de botón usando la clase FormEditor, verificar que la operación se haya realizado con éxito y guardar el documento PDF actualizado.
---

Los formularios PDF pueden diseñarse para enviar sus datos a un servidor web cuando un usuario hace clic en un botón de envío. Usando Aspose.PDF for Python, los desarrolladores pueden configurar programáticamente una acción de envío para los campos del formulario.
Al establecer una URL de envío, el formulario puede enviar los datos ingresados por el usuario a un servidor cuando se hace clic en el botón. Esta funcionalidad es útil para flujos de trabajo donde los formularios PDF deben enviar información a aplicaciones web, bases de datos o servicios de procesamiento.

Usando el [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) clase de la [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) Módulo, los desarrolladores pueden asignar programáticamente una URL de envío a un campo de botón en un formulario PDF existente.

1. Abra un formulario PDF existente.
1. Localice un campo de botón llamado Script_Demo_Button.
1. Asigne una URL donde se enviarán los datos del formulario.
1. Verifique que la acción se haya aplicado correctamente.
1. Guarde el documento PDF actualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_submit_url(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Set license
    set_license()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set submit URL for the button
    if not form_editor.set_submit_url(
        "Script_Demo_Button", "http://www.example.com/submit"
    ):
        raise Exception("Failed to set submit URL")

    # Save output PDF file
    form_editor.save(output_file_name)
```
