---
title: Watermark Annotations using Java
linktitle: Watermark Annotations
type: docs
weight: 70
url: /java/watermark-annotations/
description: Learn how to add, inspect, and delete watermark annotations in PDF documents using Aspose.PDF for Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Work with watermark annotations in PDF files using Java.
Abstract: This article explains how to create, inspect, and remove watermark annotations in PDF documents using Aspose.PDF for Java. It covers adding a text watermark annotation with custom text state and opacity, reading existing watermark annotation areas, and deleting watermark annotations.
---
Watermark annotations let you place reusable overlay content on a page while still managing it through the annotation collection.

## Add a watermark annotation

Use this example when you need a text watermark annotation with custom font settings and opacity.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Create a [WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkannotation/) and add it to the page.
1. Configure the [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/), watermark text, and opacity, then save the document.

```java
public static void watermarkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        WatermarkAnnotation watermarkAnnotation = new WatermarkAnnotation(
                page,
                new Rectangle(100, 100, 400, 200, true));

        page.getAnnotations().add(watermarkAnnotation);

        TextState textState = new TextState();
        textState.setForegroundColor(Color.getBlue());
        textState.setFontSize(25);
        textState.setFont(FontRepository.findFont("Arial"));

        watermarkAnnotation.setOpacity(0.5);
        watermarkAnnotation.setTextAndState(new String[]{"HELLO", "Line 1", "Line 2"}, textState);

        document.save(outputFile.toString());
    }
}
```

## Get watermark annotations

This example scans the annotation collection and prints the rectangle of each watermark annotation.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterate through the annotations on the target page.
1. Filter annotations by [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Watermark` and print their rectangles.

```java
public static void watermarkGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation a : document.getPages().get_Item(1).getAnnotations()) {
            if (a.getAnnotationType() == AnnotationType.Watermark) {
                System.out.println(a.getRect());
            }
        }
    }
}
```

## Delete watermark annotations

Use this approach when existing watermark annotations should be removed from the document.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Collect annotations of type [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Watermark`.
1. Delete the collected annotations and save the output file.

```java
public static void watermarkDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation a : document.getPages().get_Item(1).getAnnotations()) {
            if (a.getAnnotationType() == AnnotationType.Watermark) {
                toDelete.add(a);
            }
        }
        for (Annotation a : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(a);
        }
        document.save(outputFile.toString());
    }
}
```

## Related annotation topics

- [Interactive Annotations](/pdf/java/interactive-annotations/)
- [Markup Annotations](/pdf/java/markup-annotations/)
- [Security Annotations](/pdf/java/security-annotations/)
- [Shape Annotations](/pdf/java/shape-annotations/)
- [Text Annotations](/pdf/java/text-based-annotations/)
- [Import and Export Annotations](/pdf/java/import-export-annotations/)
