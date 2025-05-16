---
title: Add Curve Object to PDF file
linktitle: Add Curve
type: docs
weight: 30
url: /python-net/add-curve/
description: This article explains how to create a curve object to your PDF using Aspose.PDF for Python via .NET.
lastmod: "2025-05-14"
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
1. Create [Drawing object](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) with certain dimensions.
1. Set [border](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) for Drawing object.
1. Add [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) object to paragraphs collection of page.
1. Save our PDF file.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 200)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create a curve and set its properties
    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info = drawing.GraphInfo()
    curve1.graph_info.color = ap.Color.green_yellow

    # Add the curve to the graph shapes
    graph.shapes.add(curve1)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

The following picture shows the result executed with our code snippet:

![Drawing Curve](drawing_curve.png)

## Create Filled Curve Object

This example shows how to add a Curve object that is filled with color.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 200)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create a curve and set fill color
    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info = drawing.GraphInfo()
    curve1.graph_info.fill_color = ap.Color.green_yellow

    # Add the curve to the graph shapes
    graph.shapes.add(curve1)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

Look at the result of adding a filled Curve:

![Filled Curve](filled_curve.png)
