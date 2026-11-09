---
title: Add PDF headers, footers, and page numbers in C++
linktitle: PdfFileStamp Class
type: docs
weight: 130
url: /cpp/pdffilestamp-class/
description: Add text and image headers or footers, image stamps, and page numbers with configurable position and style using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Stamp PDF Pages and Add Pagination in C++
Abstract: Use PdfFileStamp to add text or image headers and footers and apply image stamps. Page-numbering examples demonstrate defaults, coordinates, margins, and Roman numerals with a custom starting number.
---

Use [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/) to add text and image headers or footers, image stamps, and page numbers with configurable position and style.

The examples bind an existing PDF and save the stamped result. Image variants require imageFile. The # placeholder in page-number text is replaced by the generated page number.

The snippets are independent example functions with their SDK includes and example namespaces. Configure the Aspose.PDF for C++ SDK, supply the input resources referenced by the sample, and choose writable output paths. The examples retain the source field names, page indexes, coordinates, and options.

## Add footer with margins

Add formatted footer text using the overload with three margin values set to 20.

1. Create [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Add the footer with [PdfFileStamp::AddFooter()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/addfooter/).
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

	void AddFooterWithMargins(String inputFile, String outputFile)
	{
		auto pdfStamper = MakeObject<PdfFileStamp>();
		pdfStamper->BindPdf(inputFile);
		auto text = MakeObject<FormattedText>(u"This footer has margins on all sides.");
		pdfStamper->AddFooter(text, 20, 20, 20);
		pdfStamper->Save(outputFile);
	}
} // namespace Facades::Examples::PDF_FileStamp
```

## Add header with margins

Add a blue 12-point Helvetica header using margin values of 20.

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

## Add image footer

Add an image footer from a file stream with a margin value of 20.

1. Create [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Add the footer with [PdfFileStamp::AddFooter()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/addfooter/).
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

void AddImageFooter(String inputFile, String imageFile, String outputFile)
{
    auto pdfStamper = MakeObject<PdfFileStamp>();
    auto imageStream = System::IO::File::OpenRead(imageFile);

    pdfStamper->BindPdf(inputFile);
    pdfStamper->AddFooter(imageStream, 20);
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

## Add stamp to PDF

Bind an image to a Stamp and apply it with PdfFileStamp.

1. Create [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Apply the configured stamp with [PdfFileStamp::AddStamp()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/addstamp/).
1. Save the resulting PDF with [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileStamp.h>
#include <Aspose.PDF.Cpp/Facades/Stamp.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileStamp
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Stamp = Aspose::Pdf::Facades::Stamp;

void AddStampToPdf(String inputFile, String imageFile, String outputFile)
{
    auto pdfStamper = MakeObject<PdfFileStamp>();
    pdfStamper->BindPdf(inputFile);
    auto stamp = MakeObject<Stamp>();
    stamp->BindImage(imageFile);
    pdfStamper->AddStamp(stamp);
    pdfStamper->Save(outputFile);
}
} // namespace Facades::Examples::PDF_FileStamp
```

## Add text footer

Add Sample Footer as formatted text with a margin value of 20.

1. Create [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Add the footer with [PdfFileStamp::AddFooter()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/addfooter/).
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

void AddTextFooter(String inputFile, String outputFile)
{
    auto pdfStamper = MakeObject<PdfFileStamp>();
    pdfStamper->BindPdf(inputFile);
    auto text = MakeObject<FormattedText>(u"Sample Footer");
    pdfStamper->AddFooter(text, 20);
    pdfStamper->Save(outputFile);
}
} // namespace Facades::Examples::PDF_FileStamp
```

## Add text header

Add Sample Header as formatted text with a margin value of 20.

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
