---
title: Add and Delete a Bookmark 
linktitle: Add and Delete a Bookmark
type: docs
weight: 10
url: /java/add-and-delete-bookmark/
description: You can add a bookmark to a PDF document with Java. It is possible to delete all or particular bookmarks from a PDF document.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: 
Abstract: This article provides a comprehensive guide on managing bookmarks in PDF documents using the Aspose PDF Java library. It covers the creation and deletion of bookmarks, including adding parent and child bookmarks and removing all or specific bookmarks. The process begins with opening a PDF document with the `Document` object, followed by creating a bookmark using the `OutlineItemCollection`, and adding it to the document's `OutlineCollection`. Code snippets are provided to illustrate how to add bookmarks, including child bookmarks, and how to delete all bookmarks or specific ones by title. The article includes detailed instructions and example code, demonstrating the use of methods like `add`, `delete`, and `save` for manipulating bookmarks effectively.
---

## Add a Bookmark to a PDF Document

Bookmarks are held in the Document object's [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) collection, itself in the [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) collection.

To add a bookmark to a PDF:

1. Open a PDF document using [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object.
1. Create a bookmark and define its properties.
1. Add the [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) collection to the Outlines collection.

The following code snippet shows you how to add a bookmark in a PDF document.

```java
package com.aspose.pdf.examples;

import java.io.IOException;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.Bookmark;
import com.aspose.pdf.facades.Bookmarks;
import com.aspose.pdf.facades.PdfBookmarkEditor;

public class ExampleBookmarks {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Bookmarks/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Bookmarks\\";
        return _dataDir;
    }

    public static void AddBookmarks() throws IOException {

        Document pdfDocument = new Document(GetDataDir() + "AddBookmark.pdf");

        // Create a bookmark object
        OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfOutline.setTitle("Test Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        // Set the destination page number
        pdfOutline.setAction(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // Add a bookmark in the document's outline collection.
        pdfDocument.getOutlines().add(pdfOutline);

        // Save the update document
        pdfDocument.save(_dataDir + "AddBookmark_out.pdf");
    }
```

## Add a Child Bookmark to the PDF Document

Bookmarks can be nested, indicating a hierarchical relationship with parent and child bookmarks. This article explains how to add a child bookmark, that is, a second-level bookmark, to a PDF.

To add a child bookmark to a PDF file, first add a parent bookmark:

1. Open a document.
1. Add a bookmark to the [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection), defining its properties.
1. Add the OutlineItemCollection to the Document object's [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) collection.

The child bookmark is created just like the parent bookmark, explained above, but is added to the parent bookmark's Outlines collection

The following code snippets show how to add child bookmark to a PDF document.

```java
    public static void AddChildBookmark() {
        // Open document
        Document pdfDocument = new Document(GetDataDir() + "AddChildBookmark.pdf");

        // Create a parent bookmark object
        OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfOutline.setTitle("Parent Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        // Create a child bookmark object
        OutlineItemCollection pdfChildOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfChildOutline.setTitle("Child Outline");
        pdfChildOutline.setItalic(true);
        pdfChildOutline.setBold(true);

        // Add child bookmark in parent bookmark's collection
        pdfOutline.add(pdfChildOutline);
        // Add parent bookmark in the document's outline collection.
        pdfDocument.getOutlines().add(pdfOutline);

        // Save output
        pdfDocument.save(_dataDir + "AddChildBookmark_out.pdf");
    }
```

## Delete all Bookmarks from a PDF Document

All bookmarks in a PDF are held in the [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) collection. This article explains how to delete all bookmarks from a PDF file.

To delete all bookmarks from a PDF file:

1. Call the [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) collection's Delete method.
1. Save the modified file using the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object's Save method.

The following code snippets show how to delete all bookmarks from a PDF document.

```java
    public static void DeleteAllBookmarksFromPDFDocument() {
        // Open document
        Document pdfDocument = new Document(GetDataDir() + "DeleteAllBookmarks.pdf");

        // Delete all bookmarks
        pdfDocument.getOutlines().delete();

        // Save updated file
        pdfDocument.save(_dataDir + "DeleteAllBookmarks_out.pdf");
    }
```

## Delete a Particular Bookmark from a PDF Document

[Delete All Attachments from PDF document](https://docs.aspose.com/pdf/java/working-with-attachments/) showed how to delete all attachments from a PDF file. It is also possible to only remove specific attachments.

To delete a particular bookmark from a PDF file:

1. Pass the bookmark's title as parameter to the [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) collection's [Delete](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection#delete--) method.
1. Then save the updated file with the Document object Save method.

The [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class’ provides the [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) collection. The [Delete](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection#delete--) method removes any bookmark with the title passed to the method.

The following code snippets show how to delete a particular bookmark from the PDF document.

```java
    public static void DeleteParticularBookmarkPDFDocument() {
        // Open document
        Document pdfDocument = new Document(GetDataDir() + "DeleteParticularBookmark.pdf");

        // Delete particular outline by Title
        pdfDocument.getOutlines().delete("Child Outline");

        // Save updated file
        pdfDocument.save(_dataDir + "DeleteParticularBookmark_out.pdf");
    }
```
