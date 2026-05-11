---
title: Agregar anotación de polilínea
type: docs
weight: 50
url: /es/python-net/add-polyline-annotation/
description: El ejemplo enlaza un PDF de entrada, crea una polilínea sólida en la primera página y guarda el documento modificado con una anotación.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar anotación de polilínea a un PDF usando PdfContentEditor en Python
Abstract: Este ejemplo muestra cómo agregar una anotación de polilínea a un documento PDF usando Aspose.PDF for Python via the Facades API. Muestra cómo definir una secuencia de vértices, estilo de borde, rectángulo de anotación, texto y guardar el documento actualizado.
---

Las anotaciones de polilínea le permiten resaltar una serie de segmentos de línea conectados en un PDF. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), puede dibujar una polilínea especificando las coordenadas de los vértices, el estilo de borde, el número de página y los límites de la anotación. Esto es útil para representar visualmente rutas, tendencias o conexiones en diagramas y documentos.

1. Crear el objeto PdfContentEditor.
1. Vincular el PDF de entrada.
1. Configure las propiedades de la polilínea.
1. Agregue la anotación de polilínea.
1. Guarda el Documento actualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_polyline_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 0  # 0 - Solid
    line_info.vertice_coordinate = [120, 420, 180, 460, 230, 430, 290, 470]
    content_editor.create_poly_line(
        line_info,
        1,
        apd.Rectangle(110, 410, 200, 90),
        "This is polyline annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```
