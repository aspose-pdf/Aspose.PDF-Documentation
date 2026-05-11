---
title: Mover campo
type: docs
weight: 50
url: /es/python-net/move-field/
description: Mover un campo de formulario existente a una posición diferente en un documento PDF.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mover un campo de formulario PDF a una nueva posición usando Python
Abstract: Este ejemplo demuestra cómo mover un campo de formulario existente a una posición diferente en un documento PDF usando Aspose.PDF for Python. El código abre un PDF existente, reubica el campo de formulario especificado a nuevas coordenadas y guarda el documento actualizado.
---

Los formularios PDF a menudo requieren ajustes de diseño después de su creación. Usando Aspose.PDF for Python, los desarrolladores pueden mover campos de formulario existentes a una nueva posición sin recrearlos.

Este ejemplo muestra cómo reposicionar el campo "Country" especificando nuevas coordenadas para su ubicación dentro de la página. El [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) La clase proporciona el método move_field para reubicar campos dentro de una página PDF.

1. Abra el formulario PDF existente.
1. Cree un objeto FormEditor.
1. Vincula el documento PDF al FormEditor.
1. Mueva el campo 'Country' a una nueva posición usando coordenadas.
1. Guarde el documento modificado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Move field to new page
    form_editor.move_field("Country", 200, 600, 280, 620)
    # Save updated document
    form_editor.save(outfile)
```
