---
title: Split PDF documents in C++
linktitle: Split PDF documents
type: docs
weight: 60
url: /cpp/split-pdf-document/
description: Split PDF documents into individual pages, balanced parts, page ranges, custom groups, or odd and even pages with Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Separate PDF Pages into Ranges and Custom Groups in C++
Abstract: Learn how to split PDF documents into individual pages, balanced parts, or selected ranges with Aspose.PDF for C++. The examples also create custom page groups and separate odd and even pages.
---

Split PDF documents into individual pages, balanced parts, page ranges, custom groups, or odd and even pages with Aspose.PDF for C++.

## Split into individual pages

1. Create the output directory.
1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Iterate through the one-based page numbers.
1. Create an output [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) for each page and copy it with [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/).
1. Save each part with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/) as Page_N.pdf.

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

void SplitDocuments(String inputFile, String outputDir)
{
    std::filesystem::create_directories(std::filesystem::path(outputDir.ToWCS()));
    auto document = MakeObject<Document>(inputFile);
    const int totalPages = document->get_Pages()->get_Count();
    for (int pageNumber = 1; pageNumber <= totalPages; ++pageNumber) {
        auto part = MakeObject<Document>();
        part->get_Pages()->CopyPage(document->get_Pages()->idx_get(pageNumber));
        part->Save(System::IO::Path::Combine(outputDir, String::Format(u"Page_{0}.pdf", pageNumber)));
    }
}
```

## Split into two parts

1. Create the output directory.
1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Calculate the midpoint, assigning the extra page to the first part for an odd page count.
1. Copy each nonempty range into a new [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) using [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/).
1. Save each part with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

void SplitDocumentsIntoTwoParts(String inputFile, String outputDir)
{
    std::filesystem::create_directories(std::filesystem::path(outputDir.ToWCS()));
    auto document = MakeObject<Document>(inputFile);
    const int totalPages = document->get_Pages()->get_Count();
    const int midPoint = totalPages / 2 + totalPages % 2;
    for (int partIndex = 1; partIndex <= 2; ++partIndex) {
        auto part = MakeObject<Document>();
        const int startPage = partIndex == 1 ? 1 : midPoint + 1;
        const int endPage = partIndex == 1 ? midPoint : totalPages;
        if (startPage > endPage) {
            continue;
        }
        for (int pageNumber = startPage; pageNumber <= endPage; ++pageNumber) {
            part->get_Pages()->CopyPage(document->get_Pages()->idx_get(pageNumber));
        }
        part->Save(System::IO::Path::Combine(outputDir, String::Format(u"Part_{0}.pdf", partIndex)));
    }
}
```

## Split every N pages

1. Require a positive pagesPerPart value and create the output directory.
1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Calculate each consecutive range of at most N pages.
1. Copy each range into a new [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) using [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/).
1. Save each part with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

void SplitDocumentsEveryNPages(String inputFile, String outputDir, int pagesPerPart)
{
    if (pagesPerPart <= 0) {
        throw ArgumentOutOfRangeException(u"pagesPerPart", u"Pages per part must be positive.");
    }
    std::filesystem::create_directories(std::filesystem::path(outputDir.ToWCS()));
    auto document = MakeObject<Document>(inputFile);
    const int totalPages = document->get_Pages()->get_Count();
    int partIndex = 1;
    for (int startPage = 1; startPage <= totalPages;) {
        const int count = Math::Min(pagesPerPart, totalPages - startPage + 1);
        const int endPage = startPage + count - 1;
        auto part = MakeObject<Document>();
        for (int pageNumber = startPage; pageNumber <= endPage; ++pageNumber) {
            part->get_Pages()->CopyPage(document->get_Pages()->idx_get(pageNumber));
        }
        part->Save(System::IO::Path::Combine(outputDir,
            String::Format(u"Every_{0}_Part_{1}.pdf", pagesPerPart, partIndex++)));
        if (endPage == totalPages) {
            break;
        }
        startPage = endPage + 1;
    }
}
```

## Split by page ranges

1. Create the output directory.
1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Use the supplied ranges 1–3, 4–6, and 7 through the last page.
1. Clip range ends to the page count and skip empty ranges.
1. Copy each range using [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/) and save it with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

void SplitDocumentsByPageRanges(String inputFile, String outputDir)
{
    std::filesystem::create_directories(std::filesystem::path(outputDir.ToWCS()));
    auto document = MakeObject<Document>(inputFile);
    const int totalPages = document->get_Pages()->get_Count();
    const std::array<std::pair<int, int>, 3> ranges = {{{1, 3}, {4, 6}, {7, totalPages}}};
    for (std::size_t index = 0; index < ranges.size(); ++index) {
        const int startPage = ranges[index].first;
        const int endPage = Math::Min(ranges[index].second, totalPages);
        if (startPage > endPage) {
            continue;
        }
        auto part = MakeObject<Document>();
        for (int pageNumber = startPage; pageNumber <= endPage; ++pageNumber) {
            part->get_Pages()->CopyPage(document->get_Pages()->idx_get(pageNumber));
        }
        part->Save(System::IO::Path::Combine(outputDir,
            String::Format(u"Range_{0}_{1}_to_{2}.pdf", static_cast<int>(index + 1), startPage, endPage)));
    }
}
```

