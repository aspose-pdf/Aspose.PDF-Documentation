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
AlternativeHeadline: Adding Curve Object to PDF using Python
Abstract: The article discusses the implementation of graph curves in PDF documents using the Aspose.PDF library for Python via .NET. It introduces the concept of a graph curve, which is a union of projective lines, and details the process of creating both simple and filled Bézier curves programmatically. The article provides step-by-step instructions and code snippets for drawing curves within a PDF, highlighting the manipulation of graphical elements using Aspose.PDF's drawing module. The process includes creating a `Document` instance, defining a `Drawing` object with specified dimensions, setting borders, and adding a `Graph` object to a PDF page. Visual outcomes of these code examples are illustrated through images showing the resultant curves. The article further explores the creation of filled curve objects, demonstrating how to set fill colors for curves, which is crucial for generating dynamic graphical content like technical diagrams, charts, or custom illustrations in PDFs.
---

## Add Curve object

A graph [Curve](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/curve/) is a connected union of projective lines, each line meeting three others in ordinary double points.

In this article, we will investigate  simply graph curves, and filled curves, that you can create in your PDF document.

This example illustrates how to draw a Bézier curve programmatically within a PDF document using Aspose.PDF for Python via .NET. By leveraging the drawing module, developers can create complex graphical elements with precise control over their appearance and positioning. This capability is essential for applications that require dynamic generation of graphical content within PDFs, such as technical diagrams, charts, or custom illustrations.

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

Look at the result of adding a filled Curve:

![Filled Curve](filled_curve.png)

## Related Graph Topics

- [Work with PDF graphs in Python](/pdf/python-net/working-with-graphs/)
- [Add arc shapes to PDF in Python](/pdf/python-net/add-arc/)
- [Add line shapes to PDF in Python](/pdf/python-net/add-line/)
- [Add ellipse shapes to PDF in Python](/pdf/python-net/add-ellipse/)