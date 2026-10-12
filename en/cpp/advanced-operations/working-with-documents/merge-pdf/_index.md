---
title: Merge PDF documents in C++
linktitle: Merge PDF documents
type: docs
weight: 40
url: /cpp/merge-pdf-documents/
description: Combine PDF files in sequence, merge selected ranges, insert or alternate pages, and add section separators and bookmarks with Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Combine PDF files in sequence, merge selected ranges, insert or alternate pages, and add section separators and bookmarks with Aspose.PDF for C++.

## Merge two PDFs

1. Open both input files as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) objects.
1. Append the second document pages to the first with [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/).
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>
#include <system/console.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

void MergeTwoDocuments(String inputFile1, String inputFile2, String outputFile) {
    auto document1 = MakeObject<Document>(inputFile1);
    auto document2 = MakeObject<Document>(inputFile2);
    document1->get_Pages()->Add(document2->get_Pages());
    document1->Save(outputFile);
}
```

## Merge multiple PDFs

The helper clamps page ranges to the available pages. Include the standard vector header when integrating functions that use std::vector.

1. Check that the input file list is not empty.
1. Create an output [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Open each input file in the supplied order.
1. Copy all pages using appendPageRange() and [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/).
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;


static void appendPageRange(SharedPtr<Document> sourceDocument, SharedPtr<Document> destinationDocument, int startPage, int endPage) {
    int totalPages = sourceDocument->get_Pages()->get_Count();
    if (totalPages == 0) {
        return;
    }

    int start = Math::Max(1, startPage);
    int end = Math::Min(endPage, totalPages);
    if (start > end) {
        return;
    }

    for (int pageNumber = start; pageNumber <= end; pageNumber++) {
        auto page = sourceDocument->get_Pages()->idx_get(pageNumber);
        destinationDocument->get_Pages()->CopyPage(page);
    }
}

void MergeMultipleDocuments(const std::vector<System::String>& inputFiles, String outputFile) {
    if (inputFiles.empty()) {
        throw ArgumentException(u"At least one input document is required.");
    }

    auto outputDocument = MakeObject<Document>();
    for (String inputFile : inputFiles) {
        auto sourceDocument = MakeObject<Document>(inputFile);
        appendPageRange(sourceDocument, outputDocument, 1, sourceDocument->get_Pages()->get_Count());
    }
    outputDocument->Save(outputFile);
}
```

## Merge selected page ranges

The helper clips each range to the source page count and skips empty ranges.

