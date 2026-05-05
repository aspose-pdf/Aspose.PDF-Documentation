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
AlternativeHeadline: Draw line shapes in PDF files using Python
Abstract: This article shows how to add line shapes to PDF documents with Aspose.PDF for Python via .NET. It covers creating basic lines, configuring dashed line styles, and drawing lines across a page.
---

## Add Line object

Aspose.PDF for Python via .NET lets you add [Line](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) shapes to PDF pages using the [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) class. You can control line color, dash pattern, and placement.

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

Result of adding a dotted dashed line:

![Dashed Line](dash_line.png)

## Draw Line Across the Page

You can also draw lines across the page to form a cross.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

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
