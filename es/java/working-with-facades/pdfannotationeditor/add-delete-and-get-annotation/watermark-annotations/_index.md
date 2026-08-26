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
## Agregar una anotación de marca de agua

1. Abra el PDF de entrada y defina el rectángulo donde se colocará la anotación de la marca de agua.
2. Cree `WatermarkAnnotation`, agréguelo a la página y configure el estado y la opacidad del texto de la marca de agua.
3. Aplique las líneas de texto de la marca de agua y guarde el PDF modificado.

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
