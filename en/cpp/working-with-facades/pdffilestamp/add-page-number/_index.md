---
title: Add Page Number to PDF in C++
linktitle: Add Page Number to PDF
type: docs
weight: 30
url: /cpp/page-number/
description: Add Page Number to PDF in C++ with the PdfFileStamp facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Page Number to PDF with the PdfFileStamp Facade
Abstract: Add Page # numbering at (300, 20). Add Page # numbering using default positioning. Add Page # numbering at PosBottomRight with all four margins set to 10. Set uppercase Roman numbering, start at 42, and add the page number at PosUpperRight.
---

Use [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/) for this task. The examples below retain the original C++ code and API Reference steps.

## Add page numbers at coordinates

Add Page # numbering at (300, 20).

1. Create [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Add page numbering with [PdfFileStamp::AddPageNumber()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/addpagenumber/).
1. Save the resulting PDF with [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileStamp.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileStamp
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void AddPageNumbersAtCoordinates(String inputFile, String outputFile)
{
    auto pdfStamper = MakeObject<PdfFileStamp>();
    pdfStamper->BindPdf(inputFile);
    pdfStamper->AddPageNumber(u"Page #", 300, 20);
    pdfStamper->Save(outputFile);
}
} // namespace Facades::Examples::PDF_FileStamp
```

## Add page numbers default

Add Page # numbering using default positioning.

1. Create [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Add page numbering with [PdfFileStamp::AddPageNumber()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/addpagenumber/).
1. Save the resulting PDF with [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileStamp.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileStamp
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void AddPageNumbersDefault(String inputFile, String outputFile)
{
    auto pdfStamper = MakeObject<PdfFileStamp>();
    pdfStamper->BindPdf(inputFile);
    pdfStamper->AddPageNumber(u"Page #");
    pdfStamper->Save(outputFile);
}
} // namespace Facades::Examples::PDF_FileStamp
```

## Add page numbers with position and margins

Add Page # numbering at PosBottomRight with all four margins set to 10.

1. Create [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Add page numbering with [PdfFileStamp::AddPageNumber()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/addpagenumber/).
1. Save the resulting PDF with [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileStamp.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileStamp
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void AddPageNumbersWithPositionAndMargins(String inputFile, String outputFile)
{
    auto pdfStamper = MakeObject<PdfFileStamp>();
    pdfStamper->BindPdf(inputFile);
    pdfStamper->AddPageNumber(u"Page #", PdfFileStamp::PosBottomRight, 10, 10, 10, 10);
    pdfStamper->Save(outputFile);
}
} // namespace Facades::Examples::PDF_FileStamp
```

## Add page numbers with roman style

Set uppercase Roman numbering, start at 42, and add the page number at PosUpperRight.

1. Create [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Set numbering style through [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/) using the example values.
1. Set starting number through [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/) using the example values.
1. Add page numbering with [PdfFileStamp::AddPageNumber()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/addpagenumber/).
1. Save the resulting PDF with [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileStamp.h>
#include <Aspose.PDF.Cpp/NumberingStyle.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileStamp
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void AddPageNumbersWithRomanStyle(String inputFile, String outputFile)
{
    auto pdfStamper = MakeObject<PdfFileStamp>();
    pdfStamper->BindPdf(inputFile);
    pdfStamper->set_NumberingStyle(NumberingStyle::NumeralsRomanUppercase);
    pdfStamper->set_StartingNumber(42);
    pdfStamper->AddPageNumber(u"Page #", PdfFileStamp::PosUpperRight);
    pdfStamper->Save(outputFile);
}
} // namespace Facades::Examples::PDF_FileStamp
```
