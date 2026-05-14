---
title: Campo de una sola línea a campo de varias líneas
linktitle: Campo de una sola línea a campo de varias líneas
type: docs
weight: 80
url: /es/python-net/single-to-multiple/
description: Convierta un campo de texto de una sola línea en un campo de varias líneas en un documento PDF usando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Convierta un Campo de Texto de una Sola Línea a un Campo de Varias Líneas en un PDF usando Python
Abstract: Este ejemplo muestra cómo convertir un campo de texto de una sola línea en un campo de varias líneas en un documento PDF usando Aspose.PDF for Python. El código carga un formulario PDF existente, modifica el campo especificado para permitir múltiples líneas de texto y guarda el documento actualizado.
---

Los formularios PDF a veces contienen campos de texto diseñados para entrada de una sola línea, lo que puede no ser suficiente para ciertos tipos de datos. Con Aspose.PDF for Python, los desarrolladores pueden convertir fácilmente dichos campos en campos de texto de varias líneas sin recrearlos.

Usando el [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class, los desarrolladores pueden modificar los campos de texto existentes sin afectar su posición u otras propiedades.

1. Cargue el documento PDF existente.
1. Crear una instancia de FormEditor.
1. Vincular el documento PDF al editor.
1. Convierta el campo seleccionado a varias líneas.
1. Guarde el documento actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def single2multiple(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Change a single-lined text field to a multiple-lined one
    form_editor.single_2_multiple("City")
    # Save updated document
    form_editor.save(outfile)
```

