---
title: Add Watermarks to PDF in Java
linktitle: Add Watermarks
type: docs
weight: 30
url: /java/add-watermarks/
description: Add styled text watermark artifacts to PDF pages in Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Watermarks in Java
Abstract: Add styled text watermark artifacts to PDF pages in Java.
---
Watermark artifacts let you place persistent visual markings on a page without mixing them into the main document content.

## Add a watermark artifact

Use this example when the page should display a centered text watermark with custom rotation, opacity, and background placement.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Create a [WatermarkArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkartifact/) and configure its text state and placement settings.
1. Add the watermark to the page and save the output file.

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

## Related artifact topics

- [Extract Watermark Details](/pdf/java/extract-watermarks/)
- [Remove Watermarks](/pdf/java/remove-watermarks/)
- [Work with PDF Artifacts in Java](/pdf/java/artifacts/)
