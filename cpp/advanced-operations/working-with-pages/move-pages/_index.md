---
title: Move PDF Pages programmatically C++
linktitle: Move PDF Pages
type: docs
weight: 20
url: /cpp/move-pages/
description: Try to move pages at desired location or at the end of a PDF file using Aspose.PDF for C++.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Moving a Page from one PDF Document to Another

Moving PDF pages in document is very interesting and popular task.
This topic explains how to move page from one PDF document to the end of another document using C++.
To move an page we should:

1. Create a [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) class object with the source PDF file.
1. Get Page from the the [PageCollection](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) collection's.
1. [Add](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) page to the destination document.
1. Save the output PDF using the Save method.
1. [Delete](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15) page in source document.
1. Save the source PDF using the Save method.

The following code snippet shows you how to move one page.

```cpp
void MovePage()
{
	// Open document
	String _dataDir("C:\\Samples\\");
	String srcFileName("<enter file name>");
	String dstFileName("<enter file name>");

	auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
	auto dstDocument = MakeObject<Document>();

	auto page = srcDocument->get_Pages()->idx_get(2);
	dstDocument->get_Pages()->Add(page);
	// Save output file
	dstDocument->Save(srcFileName);
	srcDocument->get_Pages()->Delete(2);
	srcDocument->Save(dstFileName);
}
```

## Moving bunch of Pages from one PDF Document to Another

1. Create a [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) class object with the source PDF file.
1. Define an array with page numbers to be moved.
1. Run loop through array:
1. Get Page from the the [PageCollection](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) collection's.
1. [Add](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) page to the destination document.
1. Save the output PDF using the Save method.
1. [Delete](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15) page in source document.
1. Save the source PDF using the Save method.

The following code snippet shows you how to insert an empty page at the end of a PDF file.

```cpp
void MoveBunchPages()
{
	// Open document
	String _dataDir("C:\\Samples\\");
	String srcFileName("<enter file name>");
	String dstFileName("<enter file name>");

	auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
	auto dstDocument = MakeObject<Document>();


	auto pages = MakeArray<int>({ 1,3 });

	for (auto pageIndex : pages)
	{
		auto page = srcDocument->get_Pages()->idx_get(pageIndex);
		dstDocument->get_Pages()->Add(page);
	}
	// Save output files
	dstDocument->Save(srcFileName);
	srcDocument->get_Pages()->Delete();
	srcDocument->Save(dstFileName);
}
```

## Moving a Page in new location in the current PDF Document

1. Create a [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) class object with the source PDF file.
1. Get Page from the the [PageCollection](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) collection's. collection's.
1. [Add](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1)  page to the new location (for example to end).
1. [Delete](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15)  page in previous location.
1. Save the output PDF using the Save method.

```cpp
void MovePagesInOnePDF()
{
	// Open document
	String _dataDir("C:\\Samples\\");
	String srcFileName("<enter file name>");
	String dstFileName("<enter file name>");

	auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
	auto dstDocument = MakeObject<Document>();

	auto page = srcDocument->get_Pages()->idx_get(2);
	srcDocument->get_Pages()->Add(page);
	srcDocument->get_Pages()->Delete(2);

	// Save output file
	srcDocument->Save(dstFileName);
}
```
