---
title: Renombrar campo
linktitle: Renombrar campo
type: docs
weight: 70
url: /es/python-net/rename-field/
description: Renombrar un campo de formulario existente en un documento PDF usando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Renombrar un campo de formulario PDF usando Python
Abstract: Este ejemplo muestra cómo renombrar un campo de formulario existente en un documento PDF usando Aspose.PDF for Python. El código abre un PDF de entrada, cambia el nombre de un campo de formulario especificado utilizando la clase FormEditor y guarda el documento actualizado.
---

Los formularios PDF a menudo dependen de los nombres de los campos para scripting, automatización y procesamiento de datos. Usando Aspose.PDF for Python, los desarrolladores pueden renombrar campos existentes sin recrearlos ni alterar el diseño del formulario.

El [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) La clase proporciona el método 'rename_field', que permite a los desarrolladores cambiar el nombre de un campo existente mientras se preservan su posición, valor y apariencia.

1. Cargar el formulario PDF existente.
1. Crear una instancia de FormEditor.
1. Vincular el documento PDF al editor.
1. Renombrar el campo objetivo.
1. Guarde el PDF actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def rename_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Rename field in document
    form_editor.rename_field("City", "Town")
    # Save updated document
    form_editor.save(outfile)
```

