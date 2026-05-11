---
title: Agregar anotación de curva
type: docs
weight: 20
url: /es/python-net/add-curve-annotation/
description: Este ejemplo enlaza un PDF de entrada, dibuja una curva discontinua en la primera página y guarda el documento modificado.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar anotación de curva a un PDF usando PdfContentEditor en Python
Abstract: Este ejemplo demuestra cómo agregar una anotación de curva a un documento PDF usando Aspose.PDF for Python via the Facades API. Muestra cómo definir los vértices de la curva, el estilo de borde, los límites de la anotación, el contenido de texto y guardar el documento actualizado.
---

Las anotaciones de curva se utilizan para resaltar rutas o formas irregulares en un PDF, proporcionando énfasis visual o señalando áreas importantes. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), puedes dibujar curvas especificando una secuencia de vértices, estilo de borde, visibilidad, rectángulo de anotación y texto descriptivo.

1. Crea el objeto PdfContentEditor.
1. Vincular el PDF onput.
1. Configure las propiedades de la Curve.
1. Dibuje la anotación de la Curve.
1. Guardar el documento actualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_curve_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 1  # 1 - Dashed
    line_info.vertice_coordinate = [120, 520, 160, 560, 220, 540, 280, 580]
    line_info.visibility = True
    content_editor.draw_curve(
        line_info,
        1,
        apd.Rectangle(110, 510, 220, 100),
        "This is curve annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```
