---
title: Add text and images to PDF pages in C++
linktitle: PdfFileMend Class
type: docs
weight: 100
url: /cpp/pdffilemend-class/
description: Place images and formatted text on PDF pages and configure compositing or word wrapping using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Place PDF Text and Images with PdfFileMend in C++
Abstract: Use PdfFileMend to place images and formatted text at explicit coordinates. The examples include compositing settings, word wrapping, and text placement on multiple pages.
---

Use [PdfFileMend](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilemend/) to place images and formatted text on PDF pages and configure compositing or word wrapping.

In AddImage01 through AddImage04, inputFile is an image path and the function creates a new PDF page. Text examples accept a PDF path. AddText03 appends three pages before adding text to pages 1 and 3.

The snippets are independent example functions with their SDK includes and example namespaces. Configure the Aspose.PDF for C++ SDK, supply the input resources referenced by the sample, and choose writable output paths. The examples retain the source field names, page indexes, coordinates, and options.

## Add an image to a new PDF

Create a new one-page PDF and add inputFile as an image in the rectangle (10, 650, 110, 750).

1. Create [PdfFileMend](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilemend/).
1. Create or open the [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and prepare its pages as shown.
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Place the image with [PdfFileMend::AddImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilemend/addimage/).
1. Save the resulting PDF with [PdfFileMend](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilemend/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileMend.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileMend
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void AddImage01(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    document->get_Pages()->Add();

    auto mender = MakeObject<PdfFileMend>();

    mender->BindPdf(document);

    mender->AddImage(inputFile, 1, 10, 650, 110, 750);

    mender->Save(outputFile);
}
} // namespace Facades::Examples::PDF_FileMend
```

## Add an image with Multiply blending

Place an image on a new page with Multiply compositing.

1. Create [PdfFileMend](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilemend/).
1. Create or open the [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and prepare its pages as shown.
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Place the image with [PdfFileMend::AddImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilemend/addimage/).
1. Save the resulting PDF with [PdfFileMend](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilemend/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/BlendMode.h>
#include <Aspose.PDF.Cpp/CompositingParameters.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileMend.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileMend
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void AddImage02(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    document->get_Pages()->Add();

    auto mender = MakeObject<PdfFileMend>();

    mender->BindPdf(document);

    int pageNum = 1;
    int lowerLeftX = 10;
    int lowerLeftY = 650;
    int upperRightX = 110;
    int upperRightY = 750;

    auto compositingParameters = MakeObject<CompositingParameters>(BlendMode::Multiply);

    mender->AddImage(inputFile, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

    mender->Save(outputFile);
}
} // namespace Facades::Examples::PDF_FileMend
```

## Add an image with Exclusion blending and Flate filtering

Place an image on a new page with Exclusion blending and Flate filtering.

1. Create [PdfFileMend](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilemend/).
1. Create or open the [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and prepare its pages as shown.
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Place the image with [PdfFileMend::AddImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilemend/addimage/).
1. Save the resulting PDF with [PdfFileMend](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilemend/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/BlendMode.h>
#include <Aspose.PDF.Cpp/CompositingParameters.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileMend.h>
#include <Aspose.PDF.Cpp/ImageFilterType.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileMend
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void AddImage03(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    document->get_Pages()->Add();

    auto mender = MakeObject<PdfFileMend>();

    mender->BindPdf(document);

    int pageNum = 1;
    int lowerLeftX = 10;
    int lowerLeftY = 650;
    int upperRightX = 110;
    int upperRightY = 750;

    auto compositingParameters = MakeObject<CompositingParameters>(BlendMode::Exclusion, ImageFilterType::Flate);

    mender->AddImage(inputFile, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

    mender->Save(outputFile);
}
} // namespace Facades::Examples::PDF_FileMend
```

## Add an image with explicit compositing options

Place an image with Multiply blending, Flate filtering, and the third compositing option set to false.

1. Create [PdfFileMend](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilemend/).
1. Create or open the [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and prepare its pages as shown.
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Place the image with [PdfFileMend::AddImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilemend/addimage/).
1. Save the resulting PDF with [PdfFileMend](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilemend/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/BlendMode.h>
#include <Aspose.PDF.Cpp/CompositingParameters.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileMend.h>
#include <Aspose.PDF.Cpp/ImageFilterType.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileMend
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void AddImage04(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    document->get_Pages()->Add();

    auto mender = MakeObject<PdfFileMend>();

    mender->BindPdf(document);

    int pageNum = 1;
    int lowerLeftX = 10;
    int lowerLeftY = 650;
    int upperRightX = 110;
    int upperRightY = 750;

    auto compositingParameters = MakeObject<CompositingParameters>(BlendMode::Multiply, ImageFilterType::Flate, false);

    mender->AddImage(inputFile, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

    mender->Save(outputFile);
}
} // namespace Facades::Examples::PDF_FileMend
```

## Add formatted text to a page

Add Welcome to Aspose! to page 1 at (10, 750).

1. Create [PdfFileMend](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilemend/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Place formatted text with [PdfFileMend::AddText()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilemend/addtext/).
1. Save the resulting PDF with [PdfFileMend](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilemend/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/FormattedText.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileMend.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileMend
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void AddText01(String inputFile, String outputFile)
{
    auto mender = MakeObject<PdfFileMend>();

    mender->BindPdf(inputFile);

    auto message = MakeObject<FormattedText>(u"Welcome to Aspose!");

    mender->AddText(message, 1, 10, 750);

    mender->Save(outputFile);
}
} // namespace Facades::Examples::PDF_FileMend
```

## Set word wrapping for formatted text

Add formatted text to page 1 and set WrapMode to ByWords before saving.

1. Create [PdfFileMend](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilemend/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Place formatted text with [PdfFileMend::AddText()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilemend/addtext/).
1. Set wrap mode through [PdfFileMend](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilemend/) using the example values.
1. Save the resulting PDF with [PdfFileMend](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilemend/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/FormattedText.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileMend.h>
#include <Aspose.PDF.Cpp/Facades/WordWrapMode.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileMend
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void AddText02(String inputFile, String outputFile)
{
    auto mender = MakeObject<PdfFileMend>();

    mender->BindPdf(inputFile);

    auto message = MakeObject<FormattedText>(u"Welcome to Aspose!");

    mender->AddText(message, 1, 10, 750);
    mender->set_WrapMode(WordWrapMode::ByWords);

    mender->Save(outputFile);
}
} // namespace Facades::Examples::PDF_FileMend
```

## Add text to multiple pages

Append three pages to the input PDF and add formatted text to pages 1 and 3 within the specified rectangle.

1. Create [PdfFileMend](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilemend/).
1. Create or open the [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and prepare its pages as shown.
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Place formatted text with [PdfFileMend::AddText()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilemend/addtext/).
1. Save the resulting PDF with [PdfFileMend](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilemend/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/FormattedText.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileMend.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <system/array.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileMend
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void AddText03(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);

    document->get_Pages()->Add();
    document->get_Pages()->Add();
    document->get_Pages()->Add();

    auto mender = MakeObject<PdfFileMend>();

    mender->BindPdf(document);

    auto message = MakeObject<FormattedText>(u"Welcome to Aspose!");

    auto pageNums = MakeArray<int32_t>({1, 3});

    float llx = 10;
    float lly = 750;
    float urx = 310;
    float ury = 760;
    mender->AddText(message, pageNums, llx, lly, urx, ury);

    mender->Save(outputFile);
}
} // namespace Facades::Examples::PDF_FileMend
```
