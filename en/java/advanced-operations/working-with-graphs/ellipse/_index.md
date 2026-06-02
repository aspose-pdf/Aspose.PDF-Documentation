---
title: Add Ellipse Shapes to PDF in Java
linktitle: Add Ellipse
type: docs
weight: 60
url: /java/add-ellipse/
description: Learn how to draw, fill, and label ellipse shapes in PDF files in Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Draw ellipse shapes in PDF files using Java
Abstract: This article shows how to add ellipse shapes to PDF documents using Aspose.PDF for Java. It covers outlined ellipses, filled ellipses, and placing text fragments inside ellipse shapes.
---
## Add ellipse outlines

1. Open or create the PDF document used in this example.
2. Configure the Aspose.PDF objects needed to add ellipse outlines.
3. Save the result to apply the change.

```java
public static void addEllipse(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Ellipse ellipse1 = new Ellipse(150, 100, 120, 60);
        ellipse1.getGraphInfo().setColor(Color.getGreenYellow());
        ellipse1.setText(new TextFragment("Ellipse"));
        graph.getShapes().addItem(ellipse1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```

The full example adds two different outline ellipses to the same graph.

## Add filled ellipses

`createEllipseFilled` fills two ellipses with `Color.getGreenYellow()` and `Color.getDarkRed()`.

## Add text inside ellipses

1. Open or create the PDF document used in this example.
2. Configure the Aspose.PDF objects needed to add text inside ellipses.
3. Save the result to apply the change.

```java
public static void addTextInsideEllipse(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        TextFragment textFragment = new TextFragment("Ellipse");
        textFragment.getTextState().setFont(FontRepository.findFont("Helvetica"));
        textFragment.getTextState().setFontSize(24);

        Ellipse ellipse1 = new Ellipse(100, 100, 120, 180);
        ellipse1.getGraphInfo().setFillColor(Color.getGreenYellow());
        ellipse1.setText(textFragment);
        graph.getShapes().addItem(ellipse1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