1. Open both input PDFs and create an output [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Copy pages 1–2 from the first input using [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/).
1. Copy pages 2–3 from the second input.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

static void appendPageRange(SharedPtr<Aspose::Pdf::Document> sourceDocument, SharedPtr<Aspose::Pdf::Document> destinationDocument, int startPage, int endPage)
{
    int totalPages = sourceDocument->get_Pages()->get_Count();
    if (totalPages == 0) {
        return;
    }
    int start = Math::Max(1, startPage);
    int end = Math::Min(endPage, totalPages);
    if (start > end) {
        return;
    }
    for (int pageNumber = start; pageNumber <= end; pageNumber++) {
        auto page = sourceDocument->get_Pages()->idx_get(pageNumber);
        destinationDocument->get_Pages()->CopyPage(page);
    }
}

void MergeSelectedPageRanges(String inputFile1, String inputFile2, String outputFile) {
    auto document1 = MakeObject<Document>(inputFile1);
    auto document2 = MakeObject<Document>(inputFile2);
    auto outputDocument = MakeObject<Document>();
    appendPageRange(document1, outputDocument, 1, 2);
    appendPageRange(document2, outputDocument, 2, 3);
    outputDocument->Save(outputFile);
}
```

## Insert a document at a page position

Zero inserts at the beginning; the base page count inserts at the end.

1. Open the base and inserted PDFs as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) objects.
1. Clamp insertAfterPage to the range from zero to the base page count.
1. Copy base pages before the insertion point using [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/).
1. Copy all pages from the inserted PDF, then the remaining base pages.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

static void appendPageRange(SharedPtr<Aspose::Pdf::Document> sourceDocument, SharedPtr<Aspose::Pdf::Document> destinationDocument, int startPage, int endPage)
{
    int totalPages = sourceDocument->get_Pages()->get_Count();
    if (totalPages == 0) {
        return;
    }
    int start = Math::Max(1, startPage);
    int end = Math::Min(endPage, totalPages);
    if (start > end) {
        return;
    }
    for (int pageNumber = start; pageNumber <= end; pageNumber++) {
        auto page = sourceDocument->get_Pages()->idx_get(pageNumber);
        destinationDocument->get_Pages()->CopyPage(page);
    }
}

void MergeInsertDocumentAtPosition(String inputFile1, String inputFile2, int insertAfterPage, String outputFile) {
    auto baseDocument = MakeObject<Document>(inputFile1);
    auto insertDocument = MakeObject<Document>(inputFile2);
    auto outputDocument = MakeObject<Document>();
    int baseTotalPages = baseDocument->get_Pages()->get_Count();
    int insertIndex = Math::Max(0, Math::Min(insertAfterPage, baseTotalPages));

    appendPageRange(baseDocument, outputDocument, 1, insertIndex);
    appendPageRange(insertDocument, outputDocument, 1, insertDocument->get_Pages()->get_Count());
    appendPageRange(baseDocument, outputDocument, insertIndex + 1, baseTotalPages);

    outputDocument->Save(outputFile);
}
```

## Merge alternating pages

1. Open both input PDFs and create an output [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Iterate up to the larger page count.
1. Copy an available page from the first input, then the corresponding page from the second with [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/).
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

void MergeAlternatingPages(String inputFile1, String inputFile2, String outputFile) {
    auto document1 = MakeObject<Document>(inputFile1);
    auto document2 = MakeObject<Document>(inputFile2);
    auto outputDocument = MakeObject<Document>();
    int document1Pages = document1->get_Pages()->get_Count();
    int document2Pages = document2->get_Pages()->get_Count();
    int maxPages = Math::Max(document1Pages, document2Pages);

    for (int pageNumber = 1; pageNumber <= maxPages; pageNumber++) {
        if (pageNumber <= document1Pages) {
            outputDocument->get_Pages()->CopyPage(document1->get_Pages()->idx_get(pageNumber));
        }
        if (pageNumber <= document2Pages) {
            outputDocument->get_Pages()->CopyPage(document2->get_Pages()->idx_get(pageNumber));
        }
    }

    outputDocument->Save(outputFile);
}
```

## Add section separators and bookmarks

This example creates new section bookmarks; it does not explicitly copy the source documents' outline trees.

1. Check the input list and create an output [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Add a separator page with a [TextFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/) for each input.
1. Create an [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/outlineitemcollection/) bookmark pointing to the separator using [GoToAction](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/gotoaction/).
1. Copy the input pages with [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/).
1. Add a child bookmark pointing to the first content page when the source has pages.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Outlines/OutlineCollection.h>
#include <Aspose.PDF.Cpp/Outlines/OutlineItemCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/GoToAction.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

static void appendPageRange(SharedPtr<Aspose::Pdf::Document> sourceDocument, SharedPtr<Aspose::Pdf::Document> destinationDocument, int startPage, int endPage)
{
    int totalPages = sourceDocument->get_Pages()->get_Count();
    if (totalPages == 0) {
        return;
    }
    int start = Math::Max(1, startPage);
    int end = Math::Min(endPage, totalPages);
    if (start > end) {
        return;
    }
    for (int pageNumber = start; pageNumber <= end; pageNumber++) {
        auto page = sourceDocument->get_Pages()->idx_get(pageNumber);
        destinationDocument->get_Pages()->CopyPage(page);
    }
}

void MergeWithSectionSeparatorsAndBookmarks(const std::vector<System::String>& inputFiles, String outputFile) {
    if (inputFiles.empty()) {
        throw ArgumentException(u"At least one input document is required.");
    }
    auto outputDocument = MakeObject<Document>();
    int sectionIndex = 1;
    for (auto& inputFile : inputFiles) {
        auto sourceDocument = MakeObject<Document>(inputFile);
        int sourcePageCount = sourceDocument->get_Pages()->get_Count();
        auto separatorPage = outputDocument->get_Pages()->Add();
        auto inputFileName = System::IO::Path::GetFileNameWithoutExtension(inputFile);
        separatorPage->get_Paragraphs()->Add(MakeObject<TextFragment>(
            String::Format(u"Section {0}: {1}", sectionIndex, inputFileName)));

        auto sectionBookmark = MakeObject<OutlineItemCollection>(outputDocument->get_Outlines());
        sectionBookmark->set_Title(String::Format(u"Section {0}", sectionIndex));
        sectionBookmark->set_Action(MakeObject<GoToAction>(separatorPage));
        outputDocument->get_Outlines()->Add(sectionBookmark);

        int firstContentPageNumber = outputDocument->get_Pages()->get_Count() + 1;
        appendPageRange(sourceDocument, outputDocument, 1, sourcePageCount);

        if (sourcePageCount > 0 && firstContentPageNumber <= outputDocument->get_Pages()->get_Count()) {
            auto contentBookmark = MakeObject<OutlineItemCollection>(outputDocument->get_Outlines());
            contentBookmark->set_Title(String::Format(u"Section {0} Content", sectionIndex));
            contentBookmark->set_Action(MakeObject<GoToAction>(outputDocument->get_Pages()->idx_get(firstContentPageNumber)));
            sectionBookmark->Add(contentBookmark);
        }
        sectionIndex++;
    }

    outputDocument->Save(outputFile);
}
```
