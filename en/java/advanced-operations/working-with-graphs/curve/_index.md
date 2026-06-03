---
title: Add Curve Shapes to PDF in Java
linktitle: Add Curve
type: docs
weight: 30
url: /java/add-curve/
description: Learn how to draw and fill curve shapes in PDF files in Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Draw curve shapes in PDF files using Java
Abstract: This article shows how to add curve shapes to PDF documents using Aspose.PDF for Java. It covers creating a curve from coordinate arrays and applying either stroke color or fill color inside a Graph container.
---
Curves in Aspose.PDF for Java are defined by a float coordinate array passed to `Curve`.

## Add a curve outline

1. Open or create the PDF document used in this example.
2. Configure the Aspose.PDF objects needed to add a curve outline.
3. Save the result to apply the change.

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
