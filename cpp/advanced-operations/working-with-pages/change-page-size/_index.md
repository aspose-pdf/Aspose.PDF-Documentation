---
title: Change PDF Page Size Programmatically with C++
linktitle: Change PDF Page Size
type: docs
weight: 40
url: /cpp/change-page-size/
description: Change Page Size from your PDF file using C++ library.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF is a static layout printable format, which is why it has become widespread in business life.

However, you may have tasks when you need to resize your PDF document since the page size is larger than the paper size. But how?

Do not worry. On this page, you will find a way to solve your task.

But first, let's remember that there is Page Size Series. 

There are two-page size series widely adopted in the world. 
Of course, there are many formats, but there are the most commonly used ones.
The first one is ISO Paper Sizes. Series A4 is used for Standard Printing and Stationery. Letter size paper is used for Posters, Wall-Charts, etc. The United States, Canada, and in part Mexico adopted the second Page Size Series and they are today the only industrialized nations in which the ISO standard paper sizes are not yet widely used. 

Now let's see how Aspose.PDF prompts you to resize the page using the C++ library.

## Change PDF Page Size

Aspose.PDF for С++ lets you change PDF page size with simple lines of code in your С++  applications. This topic explains how to update/change the page dimensions (size) of an existing PDF file.

The [Page](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page) class contains the SetPageSize(...) method which lets you set the page size. The code snippet below updates page dimensions in a few easy steps:

1. Load the source PDF file.
1. Get the pages into the [PageCollection](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) object.
1. Get a given page.
1. Call the SetPageSize(..) method to update its dimensions.
1. Call the [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) class' Save(..) method to generate the PDF file with updated page dimensions.

The following code snippet shows how to change the PDF page dimensions to A4 size.

```cpp
void ChangePageSize() {

	String _dataDir("C:\\Samples\\");
	String inputFileName("UpdateDimensions.pdf");
	String outputFileName("UpdateDimensions_out.pdf");

	// Open document
	auto document = MakeObject<Document>(_dataDir + inputFileName);

	// Get particular page
	auto pdfPage = document->get_Pages()->idx_get(1);

	// Set the page size as A4 (11.7 x 8.3 in) and in Aspose.Pdf, 1 inch = 72 points
	// So A4 dimensions in points will be (842.4, 597.6)
	pdfPage->SetPageSize(597.6, 842.4);
	// Save the updated document
	document->Save(_dataDir + outputFileName);
}
```

## Get PDF Page Size

You can read PDF page size of an existing PDF file using Aspose.PDF for С++. The following code sample shows how to read PDF page dimensions using C++.

```cpp
void GetPDFPageSize() {

	String _dataDir("C:\\Samples\\");
	String inputFileName("UpdateDimensions.pdf");

	// Open document
	auto document = MakeObject<Document>(_dataDir + inputFileName);

	// Get particular page
	auto page = document->get_Pages()->idx_get(1);

	// Get page height and width information
	Console::WriteLine(u"{0} {1}", page->GetPageRect(true)->get_Width(), page->GetPageRect(true)->get_Height());
	// Rotate page at 90 degree angle
	page->set_Rotate(Rotation::on90);
	// Get page height and width information
	Console::WriteLine(u"{0} {1}", page->GetPageRect(true)->get_Width(), page->GetPageRect(true)->get_Height());

}
```
