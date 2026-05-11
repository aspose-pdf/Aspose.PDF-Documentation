---
title: Agregar anotación de línea
type: docs
weight: 30
url: /es/python-net/add-line-annotation/
description: Este ejemplo asocia un PDF de entrada, dibuja una anotación de línea roja con terminaciones de línea cuadradas y guarda el PDF modificado.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar anotación de línea a un PDF usando PdfContentEditor en Python
Abstract: Este ejemplo demuestra cómo agregar una anotación de línea a un documento PDF usando Aspose.PDF for Python a través de la API Facades. Explica cómo definir los puntos de inicio y fin de la línea, los límites del rectángulo, las propiedades de apariencia y guardar el documento actualizado.
---

Las anotaciones de línea son útiles para enfatizar texto, resaltar relaciones o llamar la atención sobre áreas específicas en un PDF. Con [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), puedes crear programáticamente anotaciones de línea especificando los puntos de inicio y fin, el rectángulo delimitador, el color, el estilo de borde y las terminaciones de línea.

1. Crear el objeto PdfContentEditor.
1. Vincular el PDF de entrada.
1. Definir propiedades de la anotación de línea.
1. Agregar la anotación de línea.
1. Guarda el Documento actualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_line_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create LineAnnotation object
    rect = apd.Rectangle(100, 100, 200, 200)
    contents = "This is line annotation"
    content_editor.create_line(
        rect,
        contents,
        100,
        100,
        200,
        200,
        1,
        1,
        apd.Color.red,
        "Solid",
        [3, 2],
        ["Square"],
    )

    # Save output PDF file
    content_editor.save(outfile)
```
