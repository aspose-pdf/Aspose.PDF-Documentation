---
title: Working with Graphs in PDF using Python
linktitle: Working with Graphs
type: docs
weight: 70
url: /python-net/working-with-graphs/
description: This article explains what a is Graph, how to create a filled rectangle object, and other functions
lastmod: "2025-05-14"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Adding Graphs to PDF using Python
Abstract: The article discusses the integration of graphs into PDF documents, a common requirement for developers using Adobe Acrobat Writer or similar PDF processing tools. It introduces the Graph class in Aspose.PDF for Python via .NET, which facilitates this task by allowing the addition of various types of shapes to PDF documents. The Graph class is a paragraph-level element that can be added to the Paragraphs collection in a Page instance and supports a collection of shapes, including Arc, Circle, Curve, Line, Rectangle, and Ellipse. Each shape serves a unique purpose, such as Arcs representing adjacency, Circles illustrating data portions, Curves depicting connected lines, Lines displaying continuous data trends, Rectangles solving spatial problems, and Ellipses forming oval shapes. The article also provides visual representations of these shapes to aid understanding.
---

## What is Graph

Adding graphs to PDF documents is a very common task for developers while working with Adobe Acrobat Writer or other PDF processing applications. There are many types of graphs that can be used in PDF applications.
[Aspose.PDF for Python via .NET](/pdf/python-net/) also supports adding graphs to PDF documents. For this purpose, the Graph class is provided. Graph is a paragraph level element and it can be added to the Paragraphs collection in a Page instance. A Graph instance contains a collection of Shapes.

The following types of shapes are supported by the [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) class:

- [Arc](/pdf/python-net/add-arc/) - sometimes also called a flag is an ordered pair of adjacent vertices, but sometimes also called a directed line.
- [Circle](/pdf/python-net/add-circle/) - displays data using a circle divided into sectors. We use a circle graph (also called a pie chart) to show how data represent portions of one whole or one group.
- [Curve](/pdf/python-net/add-curve/) - is a connected union of projective lines, each line meeting three others in ordinary double points.
- [Line](/pdf/python-net/add-line) - line graphs are used to display continuous data and can be useful in predicting future events when they show trends over time.
- [Rectangle](/pdf/python-net/add-rectangle/) - is one of the many fundamental shapes you'll see in graphs, its can be very useful in helping you solve a problem.
- [Ellipse](/pdf/python-net/add-ellipse/) - is a set of points on a plane, creating an oval, curved shape.

The above details are also depicted in the figures below:

![Figures in Graphs](graphs.png)

