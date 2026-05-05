---
title: Check Shape Bounds in PDF Graphs with Python
linktitle: Check Shape Bounds
type: docs
weight: 70
url: /python-net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Learn how to validate shape bounds in PDF graph collections in Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Validate graph shape bounds in PDF files using Python
Abstract: This article shows how to validate shape bounds in Graph collections with Aspose.PDF for Python via .NET. It covers configuring BoundsCheckMode, detecting out-of-range shapes, and handling bounds exceptions safely.
---

## Check shape bounds in a Graph

When you add shapes to a [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/), you can enable bounds validation to ensure each shape fits within the graph area.

Use [BoundsCheckMode](https://reference.aspose.com/pdf/python-net/aspose.pdf/boundscheckmode/) to define behavior when a shape is out of range. In this example, `THROW_EXCEPTION_IF_DOES_NOT_FIT` is used to raise an exception.

Follow the steps below:

1. Create a new PDF [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Add a [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Create a [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) and add it to the page.
1. Create a [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) that extends outside graph bounds.
1. Set bounds checking mode to `THROW_EXCEPTION_IF_DOES_NOT_FIT`.
1. Add the rectangle and handle the exception.
1. Save the document.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def check_shape_bounds(outfile: str):
    document = ap.Document()
    page = document.pages.add()

    graph = drawing.Graph(100, 100)
    graph.top = 10
    graph.left = 15
    graph.border = ap.BorderInfo(ap.BorderSide.BOX, 1, ap.Color.black)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(-1, 0, 50, 50)
    rect.graph_info.fill_color = ap.Color.tomato

    try:
        graph.shapes.update_bounds_check_mode(
            ap.BoundsCheckMode.THROW_EXCEPTION_IF_DOES_NOT_FIT
        )
        graph.shapes.add(rect)
    except Exception as e:
        print(e)

    document.save(outfile)
```

## Notes

- Use `THROW_EXCEPTION_IF_DOES_NOT_FIT` when strict layout validation is required.
- For permissive behavior, choose another `BoundsCheckMode` option based on your layout needs.

## Related Graph Topics

- [Work with PDF graphs in Python](/pdf/python-net/working-with-graphs/)
- [Add rectangle shapes to PDF in Python](/pdf/python-net/add-rectangle/)
- [Add line shapes to PDF in Python](/pdf/python-net/add-line/)
- [Add ellipse shapes to PDF in Python](/pdf/python-net/add-ellipse/)
