---
title: Check Shape Bounds in PDF Graphs with Python
type: docs
weight: 70
url: /python-net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Learn how to validate shape bounds in PDF graph collections in Python.
lastmod: "2026-04-16"
draft: false
TechArticle: true 
AlternativeHeadline: Guide on checking shape bounds in Shapes
Abstract: This article offers a comprehensive guide on utilizing the bounds-checking feature in the Shapes collection, particularly within PDF documents using Python. The feature is instrumental in ensuring that graphical elements, such as shapes, fit appropriately within their parent containers. It can be configured to throw an exception if the component exceeds the container's bounds, ensuring robust error handling. The guide walks through creating a new PDF document, adding a page, and establishing a graphical element (a rectangle shape) within a graph object. Detailed instructions are provided for instantiating a `Document`, adding a `Page`, and creating a `Graph` object. It describes setting up a `Rectangle` shape and configuring the `BoundsCheckMode` to `THROW_EXCEPTION_IF_DOES_NOT_FIT`, which ensures that an exception is thrown if the shape does not fit within the specified dimensions of the graph. The process is illustrated with a Python code example using the Aspose.PDF library, highlighting the practical implementation of these features.
---

This article provides a detailed guide on using the bounds-checking feature in the Shapes collection. This feature ensures that elements fit within their parent container and can be configured to throw an exception if the component does not fit.

1. Create a new PDF [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Add a Page
1. Create a [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/)
1. Create a Rectangle Shape
1. Bounds Check Mode
1. Add the [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) to the Graph

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing
import datetime

# Create Document instance
document = ap.Document()

# Add page to pages collection of PDF file
page = document.pages.add()

# Create a Graph object with specified dimensions
graph = ap.drawing.Graph(100, 100)
graph.top = 10
graph.left = 15
graph.border = ap.BorderInfo(ap.BorderSide.BOX, 1, ap.Color.black)
page.paragraphs.add(graph)

# Create a shape object(for example, Rectangle) with specified dimensions
rect = drawing.Rectangle(-1, 0, 50, 50)
rect.graph_info.fill_color = ap.Color.tomato

# Set the BoundsCheck mode to THROW_EXCEPTION_IF_DOES_NOT_FIT
graph.shapes.update_bounds_check_mode(
    ap.BoundsCheckMode.THROW_EXCEPTION_IF_DOES_NOT_FIT
)

# Add the rectangle to the graph
graph.shapes.add(rect)
```

## Related Graph Topics

- [Work with PDF graphs in Python](/pdf/python-net/working-with-graphs/)
- [Add rectangle shapes to PDF in Python](/pdf/python-net/add-rectangle/)
- [Add line shapes to PDF in Python](/pdf/python-net/add-line/)
- [Add ellipse shapes to PDF in Python](/pdf/python-net/add-ellipse/)
