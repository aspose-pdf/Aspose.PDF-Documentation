---
title: Add Watermarks to PDF in Java
linktitle: Adding Watermark
type: docs
weight: 30
url: /java/add-watermarks/
description: Learn how to add, extract, and delete watermark artifacts in PDF files using Aspose.PDF for Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to add watermark to PDF with Java
Abstract: This article explains how to add, inspect, and remove watermark artifacts in PDF documents using Aspose.PDF for Java. It covers creating a text watermark with alignment, rotation, opacity, and background settings, inspecting watermark artifacts on a page, and deleting them.
---
## Add a watermark artifact

1. Open or create the PDF document used in this example.
2. Configure the Aspose.PDF objects needed to add a watermark artifact.
3. Save the result to apply the change.

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


