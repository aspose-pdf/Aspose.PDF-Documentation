---
title: Add PDF pages in C++
linktitle: Add Pages
type: docs
weight: 10
url: /cpp/add-pages/
description: Add blank pages, insert a page at a specific position, or copy a page from another PDF using Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Append, Insert, and Copy Pages into PDFs in C++
Abstract: Learn how to append a blank PDF page or insert one at a specified position with Aspose.PDF for C++. A separate example copies a page from another PDF document.
---

Add blank pages, insert a page at a specific position, or copy a page from another PDF using Aspose.PDF for C++.

## Add an empty page at the end

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Call [Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/add/) on the document [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/).
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).


```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of AddPagesExamples.addEmptyPageToEnd.
void AddEmptyPageToEnd(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);

    document->get_Pages()->Add();
    document->Save(outputFile);
}
```

## Insert an empty page

Use an input PDF with at least one page.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Call [Insert()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/insert/) on [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/) at position 2.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of AddPagesExamples.insertEmptyPage.
void InsertEmptyPage(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);

    document->get_Pages()->Insert(2);
    document->Save(outputFile);
}
```

## Copy a page from another document

The output contains a new text page followed by the copied page.

1. Create an output [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and open the input PDF.
1. Add a first page with a [TextFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/).
1. Call [CopyPage()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/) to append page 1 from the input PDF.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

// Port of AddPagesExamples.addPageFromAnotherDocument.
void AddPageFromAnotherDocument(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto anotherDocument = MakeObject<Document>(inputFile);

    document->get_Pages()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>(u"This is first page!"));
    document->get_Pages()->CopyPage(anotherDocument->get_Pages()->idx_get(1));
    document->Save(outputFile);
}
```
