---
title: Create PDF document programmatically
linktitle: Create PDF
type: docs
weight: 10
url: /cpp/create-document/
description: Create a PDF document in C++, add a page and text, and save it using Aspose.PDF.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Generate a PDF Page with Text in C++
Abstract: Learn how to create a PDF document, add a page, and insert a TextFragment with Aspose.PDF for C++. The example saves a single-page document containing Hello World! text.
---

Create PDF files programmatically for reports, invoices, and other generated documents.

## Create a PDF with text

The example from `create-pdf.cpp` creates a single-page PDF containing “Hello World!”.

1. Create an empty [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Add a page to the document with [PageCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/add/).
1. Create a [TextFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/) containing Hello World!.
1. Add the text fragment to the page's [Paragraphs](https://reference.aspose.com/pdf/cpp/aspose.pdf/paragraphs/) collection.
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void CreatePDF(String path_outfile) {
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto textFragment = MakeObject<TextFragment>(u"Hello World!");
    page->get_Paragraphs()->Add(textFragment);
    document->Save(path_outfile);
}
```
