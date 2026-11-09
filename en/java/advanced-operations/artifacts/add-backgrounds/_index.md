---
title: Add PDF Backgrounds in Java
linktitle: Add Backgrounds
type: docs
weight: 20
url: /java/add-backgrounds/
description: Add image and solid-color backgrounds to PDF pages in Java and adjust image opacity.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Backgrounds in Java
Abstract: Add image and solid-color backgrounds to PDF pages in Java and adjust image opacity.
---
Background artifacts let you place non-content visual elements behind the main page content without changing the logical document text.

## Add a background image to a PDF

Use this example when the page should display an image as a background artifact.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) and the image input stream.
1. Create a [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) and assign the image stream.
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

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) and image stream.
1. Create a [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/), assign the image, and set the opacity.
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

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Create a [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) and assign the background color.
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

## Related artifact topics

- [Remove Backgrounds](/pdf/java/remove-backgrounds/)
- [Work with PDF Artifacts in Java](/pdf/java/artifacts/)
