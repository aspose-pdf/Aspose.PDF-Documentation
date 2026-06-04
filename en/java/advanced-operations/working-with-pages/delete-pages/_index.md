---
title: Delete PDF Pages in Java
linktitle: Deleting PDF Pages
type: docs
weight: 80
url: /java/delete-pages/
description: Learn how to delete pages from PDF files in Java.
lastmod: "2026-06-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Delete one or more PDF pages in Java
Abstract: This article explains how to remove pages from PDF files using Aspose.PDF for Java. It covers deleting a single page and deleting multiple pages at once through the page collection API.
---
## Delete one page

1. Open the source PDF document.
1. Delete the required page range from the document.
1. Save the updated PDF document.

```java
public static void deletePage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(2);
        document.save(outputFile.toString());
    }
}
```
