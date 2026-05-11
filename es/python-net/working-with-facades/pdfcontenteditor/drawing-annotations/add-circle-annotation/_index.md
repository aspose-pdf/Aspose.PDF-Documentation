---
title: Agregar anotación de círculo
linktitle: Agregar anotación de círculo
type: docs
weight: 10
url: /es/python-net/add-circle-annotation/
description: Este ejemplo enlaza un PDF de entrada, crea una anotación de círculo en la primera página y guarda el documento modificado.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar anotación de círculo a un PDF usando PdfContentEditor en Python
Abstract: Este ejemplo demuestra cómo agregar una anotación de círculo a un documento PDF usando Aspose.PDF for Python a través de la API Facades. Muestra cómo definir los límites de la anotación, establecer el texto del contenido, configurar el color y la apariencia, y guardar el documento actualizado.
---

Las anotaciones de círculo son útiles para resaltar áreas de interés en un documento PDF. Con [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), puedes crear formas circulares especificando el rectángulo que define los límites del círculo, junto con el texto de la anotación, el color, las opciones de relleno, el número de página y el ancho del borde.

1. Crea el objeto PdfContentEditor.
1. Vincular el PDF de entrada.
1. Definir los límites del círculo.
1. Agregar la anotación de círculo.
1. Guardar el documento actualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_circle_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create CircleAnnotation object
    rect = apd.Rectangle(300, 300, 400, 400)
    contents = "This is circle annotation"
    content_editor.create_square_circle(rect, contents, apd.Color.blue, False, 1, 3)

    # Save output PDF file
    content_editor.save(outfile)
```
