---
title: Crear botón de envío
linktitle: Crear botón de envío
type: docs
weight: 50
url: /es/python-net/create-submit-button/
description: Aprenda cómo agregar un botón de envío a un documento PDF de forma programática usando Aspose.PDF for Python. Este tutorial demuestra cómo crear un botón que envía los datos del formulario a una URL especificada y guarda el PDF actualizado.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crear un botón de envío en un PDF usando Aspose.PDF for Python
Abstract: Los botones de envío en formularios PDF permiten a los usuarios enviar los datos del formulario directamente a un servidor o punto final. En esta guía, aprenderá cómo agregar un campo de botón de envío a un PDF usando la clase FormEditor en Aspose.PDF for Python. El ejemplo muestra cómo configurar el nombre del botón, la etiqueta, la URL de destino y la posición, y luego guardar el documento PDF actualizado.
---

Los formularios PDF interactivos a menudo requieren que los usuarios envíen sus entradas para su procesamiento, como el envío de resultados de encuestas, formularios de solicitud o datos de retroalimentación. Un campo de botón de envío proporciona esta funcionalidad al vincular el botón a un punto final web.

El [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class permite agregar botones, casillas de verificación, botones de opción, campos de texto y otros controles de formulario.

1. Cargar un documento PDF existente.
1. Agregar un campo de botón de envío a una página específica.
1. Establecer la etiqueta del botón y la URL de envío de destino.
1. Guardar el PDF actualizado con el nuevo botón.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_submit_button(infile, outfile):
    """Create Submit Button in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add Submit Button to PDF form
    pdf_form_editor.add_submit_btn(
        "submitbtn1",
        1,
        "Submit Button",
        "http://example.com/submit",
        100,
        450,
        200,
        470,
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
