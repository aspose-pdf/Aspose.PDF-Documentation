---
title: Extract PDF Pages in Java
linktitle: Extracting PDF Pages
type: docs
weight: 80
url: /java/extract-pages/
description: Learn how to extract single or multiple PDF pages into new files in Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract PDF pages into new documents with Java
Abstract: This article explains how to extract pages from PDF files using Aspose.PDF for Java. It covers copying a single page and extracting multiple pages into a separate destination document using 1-based page indexing.
---
Aspose.PDF for Java lets you copy selected pages into a new destination document.

## Extract a single page

Use this example when you need to save one page from the source PDF into a separate document.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) and create a destination document.
1. Copy the target page into the destination page collection.
1. Save the new PDF.

```java
public static void extractPage(Path inputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString());
         Document dstDocument = new Document()) {
        dstDocument.getPages().add(srcDocument.getPages().get_Item(2));
        dstDocument.save(outputFile.toString());
    }
}
```

## Extract multiple pages

Use this example when you need to copy several pages into a separate PDF.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) and create a destination document.
1. Iterate through the selected page indexes and add them to the destination.
1. Save the extracted-pages document.

```java
public static void extractBunchPages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString());
         Document anotherDocument = new Document()) {
        Integer[] pages = {2, 3};
        for (Integer pageIndex : pages) {
            anotherDocument.getPages().add(document.getPages().get_Item(pageIndex));
        }
        anotherDocument.save(outputFile.toString());
    }
}
```
