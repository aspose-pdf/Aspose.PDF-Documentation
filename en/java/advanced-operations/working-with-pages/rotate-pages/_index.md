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
## Rotate all pages in a PDF

1. Open the source PDF document used in this example.
2. Iterate through the page collection and apply the required rotation to each page.
3. Save the updated PDF document to preserve the new page orientation.

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
