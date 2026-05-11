---
title: Establecer límite de campo
type: docs
weight: 80
url: /es/python-net/set-field-limit/
description: Este ejemplo muestra cómo establecer un límite máximo de caracteres para un campo de formulario en un documento PDF usando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Establecer límite máximo de caracteres para campos de formulario PDF usando Python
Abstract: Este ejemplo demuestra cómo establecer el límite de caracteres para un campo llamado "Last Name" a 10 caracteres, asegurando que los usuarios no puedan ingresar más que el límite especificado.
---

Los campos de formulario en documentos PDF pueden requerir restricciones de entrada para mantener un formato adecuado. Usando Aspose.PDF for Python, los desarrolladores pueden programar la configuración de un número máximo de caracteres para un campo.

El [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) La clase proporciona el método 'set_field_limit' para definir la longitud máxima de entrada para un campo.

1. Abra un formulario PDF existente.
1. Cree un objeto FormEditor.
1. Establezca el límite máximo de caracteres para el campo "Last Name".
1. Guarde el PDF actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_limit(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field limit to 10
    if not form_editor.set_field_limit("Last Name", 10):
        raise Exception(
            "Failed to set field limit. Field may not support specified limit."
        )

    # Save updated document
    form_editor.save(outfile)
```
