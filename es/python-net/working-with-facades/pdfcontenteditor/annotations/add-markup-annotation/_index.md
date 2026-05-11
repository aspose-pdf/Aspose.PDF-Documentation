---
title: Agregar anotaciones de marcado
type: docs
weight: 30
url: /es/python-net/add-markup-annotation/
description: Este ejemplo enlaza un PDF de entrada, agrega cuatro anotaciones de marcado diferentes a la primera página y guarda el documento actualizado. Cada anotación muestra un estilo y color de marcado diferentes.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar anotaciones de marcado de resaltado, subrayado, tachado y ondulado en un PDF usando Python
Abstract: Este ejemplo muestra cómo agregar múltiples anotaciones de marcado—resaltado, subrayado, tachado y ondulado—a un documento PDF usando Aspose.PDF for Python via the Facades API. El ejemplo muestra cómo definir áreas de anotación, especificar tipos de marcado, aplicar colores y guardar el documento modificado.
---

Las anotaciones de marcado se utilizan para enfatizar o revisar texto dentro de un PDF. Con PdfContentEditor, puedes aplicar programáticamente diferentes estilos de marcado especificando un área rectangular, texto de comentario, tipo de marcado, número de página y color.

1. Crear el [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) objeto.
1. Vincular el PDF de entrada.
1. Definir rectángulos de anotación.
1. Agregar anotaciones de marcado.
1. Guardar el documento actualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_markup_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add markup annotation to page 1
    content_editor.create_markup(
        apd.Rectangle(120, 440, 200, 20),
        "This is a highlight annotation",
        0,
        1,
        apd.Color.yellow,
    )
    content_editor.create_markup(
        apd.Rectangle(110, 542, 200, 20),
        "This is a underline annotation",
        1,
        1,
        apd.Color.yellow,
    )
    content_editor.create_markup(
        apd.Rectangle(120, 568, 200, 20),
        "This is a strikeout annotation",
        2,
        1,
        apd.Color.orange_red,
    )
    content_editor.create_markup(
        apd.Rectangle(110, 598, 200, 20),
        "This is a squiggly annotation",
        3,
        1,
        apd.Color.dark_blue,
    )
    # Save updated document
    content_editor.save(outfile)
```
