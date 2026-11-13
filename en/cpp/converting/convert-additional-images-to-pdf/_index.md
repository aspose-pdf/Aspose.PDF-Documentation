---
title: Convert GIF, CDR, and rasterized EMF to PDF in C++
linktitle: Convert Additional Images to PDF
type: docs
weight: 65
url: /cpp/convert-additional-images-to-pdf/
description: Create PDFs from GIF and CDR files or rasterize EMF through PNG before placing it on a PDF page.
lastmod: "2026-11-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Export GIF, CDR, and Rasterized EMF to PDF Using C++
Abstract: Place a GIF inside a fixed page rectangle, load CDR with dedicated options, or rasterize EMF to a PNG stream before creating PDF. These examples complement the existing image conversion guide.
---

Create PDFs from GIF and CDR files or rasterize EMF through PNG before placing it on a PDF page.

Configure the Aspose.PDF for C++ SDK before running these functions. Pass an existing input file and a writable destination path; create any required output directories first. Each function is an independent example, and its options do not carry over to other examples.

For BMP, JPEG, PNG, direct EMF placement, DICOM, TIFF, CGM, and SVG, see [Convert Images to PDF](/pdf/cpp/convert-images-format-to-pdf/).

## Convert GIF to PDF

Place the GIF on one new PDF page inside the fixed rectangle (0, 0, 595, 842). The example does not iterate through animation frames.

1. Create an empty [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page.
1. Call [Page::AddImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/addimage/) with the input path and a [Rectangle](https://reference.aspose.com/pdf/cpp/aspose.pdf/rectangle/) spanning (0, 0, 595, 842).
1. Save the PDF.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

namespace ConvertingExamples
{
using namespace System;
using namespace Aspose::Pdf;

void ConvertGifToPdf(String inputFile, String outputFile)
{
	auto document = MakeObject<Document>();
	auto page = document->get_Pages()->Add();
	page->AddImage(inputFile, MakeObject<Rectangle>(0, 0, 595, 842));
	document->Save(outputFile);
}
}
```

## Convert CDR to PDF

Load the CorelDRAW file with CdrLoadOptions and save the resulting document as PDF.

1. Create [CdrLoadOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/cdrloadoptions/).
1. Load `inputFile` into a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) using the load options.
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/CdrLoadOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertCdrToPdf(String inputFile, String outputFile)
	{
		auto options = MakeObject<CdrLoadOptions>();
		auto document = MakeObject<Document>(inputFile, options);
		document->Save(outputFile);
	}
}
```

## Rasterize EMF before creating PDF

Render the EMF through the C++ drawing library, encode the bitmap as PNG in memory, and add that stream to a PDF image. This workflow rasterizes the source rather than retaining vector content.

1. Load the EMF with System::Drawing::[Image](https://reference.aspose.com/pdf/cpp/aspose.pdf/image/)::FromFile() and construct a bitmap.
1. Save the bitmap as PNG to a MemoryStream and reset its position to zero.
1. Create a PDF [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and an [Image](https://reference.aspose.com/pdf/cpp/aspose.pdf/image/), assign the PNG stream with set_[Image](https://reference.aspose.com/pdf/cpp/aspose.pdf/image/)Stream(), and add the image to a new page.
1. Save the PDF while the image stream remains available.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/Image.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <drawing/bitmap.h>
#include <drawing/imaging/image_format.h>
#include <system/io/memory_stream.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertEmfToPdfRasterized(String inputFile, String outputFile)
	{
		auto emf = System::Drawing::Image::FromFile(inputFile);
		auto bitmap = MakeObject<System::Drawing::Bitmap>(emf);
		auto png = MakeObject<System::IO::MemoryStream>();
		bitmap->Save(png, System::Drawing::Imaging::ImageFormat::get_Png());
		png->set_Position(0);

		auto document = MakeObject<Document>();
		auto image = MakeObject<Aspose::Pdf::Image>();
		image->set_ImageStream(png);
		document->get_Pages()->Add()->get_Paragraphs()->Add(image);
		document->Save(outputFile);
	}
}
```

## Related conversion guides

- [PDF Conversion](/pdf/cpp/converting/)

