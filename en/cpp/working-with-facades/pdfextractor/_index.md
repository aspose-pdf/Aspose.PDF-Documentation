---
title: Extract PDF text, images, and attachments in C++
linktitle: PdfExtractor Class
type: docs
weight: 80
url: /cpp/pdfextractor-class/
description: Inspect content availability and extract page text, images, and file attachments using facade APIs using Aspose.PDF for C++.
lastmod: "2026-11-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract PDF Content and Attachments in C++
Abstract: Use PdfExtractor to retrieve text, image resources, and embedded attachments. The examples demonstrate page selection, extraction modes, stream output, and content-presence checks.
---

Use [PdfExtractor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/) to inspect content availability and extract page text, images, and file attachments using facade APIs.

Create a writable outputDir before running examples that write into it. Page-specific samples require pages 2 or 2 through 3. Extraction retrieves existing content; text extraction does not perform OCR.

The snippets are independent example functions with their SDK includes and example namespaces. Configure the Aspose.PDF for C++ SDK, supply the input resources referenced by the sample, and choose writable output paths. The examples retain the source field names, page indexes, coordinates, and options.

## PdfExtractor workflows

- [Check if PDF contains text or images](#check-if-pdf-contains-text-or-images)
- [Extract attachments](#extract-attachments)
- [Extract images image extraction mode](#extract-images-image-extraction-mode)
- [Extract images particular page](#extract-images-particular-page)
- [Extract images range pages](#extract-images-range-pages)
- [Extract images whole PDF streams](#extract-images-whole-pdf-streams)
- [Extract images whole PDF](#extract-images-whole-pdf)
- [Extract text extraction mode](#extract-text-extraction-mode)
- [Extract text](#extract-text)

## Check if PDF contains text or images

Start text and image extraction and print whether the PDF contains either type of content.

1. Create [PdfExtractor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Prepare text extraction with [PdfExtractor::ExtractText()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/extracttext/).
1. Check for another page of text with [PdfExtractor::HasNextPageText()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/hasnextpagetext/).
1. Prepare image extraction with [PdfExtractor::ExtractImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/extractimage/).
1. Check for another image with [PdfExtractor::HasNextImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/hasnextimage/).
1. Print the results or diagnostic messages shown in the example.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfExtractor.h>
#include <iostream>
#include <system/string.h>

namespace  Facades::Examples::PDF_Extractor
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Facades;

	void CheckIfPdfContainsTextOrImages(String inputFile)
	{
		auto pdfExtractor = MakeObject<PdfExtractor>();

		pdfExtractor->BindPdf(inputFile);

		pdfExtractor->ExtractText();
		auto containsText = pdfExtractor->HasNextPageText();

		pdfExtractor->ExtractImage();

		auto containsImage = pdfExtractor->HasNextImage();

		String content = containsText ? (containsImage ? u"both text and image" : u"text only")
			: (containsImage ? u"image only" : u"neither text nor image");
		std::cout << "PDF contains " << content << std::endl;
	}
} // namespace  Facades::Examples::PDF_Extractor
```

## Extract attachments

Extract attachments and write them to outputDir when attachment names are present.

1. Create [PdfExtractor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Prepare attachment extraction with [PdfExtractor::ExtractAttachment()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/extractattachment/).
1. Read attachment names with [PdfExtractor::GetAttachNames()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/getattachnames/).
1. Write attachments with [PdfExtractor::GetAttachment()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/getattachment/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfExtractor.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_Extractor
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Facades;

	void ExtractAttachments(String inputFile, String outputDir)
	{
		auto pdfExtractor = MakeObject<PdfExtractor>();

		pdfExtractor->BindPdf(inputFile);

		pdfExtractor->ExtractAttachment();

		if (pdfExtractor->GetAttachNames()->get_Count() > 0)
		{
			pdfExtractor->GetAttachment(outputDir);
		}
	}
} // namespace  Facades::Examples::PDF_Extractor
```

## Extract images image extraction mode

Select DefinedInResources mode and write extracted images as numbered PNG files.

1. Create [PdfExtractor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Set extract image mode through [PdfExtractor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/) using the example values.
1. Prepare image extraction with [PdfExtractor::ExtractImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/extractimage/).
1. Check for another image with [PdfExtractor::HasNextImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/hasnextimage/).
1. Write each image with [PdfExtractor::GetNextImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/getnextimage/).

```cpp
#include <Aspose.PDF.Cpp/ExtractImageMode.h>
#include <Aspose.PDF.Cpp/Facades/PdfExtractor.h>
#include <Aspose.PDF.Cpp/Presentation/IndependentImpl/ImageFormat.h>
#include <drawing/imaging/image_format.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_Extractor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ExtractImagesImageExtractionMode(String inputFile, String outputDir)
{
    auto pdfExtractor = MakeObject<PdfExtractor>();

    pdfExtractor->BindPdf(inputFile);

    pdfExtractor->set_ExtractImageMode(ExtractImageMode::DefinedInResources);
    pdfExtractor->ExtractImage();

    int index = 0;

    while (pdfExtractor->HasNextImage())
    {
        index++;

        auto outputFile = (outputDir + u"/" + String::Format(u"{0}", index) + u"_out.png");
        auto outputImage = System::IO::File::Create(outputFile);

        pdfExtractor->GetNextImage(outputImage, System::Drawing::Imaging::ImageFormat::get_Png());
    }
}
} // namespace  Facades::Examples::PDF_Extractor
```

## Extract images particular page

Extract images from page 2 and write numbered JPEG files.

1. Create [PdfExtractor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Set start page through [PdfExtractor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/) using the example values.
1. Set end page through [PdfExtractor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/) using the example values.
1. Prepare image extraction with [PdfExtractor::ExtractImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/extractimage/).
1. Check for another image with [PdfExtractor::HasNextImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/hasnextimage/).
1. Write each image with [PdfExtractor::GetNextImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/getnextimage/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfExtractor.h>
#include <Aspose.PDF.Cpp/Presentation/IndependentImpl/ImageFormat.h>
#include <drawing/imaging/image_format.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_Extractor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ExtractImagesParticularPage(String inputFile, String outputDir)
{
    auto pdfExtractor = MakeObject<PdfExtractor>();

    pdfExtractor->BindPdf(inputFile);

    pdfExtractor->set_StartPage(2);
    pdfExtractor->set_EndPage(2);

    pdfExtractor->ExtractImage();
    int index = 0;

    while (pdfExtractor->HasNextImage())
    {
        index++;

        auto outputFile = (outputDir + u"/" + String::Format(u"{0}", index) + u"_out.jpg");
        auto outputImage = System::IO::File::Create(outputFile);

        pdfExtractor->GetNextImage(outputImage, System::Drawing::Imaging::ImageFormat::get_Jpeg());
    }
}
} // namespace  Facades::Examples::PDF_Extractor
```

## Extract images range pages

Extract images from pages 2 through 3 and write numbered JPEG files.

1. Create [PdfExtractor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Set start page through [PdfExtractor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/) using the example values.
1. Set end page through [PdfExtractor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/) using the example values.
1. Prepare image extraction with [PdfExtractor::ExtractImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/extractimage/).
1. Check for another image with [PdfExtractor::HasNextImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/hasnextimage/).
1. Write each image with [PdfExtractor::GetNextImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/getnextimage/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfExtractor.h>
#include <Aspose.PDF.Cpp/Presentation/IndependentImpl/ImageFormat.h>
#include <drawing/imaging/image_format.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_Extractor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ExtractImagesRangePages(String inputFile, String outputDir)
{
    auto pdfExtractor = MakeObject<PdfExtractor>();

    pdfExtractor->BindPdf(inputFile);

    pdfExtractor->set_StartPage(2);
    pdfExtractor->set_EndPage(3);

    pdfExtractor->ExtractImage();
    int index = 0;

    while (pdfExtractor->HasNextImage())
    {
        index++;

        auto outputFile = (outputDir + u"/" + String::Format(u"{0}", index) + u"_out.jpg");
        auto outputImage = System::IO::File::Create(outputFile);

        pdfExtractor->GetNextImage(outputImage, System::Drawing::Imaging::ImageFormat::get_Jpeg());
    }
}
} // namespace  Facades::Examples::PDF_Extractor
```

## Extract images whole PDF streams

Extract images from the PDF and write each JPEG through a file stream.

1. Create [PdfExtractor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Prepare image extraction with [PdfExtractor::ExtractImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/extractimage/).
1. Check for another image with [PdfExtractor::HasNextImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/hasnextimage/).
1. Write each image with [PdfExtractor::GetNextImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/getnextimage/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfExtractor.h>
#include <Aspose.PDF.Cpp/Presentation/IndependentImpl/ImageFormat.h>
#include <drawing/imaging/image_format.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_Extractor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ExtractImagesWholePDFStreams(String inputFile, String outputDir)
{
    auto pdfExtractor = MakeObject<PdfExtractor>();

    pdfExtractor->BindPdf(inputFile);

    pdfExtractor->ExtractImage();
    int index = 0;

    while (pdfExtractor->HasNextImage())
    {
        index++;

        auto outputFile = (outputDir + u"/" + String::Format(u"{0}", index) + u"_out.jpg");
        auto outputImage = System::IO::File::Create(outputFile);

        pdfExtractor->GetNextImage(outputImage, System::Drawing::Imaging::ImageFormat::get_Jpeg());
    }
}
} // namespace  Facades::Examples::PDF_Extractor
```

## Extract images whole PDF

Extract images from the PDF directly to numbered JPEG paths.

1. Create [PdfExtractor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Prepare image extraction with [PdfExtractor::ExtractImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/extractimage/).
1. Check for another image with [PdfExtractor::HasNextImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/hasnextimage/).
1. Write each image with [PdfExtractor::GetNextImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/getnextimage/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfExtractor.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_Extractor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ExtractImagesWholePDF(String inputFile, String outputDir)
{
    auto pdfExtractor = MakeObject<PdfExtractor>();

    pdfExtractor->BindPdf(inputFile);

    pdfExtractor->ExtractImage();
    int index = 0;

    while (pdfExtractor->HasNextImage())
    {
        ++index;
        pdfExtractor->GetNextImage((outputDir + u"/" + String::Format(u"{0}", index) + u"_out.jpg"));
    }
}
} // namespace  Facades::Examples::PDF_Extractor
```

## Extract text extraction mode

Set extraction mode to the numeric value 1 and write text from each extracted page to a separate file.

1. Create [PdfExtractor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Set extract text mode through [PdfExtractor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/) using the example values.
1. Prepare text extraction with [PdfExtractor::ExtractText()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/extracttext/).
1. Check for another page of text with [PdfExtractor::HasNextPageText()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/hasnextpagetext/).
1. Write each page of text with [PdfExtractor::GetNextPageText()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/getnextpagetext/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfExtractor.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_Extractor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ExtractTextExtractionMode(String inputFile, String outputDir)
{
    auto pdfExtractor = MakeObject<PdfExtractor>();

    pdfExtractor->BindPdf(inputFile);

    pdfExtractor->set_ExtractTextMode(1);
    pdfExtractor->ExtractText();

    int pageNumber = 1;
    while (pdfExtractor->HasNextPageText())
    {
        pdfExtractor->GetNextPageText(
            (outputDir + u"/" + String(u"sample") + String::Format(u"{0}", pageNumber) + u".txt"));
        pageNumber++;
    }
}
} // namespace  Facades::Examples::PDF_Extractor
```

## Extract text

Write extracted page text to numbered text files.

1. Create [PdfExtractor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Prepare text extraction with [PdfExtractor::ExtractText()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/extracttext/).
1. Check for another page of text with [PdfExtractor::HasNextPageText()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/hasnextpagetext/).
1. Write each page of text with [PdfExtractor::GetNextPageText()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfextractor/getnextpagetext/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfExtractor.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_Extractor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ExtractText(String inputFile, String outputDir)
{
    auto pdfExtractor = MakeObject<PdfExtractor>();

    pdfExtractor->BindPdf(inputFile);

    pdfExtractor->ExtractText();

    int pageNumber = 1;
    while (pdfExtractor->HasNextPageText())
    {
        pdfExtractor->GetNextPageText((outputDir + u"/" + String::Format(u"{0}", pageNumber) + u".txt"));
        pageNumber++;
    }
}
} // namespace  Facades::Examples::PDF_Extractor
```
