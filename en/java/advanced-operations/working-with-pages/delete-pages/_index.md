---
title: Delete PDF Pages in Java
linktitle: Deleting PDF Pages
type: docs
weight: 80
url: /java/delete-pages/
description: Learn how to delete pages from PDF files in Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Delete one or more PDF pages in Java
Abstract: This article explains how to remove pages from PDF files using Aspose.PDF for Java. It covers deleting a single page and deleting multiple pages at once through the page collection API.
---
## Delete one page

1. Load the PDF document and locate the target content.
2. Use the Aspose.PDF objects shown in the example to delete one page.
3. Save the document after the content is removed.

```java
public static void deletePage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(2);
        document.save(outputFile.toString());
    }
}
```

## Delete multiple pages

`deleteBunchPages` removes pages `2`, `3`, and `4` by passing an `Integer[]` to `document.getPages().delete(...)`.
