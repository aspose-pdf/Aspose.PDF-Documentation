---
title: Move PDF Pages in Java
linktitle: Moving PDF Pages
type: docs
weight: 100
url: /java/move-pages/
description: Learn how to move PDF pages within a document or between documents in Java.
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Move PDF pages between documents in Java
Abstract: This article explains how to move pages in PDFs using Aspose.PDF for Java. It covers moving a single page or multiple pages to another document, and repositioning a page inside the same PDF.
---
## Move a page to another document

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create the destination PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Add the required [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) from the source document to the destination document.
1. Delete the moved [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) from the source document.
1. Save both PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) objects.

```java
public static void movePageFromOneDocumentToAnother(Path inputFile, Path sourceOutputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString());
         Document anotherDocument = new Document()) {
        anotherDocument.getPages().add(document.getPages().get_Item(2));
        document.getPages().delete(2);
        document.save(sourceOutputFile.toString());
        anotherDocument.save(outputFile.toString());
    }
}
```
