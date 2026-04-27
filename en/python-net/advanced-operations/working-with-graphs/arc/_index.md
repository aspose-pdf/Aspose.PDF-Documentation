---
title: Add Arc Shapes to PDF in Python
linktitle: Add Arc
type: docs
weight: 10
url: /python-net/add-arc/
description: Learn how to draw and fill arc shapes in PDF files in Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Adding Arc Object to PDF using Python
Abstract: The article provides a detailed guide on how to add and customize arc objects within PDF documents using Aspose.PDF for Python via .NET. It highlights the capability of the library to incorporate graphical elements like arcs, crucial for applications needing dynamic PDF content generation such as technical diagrams and custom illustrations. The article includes step-by-step instructions and code snippets demonstrating how to create a `Document` instance, set up a `Drawing` object with specified dimensions and border properties, and add `Graph` and `Arc` objects to a PDF page. Additionally, it covers the process of filling arc objects with color, showcasing how to set fill properties for arcs and lines, and ultimately save the PDF document. The examples provided serve as a practical guide for developers seeking to leverage Aspose.PDF for precise graphical manipulations in PDF files.
---

## Add Arc object

Aspose.PDF for Python via .NET supports the feature to add graph objects (for example graph, line, rectangle etc.) to PDF documents. It also offers the feature to fill arc object with a certain color.

This example illustrates how to programmatically draw arcs within a PDF document using Aspose.PDF for Python via .NET. By leveraging the drawing module, developers can create complex graphical elements, such as arcs, with precise control over their appearance and positioning. This capability is essential for applications that require dynamic generation of graphical content within PDFs, such as technical diagrams, charts, or custom illustrations.

Follow the steps below:

1. Create [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) instance.
1. Create [Drawing object](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) with certain dimensions.
1. Set [border](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) for Drawing object.
1. Add [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) object to paragraphs collection of page.
1. Save our PDF file.

The following code snippet shows how to add a [Arc](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) object.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing
import sys
from os import path

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

## Create Filled Arc Object

Next example shows how to add a Arc object that is filled with color and certain dimensions.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing
import sys
from os import path

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

Let's see the result of adding a filled Arс:

![Filled Arc](filled_arc.png)

## Related Graph Topics

- [Work with PDF graphs in Python](/pdf/python-net/working-with-graphs/)
- [Add circle shapes to PDF in Python](/pdf/python-net/add-circle/)
- [Add curve shapes to PDF in Python](/pdf/python-net/add-curve/)
- [Add line shapes to PDF in Python](/pdf/python-net/add-line/)