---
title: Rotate PDF Pages in Java
linktitle: Rotating PDF Pages
type: docs
weight: 110
url: /java/rotate-pages/
description: Learn how to rotate PDF pages and change page orientation in Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rotate PDF pages with Java
Abstract: This article explains how to rotate PDF pages using Aspose.PDF for Java. The example iterates through all pages in a document, applies a 90-degree rotation, and saves the updated PDF.
---
Use the page rotation API when you need to change orientation across one or more pages.

## Rotate all pages by 90 degrees

Use this example when every page in the document should be rotated clockwise.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Iterate through all [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) objects and set the rotation value.
1. Save the updated PDF.

```java
public static void rotatePage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            page.setRotate(Rotation.on90);
        }
        document.save(outputFile.toString());
    }
}
```
