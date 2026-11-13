---
title: Convert PDF to images in C++
linktitle: Convert PDF to Images
type: docs
weight: 40
url: /cpp/convert-pdf-to-images/
description: Render PDF pages as BMP, GIF, JPEG, PNG, or multipage TIFF and export SVG files.
lastmod: "2026-11-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Export PDF to Images Using C++
Abstract: Render every PDF page to numbered raster image files at 300 DPI or create a single multipage TIFF. Additional examples configure a PNG fallback font and export SVG without ZIP compression.
---

Render PDF pages as BMP, GIF, JPEG, PNG, or multipage TIFF and export SVG files.

Configure the Aspose.PDF for C++ SDK before running these functions. Pass an existing input file and a writable destination path; create any required output directories first. Each function is an independent example, and its options do not carry over to other examples.

## Render every PDF page as BMP

Render all pages at 300 DPI with BmpDevice. Each file name appends the one-based page number and .bmp to outputFile; pass a prefix such as output/page- rather than a complete image file name.

1. Open the PDF and get its Pages collection.
1. Create the image device with [Resolution](https://reference.aspose.com/pdf/cpp/aspose.pdf.devices/resolution/)(300).
1. Iterate from page 1 through the page count and create a separate FileStream for each numbered output file.
1. Call the device Process() method for the current page, then close the output stream.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Devices/BmpDevice.h>
#include <Aspose.PDF.Cpp/Devices/Resolution.h>
#include <system/io/file_stream.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Devices;

	void ConvertPdfToBmp(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto pages = document->get_Pages();
		auto device = MakeObject<BmpDevice>(MakeObject<Resolution>(300));
		for (int page = 1; page <= pages->get_Count(); ++page) {
			auto output = MakeObject<System::IO::FileStream>(outputFile + String::Format(u"{0}.bmp", page), System::IO::FileMode::Create);
			device->Process(pages->idx_get(page), output);
			output->Close();
		}
	}
}
```

## Render every PDF page as GIF

Render all pages at 300 DPI with GifDevice. Each file name appends the one-based page number and .gif to outputFile; pass a prefix such as output/page- rather than a complete image file name.

1. Open the PDF and get its Pages collection.
1. Create the image device with [Resolution](https://reference.aspose.com/pdf/cpp/aspose.pdf.devices/resolution/)(300).
1. Iterate from page 1 through the page count and create a separate FileStream for each numbered output file.
1. Call the device Process() method for the current page, then close the output stream.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Devices/GifDevice.h>
#include <Aspose.PDF.Cpp/Devices/Resolution.h>
#include <system/io/file_stream.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Devices;

	void ConvertPdfToGif(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto pages = document->get_Pages();
		auto device = MakeObject<GifDevice>(MakeObject<Resolution>(300));
		for (int page = 1; page <= pages->get_Count(); ++page) {
			auto output = MakeObject<System::IO::FileStream>(outputFile + String::Format(u"{0}.gif", page), System::IO::FileMode::Create);
			device->Process(pages->idx_get(page), output);
			output->Close();
		}
	}
}
```

## Render every PDF page as JPEG

Render all pages at 300 DPI with JpegDevice. Each file name appends the one-based page number and .jpeg to outputFile; pass a prefix such as output/page- rather than a complete image file name.

1. Open the PDF and get its Pages collection.
1. Create the image device with [Resolution](https://reference.aspose.com/pdf/cpp/aspose.pdf.devices/resolution/)(300).
1. Iterate from page 1 through the page count and create a separate FileStream for each numbered output file.
1. Call the device Process() method for the current page, then close the output stream.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Devices/JpegDevice.h>
#include <Aspose.PDF.Cpp/Devices/Resolution.h>
#include <system/io/file_stream.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Devices;

	void ConvertPdfToJpeg(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto pages = document->get_Pages();
		auto device = MakeObject<JpegDevice>(MakeObject<Resolution>(300));
		for (int page = 1; page <= pages->get_Count(); ++page) {
			auto output = MakeObject<System::IO::FileStream>(outputFile + String::Format(u"{0}.jpeg", page), System::IO::FileMode::Create);
			device->Process(pages->idx_get(page), output);
			output->Close();
		}
	}
}
```

## Render every PDF page as PNG

Render all pages at 300 DPI with PngDevice. Each file name appends the one-based page number and .png to outputFile; pass a prefix such as output/page- rather than a complete image file name.

1. Open the PDF and get its Pages collection.
1. Create the image device with [Resolution](https://reference.aspose.com/pdf/cpp/aspose.pdf.devices/resolution/)(300).
1. Iterate from page 1 through the page count and create a separate FileStream for each numbered output file.
1. Call the device Process() method for the current page, then close the output stream.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Devices/PngDevice.h>
#include <Aspose.PDF.Cpp/Devices/Resolution.h>
#include <system/io/file_stream.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Devices;

	void ConvertPdfToPng(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto pages = document->get_Pages();
		auto device = MakeObject<PngDevice>(MakeObject<Resolution>(300));
		for (int page = 1; page <= pages->get_Count(); ++page) {
			auto output = MakeObject<System::IO::FileStream>(outputFile + String::Format(u"{0}.png", page), System::IO::FileMode::Create);
			device->Process(pages->idx_get(page), output);
			output->Close();
		}
	}
}
```

