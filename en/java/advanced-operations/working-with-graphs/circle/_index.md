---
title: Add Circle Shapes to PDF in Java
linktitle: Add Circle
type: docs
weight: 20
url: /java/add-circle/
description: Learn how to draw and fill circle shapes in PDF files in Java.
lastmod: "2026-06-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Draw circle shapes in PDF files using Java
Abstract: This article shows how to add circle shapes to PDF documents using Aspose.PDF for Java. It covers drawing circle outlines, filling circles with color, and placing text inside a circle shape.
---
## Add a circle outline

1. Create a new PDF document.
1. Add a page to the document.
1. Create a Graph container and add it to the page.
1. Create the circle shape and configure its geometry.
1. Add the shape to the Graph container.
1. Set the annotation or object properties required by the example.
1. Save the output PDF document.

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

1. Create a new PDF document.
1. Add a page to the document.
1. Create a Graph container and add it to the page.
1. Create the circle shape and configure its geometry.
1. Add the shape to the Graph container.
1. Set the annotation or object properties required by the example.
1. Save the output PDF document.

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
