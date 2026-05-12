---
title: Establecer bandera de envío
linktitle: Establecer bandera de envío
type: docs
weight: 50
url: /es/python-net/set-submit-flag/
description: Aprenda cómo establecer programáticamente una bandera de envío para un botón de formulario PDF usando Aspose.PDF for Python. Esto permite que el botón envíe los datos del formulario en un formato específico, como XFDF, cuando es pulsado por un usuario.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Establecer bandera de envío para un botón de formulario PDF usando Aspose.PDF for Python
Abstract: Los formularios PDF pueden configurarse para enviar datos del formulario a un servidor o punto final en diferentes formatos. Al establecer una bandera de envío en un campo de botón, los desarrolladores pueden definir cómo se envían los datos. Este tutorial muestra cómo usar la clase FormEditor para establecer una bandera de envío en un botón de envío existente en un documento PDF y guardar el archivo actualizado.
---

Los formularios PDF a menudo incluyen botones de envío para enviar la entrada del usuario a un servidor. La bandera de envío determina el formato de datos enviado (p. ej., XFDF, FDF, HTML).

1. Vincular un documento PDF.
1. Acceda a un botón de envío existente.
1. Establezca el indicador de envío para el formato deseado.
1. Guarde el documento PDF actualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_submit_flag(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set submit flag for the form
    form_editor.set_submit_flag("Script_Demo_Button", ap.facades.SubmitFormFlag.XFDF)

    # Save output PDF file
    form_editor.save(output_file_name)
```
