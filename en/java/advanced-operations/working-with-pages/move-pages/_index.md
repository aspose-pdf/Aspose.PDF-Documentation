---
title: Move PDF Pages in Java
linktitle: Moving PDF Pages
type: docs
weight: 100
url: /java/move-pages/
description: Learn how to move PDF pages within a document or between documents in Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Move PDF pages between documents in Java
Abstract: This article explains how to move pages in PDFs using Aspose.PDF for Java. It covers moving a single page or multiple pages to another document, and repositioning a page inside the same PDF.
---
## Move a page to another document

1. Open the PDF document and locate the target page or content.
2. Apply the Aspose.PDF operations shown in the example to move a page to another document.
3. Save the document to preserve the change.

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

## Move multiple pages to another document

`moveBunchPagesFromOneDocumentToAnother` copies the selected pages to a destination document, saves it, then deletes those pages from the source.

## Move a page inside the same document

`movePageInNewLocationInSameDocument` re-adds page `2` to the end of the page collection and then deletes the original page `2`.
