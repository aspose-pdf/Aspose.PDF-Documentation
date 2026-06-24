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

Use this example when you need to inspect the top-level bookmark entries in the document outline.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterate through the outlines collection.
1. Read and print the bookmark title, style, and color values.

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

This example uses `PdfBookmarkEditor` to extract bookmark titles, levels, page numbers, and actions.

1. Bind the source PDF to [PdfBookmarkEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdfbookmarkeditor/).
1. Extract the bookmark collection and iterate through it.
1. Print the level, title, page number, and action information for each bookmark.

```java
public static void getBookmarkPageNumber(Path inputFile) {
    PdfBookmarkEditor bookmarkEditor = new PdfBookmarkEditor();
    try {
        bookmarkEditor.bindPdf(inputFile.toString());
        for (Bookmark bookmark : bookmarkEditor.extractBookmarks()) {
            String levelSeparator = "";
            for (int i = 0; i < bookmark.getLevel(); i++) {
                levelSeparator += "----";
            }

            System.out.println(levelSeparator + " Title: " + bookmark.getTitle());
            System.out.println(levelSeparator + " Page Number: " + bookmark.getPageNumber());
            System.out.println(levelSeparator + " Page Action: " + bookmark.getAction());
        }
    } finally {
        bookmarkEditor.close();
    }
}
```

## Get child bookmarks

Use this example when you need to inspect both top-level and nested outline items.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterate through the top-level outlines and print their properties.
1. Detect child bookmarks, then iterate through them and print their properties.

```java
public static void getChildBookmarks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection outlineItem = document.getOutlines().get_Item(i);
            System.out.println(outlineItem.getTitle());
            System.out.println(outlineItem.getItalic());
            System.out.println(outlineItem.getBold());
            System.out.println(outlineItem.getColor());
            int count = outlineItem.size();
            if (count > 0) {
                System.out.println("Child Bookmarks");
                for (int j = 1; j <= outlineItem.size(); j++) {
                    OutlineItemCollection childOutlineItem = outlineItem.get_Item(j);
                    System.out.println(childOutlineItem.getTitle());
                    System.out.println(childOutlineItem.getItalic());
                    System.out.println(childOutlineItem.getBold());
                    System.out.println(childOutlineItem.getColor());
                }
            }
        }
    }
}
```

## Update bookmarks

Use this example when an existing bookmark title and style should be modified.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Access the target outline item and its child bookmark.
1. Update the bookmark properties and save the document.

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

## Expand bookmarks by default

Use this example when the bookmark panel should open and show expanded outline items when the document is displayed.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Set the page mode to use outlines and mark each outline item as open.
1. Save the updated document.

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
