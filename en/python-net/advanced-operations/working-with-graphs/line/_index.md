---
title: Add Line Shapes to PDF in Python
linktitle: Add Line
type: docs
weight: 40
url: /python-net/add-line/
description: Learn how to draw line shapes and styled lines in PDF files in Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Adding Line Object to PDF using Python
Abstract: The article discusses how to add line objects to a PDF document using Aspose.PDF for Python via .NET. It explains the process of creating a `Document` instance and adding a `Graph` object to the PDF. The article provides detailed steps to create and configure a `Line` object, including specifying its dash pattern and color. It includes code snippets demonstrating how to add a simple line, a dotted dashed line, and how to draw lines across a page to form a cross pattern. Each section is accompanied by a visual representation of the resulting PDF. This guide serves as a practical resource for developers looking to enhance their PDF documents with graphical elements using Aspose.PDF.
---

## Add Line object

Aspose.PDF for Python via .NET supports the feature to add graph objects (for example graph, line, rectangle etc.) to PDF documents. You also get the leverage to add [Line](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) object where you can also specify the dash pattern, color and other formatting for Line element.

Follow the steps below:

1. Create [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) instance.
1. Create a Graph Object
1. Add [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) object to paragraphs collection of page.
1. Create and Configure the Line
1. Add the [Line](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) to the Graph
1. Save our PDF file.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing
import sys
from os import path

def add_line(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    line = drawing.Line([100, 100, 200, 100])
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1
    graph.shapes.add(line)

    document.save(outfile)
```

![Add Line](add_line.png)

## How to add Dotted Dashed Line to your PDF document

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing
import sys
from os import path

def add_dotted_dashed_line(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    line = drawing.Line([100, 100, 200, 100])
    line.graph_info.color = ap.Color.red
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1
    graph.shapes.add(line)

    document.save(outfile)
```

Let's check the result:

![Dashed Line](dash_line.png)

## Draw Line Across the Page

We can also use line object to draw a cross starting from Left-Bottom to Right-Upper corner and Left-Top corner to Bottom-Right corner.

Please take a look over following code snippet to accomplish this requirement.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing
import sys
from os import path

def draw_line_across_page(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    page.page_info.margin.left = 0
    page.page_info.margin.right = 0
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0

    graph = drawing.Graph(page.page_info.width, page.page_info.height)
    line = drawing.Line([page.rect.llx, 0, page.page_info.width, page.rect.ury])
    graph.shapes.add(line)
    line2 = drawing.Line([0, page.rect.ury, page.page_info.width, page.rect.llx])
    graph.shapes.add(line2)
    page.paragraphs.add(graph)

    document.save(outfile)
```

![Drawing Line](draw_line.png)

## Related Graph Topics

- [Work with PDF graphs in Python](/pdf/python-net/working-with-graphs/)
- [Add curve shapes to PDF in Python](/pdf/python-net/add-curve/)
- [Add rectangle shapes to PDF in Python](/pdf/python-net/add-rectangle/)
- [Check shape bounds in PDF graphs with Python](/pdf/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/)
