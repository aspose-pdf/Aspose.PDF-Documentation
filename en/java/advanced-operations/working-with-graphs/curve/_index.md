---
title: Add Curve Shapes to PDF in Java
linktitle: Add Curve
type: docs
weight: 30
url: /java/add-curve/
description: Learn how to draw and fill curve shapes in PDF files in Java.
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Draw curve shapes in PDF files using Java
Abstract: This article shows how to add curve shapes to PDF documents using Aspose.PDF for Java. It covers creating a curve from coordinate arrays and applying either stroke color or fill color inside a Graph container.
---
Curves in Aspose.PDF for Java are defined by a float coordinate array passed to `Curve`.

## Add a curve outline

1. Create a new PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Add a [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) to the document.
1. Create a [Graph](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.drawing/graph/) container and add it to the page.
1. Create the [Curve](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.drawing/curve/) shape and configure its control points.
1. Add the [Curve](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.drawing/curve/) to the [Graph](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.drawing/graph/) container.
1. Set the shape properties required by the example, including [Color](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/color/).
1. Save the output PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void addCurve(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Curve curve1 = new Curve(new float[]{10, 10, 50, 60, 70, 10, 100, 120});
        curve1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(curve1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
