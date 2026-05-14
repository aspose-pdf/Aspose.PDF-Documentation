---
title: Agregar formas de arco a PDF en Python
linktitle: Agregar arco
type: docs
weight: 10
url: /es/python-net/add-arc/
description: Aprende cómo dibujar y rellenar formas de arco en archivos PDF con Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dibuja formas de arco en archivos PDF usando Python
Abstract: Este artículo muestra cómo agregar formas de arco a documentos PDF con Aspose.PDF for Python via .NET. Cubre la creación de arcos contorneados, el dibujo de segmentos de arco rellenos y su incorporación a un contenedor Graph.
---

## Agregar objeto Arc

Aspose.PDF for Python via .NET le permite agregar [Arco](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) formas a páginas PDF usando el [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) clase. Puede dibujar arcos contorneados y segmentos de arco rellenos para diagramas e ilustraciones técnicas.

Siga los pasos a continuación:

1. Crear [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) instancia.
1. Crear [Objeto de gráfico](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) con ciertas dimensiones.
1. Establecer [borde](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) para el objeto Graph.
1. Cree un objeto arco correspondiente.
1. Agregue este objeto a la colección Shapes del objeto graph.
1. Agregar [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) objeto a la colección de párrafos de la página.
1. Guarde nuestro archivo PDF.

El siguiente fragmento de código muestra cómo agregar un [Arco](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) objeto.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_arc(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    arc1 = drawing.Arc(100, 100, 95, 0, 90)
    arc1.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(arc1)

    arc2 = drawing.Arc(100, 100, 90, 70, 180)
    arc2.graph_info.color = ap.Color.dark_blue
    graph.shapes.add(arc2)

    arc3 = drawing.Arc(100, 100, 85, 120, 210)
    arc3.graph_info.color = ap.Color.red
    graph.shapes.add(arc3)

    page.paragraphs.add(graph)
    document.save(outfile)
```

## Crear objeto de arco relleno

Este ejemplo muestra cómo agregar un segmento de arco relleno de color.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_arc_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    arc = drawing.Arc(100, 100, 95, 0, 90)

    arc.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(arc)

    line = drawing.Line([195, 100, 100, 100, 100, 195])
    line.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(line)

    page.paragraphs.add(graph)
    document.save(outfile)
```

Resultado de agregar un arco relleno:

![Arco relleno](filled_arc.png)

## Temas relacionados con gráficos

- [Trabajar con gráficos PDF en Python](/pdf/es/python-net/working-with-graphs/)
- [Agregar formas de círculo al PDF en Python](/pdf/es/python-net/add-circle/)
- [Agregar formas de curva al PDF en Python](/pdf/es/python-net/add-curve/)
- [Agregar formas de línea al PDF en Python](/pdf/es/python-net/add-line/)