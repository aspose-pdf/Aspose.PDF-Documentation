---
title: Split PDF files in C++
linktitle: Split PDF files
type: docs
weight: 60
url: /cpp/split-pdf/
description: Split a PDF into separate single-page files in C++ using Aspose.PDF.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Export Each PDF Page to a Separate File in C++
Abstract: Learn how to split a PDF into individual single-page documents with Aspose.PDF for C++. Copy each source page into a new document and save it with a unique file name, reporting page errors while continuing processing.
---

Export each page of a PDF to its own file for review or further processing.

## Split a PDF into single-page files

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Iterate through the [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/), starting at index 1.
1. Create an empty [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) for each page.
1. Copy the source page into the new document with [CopyPage()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/).
1. Save each document with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/) using a unique name such as page_1.pdf.
1. Report any page processing errors and continue with the remaining pages.

```cpp
#include <exception>
#include <iostream>

#include <system/io/path.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

void SplitDocument(String inputFile, String outputDir) {
    auto document = MakeObject<Document>(inputFile);
    try {
        
        for (int pageNumber = 1; pageNumber <= document->get_Pages()->get_Count(); pageNumber++) {
            auto newDocument = MakeObject<Document>();
            try {
                auto page = document->get_Pages()->idx_get(pageNumber);
                newDocument->get_Pages()->CopyPage(page);
                auto outputFile = System::IO::Path::Combine(outputDir, System::String::Format(u"page_{0}.pdf", pageNumber));
                newDocument->Save(outputFile);
            }
            catch (std::exception& e) {
                std::cerr << e.what();
            }            
        }
    }
    catch (std::exception& e) {
        std::cerr << e.what();
    }
}
```
