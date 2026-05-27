---
title: Add PDF Backgrounds in Java
linktitle: Adding backgrounds
type: docs
weight: 20
url: /java/add-backgrounds/
description: Learn how to add a background image or background color to PDF pages in Java using `BackgroundArtifact` with Aspose.PDF.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to add background to PDF with Java
Abstract: This article explains how to add or remove PDF page backgrounds in Java using Aspose.PDF. It covers adding a background image, adjusting image opacity, applying a background color, and removing background artifacts from a page.
---
## Add a background image to a PDF page

```java
public static void addBackgroundImageToPdf(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundImage(imageStream);
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## Add a background image with opacity

```java
public static void addBackgroundImageWithOpacityToPdf(Path inputFile, Path imageFile, Path outputFile)
        throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundImage(imageStream);
        artifact.setOpacity(0.5);
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## Add a background color or remove background artifacts

`ArtifactsBackgroundsExamples.java` also includes:

- `addBackgroundColorToPdf` to apply a color-based background artifact
- `removeBackground` to delete page artifacts where subtype is `Background`
