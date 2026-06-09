---
title: Extract PDF Pages in Java
linktitle: Extracting PDF Pages
type: docs
weight: 80
url: /java/extract-pages/
description: Learn how to extract single or multiple PDF pages into new files in Java.
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract PDF pages into new documents with Java
Abstract: This article explains how to extract pages from PDF files using Aspose.PDF for Java. It covers copying a single page and extracting multiple pages into a separate destination document using 1-based page indexing.
---
## Extract a single page

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create the destination PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Add the required [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) from the source document to the destination document.
1. Save the extracted PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void extractPage(Path inputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString());
         Document dstDocument = new Document()) {
        dstDocument.getPages().add(srcDocument.getPages().get_Item(2));
        dstDocument.save(outputFile.toString());
    }
}
```
