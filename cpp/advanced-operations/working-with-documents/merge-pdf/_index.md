---
title: Merge PDF using C++
linktitle: Merge PDF files
type: docs
weight: 50
url: /cpp/merge-pdf-documents/
description: This page explain how to merge PDF documents into a single PDF file with C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Merging pdf files is not an easy task, but very popular. You can use the Aspose.PDF for C++  library to combine PDF files into one document quickly and easily.

## Merge PDF Files using C++

To concatenate two PDF files:

1. Create two [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)  objects, each containing one of the input PDF files.
1. Then call the [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) collection’s Add method for the Document object you want to add the other PDF file to.
1. Add [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) of second document to the first file.
1. Finally, save the output PDF file using the Save method.

The following code snippet shows how to concatenate PDF files.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
void MergingDocuments() {
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String pdfDocumentFileName1("Concat1.pdf");
    String pdfDocumentFileName2("Concat2.pdf");
    String outputFileName("ConcatenatePdfFiles.pdf");

    // Open document
    auto pdfDocument1 = MakeObject<Document>(_dataDir + pdfDocumentFileName1);
    auto pdfDocument2 = MakeObject<Document>(_dataDir + pdfDocumentFileName2);

    // Add pages of second document to the first
    pdfDocument1->get_Pages()->Add(pdfDocument2->get_Pages());

    // Save concatenated output file
    pdfDocument1->Save(_dataDir+outputFileName);
}
```

## Live Example

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) is an online free web application that allows you to investigate how presentation merging functionality works.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)
