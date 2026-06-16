---
title: Watermark Annotations using Java
linktitle: Watermark Annotations
type: docs
weight: 70
url: /java/pdfannotationeditor-class/watermark-annotations/
description: Learn how to add, inspect, and delete watermark annotations in PDF documents using Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Work with watermark annotations in PDF files using Java
Abstract: This article explains how to create, inspect, and remove watermark annotations in PDF documents using Java. It covers adding a text watermark annotation with custom text state and opacity, reading existing watermark annotation areas, and deleting watermark annotations.
---
## Add a watermark annotation

1. Open the input PDF and define the rectangle where the watermark annotation will be placed.
2. Create the `WatermarkAnnotation`, add it to the page, and configure the watermark text state and opacity.
3. Apply the watermark text lines and save the modified PDF.

```java
public static void watermarkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        WatermarkAnnotation watermarkAnnotation = new WatermarkAnnotation(
                document.getPages().get_Item(1), new Rectangle(100, 0, 400, 100, true));

        document.getPages().get_Item(1).getAnnotations().add(watermarkAnnotation);

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
