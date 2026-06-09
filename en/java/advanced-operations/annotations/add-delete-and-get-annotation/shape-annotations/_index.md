---
title: Shape Annotations via Java
linktitle: Shape Annotations
type: docs
weight: 20
url: /java/shape-annotations/
description: Learn how to add, inspect, and delete square, circle, polygon, and polyline annotations in PDF documents using Aspose.PDF for Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Work with geometric PDF annotations in Java.
Abstract: This article explains how to create, inspect, and remove geometric annotations in PDF documents using Aspose.PDF for Java. It covers square, circle, polygon, and polyline annotations with color, opacity, popup, and point configuration.
---
## Add shape annotations

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create the [Rectangle](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/rectangle/) shape and configure its geometry.
1. Create the required shape annotation, such as [SquareAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/squareannotation/) or [PolygonAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/polygonannotation/), on the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Set the annotation or related object properties required by the example.
1. Add the annotation to the target page.
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Add the annotation to the page and save the modified PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

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

## Related annotation topics

- [Interactive Annotations](/pdf/java/interactive-annotations/)
- [Markup Annotations](/pdf/java/markup-annotations/)
- [Security Annotations](/pdf/java/security-annotations/)
- [Text Annotations](/pdf/java/text-based-annotations/)
- [Watermark Annotations](/pdf/java/watermark-annotations/)
- [Import and Export Annotations](/pdf/java/import-export-annotations/)
