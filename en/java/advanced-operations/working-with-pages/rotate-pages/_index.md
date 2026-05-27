---
title: Rotate PDF Pages in Java
linktitle: Rotating PDF Pages
type: docs
weight: 110
url: /java/rotate-pages/
description: Learn how to rotate PDF pages and change page orientation in Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rotate PDF pages with Java
Abstract: This article explains how to rotate PDF pages using Aspose.PDF for Java. The example iterates through all pages in a document, applies a 90-degree rotation, and saves the updated PDF.
---
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