## Separate the first page

1. Create the output directory.
1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Return when there are no pages.
1. Copy page 1 into a new [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and save it with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).
1. Copy pages 2 through the end using [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/) and save them when present.

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

void SplitDocumentsFirstPageAndRest(String inputFile, String outputDir)
{
    std::filesystem::create_directories(std::filesystem::path(outputDir.ToWCS()));
    auto document = MakeObject<Document>(inputFile);
    const int totalPages = document->get_Pages()->get_Count();
    if (totalPages == 0) {
        return;
    }
    auto firstPage = MakeObject<Document>();
    firstPage->get_Pages()->CopyPage(document->get_Pages()->idx_get(1));
    firstPage->Save(System::IO::Path::Combine(outputDir, u"First_Page.pdf"));
    if (totalPages == 1) {
        return;
    }
    auto remainingPages = MakeObject<Document>();
    for (int pageNumber = 2; pageNumber <= totalPages; ++pageNumber) {
        remainingPages->get_Pages()->CopyPage(document->get_Pages()->idx_get(pageNumber));
    }
    remainingPages->Save(System::IO::Path::Combine(outputDir, u"Remaining_Pages.pdf"));
}
```

## Separate the last page

1. Create the output directory.
1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Return when there are no pages.
1. Copy the last page into a new [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and save it with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).
1. Delete the last page from the original [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/) and save the preceding pages when present.

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

void SplitDocumentsLastPageAndRest(String inputFile, String outputDir)
{
    std::filesystem::create_directories(std::filesystem::path(outputDir.ToWCS()));
    auto document = MakeObject<Document>(inputFile);
    const int totalPages = document->get_Pages()->get_Count();
    if (totalPages == 0) {
        return;
    }
    auto lastPage = MakeObject<Document>();
    lastPage->get_Pages()->CopyPage(document->get_Pages()->idx_get(totalPages));
    lastPage->Save(System::IO::Path::Combine(outputDir, u"Last_Page.pdf"));
    if (totalPages == 1) {
        return;
    }
    document->get_Pages()->Delete(totalPages);
    document->Save(System::IO::Path::Combine(outputDir, u"Previous_Pages.pdf"));
}
```

## Split into three balanced parts

1. Create the output directory.
1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Use up to three nonempty parts.
1. Distribute remainder pages among the first parts.
1. Copy each consecutive range using [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/) and save it with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

