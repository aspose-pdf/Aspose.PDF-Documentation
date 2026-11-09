---
title: Add Footer to PDF in C++
linktitle: Add Footer to PDF
type: docs
weight: 10
url: /cpp/add-footer/
description: Add Footer to PDF in C++ with the PdfFileStamp facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Footer to PDF with the PdfFileStamp Facade
Abstract: Add formatted footer text using the overload with three margin values set to 20. Add an image footer from a file stream with a margin value of 20. Add Sample Footer as formatted text with a margin value of 20.
---

Use [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/) for this task. The examples below retain the original C++ code and API Reference steps.

## Add footer with margins

Add formatted footer text using the overload with three margin values set to 20.

1. Create the text content and formatting with [FormattedText](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formattedtext/).
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

## Add text footer

Add Sample Footer as formatted text with a margin value of 20.

1. Create the text content and formatting with [FormattedText](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/formattedtext/).
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
