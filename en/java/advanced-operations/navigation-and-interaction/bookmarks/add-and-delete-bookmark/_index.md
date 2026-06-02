---
title: Add and Delete PDF Bookmarks in Java
linktitle: Add and Delete a Bookmark
type: docs
weight: 10
url: /java/add-and-delete-bookmark/
description: Learn how to add and delete bookmarks in PDF documents using Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add or remove bookmarks in PDF documents with Java
Abstract: This article shows how to create and delete bookmarks using Aspose.PDF for Java. The examples demonstrate adding a top-level bookmark, creating a child bookmark hierarchy, deleting all bookmarks, and removing a specific bookmark by title.
---
Use the document outline collection to manage bookmarks programmatically.

## Add a bookmark

1. Open or create the PDF document used in this example.
2. Configure the Aspose.PDF objects needed to add a bookmark.
3. Save the result to apply the change.

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

`addChildBookmark` creates a parent `OutlineItemCollection`, adds a child outline to it, and then appends the parent to `document.getOutlines()`.

## Delete bookmarks

The Java examples also include:

- `deleteBookmarks` to remove the full outline collection with `document.getOutlines().delete()`.
- `deleteBookmark` to remove a specific item by title with `document.getOutlines().delete("Child Outline")`.
