---
title: Obtener opciones de botón de radio
type: docs
weight: 20
url: /es/python-net/get-radio-button-options/
description: Este artículo demuestra cómo recuperar el valor actualmente seleccionado de un campo de botón de radio en un documento PDF usando la API Aspose.PDF Facades.
lastmod: "2026-02-19"
---

Los campos de botón de radio en formularios PDF son controles agrupados donde solo se puede seleccionar una opción a la vez. Cada grupo tiene un nombre de campo, y cada opción tiene un valor correspondiente.

1. Crear un objeto Form.
1. Vincular el documento PDF.
1. Recuperar la opción de botón de radio seleccionada.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get radio button options
def get_radio_button_options(infile):
    """Get radio button options from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get radio button options by their names
    field_names = ["WorkType"]
    for field_name in field_names:
        options = pdf_form.get_button_option_current_value(field_name)
        print(f"Options for '{field_name}': {options}")
```
