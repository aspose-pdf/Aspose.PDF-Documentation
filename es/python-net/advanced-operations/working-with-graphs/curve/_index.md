---
title: Agregar formas de curva a PDF en Python
linktitle: Agregar curva
type: docs
weight: 30
url: /es/python-net/add-curve/
description: Aprenda cómo dibujar y rellenar formas de curva en archivos PDF en Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dibujar formas de curva en archivos PDF usando Python
Abstract: Este artículo muestra cómo agregar formas de curva a documentos PDF con Aspose.PDF for Python via .NET. Cubre la creación de curvas contorneadas, el relleno de objetos de curva y la representación de rutas de curva personalizadas en un contenedor Graph.
---

## Agregar objeto de curva

Aspose.PDF for Python via .NET le permite agregar [Curva](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/curve/) formas a páginas PDF a través del [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) clase.

Este artículo muestra cómo crear curvas con contorno y rellenas.

Siga los pasos a continuación:

1. Crear [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) instancia.
1. Crear [Objeto de gráfico](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) con ciertas dimensiones.
1. Establecer [borde](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) para el objeto Graph.
1. Agregar [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) objeto a la colección de párrafos de la página.
1. Guarde nuestro archivo PDF.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_curve(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(curve1)

    page.paragraphs.add(graph)
    document.save(outfile)
```

La siguiente imagen muestra el resultado ejecutado con nuestro fragmento de código:

![Dibujo de Curva](drawing_curve.png)

## Crear objeto de Curva rellena

Este ejemplo muestra cómo agregar un objeto de Curva que está relleno de color.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def add_curve_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(curve1)

    page.paragraphs.add(graph)
    document.save(outfile)
```

Resultado de añadir una curva rellena:

![Curva rellena](filled_curve.png)

## Temas relacionados con gráficos

- [Trabajar con gráficos PDF en Python](/pdf/es/python-net/working-with-graphs/)
- [Agregar formas de arco al PDF en Python](/pdf/es/python-net/add-arc/)
- [Agregar formas de línea al PDF en Python](/pdf/es/python-net/add-line/)
- [Agregar formas elípticas al PDF en Python](/pdf/es/python-net/add-ellipse/)