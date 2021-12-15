---
title: Add Pages in PDF with C++
linktitle: Add Pages
type: docs
weight: 10
url: /cpp/add-pages/
description: This article teaches how to insert (add) a page at the desired location PDF file. Learn how to move, remove (delete) pages from a PDF file using C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

This section shows how to add pages to a PDF using **Aspose.PDF for C++** library.

Aspose.PDF for C++ API provides full flexibility to work with pages in a PDF document using C++.

It maintains all the pages of a PDF document in [PageCollection](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) that can be used to work with PDF pages.
Aspose.PDF for C++ lets you insert a page to a PDF document at any location in the file as well as add pages to the end of a PDF file.

## Add or Insert Page in a PDF File

Aspose.PDF for C++ lets you insert a page to a PDF document at any location in the file as well as add pages to the end of a PDF file.

### Insert Empty Page in a PDF File at Desired Location

The following code sample explains you on how to add page in a PDF document.

1. Create a [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) class object with the input PDF file.
1. Call the [PageCollection](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) collection's [Insert](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#a1fb1fe44df4d325df5ad41b691501bb2) method with specified index.
1. Save the output PDF

The following code snippet shows you how to insert a page in a PDF file.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;


void InsertEmptyPageAtDesiredLocation() {
    // Open document
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("InsertEmptyPage.pdf");

    String outputFileName("InsertEmptyPage_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Insert a empty page in a PDF
    document->get_Pages()->Insert(2);

    // Save output file
    document->Save(_dataDir + outputFileName);
}
```

In the following code example, you can insert an empty page to the desired location by copying the parameters of the specified page:

```cpp
void InsertEmptyPageAtDesiredLocation2() {
    // Open document
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("InsertEmptyPage.pdf");

    String outputFileName("InsertEmptyPage_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    auto page = document->get_Pages()->idx_get(1);
    // Insert a empty page in a PDF
    auto pageNew = document->get_Pages()->Insert(2);

    //copy page parameters from page 1
    pageNew->set_ArtBox(page->get_ArtBox());
    pageNew->set_BleedBox(page->get_BleedBox());
    pageNew->set_CropBox(page->get_CropBox());
    pageNew->set_MediaBox(page->get_MediaBox());
    pageNew->set_TrimBox(page->get_TrimBox());

    // Save output file
    document->Save(_dataDir + outputFileName);
}
```

### Add an Empty Page at the End of a PDF File

Sometimes, you want to ensure that a document ends on an empty page. This topic explains how to insert an empty page at the end of the PDF document.

To insert an empty page at the end of a PDF file:

1. Create a [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) class object with the input PDF file.
1. Call the [PageCollection](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) collection's [Add](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) method, without any parameters.
1. Save the output PDF using the Save method.

The following code snippet shows you how to insert an empty page at the end of a PDF file.

```cpp
void AddEmptyPageEnd() {
    // Open document
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("InsertEmptyPageAtEnd.pdf");
    String outputFileName("InsertEmptyPageAtEnd_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Insert an empty page at the end of a PDF file
    document->get_Pages()->Add();

    // Save output file
    document->Save(_dataDir + outputFileName);
}
```
