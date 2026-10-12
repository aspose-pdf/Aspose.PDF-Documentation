---
title: Move PDF pages in C++
linktitle: Move Pages
type: docs
weight: 80
url: /cpp/move-pages/
description: Move pages to a new PDF or move a page to the end of its original document using Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Move pages to a new PDF or move a page to the end of its original document using Aspose.PDF for C++.

## Move a page to a new document

Supply distinct sourceOutputFile and outputFile paths. The input must contain page 2.

1. Open the input PDF and create a destination [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Call [CopyPage()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/) to copy page 2 into the destination.
1. Call [Delete()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/delete/) to remove page 2 from the source.
1. Save the modified source and destination to separate paths with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

Source example: `move-page-from-one-document-to-another.cpp`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of MovePagesExamples.movePageFromOneDocumentToAnother.
void MovePageFromOneDocumentToAnother(System::String inputFile, System::String sourceOutputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto anotherDocument = MakeObject<Document>();

    anotherDocument->get_Pages()->CopyPage(document->get_Pages()->idx_get(2));
    document->get_Pages()->Delete(2);
    document->Save(sourceOutputFile);
    anotherDocument->Save(outputFile);
}
```

## Move multiple pages to a new document

Use a PDF with at least two pages and distinct output paths.

1. Open the input PDF and create a destination [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Copy pages 1 and 2 into the destination using [CopyPage()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/).
1. Save the destination with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).
1. Pass the selected page array to [Delete()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/delete/) on the source.
1. Save the modified source to sourceOutputFile with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

Source example: `move-bunch-pages-from-one-document-to-another.cpp`.

```cpp
#include <system/array.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of MovePagesExamples.moveBunchPagesFromOneDocumentToAnother.
void MoveBunchPagesFromOneDocumentToAnother(System::String inputFile, System::String sourceOutputFile, System::String outputFile)
{
    auto srcDocument = MakeObject<Document>(inputFile);
    auto dstDocument = MakeObject<Document>();

    auto pages = MakeArray<int32_t>({1, 2});
    for (int pageIndex : pages) {
        dstDocument->get_Pages()->CopyPage(srcDocument->get_Pages()->idx_get(pageIndex));
    }
    dstDocument->Save(outputFile);
    srcDocument->get_Pages()->Delete(pages);
    srcDocument->Save(sourceOutputFile);
}
```

## Move page 2 to the end

This example moves page 2 to the end; it does not accept an arbitrary destination position.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Append a copy of page 2 using [CopyPage()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/).
1. Remove the original page 2 with [Delete()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/delete/).
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

Source example: `move-page-in-new-location-in-same-document.cpp`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of MovePagesExamples.movePageInNewLocationInSameDocument.
void MovePageInNewLocationInSameDocument(System::String inputFile, System::String outputFile)
{
    auto srcDocument = MakeObject<Document>(inputFile);

    srcDocument->get_Pages()->CopyPage(srcDocument->get_Pages()->idx_get(2));
    srcDocument->get_Pages()->Delete(2);
    srcDocument->Save(outputFile);
}
```
