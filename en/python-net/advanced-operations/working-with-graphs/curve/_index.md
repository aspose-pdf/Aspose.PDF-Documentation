---
title: Add Curve Shapes to PDF in Python
linktitle: Add Curve
type: docs
weight: 30
url: /python-net/add-curve/
description: Learn how to draw and fill curve shapes in PDF files in Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Draw curve shapes in PDF files using Python
Abstract: This article shows how to add curve shapes to PDF documents with Aspose.PDF for Python via .NET. It covers creating outlined curves, filling curve objects, and rendering custom curve paths in a Graph container.
---

## Add Curve object

Aspose.PDF for Python via .NET lets you add [Curve](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/curve/) shapes to PDF pages through the [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) class.

This article shows how to create both outlined and filled curves.

Follow the steps below:

1. Create [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) instance.
1. Create [Graph object](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) with certain dimensions.
1. Set [border](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) for Graph object.
1. Add [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) object to paragraphs collection of page.
1. Save our PDF file.

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

The following picture shows the result executed with our code snippet:

![Drawing Curve](drawing_curve.png)

## Create Filled Curve Object

This example shows how to add a Curve object that is filled with color.

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

Result of adding a filled curve:

![Filled Curve](filled_curve.png)

## Related Graph Topics

- [Work with PDF graphs in Python](/pdf/python-net/working-with-graphs/)
- [Add arc shapes to PDF in Python](/pdf/python-net/add-arc/)
- [Add line shapes to PDF in Python](/pdf/python-net/add-line/)
- [Add ellipse shapes to PDF in Python](/pdf/python-net/add-ellipse/)