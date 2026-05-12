---
title: Agregar enlace JavaScript
linktitle: Agregar enlace JavaScript
type: docs
weight: 30
url: /es/python-net/add-javascript-link/
description: Este ejemplo enlaza un PDF de entrada, agrega un enlace JavaScript que desencadena una alerta al hacer clic y guarda el documento modificado.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar un enlace JavaScript a un PDF usando PdfContentEditor en Python
Abstract: Este ejemplo demuestra cómo agregar un enlace JavaScript a un documento PDF usando Aspose.PDF for Python via the Facades API. Muestra cómo crear un área clicable que ejecuta código JavaScript al hacer clic y guardar el PDF actualizado.
---

Los enlaces JavaScript en los PDF permiten funcionalidades interactivas como mostrar alertas, realizar cálculos o modificar dinámicamente el contenido del documento. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), puede definir un rectángulo clicable en una página y asociarlo con código JavaScript personalizado.

1. Cree una instancia de PdfContentEditor.
1. Enlace el documento PDF de entrada.
1. Defina un rectángulo para el enlace JavaScript clickable.
1. Especifique el número de página y el color del enlace.
1. Asigne código JavaScript para ejecutar al hacer clic.
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


def add_javascript_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add JavaScript link action
    content_editor.create_java_script_link(
        "app.alert('PdfContentEditor JavaScript link');",
        apd.Rectangle(160, 560, 260, 20),
        1,
        apd.Color.orange,
    )
    # Save updated document
    content_editor.save(outfile)
```
