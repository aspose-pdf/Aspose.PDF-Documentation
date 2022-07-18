---
title: Get, Update and Expand a Bookmark 
linktitle: Get, Update and Expand a Bookmark
type: docs
weight: 20
url: /java/get-update-and-expand-bookmark/
description: This article describes how to use bookmarks in a PDF file. With our Java library, you can get bookmarks from the PDF file, get a bookmarks page number, update bookmarks in a PDF Document, and expand bookmarks when viewing a document.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Get Bookmarks

The [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object’s [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) collection contains all a PDF file’s bookmarks. This article explains how to get bookmarks from a PDF file, and how to get which page a particular bookmark is on.

To get the bookmarks, loop through the [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) collection and get each bookmark in the OutlineItemCollection. The OutlineItemCollection provides access to all the bookmark’s attributes. The following code snippet shows you how to get bookmarks from the PDF file.

```java
    public static void GettingBookmarks() {
        // Open document
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // Loop through all the bookmarks
        for (OutlineItemCollection outlineItem : (Iterable<OutlineItemCollection>) pdfDocument.getOutlines()) {
            System.out.println("Title :- " + outlineItem.getTitle());
            System.out.println("Is Italic :- " + outlineItem.getItalic());
            System.out.println("Is Bold :- " + outlineItem.getBold());
            System.out.println("Color :- " + outlineItem.getColor());
        }
    }
```

## Getting a Bookmark’s Page Number

Once you have added a bookmark you can find out what page it is on by getting the destination PageNumber associated with the Bookmark object.

```java
    public static void GettingBookmarksPageNumber() {
        // Create PdfBookmarkEditor
        PdfBookmarkEditor bookmarkEditor = new PdfBookmarkEditor();
        // Open PDF file
        bookmarkEditor.bindPdf(GetDataDir() + "UpdateBookmarks.pdf");
        // Extract bookmarks
        Bookmarks bookmarks = bookmarkEditor.extractBookmarks();
        for (Bookmark bookmark : (Iterable<Bookmark>) bookmarks) {
            String strLevelSeprator = "";
            for (int i = 1; i < bookmark.getLevel(); i++) {
                strLevelSeprator += "---- ";
            }
            System.out.println("Title :- " + strLevelSeprator + bookmark.getTitle());
            System.out.println("Page Number :- " + strLevelSeprator + bookmark.getPageNumber());
            System.out.println("Page Action :- " + strLevelSeprator + bookmark.getAction());
        }
    }
```

## Update Bookmarks in a PDF Document

To update a bookmark in a PDF file, first, get the particular bookmark from the Document object’s OutlineColletion collection by specifying the bookmark’s index. Once you have retrieved the bookmark into [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) object, you can update its properties and then save the updated PDF file using the Save method. The following code snippets show how to update bookmarks in a PDF document.

```java
    public static void UpdateBookmarksInPDFDocument() {
        // Open document
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // Get a bookmark object
        OutlineItemCollection pdfOutline = pdfDocument.getOutlines().get_Item(1);

        // Update the bookmark object
        pdfOutline.setTitle("Updated Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);
        // Set the target page as 2
        pdfOutline.setDestination(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // Save output
        pdfDocument.save(GetDataDir() + "Bookmarkupdated_output.pdf");
    }
```

## Update Child Bookmarks in a PDF Document

To update a child bookmark:

1. Retrieve the child bookmark you want to update from the PDF file by first getting the parent bookmark and then the child bookmark using appropriate index values.
1. Save the updated PDF file using the Save method.

{{% alert color="primary" %}}

Get a bookmark from the Document object’s OutlineCollection collection by specifying the bookmark’s index, and then get the child bookmark by specifying the index od this parent bookmark.

{{% /alert %}}

The following code snippet shows you how to update child bookmarks in a PDF document.

```java
    public static void UpdateChildBookmarksInPDFDocument() {
        // Open document
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // Get a bookmark object
        OutlineItemCollection pdfOutline = pdfDocument.getOutlines().get_Item(1);
        // Get child bookmark object
        OutlineItemCollection childOutline = pdfOutline.get_Item(1);

        // Update the bookmark object
        childOutline.setTitle("Updated Outline");
        childOutline.setItalic(true);
        childOutline.setBold(true);
        // Set the target page as 2
        childOutline.setDestination(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // Save output
        pdfDocument.save(GetDataDir() + "Bookmarkupdated_output.pdf");
    }
```

## Expanded Bookmarks when viewing document

Bookmarks are held in the Document object’s [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) collection, itself in the [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) collection. However, we may have a requirement to have all the bookmarks expanded when viewing the PDF file.

In order to accomplish this requirement, we can set open status for each outline/bookmark item as Open. The following code snippet shows you how to set the open status for each bookmark as expanded in a PDF document.

```java
    public static void ExpandedBookmarks() {    
        Document doc = new Document(GetDataDir()+"UpdateBookmarks.pdf");
        // set page view mode i.e. show thumbnails, full-screen, show attachment panel
        doc.setPageMode(PageMode.UseOutlines);
        // print total count of Bookmarks in PDF file
        System.out.println(doc.getOutlines().size());
        // traverse through each Outline item in outlines collection of PDF file
        for (int counter = 1; counter <= doc.getOutlines().size(); counter++) {
            // set open status for outline item
            doc.getOutlines().get_Item(counter).setOpen(true);
        }
        // save the PDF file
        doc.save(_dataDir+"Bookmarks_Expanded.pdf");
    }
```
