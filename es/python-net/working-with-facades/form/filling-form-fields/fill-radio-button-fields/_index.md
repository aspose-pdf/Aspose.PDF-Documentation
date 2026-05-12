---
title: Rellenar campos de botones de radio
linktitle: Rellenar campos de botones de radio
type: docs
weight: 30
url: /es/python-net/fill-radio-button-fields/
description: Este ejemplo demuestra cómo rellenar programáticamente campos de botones de radio en un formulario PDF usando Aspose.PDF for Python via .NET. Muestra cómo vincular un documento PDF, seleccionar una opción de botón de radio por índice y guardar el archivo actualizado.
lastmod: "2026-02-19"
---

Los botones de radio permiten a los usuarios seleccionar una única opción de un grupo predefinido, como campos de género o de preferencia. En este ejemplo, el [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada del [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) módulo se utiliza para vincular el PDF de origen y asignar una opción seleccionada mediante su valor de índice. Una vez elegida la opción deseada, el documento modificado se guarda.

1. Inicializa pdf_facades.Form() para gestionar los campos de formulario PDF.
1. Llama a 'bind_pdf()' para adjuntar el PDF que contiene campos de botones de radio.
1. Use 'fill_field()' para seleccionar la primera opción (índice 0).
1. Guarde el PDF actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Radio Button Fields
def fill_radio_button_fields(infile, outfile):
    """Fill radio button fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill radio button fields by name
    pdf_form.fill_field("gender", 0)  # Select male option (index 0)
    # pdf_form.fill_field("gender", 1) # Select female option (index 1)

    # Save updated PDF
    pdf_form.save(outfile)
```
