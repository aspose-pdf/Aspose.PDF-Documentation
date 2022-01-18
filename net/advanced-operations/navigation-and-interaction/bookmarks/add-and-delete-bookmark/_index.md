---
title: Add and Delete a Bookmark 
linktitle: Add and Delete a Bookmark
type: docs
weight: 10
url: /net/add-and-delete-bookmark/
description: You can add a bookmark to a PDF document with C#. It is possible to delete all or particular bookmarks from a PDF document.
aliases:
    - /net/add-and-delete-a-bookmark/
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Add a Bookmark to a PDF Document

Bookmarks are held in the Document object’s [OutlineItemCollection](https://apireference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) collection, itself in the [OutlineCollection](https://apireference.aspose.com/pdf/net/aspose.pdf/outlinecollection) collection.

To add a bookmark to a PDF:

1. Open a PDF document using [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object.
1. Create a bookmark and define its properties.
1. Add the [OutlineItemCollection](https://apireference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) collection to the Outlines collection.

The following code snippet shows you how to add a bookmark in a PDF document.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// Open document
Document pdfDocument = new Document(dataDir + "AddBookmark.pdf");

// Create a bookmark object
OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfOutline.Title = "Test Outline";
pdfOutline.Italic = true;
pdfOutline.Bold = true;
// Set the destination page number
pdfOutline.Action = new GoToAction(pdfDocument.Pages[1]);
// Add bookmark in the document's outline collection.
pdfDocument.Outlines.Add(pdfOutline);

dataDir = dataDir + "AddBookmark_out.pdf";
// Save output
pdfDocument.Save(dataDir);
```

## Add a Child Bookmark to the PDF Document

Bookmarks can be nested, indicating a hierarchical relationship with parent and child bookmarks. This article explains how to add a child bookmark, that is, a second-level bookmark, to a PDF.

To add a child bookmark to a PDF file, first add a parent bookmark:

1. Open a document.
1. Add a bookmark to the [OutlineItemCollection](https://apireference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection), defining its properties.
1. Add the OutlineItemCollection to the Document object’s [OutlineCollection](https://apireference.aspose.com/pdf/net/aspose.pdf/outlinecollection) collection.

The child bookmark is created just like the parent bookmark, explained above, but is added to the parent bookmark’s Outlines collection

The following code snippets show how to add child bookmark to a PDF document.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// Open document
Document pdfDocument = new Document(dataDir + "AddChildBookmark.pdf");

// Create a parent bookmark object
OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfOutline.Title = "Parent Outline";
pdfOutline.Italic = true;
pdfOutline.Bold = true;

// Create a child bookmark object
OutlineItemCollection pdfChildOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfChildOutline.Title = "Child Outline";
pdfChildOutline.Italic = true;
pdfChildOutline.Bold = true;

// Add child bookmark in parent bookmark's collection
pdfOutline.Add(pdfChildOutline);
// Add parent bookmark in the document's outline collection.
pdfDocument.Outlines.Add(pdfOutline);

dataDir = dataDir + "AddChildBookmark_out.pdf";
// Save output
pdfDocument.Save(dataDir);
```

## Delete all Bookmarks from a PDF Document

All bookmarks in a PDF are held in the [OutlineCollection](https://apireference.aspose.com/pdf/net/aspose.pdf/outlinecollection) collection. This article explains how to delete all bookmarks from a PDF file.

To delete all bookmarks from a PDF file:

1. Call the [OutlineCollection](https://apireference.aspose.com/pdf/net/aspose.pdf/outlinecollection) collection’s Delete method.
1. Save the modified file using the [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object’s [Save](https://apireference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) method.

The following code snippets show how to delete all bookmarks from a PDF document.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// Open document
Document pdfDocument = new Document(dataDir + "DeleteAllBookmarks.pdf");

// Delete all bookmarks
pdfDocument.Outlines.Delete();

dataDir = dataDir + "DeleteAllBookmarks_out.pdf";
// Save updated file
pdfDocument.Save(dataDir);
```

## Delete a Particular Bookmark from a PDF Document

[Delete All Attachments from PDF document](https://docs.aspose.com/pdf/net/working-with-attachments/) showed how to delete all attachments from a PDF file. It is also possible to only remove specific attachments.

To delete a particular bookmark from a PDF file:

1. Pass the bookmark’s title as parameter to the [OutlineCollection](https://apireference.aspose.com/pdf/net/aspose.pdf/outlinecollection) collection’s Delete method.
1. Then save the updated file with the Document object Save method.

The [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) class’ provides the [OutlineCollection](https://apireference.aspose.com/pdf/net/aspose.pdf/outlinecollection) collection. The [Delete](https://apireference.aspose.com/pdf/net/aspose.pdf/outlinecollection/methods/delete) method removes any bookmark with the title passed to the method.

The following code snippets show how to delete a particular bookmark from the PDF document.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// Open document
Document pdfDocument = new Document(dataDir + "DeleteParticularBookmark.pdf");

// Delete particular outline by Title
pdfDocument.Outlines.Delete("Child Outline");

dataDir = dataDir + "DeleteParticularBookmark_out.pdf";
// Save updated file
pdfDocument.Save(dataDir);
```
