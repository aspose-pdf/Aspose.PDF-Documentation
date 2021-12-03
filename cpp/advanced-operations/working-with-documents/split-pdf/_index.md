---
title: Split PDF programmatically
linktitle: Split PDF files
type: docs
weight: 60
url: /cpp/split-pdf-document/
description: This topic shows how to split PDF pages into individual PDF files with C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Live Example

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) is an online free web application that allows you to investigate how presentation splitting functionality works.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

This topic shows how to split PDF pages into individual PDF files in your C++ applications. To split PDF pages into single page PDF files using C++, the following steps can be followed:

1. Loop through the pages of PDF document through the [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) object's [PageCollection](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) collection
1. For each iteration, create a new Document object and add the individual [Page](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page) object into the empty document
1. Save the new PDF using Save method

The following C++ code snippet shows you how to split PDF pages into individual PDF files.

```cpp
void SplittingDocuments() {
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String documentFileName("sample.pdf");
    
    // Open document
    auto document = MakeObject<Document>(_dataDir + documentFileName);

    int pageCount = 1;

    // Loop through all the pages
    for(auto page : document->get_Pages())
    {
        auto newDocument = MakeObject<Document>(_dataDir + documentFileName);
        newDocument->get_Pages()->Add(page);
        newDocument->Save(_dataDir + u"page_" + pageCount + u"_out.pdf");
        pageCount++;
    }
}
```
