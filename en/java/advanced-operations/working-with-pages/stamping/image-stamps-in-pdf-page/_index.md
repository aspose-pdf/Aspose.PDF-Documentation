---
title: Add Image Stamps to PDF in Java
linktitle: Image stamps in PDF File
type: docs
weight: 10
url: /java/image-stamps-in-pdf-page/
description: Learn how to add image stamps to PDF pages in Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add image stamps and image backgrounds to PDF pages with Java
Abstract: This article explains how to add image stamps to PDF files using Aspose.PDF for Java. It covers image stamps with positioning, rotation, opacity, and quality control, and using an image as the background of a floating box.
---
Aspose.PDF for Java supports image stamps as overlays and image-backed layout elements.

## Add an image stamp

Use this example when a page should display an image stamp with custom placement and opacity.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create an [ImageStamp](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/imagestamp/) and configure its appearance.
1. Add the stamp to the page and save the document.

```java
public static void addImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImageStamp imageStamp = new ImageStamp(imageFile.toString());
        imageStamp.setBackground(true);
        imageStamp.setXIndent(100);
        imageStamp.setYIndent(100);
        imageStamp.setHeight(300);
        imageStamp.setWidth(300);
        imageStamp.setRotate(Rotation.on270);
        imageStamp.setOpacity(0.5);

        document.getPages().get_Item(1).addStamp(imageStamp);
        document.save(outputFile.toString());
    }
}
```

## Add an image stamp with quality control

Use this example when you need to adjust the rendering quality of the image stamp.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create an [ImageStamp](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/imagestamp/) and set the quality value.
1. Add the stamp to the page and save the result.

```java
public static void addImageStampWithQualityControl(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImageStamp imageStamp = new ImageStamp(imageFile.toString());
        imageStamp.setQuality(10);
        document.getPages().get_Item(1).addStamp(imageStamp);
        document.save(outputFile.toString());
    }
}
```

## Use an image as a floating box background

Use this example when an image should serve as the background of a styled layout container.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and access the target page.
1. Create a [FloatingBox](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/floatingbox/) with text and border settings.
1. Set the background image, add the box to the page, and save the document.

```java
public static void addImageAsBackgroundInFloatingBox(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        FloatingBox box = new FloatingBox(200.0f, 100.0f);
        box.setLeft(40);
        box.setTop(80);
        box.setHorizontalAlignment(HorizontalAlignment.Center);
        box.getParagraphs().add(new TextFragment("Text in Floating Box"));
        box.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        Image image = new Image();
        image.setFile(imageFile.toString());
        box.setBackgroundImage(image);
        box.setBackgroundColor(Color.getYellow());
        page.getParagraphs().add(box);

        document.save(outputFile.toString());
    }
}
```
