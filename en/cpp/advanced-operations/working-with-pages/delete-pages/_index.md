---
title: Delete PDF pages in C++
linktitle: Delete Pages
type: docs
weight: 50
url: /cpp/delete-pages/
description: Remove one page or a selected set of pages from a PDF document using Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Remove one page or a selected set of pages from a PDF document using Aspose.PDF for C++.

## Delete a single page

The input PDF must contain page 2.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Call [Delete()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/delete/) on [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/) for page 2.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

Source example: `delete-page.cpp`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of DeletePagesExamples.deletePage.
void DeletePage(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);

    document->get_Pages()->Delete(2);
    document->Save(outputFile);
}
```

## Delete multiple pages

The input PDF must contain at least four pages.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create an array containing page numbers 2, 3, and 4.
1. Pass the array to [Delete()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/delete/) on [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/).
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

Source example: `delete-bunch-pages.cpp`.

```cpp
#include <system/array.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of DeletePagesExamples.deleteBunchPages.
void DeleteBunchPages(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);

    document->get_Pages()->Delete(MakeArray<int32_t>({2, 3, 4}));
    document->Save(outputFile);
}
```
