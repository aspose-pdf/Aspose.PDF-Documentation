---
title: Check Shape Bounds in PDF Graphs with Java
linktitle: Check Shape Bounds
type: docs
weight: 70
url: /java/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Learn how to validate shape bounds in PDF graph collections in Java.
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Validate graph shape bounds in PDF files using Java
Abstract: This article shows how to validate shape bounds in Graph collections using Aspose.PDF for Java. It covers enabling strict bounds checking, attempting to add an out-of-range shape, and handling the resulting exception while still saving the document.
---
Use `BoundsCheckMode` when you need to ensure that shapes fit inside a graph container.

## Validate graph shape bounds

1. Create a new PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Add a [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) to the document.
1. Create a [Graph](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.drawing/graph/) container and add it to the page.
1. Create the [Rectangle](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.drawing/rectangle/) shape and configure its geometry.
1. Enable strict bounds checking and try to add the shape to the graph collection with `BoundsCheckMode`.
1. Handle the exception if the shape does not fit.
1. Save the output PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void checkShapeBounds(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(100.0, 100.0);
        graph.setTop(10);
        graph.setLeft(15);
        graph.setBorder(new BorderInfo(BorderSide.Box, 1, Color.getBlack()));
        page.getParagraphs().add(graph);

        Rectangle rectangle = new Rectangle(-1, 0, 50, 50);
        rectangle.getGraphInfo().setFillColor(Color.getTomato());
        try {
            graph.getShapes().updateBoundsCheckMode(BoundsCheckMode.ThrowExceptionIfDoesNotFit);
            graph.getShapes().addItem(rectangle);
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }

        document.save(outputFile.toString());
    }
}
```