## Render PNG with a fallback font

Render every page at 300 DPI after setting RenderingOptions::DefaultFontName to Arial. Ensure Arial is available. Output names append the page number and .png to outputFile.

1. Open the PDF and create a [PngDevice](https://reference.aspose.com/pdf/cpp/aspose.pdf.devices/pngdevice/) with [Resolution](https://reference.aspose.com/pdf/cpp/aspose.pdf.devices/resolution/)(300).
1. Create [RenderingOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/renderingoptions/), set DefaultFontName to Arial, and assign the options to the device.
1. Loop through all pages, process each page into its numbered PNG stream, and close the stream.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Devices/PngDevice.h>
#include <Aspose.PDF.Cpp/Devices/Resolution.h>
#include <system/io/file_stream.h>
#include <Aspose.PDF.Cpp/RenderingOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Devices;

	void ConvertPdfToPngWithDefaultFont(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto pages = document->get_Pages();
		auto device = MakeObject<PngDevice>(MakeObject<Resolution>(300));
		auto renderingOptions = MakeObject<RenderingOptions>();
		renderingOptions->set_DefaultFontName(u"Arial");
		device->set_RenderingOptions(renderingOptions);
		for (int page = 1; page <= pages->get_Count(); ++page) {
			auto output = MakeObject<System::IO::FileStream>(outputFile + String::Format(u"{0}.png", page), System::IO::FileMode::Create);
			device->Process(pages->idx_get(page), output);
			output->Close();
		}
	}
}
```

## Export PDF to SVG

Disable CompressOutputToZipArchive and set TreatTargetFileNameAsDirectory to true. Pass a destination directory as outputFile; this example writes SVG output rather than a ZIP archive.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [SvgSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/svgsaveoptions/).
1. Set `CompressOutputToZipArchive` to `false` in [SvgSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/svgsaveoptions/).
1. Set `TreatTargetFileNameAsDirectory` to `true` in [SvgSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/svgsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/SvgSaveOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToSvg(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<SvgSaveOptions>();
		options->CompressOutputToZipArchive = false;
		options->TreatTargetFileNameAsDirectory = true;
		document->Save(outputFile, options);
	}
}
```

## Render all pages to one TIFF

Render pages 1 through the document page count into a single TIFF at 300 DPI. Use LZW compression, default color depth, and SkipBlankPages=false to retain blank pages.

1. Open the PDF and create [TiffSettings](https://reference.aspose.com/pdf/cpp/aspose.pdf.devices/tiffsettings/).
1. Set Compression to LZW, Depth to Default, and SkipBlankPages to false.
1. Create a [TiffDevice](https://reference.aspose.com/pdf/cpp/aspose.pdf.devices/tiffdevice/) with [Resolution](https://reference.aspose.com/pdf/cpp/aspose.pdf.devices/resolution/)(300) and the settings.
1. Process the document from page 1 through the page count into one output stream, then close it.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Devices/TiffDevice.h>
#include <Aspose.PDF.Cpp/Devices/TiffSettings.h>
#include <Aspose.PDF.Cpp/Devices/CompressionType.h>
#include <Aspose.PDF.Cpp/Devices/ColorDepth.h>
#include <Aspose.PDF.Cpp/Devices/Resolution.h>
#include <system/io/file_stream.h>

namespace ConvertingExamples
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Devices;

void ConvertPdfToTiff(String inputFile, String outputFile)
{
	auto document = MakeObject<Document>(inputFile);
	auto settings = MakeObject<TiffSettings>();
	settings->set_Compression(CompressionType::LZW);
	settings->set_Depth(ColorDepth::Default);
	settings->set_SkipBlankPages(false);
	auto device = MakeObject<TiffDevice>(MakeObject<Resolution>(300), settings);
	auto output = MakeObject<System::IO::FileStream>(outputFile, System::IO::FileMode::Create);
	device->Process(document, 1, document->get_Pages()->get_Count(), output);
	output->Close();
}
}
```

## Related conversion guides

- [PDF Conversion](/pdf/cpp/converting/)

