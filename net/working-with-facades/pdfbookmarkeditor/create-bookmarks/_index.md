---
title: Create Bookmarks
type: docs
weight: 10
url: /net/create-bookmarks/
description: This section explains how to create bookmarks to your PDF file with Aspose.PDF Facades using PdfBookmarEditor Class.
lastmod: "2021-01-15"
draft: false
---

## Create Bookmarks of All Pages

In order to create bookmarks of all the pages, you need to use [CreateBookmarks](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) method without any parameters . [PdfBookmarkEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) class allows you to create bookmarks of all the pages of a PDF file. First, you need to create an object of [PdfBookmarkEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) class and bind the input PDF using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. Then, you have to call [CreateBookmarks](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) method and save the output PDF file using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method. The following code snippet shows you how to create Bookmarks.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarksAll-CreateBookmarksAll.cs" >}}

## Create Bookmarks of All Pages with Properties

[PdfBookmarkEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) class allows you to create bookmarks of all the pages of a PDF file and specify the properties (Color, Bold, Italic). You can do that with the help of [CreateBookmarks](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) method. First, you need to create an object of [PdfBookmarkEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) class and bind the input PDF using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. Then, you have to call [CreateBookmarks](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) method and save the output PDF file using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method. The following code snippet shows you how to create bookmarks of all the pages with properties.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarksPagesProperties-CreateBookmarksPagesProperties.cs" >}}

## Create Bookmark of a Particular Page

You can create a bookmark of a particular page in an existing PDF file using [CreateBookmarkOfPage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) method. This method takes two arguments: bookmark title and page number. First, you need to create an object of [PdfBookmarkEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) class and bind input PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. Then, you have to call the [CreateBookmarkOfPage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) method and save the output PDF file using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method. The following code snippet shows you how to create bookmark of a particular page.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarkPage-CreateBookmarkPage.cs" >}}

## Create Bookmarks of a Range of Pages

[PdfBookmarkEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) class allows you to create bookmarks of a range of pages. You can use [CreateBookmarkOfPage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) method with two parameters: bookmark list (the list of the bookmark titles) and page list (the list of the pages to bookmark). First, you need to create an object of [PdfBookmarkEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) class and bind the input PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. Then, you have to call [CreateBookmarkOfPage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) method and save the output PDF using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method. The following code snippet shows you how to create bookmarks of a range of pages.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarkPageRange-CreateBookmarkPageRange.cs" >}}

## Add Bookmark in an Existing PDF File

You can add bookmark in an existing PDF file using [PdfBookmarkEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) class. In order to create the bookmark, you need to create [Bookmark](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) object and set the required attributes of the bookmark. After that, you need to pass the [Bookmark](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) object to the [CreateBookmarks](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) method of [PdfBookmarkEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) class. Finally, you need to save the updated PDF file using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method. The following code snippet shows you how to add the bookmark in an existing PDF file.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-AddBookmark-AddBookmark.cs" >}}

## Add Child Bookmark in an Existing PDF File

You can add child bookmarks in an existing PDF file using [PdfBookmarkEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) class. In order to add child bookmarks, you need to create [Bookmark](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) objects. You can add individual [Bookmark](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) objects into [Bookmarks](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks) object. You also need to create a [Bookmark](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) object and set its [ChildItem](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/bookmark/properties/childitem) property to [Bookmarks](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks) object. You then need to pass this [Bookmark](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) object with [ChildItem](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/bookmark/properties/childitem) to the [CreateBookmarks](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) method. Finally, you need to save the updated PDF using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method of the [PdfBookmarkEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) class. The following code snippet shows you how to add child bookmarks in an existing PDF file.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-AddChildBookmark-AddChildBookmark.cs" >}}

## See also

Try to compare and find a way to work with bookmarks that suits you. Lets learn [Working with Bookmarks in PDF](/pdf/net/bookmarks/) section.