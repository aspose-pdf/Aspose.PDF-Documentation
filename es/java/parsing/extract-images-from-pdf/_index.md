---
title: Extract Images from PDF using Java
linktitle: Extract Images from PDF
type: docs
weight: 20
url: /java/extract-images-from-the-pdf-file/
description: Learn how to extract embedded images from PDF files with Aspose.PDF for Java.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to Extract Images from PDF via Java
Abstract: This article explains how to extract embedded images from a PDF document with Aspose.PDF for Java. It shows how to open the source PDF, access an image from the page resources collection, and save the extracted XImage to an external file.
---
Extract images from PDF pages when you need to reuse embedded graphics, inspect document assets, or export images for downstream processing.

1. Open the source PDF in a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instance and open an output stream for the extracted image file.
1. Get the target [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) from the document and access its `Resources.Images` collection.
1. Retrieve the required [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) object from that image collection by index.
1. Call `image.save(outputImage)` to write the extracted image bytes to the target stream.

```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```