void SplitDocumentsIntoThreeParts(String inputFile, String outputDir)
{
    std::filesystem::create_directories(std::filesystem::path(outputDir.ToWCS()));
    auto document = MakeObject<Document>(inputFile);
    const int totalPages = document->get_Pages()->get_Count();
    if (totalPages == 0) {
        return;
    }
    const int partCount = Math::Min(3, totalPages);
    int startPage = 1;
    for (int partIndex = 0; partIndex < partCount; ++partIndex) {
        const int partSize = totalPages / partCount + (partIndex < totalPages % partCount ? 1 : 0);
        if (startPage > totalPages) {
            break;
        }
        const int endPage = startPage + Math::Min(partSize, totalPages - startPage + 1) - 1;
        auto part = MakeObject<Document>();
        for (int pageNumber = startPage; pageNumber <= endPage; ++pageNumber) {
            part->get_Pages()->CopyPage(document->get_Pages()->idx_get(pageNumber));
        }
        part->Save(System::IO::Path::Combine(outputDir,
            String::Format(u"Three_Parts_{0}.pdf", partIndex + 1)));
        if (endPage == totalPages) { break; }
        startPage = endPage + 1;
    }
}
```

## Split into custom page groups

Pages outside these groups are omitted. Adjust the groups for your input.

1. Create the output directory.
1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Use the supplied groups {1, 2, 5} and {3, 4, 6, 7}.
1. Copy only valid page numbers using [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/).
1. Save each nonempty group with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

void SplitDocumentsCustomPageGroups(String inputFile, String outputDir)
{
    std::filesystem::create_directories(std::filesystem::path(outputDir.ToWCS()));
    auto document = MakeObject<Document>(inputFile);
    const int totalPages = document->get_Pages()->get_Count();
    const std::vector<std::vector<int>> groups = {{1, 2, 5}, {3, 4, 6, 7}};
    int groupIndex = 1;
    for (const auto& group : groups) {
        auto part = MakeObject<Document>();
        for (int pageNumber : group) {
            if (pageNumber >= 1 && pageNumber <= totalPages) {
                part->get_Pages()->CopyPage(document->get_Pages()->idx_get(pageNumber));
            }
        }
        if (part->get_Pages()->get_Count() > 0) {
            part->Save(System::IO::Path::Combine(outputDir,
                String::Format(u"Custom_Group_{0}.pdf", groupIndex)));
        }
        ++groupIndex;
    }
}
```

## Split with padded filenames

1. Create the output directory.
1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Copy each page into a new [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) using [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/).
1. Save each page with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/) using a three-digit minimum width, such as Page_001.pdf.

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

void SplitDocumentsWithStableFilenames(String inputFile, String outputDir)
{
    std::filesystem::create_directories(std::filesystem::path(outputDir.ToWCS()));
    auto document = MakeObject<Document>(inputFile);
    const int totalPages = document->get_Pages()->get_Count();
    for (int pageNumber = 1; pageNumber <= totalPages; ++pageNumber) {
        auto part = MakeObject<Document>();
        part->get_Pages()->CopyPage(document->get_Pages()->idx_get(pageNumber));
        part->Save(System::IO::Path::Combine(outputDir, String::Format(u"Page_{0:D3}.pdf", pageNumber)));
    }
}
```

## Split odd and even pages

1. Create the output directory.
1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Copy odd-numbered pages into one [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) with [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/).
1. Copy even-numbered pages into another document.
1. Save each nonempty result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

void SplitDocumentsOddEvenPages(String inputFile, String outputDir)
{
    std::filesystem::create_directories(std::filesystem::path(outputDir.ToWCS()));
    auto document = MakeObject<Document>(inputFile);
    const int totalPages = document->get_Pages()->get_Count();
    auto oddPages = MakeObject<Document>();
    for (int pageNumber = 1; pageNumber <= totalPages; pageNumber += 2) {
        oddPages->get_Pages()->CopyPage(document->get_Pages()->idx_get(pageNumber));
    }
    if (oddPages->get_Pages()->get_Count() > 0) {
        oddPages->Save(System::IO::Path::Combine(outputDir, u"Odd_Pages.pdf"));
    }

    auto evenPages = MakeObject<Document>();
    for (int pageNumber = 2; pageNumber <= totalPages; pageNumber += 2) {
        evenPages->get_Pages()->CopyPage(document->get_Pages()->idx_get(pageNumber));
    }
    if (evenPages->get_Pages()->get_Count() > 0) {
        evenPages->Save(System::IO::Path::Combine(outputDir, u"Even_Pages.pdf"));
    }
}
```
