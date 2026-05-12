---
title: Comprobar límites de forma en gráficos PDF con Python
linktitle: Comprobar límites de forma
type: docs
weight: 70
url: /es/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Aprenda cómo validar los límites de forma en colecciones de gráficos PDF con Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Validar los límites de forma de los gráficos en archivos PDF usando Python
Abstract: Este artículo muestra cómo validar los límites de forma en colecciones de Graph con Aspose.PDF for Python via .NET. Cubre la configuración de BoundsCheckMode, la detección de formas fuera de rango y el manejo seguro de excepciones de límites.
---

## Comprobar límites de forma en un Graph

Cuando agregas formas a un [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/), puedes habilitar la validación de límites para asegurar que cada forma encaje dentro del área del gráfico.

Usar [BoundsCheckMode](https://reference.aspose.com/pdf/python-net/aspose.pdf/boundscheckmode/) para definir el comportamiento cuando una forma está fuera de rango. En este ejemplo, `THROW_EXCEPTION_IF_DOES_NOT_FIT` se usa para generar una excepción.

Siga los pasos a continuación:

1. Crea un nuevo PDF [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Añadir un [Página](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Cree un [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) y añádelo a la página.
1. Cree un [Rectángulo](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) que se extiende fuera de los límites del gráfico.
1. Establecer modo de verificación de límites a `THROW_EXCEPTION_IF_DOES_NOT_FIT`.
1. Agregue el rectángulo y maneje la excepción.
1. Guarde el documento.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def check_shape_bounds(outfile: str):
    document = ap.Document()
    page = document.pages.add()

    graph = drawing.Graph(100, 100)
    graph.top = 10
    graph.left = 15
    graph.border = ap.BorderInfo(ap.BorderSide.BOX, 1, ap.Color.black)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(-1, 0, 50, 50)
    rect.graph_info.fill_color = ap.Color.tomato

    try:
        graph.shapes.update_bounds_check_mode(
            ap.BoundsCheckMode.THROW_EXCEPTION_IF_DOES_NOT_FIT
        )
        graph.shapes.add(rect)
    except Exception as e:
        print(e)

    document.save(outfile)
```

## Notas

- Usar `THROW_EXCEPTION_IF_DOES_NOT_FIT` cuando se requiere una validación estricta del diseño.
- Para un comportamiento permisivo, elige otro `BoundsCheckMode` opción basada en sus necesidades de diseño.

## Temas relacionados con gráficos

- [Trabajar con gráficos PDF en Python](/pdf/es/python-net/working-with-graphs/)
- [Agregar formas rectangulares al PDF en Python](/pdf/es/python-net/add-rectangle/)
- [Agregar formas de línea al PDF en Python](/pdf/es/python-net/add-line/)
- [Agregar formas elípticas al PDF en Python](/pdf/es/python-net/add-ellipse/)
