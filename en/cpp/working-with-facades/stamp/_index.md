---
title: Configure PDF image and text stamps in C++
linktitle: Stamp Class
type: docs
weight: 150
url: /cpp/stamp-class/
description: Create image, PDF-page, and text stamps with placement, rotation, transparency, and page selection using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Configure and Apply PDF Stamp Objects in C++
Abstract: Use the Stamp facade with PdfFileStamp to apply images, PDF pages, and formatted text. The examples configure origin, size, rotation, background placement, opacity, and target pages.
---

Use [Stamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/) to create image, PDF-page, and text stamps with placement, rotation, transparency, and page selection.

These examples use Aspose::Pdf::Facades::Stamp. Supply the required image or stamp PDF file; the PDF-page sample uses page 1 of the stamp source.

The snippets are independent example functions with their SDK includes and example namespaces. Configure the Aspose.PDF for C++ SDK, supply the input resources referenced by the sample, and choose writable output paths. The examples retain the source field names, page indexes, coordinates, and options.

## Add background image stamp

Apply an image stamp behind page content with opacity 0.35, rotation 45 degrees, size 160 by 80, and origin (200, 300).

1. Create [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/) and [Stamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Bind the stamp image with [Stamp::BindImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/bindimage/).
1. Set is background through [Stamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/) using the example values.
1. Set opacity through [Stamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/) using the example values.
1. Set quality through [Stamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/) using the example values.
1. Set rotation through [Stamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/) using the example values.
1. Set the image stamp dimensions with [Stamp::SetImageSize()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/setimagesize/).
1. Set stamp placement with [Stamp::SetOrigin()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/setorigin/).
1. Apply the configured stamp with [PdfFileStamp::AddStamp()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/addstamp/).
1. Save the resulting PDF with [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileStamp.h>
#include <Aspose.PDF.Cpp/Facades/Stamp.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Stamp
{
	using namespace System;
	using namespace Aspose::Pdf::Facades;

	void AddBackgroundImageStamp(String inputFile, String imageFile, String outputFile)
	{
		auto pdfStamper = MakeObject<PdfFileStamp>();
		pdfStamper->BindPdf(inputFile);
		auto stamp = MakeObject<Stamp>();
		stamp->BindImage(imageFile);
		stamp->set_IsBackground(true);
		stamp->set_Opacity(0.35f);
		stamp->set_Quality(90);
		stamp->set_Rotation(45.0f);
		stamp->SetImageSize(160, 80);
		stamp->SetOrigin(200, 300);
		pdfStamper->AddStamp(stamp);
		pdfStamper->Save(outputFile);
	}
} // namespace Facades::Examples::PDF_Stamp
```

## Add image stamp

Apply an image stamp with ID 1 at (36, 520).

1. Create [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/) and [Stamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Bind the stamp image with [Stamp::BindImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/bindimage/).
1. Set stamp id through [Stamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/) using the example values.
1. Set stamp placement with [Stamp::SetOrigin()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/setorigin/).
1. Apply the configured stamp with [PdfFileStamp::AddStamp()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/addstamp/).
1. Save the resulting PDF with [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileStamp.h>
#include <Aspose.PDF.Cpp/Facades/Stamp.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Stamp
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Stamp = Aspose::Pdf::Facades::Stamp;

void AddImageStamp(String inputFile, String imageFile, String outputFile)
{
    auto pdfStamper = MakeObject<PdfFileStamp>();
    pdfStamper->BindPdf(inputFile);
    auto stamp = MakeObject<Stamp>();
    stamp->BindImage(imageFile);
    stamp->set_StampId(1);
    stamp->SetOrigin(36, 520);
    pdfStamper->AddStamp(stamp);
    pdfStamper->Save(outputFile);
}
} // namespace Facades::Examples::PDF_Stamp
```

## Add PDF page as stamp

Use page 1 from stampPdf as a stamp on page 1 of the target PDF at (36, 250).

1. Create [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/) and [Stamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Bind the source PDF page with [Stamp::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/bindpdf/).
1. Set page number through [Stamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/) using the example values.
1. Set stamp placement with [Stamp::SetOrigin()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/setorigin/).
1. Apply the configured stamp with [PdfFileStamp::AddStamp()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/addstamp/).
1. Save the resulting PDF with [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileStamp.h>
#include <Aspose.PDF.Cpp/Facades/Stamp.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Stamp
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Stamp = Aspose::Pdf::Facades::Stamp;

void AddPdfPageAsStamp(String inputFile, String stampPdf, String outputFile)
{
    auto pdfStamper = MakeObject<PdfFileStamp>();
    pdfStamper->BindPdf(inputFile);
    auto stamp = MakeObject<Stamp>();
    stamp->BindPdf(stampPdf, 1);
    stamp->set_PageNumber(1);
    stamp->SetOrigin(36, 250);
    pdfStamper->AddStamp(stamp);
    pdfStamper->Save(outputFile);
}
} // namespace Facades::Examples::PDF_Stamp
```

## Add rotating stamp to PDF

Place a 100 by 100 image stamp on page 1 at half the page width and height and rotate it 90 degrees.

1. Create [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) and [Stamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/) and [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/).
1. Bind the stamp image with [Stamp::BindImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/bindimage/).
1. Set is background through [Stamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/) using the example values.
1. Set pages through [Stamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/) using the example values.
1. Set rotation through [Stamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/) using the example values.
1. Set stamp placement with [Stamp::SetOrigin()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/setorigin/).
1. Read the page width with [PdfFileInfo::GetPageWidth()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/getpagewidth/).
1. Read the page height with [PdfFileInfo::GetPageHeight()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/getpageheight/).
1. Set the image stamp dimensions with [Stamp::SetImageSize()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/setimagesize/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Apply the configured stamp with [PdfFileStamp::AddStamp()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/addstamp/).
1. Save the resulting PDF with [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileInfo.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileStamp.h>
#include <Aspose.PDF.Cpp/Facades/Stamp.h>
#include <system/array.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Stamp
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Stamp = Aspose::Pdf::Facades::Stamp;

void AddRotatingStampToPdf(String inputFile, String imageFile, String outputFile)
{
    auto fileInfo = MakeObject<PdfFileInfo>(inputFile);

    auto stamp = MakeObject<Stamp>();

    stamp->BindImage(imageFile);

    stamp->set_IsBackground(false);

    stamp->set_Pages(MakeArray<int32_t>({1}));

    stamp->set_Rotation(90);

    stamp->SetOrigin(fileInfo->GetPageWidth(1) / 2, fileInfo->GetPageHeight(1) / 2);

    stamp->SetImageSize(100, 100);

    auto stamper = MakeObject<PdfFileStamp>();

    stamper->BindPdf(inputFile);

    stamper->AddStamp(stamp);
    stamper->Save(outputFile);
}
} // namespace Facades::Examples::PDF_Stamp
```

## Add stamp to specific pages

Limit the image stamp to page 1 with size 120 by 60 and origin (400, 40).

1. Create [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/) and [Stamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Bind the stamp image with [Stamp::BindImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/bindimage/).
1. Set pages through [Stamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/) using the example values.
1. Set stamp placement with [Stamp::SetOrigin()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/setorigin/).
1. Set the image stamp dimensions with [Stamp::SetImageSize()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/setimagesize/).
1. Apply the configured stamp with [PdfFileStamp::AddStamp()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/addstamp/).
1. Save the resulting PDF with [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileStamp.h>
#include <Aspose.PDF.Cpp/Facades/Stamp.h>
#include <system/array.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Stamp
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Stamp = Aspose::Pdf::Facades::Stamp;

void AddStampToSpecificPages(String inputFile, String imageFile, String outputFile)
{
    auto pdfStamper = MakeObject<PdfFileStamp>();
    pdfStamper->BindPdf(inputFile);
    auto stamp = MakeObject<Stamp>();
    stamp->BindImage(imageFile);
    stamp->set_Pages(MakeArray<int32_t>({1}));
    stamp->SetOrigin(400, 40);
    stamp->SetImageSize(120, 60);
    pdfStamper->AddStamp(stamp);
    pdfStamper->Save(outputFile);
}
} // namespace Facades::Examples::PDF_Stamp
```

## Add text stamp with text state

Bind formatted approval text and a TextState to a stamp and apply it at (36, 700) with 15-degree rotation.

1. Create the text content and formatting with [FormattedText](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formattedtext/).
1. Configure text appearance through [TextState](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textstate/).
1. Create [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/) and [Stamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Bind the formatted stamp text with [Stamp::BindLogo()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/bindlogo/).
1. Set stamp text styling with [Stamp::BindTextState()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/bindtextstate/).
1. Set stamp placement with [Stamp::SetOrigin()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/setorigin/).
1. Set rotation through [Stamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/) using the example values.
1. Apply the configured stamp with [PdfFileStamp::AddStamp()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/addstamp/).
1. Save the resulting PDF with [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Facades/EncodingType.h>
#include <Aspose.PDF.Cpp/Facades/FontStyle.h>
#include <Aspose.PDF.Cpp/Facades/FormattedText.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileStamp.h>
#include <Aspose.PDF.Cpp/Facades/Stamp.h>
#include <Aspose.PDF.Cpp/Text/FontStyles.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>
#include <drawing/color.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Stamp
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using namespace Aspose::Pdf::Text;
using Stamp = Aspose::Pdf::Facades::Stamp;

void AddTextStampWithTextState(String inputFile, String outputFile)
{
    auto text = MakeObject<FormattedText>(u"Approved by signing workflow", System::Drawing::Color::get_Blue(),
                                          System::Drawing::Color::get_LightGray(), FontStyle::HelveticaBold,
                                          EncodingType::Winansi, true, 14);
    auto textState = MakeObject<TextState>();
    textState->set_ForegroundColor(Aspose::Pdf::Color::get_DarkBlue());
    textState->set_FontSize(16);
    textState->set_FontStyle(FontStyles::Bold);

    auto pdfStamper = MakeObject<PdfFileStamp>();
    pdfStamper->BindPdf(inputFile);
    auto stamp = MakeObject<Stamp>();
    stamp->BindLogo(text);
    stamp->BindTextState(textState);
    stamp->SetOrigin(36, 700);
    stamp->set_Rotation(15.0f);
    pdfStamper->AddStamp(stamp);
    pdfStamper->Save(outputFile);
}
} // namespace Facades::Examples::PDF_Stamp
```
