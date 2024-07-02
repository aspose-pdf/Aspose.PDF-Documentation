---
title: Get, Update and Expand a Bookmark 
linktitle: Get, Update and Expand a Bookmark
type: docs
weight: 20
url: /cpp/get-update-and-expand-bookmark/
description: Aspose.PDF for C++ library allows you get? update in a PDF file with our .
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Get Bookmarks

The [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) object's [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection) collection contains all a PDF file's bookmarks. This article explains how to get bookmarks from a PDF file, and how to get which page a particular bookmark is on.

To get the bookmarks, loop through the [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection) collection and get each bookmark in the OutlineItemCollection. The OutlineItemCollection provides access to all the bookmark's attributes. The following code snippet shows you how to get bookmarks from the PDF file.

```cpp
void GettingBookmarks() {
	String _dataDir("C:\\Samples\\Bookmarks\\");
	// Open document
	auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");
	// Loop through all the bookmarks
	for (auto outlineItem : pdfDocument->get_Outlines()) {
		Console::WriteLine(u"Title :- " + outlineItem->get_Title());
		Console::WriteLine(u"Is Italic :- " + outlineItem->get_Italic());
		Console::WriteLine(u"Is Bold :- " + outlineItem->get_Bold());
		Console::WriteLine(u"Color :- {0}", outlineItem->get_Color());
	}
}
```

## Getting a Bookmark's Page Number

Once you have added a bookmark you can find out what page it is on by getting the destination PageNumber associated with the Bookmark object.

```cpp
void GettingBookmarksPageNumber() {

	String _dataDir("C:\\Samples\\Bookmarks\\");
	// Create PdfBookmarkEditor
	auto bookmarkEditor = MakeObject<Aspose::Pdf::Facades::PdfBookmarkEditor>();
	// Open PDF file
	bookmarkEditor->BindPdf(_dataDir + u"UpdateBookmarks.pdf");
	// Extract bookmarks
	auto bookmarks = bookmarkEditor->ExtractBookmarks();
	for (auto bookmark : bookmarks) {
		String strLevelSeprator("");
		for (int i = 1; i < bookmark->get_Level(); i++) {
			strLevelSeprator += u"---- ";
		}
		Console::WriteLine(u"Title :- " + strLevelSeprator + bookmark->get_Title());
		Console::WriteLine(u"Page Number :- " + strLevelSeprator + bookmark->get_PageNumber());
		Console::WriteLine(u"Page Action :- " + strLevelSeprator + bookmark->get_Action());
	}
}
```

## Update Bookmarks in a PDF Document

To update a bookmark in a PDF file, first, get the particular bookmark from the Document object's OutlineColletion collection by specifying the bookmark's index. Once you have retrieved the bookmark into [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection) object, you can update its properties and then save the updated PDF file using the Save method. The following code snippets show how to update bookmarks in a PDF document.

```cpp
void UpdateBookmarksInPDFDocument() {

	String _dataDir("C:\\Samples\\Bookmarks\\");
	// Open document
	auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");
	// Get a bookmark object
	auto pdfOutline = pdfDocument->get_Outlines()->idx_get(1);

	// Update the bookmark object
	pdfOutline->set_Title(u"Updated Outline");
	pdfOutline->set_Italic(true);
	pdfOutline->set_Bold(true);
	// Set the target page as 2
	pdfOutline->set_Destination(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));

	// Save output
	pdfDocument->Save(_dataDir + u"Bookmarkupdated_output.pdf");
}
```

## Update Child Bookmarks in a PDF Document

To update a child bookmark:

1. Retrieve the child bookmark you want to update from the PDF file by first getting the parent bookmark and then the child bookmark using appropriate index values.
1. Save the updated PDF file using the Save method.

{{% alert color="primary" %}}

Get a bookmark from the Document object's OutlineCollection collection by specifying the bookmark's index, and then get the child bookmark by specifying the index od this parent bookmark.

{{% /alert %}}

The following code snippet shows you how to update child bookmarks in a PDF document.

```cpp
void UpdateChildBookmarksInPDFDocument() {

	String _dataDir("C:\\Samples\\Bookmarks\\");
	// Open document
	auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");
	// Get a bookmark object
	auto pdfOutline = pdfDocument->get_Outlines()->idx_get(1);
	// Get child bookmark object
	auto childOutline = pdfOutline->idx_get(1);

	// Update the bookmark object
	childOutline->set_Title(u"Updated Outline");
	childOutline->set_Italic(true);
	childOutline->set_Bold(true);
	// Set the target page as 2
	childOutline->set_Destination(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));

	// Save output
	pdfDocument->Save(_dataDir + u"Bookmarkupdated_output.pdf");
}
```

## Expanded Bookmarks when viewing document

Bookmarks are held in the Document object's [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection) collection, itself in the [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection) collection. However, we may have a requirement to have all the bookmarks expanded when viewing the PDF file.

In order to accomplish this requirement, we can set open status for each outline/bookmark item as Open. The following code snippet shows you how to set the open status for each bookmark as expanded in a PDF document.

```cpp
void ExpandedBookmarks() {

	String _dataDir("C:\\Samples\\Bookmarks\\");

	auto doc = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");
	// set page view mode i.e. show thumbnails, full-screen, show attachment panel
	doc->set_PageMode(PageMode::UseOutlines);
	// print total count of Bookmarks in PDF file
	Console::WriteLine(doc->get_Outlines()->get_Count());
	// traverse through each Outline item in outlines collection of PDF file
	for (int counter = 1; counter <= doc->get_Outlines()->get_Count(); counter++) {
		// set open status for outline item
		doc->get_Outlines()->idx_get(counter)->set_Open(true);
	}
	// save the PDF file
	doc->Save(_dataDir + u"Bookmarks_Expanded.pdf");
}
```
