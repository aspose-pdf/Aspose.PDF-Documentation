---
title: Add Arc Shapes to PDF in Java
linktitle: Add Arc
type: docs
weight: 10
url: /java/add-arc/
description: Learn how to draw and fill arc shapes in PDF files in Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Draw arc shapes in PDF files using Java
Abstract: This article shows how to add arc shapes to PDF documents using Aspose.PDF for Java. It covers drawing multiple outlined arcs with different colors and creating a filled arc segment by combining an arc with a closing line.
---
Aspose.PDF for Java uses `Graph` together with shape objects such as `Arc` and `Line` to render vector graphics.

## Add arc outlines

1. Create a new PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Add a [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) to the document.
1. Create a [Graph](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.drawing/graph/) container and add it to the page.
1. Create the [Arc](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.drawing/arc/) shape and configure its geometry.
1. Add the [Arc](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.drawing/arc/) to the [Graph](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.drawing/graph/) container.
1. Set the shape properties required by the example, including [Color](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/color/).
1. Save the output PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void addArc(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Arc arc1 = new Arc(100, 100, 95, 0, 90);
        arc1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(arc1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```

The full example adds three arcs with different radii, angles, and colors to the same graph.

## Add a filled arc segment

1. Create a new PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Add a [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) to the document.
1. Create a [Graph](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.drawing/graph/) container and add it to the page.
1. Create the [Line](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.drawing/line/) shape and configure its coordinates.
1. Create the [Arc](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.drawing/arc/) shape and configure its geometry.
1. Add the [Line](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.drawing/line/) and [Arc](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.drawing/arc/) to the [Graph](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.drawing/graph/) container.
1. Save the output PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void addArcFilled(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Arc arc = new Arc(100, 100, 95, 0, 90);
        arc.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().addItem(arc);

        Line line = new Line(new float[]{195, 100, 100, 100, 100, 195});
        line.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().addItem(line);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
