---
title: Add PDF Pages in Java
linktitle: Adding Pages
type: docs
weight: 10
url: /java/add-pages/
description: Learn how to add or insert pages into PDF documents in Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add or insert PDF pages with Java
Abstract: This article explains how to add pages to PDF files using Aspose.PDF for Java. It covers inserting a blank page at a specific position, appending a page at the end of a document, and importing a page from another PDF.
---
## Insert an empty page

```java
public static void insertEmptyPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().insert(2);
        document.save(outputFile.toString());
    }
}
```

## Add an empty page to the end

`addEmptyPageToEnd` uses `document.getPages().add()` and then saves the updated PDF.

## Add a page from another document

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
