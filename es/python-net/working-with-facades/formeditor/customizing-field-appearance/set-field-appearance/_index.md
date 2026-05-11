---
title: Establecer apariencia del campo
type: docs
weight: 50
url: /es/python-net/set-field-appearance/
description: Este ejemplo demuestra cómo cambiar la apariencia visual de un campo de formulario PDF usando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Establecer apariencia del campo de formulario PDF usando Python
Abstract: Este artículo explica cómo abrir un PDF, establecer la apariencia de un campo de formulario usando la clase FormEditor, y guardar el documento actualizado. El ejemplo establece la apariencia de un campo llamado "First Name" como invisible usando la bandera AnnotationFlags.INVISIBLE.
---

Los campos de formulario PDF soportan banderas de apariencia que controlan la visibilidad, la imprimibilidad y la interactividad. Usando Aspose.PDF for Python, los desarrolladores pueden modificar programáticamente estas banderas para campos de formulario específicos.

Usando el [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) clase, los desarrolladores pueden modificar estas banderas para ocultar, mostrar o personalizar el comportamiento de los campos de formulario en un PDF interactivo.

1. Abra un documento PDF existente.
1. Cree un objeto FormEditor.
1. Establezca la apariencia del campo llamado "First Name" como invisible.
1. Guarde el documento actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_appearance(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field appearance to invisible
    if not form_editor.set_field_appearance(
        "First Name", ap.annotations.AnnotationFlags.INVISIBLE
    ):
        raise Exception(
            "Failed to set field appearance. Field may not support appearance flags."
        )

    # Save updated document
    form_editor.save(outfile)
```
