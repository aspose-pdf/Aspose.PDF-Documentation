---
title: Add and Delete PDF Bookmarks in Java
linktitle: Add and Delete a Bookmark
type: docs
weight: 10
url: /java/add-and-delete-bookmark/
description: Learn how to add and delete bookmarks in PDF documents using Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add or remove bookmarks in PDF documents with Java
Abstract: This article shows how to create and delete bookmarks using Aspose.PDF for Java. The examples demonstrate adding a top-level bookmark, creating a child bookmark hierarchy, deleting all bookmarks, and removing a specific bookmark by title.
---
Use the document outline collection to manage bookmarks programmatically.

## Add a top-level bookmark

Use this example when the document should include a single top-level outline entry.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Create an [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) and configure its title, style, and action.
1. Add the bookmark to the document outlines and save the file.

```java
public static void addBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection pdfOutline = new OutlineItemCollection(document.getOutlines());
        pdfOutline.setTitle("Test Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);
        pdfOutline.setAction(new GoToAction(document.getPages().get_Item(1)));

        document.getOutlines().add(pdfOutline);
        document.save(outputFile.toString());
    }
}
```

## Add a child bookmark

This example creates a parent bookmark and nests a child bookmark under it.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Create parent and child [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) objects.
1. Add the child to the parent, add the parent to the outline collection, and save the document.

```java
public static void addChildBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection pdfOutline = new OutlineItemCollection(document.getOutlines());
        pdfOutline.setTitle("Parent Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        OutlineItemCollection pdfChildOutline = new OutlineItemCollection(document.getOutlines());
        pdfChildOutline.setTitle("Child Outline");
        pdfChildOutline.setItalic(true);
        pdfChildOutline.setBold(true);

        pdfOutline.add(pdfChildOutline);
        document.getOutlines().add(pdfOutline);
        document.save(outputFile.toString());
    }
}
```

## Delete all bookmarks

Use this approach when the entire outline collection should be removed from the document.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Delete the full outlines collection.
1. Save the cleaned output file.

```java
public static void deleteBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete();
        document.save(outputFile.toString());
    }
}
```

## Delete a specific bookmark

Use this example when one named bookmark should be removed without clearing the whole outline tree.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Delete the bookmark by title from the outlines collection.
1. Save the updated document.

```java
public static void deleteBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete("Child Outline");
        document.save(outputFile.toString());
    }
}
```
