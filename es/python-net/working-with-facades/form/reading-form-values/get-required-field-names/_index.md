---
title: Obtener nombres de campos obligatorios
linktitle: Obtener nombres de campos obligatorios
type: docs
weight: 30
url: /es/python-net/get-required-field-names/
description: Este ejemplo muestra cómo identificar y obtener los nombres de los campos obligatorios de formulario en un documento PDF utilizando la API Aspose.PDF Facades.
lastmod: "2026-02-19"
---

Los formularios PDF pueden contener campos obligatorios que los usuarios deben completar antes de enviarlos. Estos campos suelen marcarse como obligatorios en las propiedades del formulario.

1. Crear un objeto Form.
1. Vincular el documento PDF.
1. Acceda a todos los nombres de campo usando 'pdf_form.field_names'.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get required field names
def get_required_field_names(infile):
    """Get required field names from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get required field names
    for field in pdf_form.field_names:
        if pdf_form.is_required_field(field):
            print(f"Required field: {field}")
```
