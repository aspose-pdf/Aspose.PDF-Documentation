---
title: Add PDF page stamps in C++
linktitle: Page Stamps
type: docs
weight: 130
url: /cpp/page-stamps-in-the-pdf-file/
description: Use the first page of another PDF as a background stamp on the first page of a target PDF with Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Overlay a Source PDF Page as a Background in C++
Abstract: Learn how to use PdfPageStamp to overlay the first page of another PDF on a target document's first page with Aspose.PDF for C++. The stamp uses background mode and adds page content without inserting a new page.
---

Use the first page of another PDF as a background stamp on the first page of a target PDF with Aspose.PDF for C++.

## Stamp a page from another PDF

Both PDFs must contain at least one page. This overlays page content rather than adding another page to the target document.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [PdfPageStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf/pdfpagestamp/) from pageStampFile and source page number 1.
1. Enable background mode.
1. Call [AddStamp()](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/addstamp/) on target page 1.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/PdfPageStamp.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of StampingExamples.addPageStamp.
void AddPageStamp(System::String inputFile, System::String pageStampFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);

    auto pageStamp = MakeObject<PdfPageStamp>(pageStampFile, 1);
    pageStamp->set_Background(true);
    document->get_Pages()->idx_get(1)->AddStamp(pageStamp);
    document->Save(outputFile);
}
```
