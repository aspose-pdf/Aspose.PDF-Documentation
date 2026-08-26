---
title: Delete PDF Pages in Java
linktitle: Deleting PDF Pages
type: docs
weight: 80
url: /java/delete-pages/
description: Learn how to delete pages from PDF files in Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Delete one or more PDF pages in Java
Abstract: This article explains how to remove pages from PDF files using Aspose.PDF for Java. It covers deleting a single page and deleting multiple pages at once through the page collection API.
---
Use the document page collection when you need to remove one or more pages from a PDF.

## Delete a single page

Use this example when you need to remove one page by its index.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Delete the target page from the page collection.
1. Save the updated document.

```java
public static void deletePage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(2);
        document.save(outputFile.toString());
    }
}
```

## Delete multiple pages

Use this example when several pages should be removed in one operation.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Pass the page indexes to delete from the page collection.
1. Save the modified PDF.

```java
public static void deleteBunchPages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(new Integer[]{2, 3, 4});
        document.save(outputFile.toString());
    }
}
```
