---
title: Crop PDF Pages in Java
linktitle: Cropping PDF Pages
type: docs
weight: 70
url: /java/crop-pages/
description: Learn how to crop PDF pages and adjust crop, trim, bleed, and media boxes in Java.
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crop pages and adjust page boxes in PDF files with Java
Abstract: This article explains how to crop PDF pages using Aspose.PDF for Java. It covers assigning a new crop rectangle to the crop, trim, art, and bleed boxes, and cropping a page automatically based on detected image content.
---
## Crop a page to a fixed rectangle

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create the target [Rectangle](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/rectangle/) crop region.
1. Apply the crop region to the required [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) boxes.
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void cropPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle newBox = new Rectangle(200, 220, 2170, 1520, true);
        document.getPages().get_Item(1).setCropBox(newBox);
        document.getPages().get_Item(1).setTrimBox(newBox);
        document.getPages().get_Item(1).setArtBox(newBox);
        document.getPages().get_Item(1).setBleedBox(newBox);
        document.save(outputFile.toString());
    }
}
```
