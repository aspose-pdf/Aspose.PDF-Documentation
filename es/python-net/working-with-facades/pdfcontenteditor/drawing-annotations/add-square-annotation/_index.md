---
title: Agregar anotación cuadrada
type: docs
weight: 60
url: /es/python-net/add-square-annotation/
description: Este ejemplo enlaza un PDF de entrada, añade una anotación cuadrada azul rellena en la primera página y guarda el documento modificado.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar anotación cuadrada a un PDF usando PdfContentEditor en Python
Abstract: Este ejemplo muestra cómo agregar una anotación cuadrada a un documento PDF usando Aspose.PDF for Python a través de la API Facades. Demuestra cómo definir el rectángulo de la anotación, el contenido de texto, el color, las opciones de relleno y guardar el documento actualizado.
---

Las anotaciones cuadradas se usan comúnmente para resaltar áreas de interés, marcar secciones importantes o proporcionar indicaciones visuales en un documento PDF. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), puedes crear anotaciones cuadradas (o circulares) especificando el rectángulo delimitador, el texto de contenido, el color del borde, la opción de relleno, el número de página y el ancho del borde.

1. Crear el objeto PdfContentEditor.
1. Vincular el PDF de entrada.
1. Definir la anotación Square.
1. Agregar la anotación Square.
1. Guarda el Documento actualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_square_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create SquareAnnotation object
    rect = apd.Rectangle(100, 300, 200, 400)
    contents = "This is square annotation"
    content_editor.create_square_circle(rect, contents, apd.Color.blue, True, 1, 3)

    # Save output PDF file
    content_editor.save(outfile)
```
