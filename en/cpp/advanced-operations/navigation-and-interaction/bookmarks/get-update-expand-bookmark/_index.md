---
title: Get, update, and expand PDF bookmarks in C++
linktitle: Get, Update and Expand a Bookmark
type: docs
weight: 20
url: /cpp/get-update-and-expand-bookmark/
description: Read bookmark titles, styles, and page numbers, update a child bookmark, and expand top-level outlines using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inspect PDF Outline Targets and Update Bookmark Display in C++
Abstract: Read bookmark properties and destination page numbers with Aspose.PDF for C++. The examples also update the first child bookmark and configure the document to display expanded top-level outlines.
---

Use these examples to inspect outline properties or change existing bookmarks. The update example requires a first top-level entry with at least one child.

Configure the Aspose.PDF for C++ SDK and create the output directory before running examples that save a file. The snippets retain the source includes, function parameters, coordinates, and action settings, with the project runner header omitted.

## Read top-level bookmarks

Print each top-level bookmark's title, italic flag, bold flag, and color.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Iterate over the one-based [OutlineCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/outlinecollection/) indexes.
1. Read and print the [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/outlineitemcollection/) title and style properties.

```cpp
#include <iostream>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Outlines/OutlineCollection.h>
#include <Aspose.PDF.Cpp/Outlines/OutlineItemCollection.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of bookmarks/GetExamples.getBookmarks.
void GetBookmarks(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (int i = 1; i <= document->get_Outlines()->get_Count(); i++) {
        auto outlineItem = document->get_Outlines()->idx_get(i);
        std::cout << outlineItem->get_Title() << std::endl;
        std::cout << outlineItem->get_Italic() << std::endl;
        std::cout << outlineItem->get_Bold() << std::endl;
        std::cout << outlineItem->get_Color().ToString() << std::endl;
    }
}
```

## Read child bookmarks

Print top-level bookmark properties and the same properties for their immediate children. The example does not recurse into deeper levels.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Iterate over the document [Outlines](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_outlines/).
1. Read each [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/outlineitemcollection/) and print its title and style.
1. Enumerate the item's immediate children and print their properties.

```cpp
#include <iostream>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/Bookmarks.h>
#include <Aspose.PDF.Cpp/Outlines/OutlineCollection.h>
#include <Aspose.PDF.Cpp/Outlines/OutlineItemCollection.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of bookmarks/GetExamples.getChildBookmarks.
void GetChildBookmarks(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (int i = 1; i <= document->get_Outlines()->get_Count(); i++) {
        auto outlineItem = document->get_Outlines()->idx_get(i);
        std::cout << outlineItem->get_Title() << std::endl;
        std::cout << outlineItem->get_Italic() << std::endl;
        std::cout << outlineItem->get_Bold() << std::endl;
        std::cout << outlineItem->get_Color().ToString() << std::endl;
        int count = outlineItem->get_Count();
        if (count > 0) {
            std::cout << "Child Bookmarks" << std::endl;
            for (int j = 1; j <= outlineItem->get_Count(); j++) {
                auto childOutlineItem = outlineItem->idx_get(j);
                std::cout << childOutlineItem->get_Title() << std::endl;
                std::cout << childOutlineItem->get_Italic() << std::endl;
                std::cout << childOutlineItem->get_Bold() << std::endl;
                std::cout << childOutlineItem->get_Color().ToString() << std::endl;
            }
        }
    }
}
```

## Read bookmark page numbers

Use PdfBookmarkEditor to extract bookmarks and print the title, target page, and action. Indentation is built from each bookmark's Level.

1. Create a [PdfBookmarkEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/) and bind the input PDF.
1. Call [ExtractBookmarks()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/extractbookmarks/).
1. Read each [Bookmark](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/bookmark/) level, title, page number, and action and print them.
1. Close the [PdfBookmarkEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/).

```cpp
#include <iostream>
#include <Aspose.PDF.Cpp/Facades/Bookmark.h>
#include <Aspose.PDF.Cpp/Facades/Bookmarks.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfBookmarkEditor.h>
#include <Aspose.PDF.Cpp/Page.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

// Port of bookmarks/GetExamples.getBookmarkPageNumber.
void GetBookmarkPageNumber(System::String inputFile)
{
    auto bookmarkEditor = MakeObject<PdfBookmarkEditor>();

    bookmarkEditor->BindPdf(inputFile);
    for (const auto& bookmark : bookmarkEditor->ExtractBookmarks()) {
        String levelSeparator = u"";
        for (int i = 0; i < bookmark->get_Level(); i++) {
            levelSeparator += u"----";
        }

        std::cout << levelSeparator << " Title: " << bookmark->get_Title() << std::endl;
        std::cout << levelSeparator << " Page Number: " << bookmark->get_PageNumber() << std::endl;
        std::cout << levelSeparator << " Page Action: " << bookmark->get_Action() << std::endl;
    }

    bookmarkEditor->Close();
}
```

## Update a child bookmark

Select the first child of the first top-level bookmark, rename it Updated Outline, and enable bold and italic text. The input must contain that hierarchy.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Get the first [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/outlineitemcollection/) from the document outline tree.
1. Select its first child using [idx_get()](https://reference.aspose.com/pdf/cpp/aspose.pdf/outlineitemcollection/idx_get/).
1. Set the child title, italic flag, and bold flag.
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Outlines/OutlineCollection.h>
#include <Aspose.PDF.Cpp/Outlines/OutlineItemCollection.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of bookmarks/GetExamples.updateBookmarks.
void UpdateBookmarks(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto outline = document->get_Outlines()->idx_get(1);
    auto childOutline = outline->idx_get(1);
    childOutline->set_Title(u"Updated Outline");
    childOutline->set_Italic(true);
    childOutline->set_Bold(true);

    document->Save(outputFile);
}
```

## Expand top-level bookmarks

Set the document page mode to UseOutlines and mark each top-level bookmark as open. The example does not recursively set Open on every descendant.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Set [Document::set_PageMode()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/set_pagemode/) to UseOutlines.
1. Iterate over the top-level [OutlineCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/outlinecollection/).
1. Set [OutlineItemCollection::set_Open()](https://reference.aspose.com/pdf/cpp/aspose.pdf/outlineitemcollection/set_open/) to true for each item.
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/DOM/PageMode.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Outlines/OutlineCollection.h>
#include <Aspose.PDF.Cpp/Outlines/OutlineItemCollection.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of bookmarks/GetExamples.expandedBookmarks.
void ExpandedBookmarks(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    document->set_PageMode(PageMode::UseOutlines);
    for (int i = 1; i <= document->get_Outlines()->get_Count(); i++) {
        auto item = document->get_Outlines()->idx_get(i);
        item->set_Open(true);
    }
    document->Save(outputFile);
}
```
