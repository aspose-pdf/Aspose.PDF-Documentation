---
title: Get, Update, and Expand PDF Bookmarks in Java
linktitle: Get, Update and Expand a Bookmark
type: docs
weight: 20
url: /java/get-update-and-expand-bookmark/
description: Learn how to retrieve, update, and expand bookmarks in PDF documents using Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inspect bookmark properties and expand outlines in PDF files with Java
Abstract: This article explains how to read, update, and expand bookmarks using Aspose.PDF for Java. It covers iterating through outline items, extracting bookmark page numbers with PdfBookmarkEditor, reading child bookmarks, updating bookmark titles and style, and forcing outlines to open when the document is displayed.
---
Aspose.PDF for Java exposes bookmarks through both the document outline model and the `PdfBookmarkEditor` facade.

## Get bookmark properties

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create or access the bookmark [OutlineItemCollection](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/outlineitemcollection/).
1. Read the returned values from the [OutlineItemCollection](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/outlineitemcollection/) or continue with your next processing step.

```java
public static void getBookmarks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection outlineItem = document.getOutlines().get_Item(i);
            System.out.println(outlineItem.getTitle());
            System.out.println(outlineItem.getItalic());
            System.out.println(outlineItem.getBold());
            System.out.println(outlineItem.getColor());
        }
    }
}
```

## Get bookmark page numbers

`getBookmarkPageNumber` binds the PDF to `PdfBookmarkEditor`, calls `extractBookmarks()`, and reads each bookmark's level, page number, and action.

## Update a bookmark

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create or access the bookmark [OutlineItemCollection](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/outlineitemcollection/).
1. Set the bookmark properties required by the example.
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void updateBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection outline = document.getOutlines().get_Item(1);
        OutlineItemCollection childOutline = outline.get_Item(1);
        childOutline.setTitle("Updated Outline");
        childOutline.setItalic(true);
        childOutline.setBold(true);

        document.save(outputFile.toString());
    }
}
```

## Expand bookmarks when the document opens

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create or access the bookmark [OutlineItemCollection](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/outlineitemcollection/).
1. Set the properties required by the example, including [PageMode](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pagemode/).
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void expandedBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setPageMode(PageMode.UseOutlines);
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection item = document.getOutlines().get_Item(i);
            item.setOpen(true);
        }
        document.save(outputFile.toString());
    }
}
```
