---
title: Add PDF Pages in Java
linktitle: Adding Pages
type: docs
weight: 10
url: /java/add-pages/
description: Learn how to add or insert pages into PDF documents in Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add or insert PDF pages with Java
Abstract: This article explains how to add pages to PDF files using Aspose.PDF for Java. It covers inserting a blank page at a specific position, appending a page at the end of a document, and importing a page from another PDF.
---
Aspose.PDF for Java lets you insert blank pages or import pages from another document.

## Insert an empty page at a specific position

Use this example when you need to add a blank page in the middle of an existing PDF.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Insert a new page into the target position in the page collection.
1. Save the updated document.

```java
public static void insertEmptyPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().insert(2);
        document.save(outputFile.toString());
    }
}
```

## Append an empty page to the end

Use this example when you need to extend the document with a new blank last page.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Add a new page to the end of the page collection.
1. Save the modified PDF.

```java
public static void addEmptyPageToEnd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().add();
        document.save(outputFile.toString());
    }
}
```

## Add a page from another document

Use this example when you want to import a page from one PDF into another PDF.

1. Create the destination [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and open the source document.
1. Add any required destination content and import the target page from the source PDF.
1. Save the resulting document.

```java
public static void addPageFromAnotherDocument(Path inputFile, Path outputFile) {
    try (Document document = new Document();
         Document anotherDocument = new Document(inputFile.toString())) {
        document.getPages().add().getParagraphs().add(new TextFragment("This is first page!"));
        document.getPages().add(anotherDocument.getPages().get_Item(1));
        document.save(outputFile.toString());
    }
}
```
