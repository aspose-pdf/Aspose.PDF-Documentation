---
title: Agregar anotación de polígono
type: docs
weight: 40
url: /es/python-net/add-polygon-annotation/
description: Este ejemplo vincula un PDF de entrada, dibuja un polígono sólido en la primera página y guarda el documento modificado con una anotación.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar anotación de polígono a un PDF usando PdfContentEditor en Python
Abstract: Este ejemplo muestra cómo agregar una anotación de polígono a un documento PDF usando Aspose.PDF for Python via the Facades API. Demuestra cómo definir los vértices del polígono, el estilo del borde, los límites de la anotación, el texto descriptivo y guardar el documento actualizado.
---

Las anotaciones de polígono se utilizan para resaltar áreas o formas irregulares en un PDF, proporcionando énfasis visual o marcando regiones específicas. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), puedes crear polígonos especificando las coordenadas de los vértices, el estilo del borde, el número de página y el rectángulo de la anotación.

1. Crea el objeto PdfContentEditor.
1. Vincular el PDF de entrada.
1. Configura las propiedades del polígono.
1. Añade la anotación Polygon.
1. Guardar el documento actualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_polygon_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 0  # 0 - Solid
    line_info.vertice_coordinate = [100, 200, 150, 260, 220, 220, 200, 160]
    content_editor.create_polygon(
        line_info,
        1,
        apd.Rectangle(90, 150, 150, 120),
        "This is polygon annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```
