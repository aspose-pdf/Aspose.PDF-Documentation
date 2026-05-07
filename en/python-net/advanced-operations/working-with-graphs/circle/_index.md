---
title: Add Circle Shapes to PDF in Python
linktitle: Add Circle
type: docs
weight: 20
url: /python-net/add-circle/
description: Learn how to draw and fill circle shapes in PDF files in Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Draw circle shapes in PDF files using Python
Abstract: This article shows how to add circle shapes to PDF documents with Aspose.PDF for Python via .NET. It covers creating outlined circles, filling circles with color, and placing text inside circle objects.
---

## Add Circle object

Aspose.PDF for Python via .NET lets you add [Circle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/circle/) shapes to PDF pages through the [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) class. Use circles for diagrams, annotations, and simple visual elements.

Follow the steps below:

1. Create [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) instance.
1. Create [Graph object](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) with certain dimensions.
1. Set [border](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) for Graph object.
1. Add [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) object to paragraphs collection of page.
1. Save our PDF file.

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

Our drawn circle will look like this:

![Drawing Circle](drawing_circle.png)

## Create Filled Circle Object

This example shows how to add a circle and fill it with color.

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

Result of adding a filled circle:

![Filled Circle](filled_circle.png)

## Related Graph Topics

- [Work with PDF graphs in Python](/pdf/python-net/working-with-graphs/)
- [Add arc shapes to PDF in Python](/pdf/python-net/add-arc/)
- [Add ellipse shapes to PDF in Python](/pdf/python-net/add-ellipse/)
- [Add rectangle shapes to PDF in Python](/pdf/python-net/add-rectangle/)