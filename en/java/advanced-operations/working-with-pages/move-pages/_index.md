---
title: Move PDF Pages in Java
linktitle: Moving PDF Pages
type: docs
weight: 100
url: /java/move-pages/
description: Learn how to move PDF pages within a document or between documents in Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Move PDF pages between documents in Java
Abstract: This article explains how to move pages in PDFs using Aspose.PDF for Java. It covers moving a single page or multiple pages to another document, and repositioning a page inside the same PDF.
---
Aspose.PDF for Java lets you move pages between documents or reposition pages within the same PDF.

## Move a page to another document

Use this example when a single page should be removed from the source PDF and saved into a separate document.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and create a destination document.
1. Add the target page to the destination and delete it from the source.
1. Save both documents.

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

Use this example when several pages should be transferred from the source PDF to a new document.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and create the destination document.
1. Copy the selected pages into the destination document.
1. Delete the moved pages from the source and save both files.

```java
public static void moveBunchPagesFromOneDocumentToAnother(Path inputFile, Path sourceOutputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString());
         Document dstDocument = new Document()) {
        Integer[] pages = {1, 2};
        for (Integer pageIndex : pages) {
            dstDocument.getPages().add(srcDocument.getPages().get_Item(pageIndex));
        }
        dstDocument.save(outputFile.toString());
        srcDocument.getPages().delete(pages);
        srcDocument.save(sourceOutputFile.toString());
    }
}
```

## Move a page within the same document

Use this example when a page should be repositioned to a new location in the same PDF.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Duplicate the target page into the new position and remove the original page entry.
1. Save the reordered document.

```java
public static void movePageInNewLocationInSameDocument(Path inputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString())) {
        srcDocument.getPages().add(srcDocument.getPages().get_Item(2));
        srcDocument.getPages().delete(2);
        srcDocument.save(outputFile.toString());
    }
}
```
