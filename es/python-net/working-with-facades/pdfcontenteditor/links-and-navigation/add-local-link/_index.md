---
title: Agregar enlace local
linktitle: Agregar enlace local
type: docs
weight: 40
url: /es/python-net/add-local-link/
description: Este ejemplo enlaza un PDF de entrada, agrega un enlace local de color rojo en la página 1 que apunta a la página 1 y guarda el documento modificado.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar un enlace local a un PDF usando PdfContentEditor en Python
Abstract: Este ejemplo muestra cómo agregar un enlace local a un documento PDF usando Aspose.PDF for Python a través de la API Facades. Demuestra cómo crear un área clickeable que navegue a otra página dentro del mismo PDF y guardar el documento actualizado.
---

Los enlaces locales en los PDFs permiten una navegación rápida entre páginas dentro del mismo documento. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), puedes definir un rectángulo clickeable que vincula una página a otra, mejorando la usabilidad y la navegación del documento.

1. Cree una instancia de PdfContentEditor.
1. Enlace el documento PDF de entrada.
1. Defina un rectángulo para el enlace local clicable.
1. Especifique la página de origen y la página de destino.
1. Establezca el color del enlace.
1. Guarde el documento PDF actualizado.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_local_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a local link on page 1 to destination page 1
    content_editor.create_local_link(
        apd.Rectangle(120, 620, 220, 20),
        1,
        1,
        apd.Color.red,
    )
    # Save updated document
    content_editor.save(outfile)
```
