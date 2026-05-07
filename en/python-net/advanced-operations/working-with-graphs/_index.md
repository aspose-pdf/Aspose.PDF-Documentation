---
title: Work with PDF Graphs in Python
linktitle: Working with Graphs
type: docs
weight: 70
url: /python-net/working-with-graphs/
description: Learn how to draw graphs and shapes in PDF files in Python, including arcs, circles, curves, lines, rectangles, and ellipses.
lastmod: "2026-05-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Draw and customize vector graph shapes in PDF files using Python
Abstract: This section introduces the Graph class in Aspose.PDF for Python via .NET and explains how to create common vector shapes in PDF documents. Learn how to add and style arcs, circles, curves, lines, rectangles, ellipses, and validate shape bounds.
---

## What is Graph

[Aspose.PDF for Python via .NET](/pdf/python-net/) provides the [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) class for drawing vector graphics in PDF documents.

`Graph` is a paragraph-level element, so you add it to a page through the page `paragraphs` collection. Each graph contains a `Shapes` collection where you can add drawing objects such as lines, arcs, circles, curves, rectangles, and ellipses.

Use this section when you need to draw vector graphics directly into PDF pages in Python, whether for charts, diagrams, illustrations, or custom page annotations.

## Graph Shapes Covered

The following types of shapes are supported by the [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) class:

- [Arc](/pdf/python-net/add-arc/) - draw arc segments for partial circles and curved diagram elements.
- [Circle](/pdf/python-net/add-circle/) - create circle outlines or filled circles for markers and visual highlights.
- [Curve](/pdf/python-net/add-curve/) - add Bezier-style curves for custom paths and smooth graphical elements.
- [Line](/pdf/python-net/add-line/) - draw straight lines, including styled and dashed lines.
- [Rectangle](/pdf/python-net/add-rectangle/) - create outlined, filled, gradient, or transparent rectangle shapes.
- [Ellipse](/pdf/python-net/add-ellipse/) - draw oval shapes and add text inside them when needed.

You can also validate shape placement with bounds checking:

- [Check shape bounds in PDF graphs with Python](/pdf/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/)

The examples in this section are illustrated in the figure below:

![Figures in Graphs](graphs.png)

