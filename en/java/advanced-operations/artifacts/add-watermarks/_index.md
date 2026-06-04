---
title: Add Watermarks to PDF in Java
linktitle: Adding Watermark
type: docs
weight: 30
url: /java/add-watermarks/
description: Learn how to add, extract, and delete watermark artifacts in PDF files using Aspose.PDF for Java.
lastmod: "2026-06-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to add watermark to PDF with Java
Abstract: This article explains how to add, inspect, and remove watermark artifacts in PDF documents using Aspose.PDF for Java. It covers creating a text watermark with alignment, rotation, opacity, and background settings, inspecting watermark artifacts on a page, and deleting them.
---
## Add a watermark artifact

1. Open the source PDF document.
1. Set the required text formatting options.
1. Set the annotation or object properties required by the example.
1. Create the required artifact and configure its appearance.
1. Add the artifact to the target page.
1. Save the updated PDF document.

```java
public static void addWatermarkArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextState textState = new TextState();
        textState.setFontSize(72);
        textState.setForegroundColor(Color.getBlueViolet());
        textState.setFontStyle(FontStyles.Bold);
        textState.setFont(FontRepository.findFont("Arial"));

        WatermarkArtifact watermark = new WatermarkArtifact();
        watermark.setTextAndState("WATERMARK", textState);
        watermark.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
        watermark.setArtifactVerticalAlignment(VerticalAlignment.Center);
        watermark.setRotation(60);
        watermark.setOpacity(0.2);
        watermark.setBackground(true);

        document.getPages().get_Item(1).getArtifacts().add(watermark);
        document.save(outputFile.toString());
    }
}
```
