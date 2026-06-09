---
title: Add Image Stamps to PDF in Java
linktitle: Image stamps in PDF File
type: docs
weight: 10
url: /java/image-stamps-in-pdf-page/
description: Learn how to add image stamps to PDF pages in Java.
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add image stamps and image backgrounds to PDF pages with Java
Abstract: This article explains how to add image stamps to PDF files using Aspose.PDF for Java. It covers image stamps with positioning, rotation, opacity, and quality control, and using an image as the background of a floating box.
---
## Add an image stamp

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create the [ImageStamp](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/imagestamp/) object from the source image file.
1. Configure the required stamp placement, size, and opacity options.
1. Set the required [Rotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/rotation/) value for the stamp.
1. Add the configured [ImageStamp](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/imagestamp/) to the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

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
