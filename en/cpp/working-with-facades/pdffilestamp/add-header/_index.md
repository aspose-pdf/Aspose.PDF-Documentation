---
title: Add Header to PDF in C++
linktitle: Add Header to PDF
type: docs
weight: 20
url: /cpp/add-header/
description: Add Header to PDF in C++ with the PdfFileStamp facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Header to PDF with the PdfFileStamp Facade
Abstract: Add a blue 12-point Helvetica header using margin values of 20. Add an image header from a file stream with a margin value of 20. Add Sample Header as formatted text with a margin value of 20.
---

Use [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/) for this task. The examples below retain the original C++ code and API Reference steps.

## Add header with margins

Add a blue 12-point Helvetica header using margin values of 20.

1. Create the text content and formatting with [FormattedText](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formattedtext/).
1. Create [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Add the header with [PdfFileStamp::AddHeader()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/addheader/).
1. Save the resulting PDF with [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Facades/EncodingType.h>
#include <Aspose.PDF.Cpp/Facades/FontStyle.h>
#include <Aspose.PDF.Cpp/Facades/FormattedText.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileStamp.h>
#include <drawing/color.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileStamp
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using DrawingColor = System::Drawing::Color;

void AddHeaderWithMargins(String inputFile, String outputFile)
{
    auto pdfStamper = MakeObject<PdfFileStamp>();
    pdfStamper->BindPdf(inputFile);
    auto text = MakeObject<FormattedText>(u"Sample Header", DrawingColor::get_Blue(), FontStyle::Helvetica,
                                          EncodingType::Winansi, true, 12.0f);
    pdfStamper->AddHeader(text, 20, 20, 20);
    pdfStamper->Save(outputFile);
}
} // namespace Facades::Examples::PDF_FileStamp
```

## Add image header

Add an image header from a file stream with a margin value of 20.

1. Create [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Add the header with [PdfFileStamp::AddHeader()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/addheader/).
1. Save the resulting PDF with [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileStamp.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileStamp
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void AddImageHeader(String inputFile, String imageFile, String outputFile)
{
    auto pdfStamper = MakeObject<PdfFileStamp>();
    auto imageStream = System::IO::File::OpenRead(imageFile);

    pdfStamper->BindPdf(inputFile);
    pdfStamper->AddHeader(imageStream, 20);
    pdfStamper->Save(outputFile);
}
} // namespace Facades::Examples::PDF_FileStamp
```

## Add text header

Add Sample Header as formatted text with a margin value of 20.

1. Create the text content and formatting with [FormattedText](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formattedtext/).
1. Create [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Add the header with [PdfFileStamp::AddHeader()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/addheader/).
1. Save the resulting PDF with [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/FormattedText.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileStamp.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileStamp
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void AddTextHeader(String inputFile, String outputFile)
{
    auto pdfStamper = MakeObject<PdfFileStamp>();
    pdfStamper->BindPdf(inputFile);
    auto text = MakeObject<FormattedText>(u"Sample Header");
    pdfStamper->AddHeader(text, 20);
    pdfStamper->Save(outputFile);
}
} // namespace Facades::Examples::PDF_FileStamp
```
