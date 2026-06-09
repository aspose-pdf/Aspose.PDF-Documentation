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
## Insert an empty page

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Insert a new [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) at the required position.
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

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

1. Create the destination PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) that contains the page to import.
1. Add a [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) to the destination document.
1. Create a [TextFragment](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textfragment/) and add it to the first page.
1. Import the required [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) from the source document into the destination document.
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

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
