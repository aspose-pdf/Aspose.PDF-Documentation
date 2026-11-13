---
title: Create a Sample Image Stamp in C++
linktitle: Create a Sample Image Stamp
type: docs
weight: 10
url: /cpp/create-stamp-sample/
description: Create a Sample Image Stamp in C++ with the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create a Sample Image Stamp with the PdfContentEditor Facade
Abstract: Write a sample PNG image, create a one-page PDF, and apply an image stamp with ID 1.
---

Use [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Create stamp sample

Write a sample PNG image, create a one-page PDF, and apply an image stamp with ID 1.

1. Create [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/).
1. Create or open the [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and prepare its pages as shown.
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Bind the stamp image with [Stamp::BindImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/bindimage/).
1. Set stamp id through [Stamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/) using the example values.
1. Set page number through [Stamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/) using the example values.
1. Set stamp placement with [Stamp::SetOrigin()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/setorigin/).
1. Apply the configured stamp with [PdfFileStamp::AddStamp()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/addstamp/).
1. Save the resulting PDF with [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileStamp.h>
#include <Aspose.PDF.Cpp/Facades/Stamp.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Presentation/IndependentImpl/ImageFormat.h>
#include <drawing/bitmap.h>
#include <drawing/color.h>
#include <drawing/graphics.h>
#include <drawing/image.h>
#include <drawing/imaging/image_format.h>
#include <drawing/solid_brush.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Facades;

	void CreateStampSample(String imageFile, String outputFile)
	{
		auto image = MakeObject<System::Drawing::Bitmap>(120, 60);
		auto graphics = System::Drawing::Graphics::FromImage(image);
		graphics->Clear(System::Drawing::Color::get_White());
		graphics->FillRectangle(MakeObject<System::Drawing::SolidBrush>(System::Drawing::Color::get_Blue()), 10, 10, 100,
			40);
		image->Save(imageFile, System::Drawing::Imaging::ImageFormat::get_Png());
		auto document = MakeObject<Aspose::Pdf::Document>();
		document->get_Pages()->Add();
		auto stamper = MakeObject<Aspose::Pdf::Facades::PdfFileStamp>();
		stamper->BindPdf(document);
		auto stamp = MakeObject<Aspose::Pdf::Facades::Stamp>();
		stamp->BindImage(imageFile);
		stamp->set_StampId(1);
		stamp->set_PageNumber(1);
		stamp->SetOrigin(100, 400);
		stamper->AddStamp(stamp);
		stamper->Save(outputFile);
	}
} // namespace Facades::Examples::PDF_ContentEditor
```
