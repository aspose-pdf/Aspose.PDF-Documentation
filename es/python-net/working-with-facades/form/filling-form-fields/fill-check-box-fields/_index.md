---
title: Rellenar campos de casilla de verificación
linktitle: Rellenar campos de casilla de verificación
type: docs
weight: 20
url: /es/python-net/fill-check-box-fields/
description: Este ejemplo demuestra cómo rellenar programáticamente campos de casilla de verificación en un formulario PDF utilizando Aspose.PDF for Python via .NET. Muestra cómo vincular un documento PDF, actualizar los valores de las casillas de verificación por nombre de campo y guardar el archivo modificado.
lastmod: "2026-02-19"
---

La casilla de verificación se usa comúnmente en formularios PDF para representar opciones binarias, como suscripciones o confirmaciones de acuerdos. En este ejemplo, la [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) se utiliza para acceder a los campos del formulario y establecer sus valores en un estado seleccionado. Después de actualizar las casillas de verificación, el PDF rellenado se guarda como un nuevo documento.

1. Inicializa \u0027pdf_facades.Form()\u0027 para gestionar interacciones con los campos del formulario.
1. Utilice 'bind_pdf()' para adjuntar el PDF de origen que contiene campos de casilla de verificación.
1. Llame a 'fill_field()' para marcar campos como 'subscribe_newsletter' y 'accept_terms' como seleccionados.
1. Guarda el Documento actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Check Box Fields
def fill_check_box_fields(infile, outfile):
    """Fill check box fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill check box fields by name
    pdf_form.fill_field("subscribe_newsletter", "Yes")
    pdf_form.fill_field("accept_terms", "Yes")

    # Save updated PDF
    pdf_form.save(outfile)
```
