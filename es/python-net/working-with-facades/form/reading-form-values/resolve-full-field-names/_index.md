---
title: Resolver nombres completos de campos
linktitle: Resolver nombres completos de campos
type: docs
weight: 60
url: /es/python-net/resolve-full-field-names/
description: Este ejemplo muestra cómo obtener los nombres totalmente calificados de los campos de formulario en un documento PDF usando la API Aspose.PDF Facades.
lastmod: "2026-02-19"
---

En los formularios PDF, los campos pueden organizarse jerárquicamente, especialmente cuando se utilizan subformularios. Cada campo tiene un nombre corto y un nombre totalmente calificado. El nombre totalmente calificado representa la ruta completa del campo dentro de la jerarquía del formulario y es requerido por muchos métodos de la API que manipulan o leen datos de formularios.

1. Crear un objeto Form.
1. Vincular el documento PDF.
1. Acceder a todos los nombres de campos de formulario.
1. Cada nombre totalmente calificado del campo\u0027s se resuelve usando get_full_field_name().

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Resolve full field names
def resolve_full_field_names(infile):
    """Resolve full field names in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Resolve full field names
    for field in pdf_form.field_names:
        name = pdf_form.get_full_field_name(field)
        print(f"Full field name: {name}")
```
