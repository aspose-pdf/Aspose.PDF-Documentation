---
title: Extract PDF pages in C++
linktitle: Extract Pages
type: docs
weight: 60
url: /cpp/extract-pages/
description: Copy selected PDF pages into a new document while retaining the input file using Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Copy Selected PDF Pages to Separate Documents in C++
Abstract: Learn how to extract one or several PDF pages into a new document with Aspose.PDF for C++. The examples copy the selected pages while retaining the input file.
---

Copy selected PDF pages into a new document while retaining the input file using Aspose.PDF for C++.

## Extract a single page

The input PDF must contain page 2. The source document is not modified.

1. Open the input PDF and create an output [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Call [CopyPage()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/) to copy page 2 into the output document.
1. Save the output with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of ExtractPagesExamples.extractPage.
void ExtractPage(System::String inputFile, System::String outputFile)
{
    auto srcDocument = MakeObject<Document>(inputFile);
    auto dstDocument = MakeObject<Document>();

    dstDocument->get_Pages()->CopyPage(srcDocument->get_Pages()->idx_get(2));
    dstDocument->Save(outputFile);
}
```

## Extract multiple pages

The input PDF must contain at least three pages.

1. Open the input PDF and create an output [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create an array containing page numbers 2 and 3.
1. Call [CopyPage()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/) for each selected page in the supplied order.
1. Save the output with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <system/array.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of ExtractPagesExamples.extractBunchPages.
void ExtractBunchPages(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto anotherDocument = MakeObject<Document>();

    auto pages = MakeArray<int32_t>({2, 3});
    for (int pageIndex : pages) {
        anotherDocument->get_Pages()->CopyPage(document->get_Pages()->idx_get(pageIndex));
    }
    anotherDocument->Save(outputFile);
}
```
