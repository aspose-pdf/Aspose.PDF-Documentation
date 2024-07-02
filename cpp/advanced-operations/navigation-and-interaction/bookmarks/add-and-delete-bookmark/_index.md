---
title: Add and Delete a Bookmark 
linktitle: Add and Delete a Bookmark
type: docs
weight: 10
url: /cpp/add-and-delete-bookmark/
description: This topic explain how to add bookmark to a PDF document with C++ library. Also you can delete all or particular bookmarks from a PDF document.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Add a Bookmark to a PDF Document

Bookmarks are held in the Document object's [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection/) collection, itself in the [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) collection.

To add a bookmark to a PDF:

1. Open a PDF document using [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) object.
1. Create a bookmark and define its properties.
1. Add the [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) collection to the Outlines collection.

The following code snippet shows you how to add a bookmark in a PDF document.

```cpp
void AddBookmarks() {

	String _dataDir("C:\\Samples\\Bookmarks\\");
	auto pdfDocument = MakeObject<Document>(_dataDir + u"AddBookmark.pdf");

	// Create a bookmark object
	auto pdfOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());
	pdfOutline->set_Title(u"Test Outline");
	pdfOutline->set_Italic(true);
	pdfOutline->set_Bold(true);

	// Set the destination page number
	pdfOutline->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));

	// Add a bookmark in the document's outline collection.
	pdfDocument->get_Outlines()->Add(pdfOutline);

	// Save the update document
	pdfDocument->Save(_dataDir + u"AddBookmark_out.pdf");
}
```

## Add a Child Bookmark to the PDF Document

Bookmarks can be nested, indicating a hierarchical relationship with parent and child bookmarks. This article explains how to add a child bookmark, that is, a second-level bookmark, to a PDF.

To add a child bookmark to a PDF file, first add a parent bookmark:

1. Open a document.
1. Add a bookmark to the [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection/), defining its properties.
1. Add the OutlineItemCollection to the Document object's [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) collection.

The child bookmark is created just like the parent bookmark, explained above, but is added to the parent bookmark's Outlines collection

The following code snippets show how to add child bookmark to a PDF document.

```cpp
void AddChildBookmark() {

	String _dataDir("C:\\Samples\\Bookmarks\\");
	// Open document
	auto pdfDocument = MakeObject<Document>(_dataDir + u"AddChildBookmark.pdf");

	// Create a parent bookmark object
	auto pdfOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());
	pdfOutline->set_Title(u"Parent Outline");
	pdfOutline->set_Italic(true);
	pdfOutline->set_Bold(true);

	// Create a child bookmark object
	auto pdfChildOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());
	pdfChildOutline->set_Title(u"Child Outline");
	pdfChildOutline->set_Italic(true);
	pdfChildOutline->set_Bold(true);

	// Add child bookmark in parent bookmark's collection
	pdfOutline->Add(pdfChildOutline);
	// Add parent bookmark in the document's outline collection.
	pdfDocument->get_Outlines()->Add(pdfOutline);

	// Save output
	pdfDocument->Save(_dataDir + u"AddChildBookmark_out.pdf");
}
```

## Delete all Bookmarks from a PDF Document

All bookmarks in a PDF are held in the [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) collection. This article explains how to delete all bookmarks from a PDF file.

To delete all bookmarks from a PDF file:

1. Call the [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) collection's Delete method.
1. Save the modified file using the [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) object's Save method.

The following code snippets show how to delete all bookmarks from a PDF document.

```cpp
void DeleteAllBookmarksFromPDFDocument() {

	String _dataDir("C:\\Samples\\Bookmarks\\");
	// Open document
	auto pdfDocument = MakeObject<Document>(_dataDir + u"DeleteAllBookmarks.pdf");

	// Delete all bookmarks
	pdfDocument->get_Outlines()->Delete();

	// Save updated file
	pdfDocument->Save(_dataDir + u"DeleteAllBookmarks_out.pdf");
}
```

## Delete a Particular Bookmark from a PDF Document

[Delete All Attachments from PDF document](https://docs.aspose.com/pdf/cpp/working-with-attachments/) showed how to delete all attachments from a PDF file. It is also possible to only remove specific attachments.

To delete a particular bookmark from a PDF file:

1. Pass the bookmark's title as parameter to the [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) collection's Delete method.
1. Then save the updated file with the Document object Save method.

The [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) class’ provides the [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) collection. The [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection#a04f36a1f4f7c4fde3189399eb046a98b) method removes any bookmark with the title passed to the method.

The following code snippets show how to delete a particular bookmark from the PDF document.

```cpp
void DeleteParticularBookmarkPDFDocument() {

	String _dataDir("C:\\Samples\\Bookmarks\\");
	// Open document
	auto pdfDocument = MakeObject<Document>(_dataDir + u"DeleteParticularBookmark.pdf");

	// Delete particular outline by Title
	pdfDocument->get_Outlines()->Delete(u"Child Outline");

	// Save updated file
	pdfDocument->Save(_dataDir + u"DeleteParticularBookmark_out.pdf");
}
```
