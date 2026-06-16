---
title: Add Watermarks to PDF in Java
linktitle: Adding Watermark
type: docs
weight: 30
url: /java/add-watermarks/
description: Learn how to add, extract, and delete watermark artifacts in PDF files using Aspose.PDF for Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to add watermark to PDF with Java
Abstract: This article explains how to add, inspect, and remove watermark artifacts in PDF documents using Aspose.PDF for Java. It covers creating a text watermark with alignment, rotation, opacity, and background settings, inspecting watermark artifacts on a page, and deleting them.
---
Watermark artifacts let you place persistent visual markings on a page without mixing them into the main document content.

## Extract watermark artifacts from a PDF

Use this example when you need to inspect existing watermark artifacts and read their text or position.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Iterate through the artifact collection of the target page.
1. Filter watermark pagination artifacts and print their text and rectangles.

```java
public static void extractWatermarkFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Artifact artifact : document.getPages().get_Item(1).getArtifacts()) {
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                System.out.println(artifact.getText() + " " + artifact.getRectangle());
            }
        }
    }
}
```

## Add a watermark artifact

Use this example when the page should display a centered text watermark with custom rotation, opacity, and background placement.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create a [WatermarkArtifact](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/watermarkartifact/) and configure its text state and placement settings.
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

## Delete watermark artifacts

Use this approach when existing watermark artifacts should be removed from the page.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Iterate through the page artifact collection in reverse order.
1. Delete pagination artifacts whose subtype is watermark, then save the document.

```java
public static void deleteWatermarkArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```
