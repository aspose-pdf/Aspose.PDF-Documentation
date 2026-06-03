---
title: Shape Annotations via Java
linktitle: Shape Annotations
type: docs
weight: 40
url: /java/pdfannotationeditor-class/shape-annotations/
description: Learn how to add, inspect, and delete square, circle, polygon, and polyline annotations in PDF documents using Java.
lastmod: "2026-06-03"
TechArticle: true
AlternativeHeadline: Work with geometric PDF annotations in Java
Abstract: This article explains how to create, inspect, and remove geometric annotations in PDF documents using Java. It covers square, circle, polygon, and polyline annotations with color, opacity, popup, and point configuration.
---
## Add shape annotations

1. Open the input PDF and choose the page and rectangle that will contain the shape annotation.
2. Create the required shape annotation, then set its title, colors, opacity, and points when needed.
3. Add the annotation to the page and save the modified PDF.

```java
public static void squareAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        SquareAnnotation squareAnnotation = new SquareAnnotation(
                document.getPages().get_Item(1), new Rectangle(60, 600, 250, 450, true));
        squareAnnotation.setTitle("John Smith");
        squareAnnotation.setColor(Color.getBlue());
        squareAnnotation.setInteriorColor(Color.getBlueViolet());
        squareAnnotation.setOpacity(0.25);

        document.getPages().get_Item(1).getAnnotations().add(squareAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void polygonAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PolygonAnnotation polygonAnnotation = new PolygonAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(200, 300, 400, 400, true),
                new Point[]{
                        new Point(200, 300),
                        new Point(220, 300),
                        new Point(250, 330),
                        new Point(300, 304),
                        new Point(300, 400)
                });
        polygonAnnotation.setTitle("John Smith");
        polygonAnnotation.setColor(Color.getBlue());
        polygonAnnotation.setInteriorColor(Color.getBlueViolet());
        polygonAnnotation.setOpacity(0.25);

        document.getPages().get_Item(1).getAnnotations().add(polygonAnnotation);
        document.save(outputFile.toString());
    }
}
```

