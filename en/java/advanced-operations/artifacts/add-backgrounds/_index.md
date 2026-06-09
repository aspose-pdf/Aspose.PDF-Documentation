---
title: Add PDF Backgrounds in Java
linktitle: Adding backgrounds
type: docs
weight: 20
url: /java/add-backgrounds/
description: Learn how to add a background image or background color to PDF pages in Java using `BackgroundArtifact` with Aspose.PDF.
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to add background to PDF with Java
Abstract: This article explains how to add or remove PDF page backgrounds in Java using Aspose.PDF. It covers adding a background image, adjusting image opacity, applying a background color, and removing background artifacts from a page.
---
## Add a background image to a PDF page

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create the required [BackgroundArtifact](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/backgroundartifact/) and configure its appearance.
1. Add the [BackgroundArtifact](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/backgroundartifact/) to the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

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

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create the required [BackgroundArtifact](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/backgroundartifact/) and set the properties required by the example.
1. Configure the [BackgroundArtifact](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/backgroundartifact/) appearance, including opacity.
1. Add the artifact to the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

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
