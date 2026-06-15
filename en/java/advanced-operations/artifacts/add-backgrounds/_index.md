---
title: Add PDF Backgrounds in Java
linktitle: Adding backgrounds
type: docs
weight: 20
url: /java/add-backgrounds/
description: Learn how to add a background image or background color to PDF pages in Java using `BackgroundArtifact` with Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to add background to PDF with Java
Abstract: This article explains how to add or remove PDF page backgrounds in Java using Aspose.PDF. It covers adding a background image, adjusting image opacity, applying a background color, and removing background artifacts from a page.
---
Background artifacts let you place non-content visual elements behind the main page content without changing the logical document text.

## Add a background image to a PDF

Use this example when the page should display an image as a background artifact.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and the image input stream.
1. Create a [BackgroundArtifact](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/backgroundartifact/) and assign the image stream.
1. Add the artifact to the target page and save the output PDF.

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

This example places a semi-transparent background image behind the page content.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and image stream.
1. Create a [BackgroundArtifact](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/backgroundartifact/), assign the image, and set the opacity.
1. Add the artifact to the page and save the document.

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

## Add a background color to a PDF

Use this example when the page should use a solid background color instead of an image.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create a [BackgroundArtifact](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/backgroundartifact/) and assign the background color.
1. Add the artifact to the page and save the output file.

```java
public static void addBackgroundColorToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundColor(Color.getDarkKhaki().toRgb());
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## Remove background artifacts

Use this approach when existing background artifacts should be deleted from the page.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Iterate through the page artifact collection in reverse order.
1. Delete artifacts whose type is pagination and subtype is background, then save the document.

```java
public static void removeBackground(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Background) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```
