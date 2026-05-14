---
title: Agregar formas de círculo a PDF en Python
linktitle: Agregar círculo
type: docs
weight: 20
url: /es/python-net/add-circle/
description: Aprenda cómo dibujar y rellenar formas de círculo en archivos PDF con Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dibujar formas de círculo en archivos PDF usando Python
Abstract: Este artículo muestra cómo agregar formas de círculo a documentos PDF con Aspose.PDF for Python via .NET. Cubre la creación de círculos contorneados, el relleno de círculos con color y la inserción de texto dentro de objetos círculo.
---

## Agregar objeto círculo

Aspose.PDF for Python via .NET le permite agregar [Círculo](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/circle/) formas a páginas PDF a través del [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) clase. Utiliza círculos para diagramas, anotaciones y elementos visuales simples.

Siga los pasos a continuación:

1. Crear [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) instancia.
1. Crear [Objeto de gráfico](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) con ciertas dimensiones.
1. Establecer [borde](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) para el objeto Graph.
1. Agregar [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) objeto a la colección de párrafos de la página.
1. Guarde nuestro archivo PDF.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_circle(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    circle = drawing.Circle(100, 100, 40)
    circle.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(circle)

    page.paragraphs.add(graph)
    document.save(outfile)
```

Nuestro círculo dibujado se verá así:

![Dibujando círculo](drawing_circle.png)

## Crear objeto de círculo relleno

Este ejemplo muestra cómo agregar un círculo y rellenarlo con color.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_circle_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    circle = drawing.Circle(100, 100, 40)
    circle.graph_info.color = ap.Color.green_yellow
    circle.graph_info.fill_color = ap.Color.green
    circle.text = ap.text.TextFragment("Circle")
    graph.shapes.add(circle)

    page.paragraphs.add(graph)
    document.save(outfile)
```

Resultado de agregar un círculo relleno:

![Círculo relleno](filled_circle.png)

## Temas relacionados con gráficos

- [Trabajar con gráficos PDF en Python](/pdf/es/python-net/working-with-graphs/)
- [Agregar formas de arco al PDF en Python](/pdf/es/python-net/add-arc/)
- [Agregar formas elípticas al PDF en Python](/pdf/es/python-net/add-ellipse/)
- [Agregar formas rectangulares al PDF en Python](/pdf/es/python-net/add-rectangle/)