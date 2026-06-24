---
title: Add Circle Shapes to PDF in Java
linktitle: Add Circle
type: docs
weight: 20
url: /java/add-circle/
description: Learn how to draw and fill circle shapes in PDF files in Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Draw circle shapes in PDF files using Java
Abstract: This article shows how to add circle shapes to PDF documents using Aspose.PDF for Java. It covers drawing circle outlines, filling circles with color, and placing text inside a circle shape.
---
## Add a circle outline

1. Create a new PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Add a [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) to the document.
1. Create a [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) container and add it to the page.
1. Create the [Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) shape and configure its geometry.
1. Add the [Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) to the [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) container.
1. Set the shape properties required by the example, including [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. Save the output PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addCircle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Circle circle = new Circle(100, 100, 40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(circle);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```

## Add a filled circle with text

1. Create a new PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Add a [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) to the document.
1. Create a [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) container and add it to the page.
1. Create the [Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) shape and configure its geometry.
1. Add the [Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) to the [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) container.
1. Set the shape properties required by the example, including [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) and [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. Save the output PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addCircleFilled(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Circle circle = new Circle(100, 100, 40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());
        circle.getGraphInfo().setFillColor(Color.getGreen());
        circle.setText(new TextFragment("Circle"));
        graph.getShapes().addItem(circle);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
