---
title: Convert PDF to HTML in C++
linktitle: Convert PDF to HTML
type: docs
weight: 30
url: /cpp/convert-pdf-to-html/
description: Export PDFs to HTML and configure image folders, page splitting, SVG graphics, background images, body markup, text, and layers.
lastmod: "2026-11-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Export PDF to HTML Using C++
Abstract: Configure HtmlSaveOptions for page splitting, resource directories, compressed SVG graphics, and PNG page backgrounds. Additional variants export body-only markup, transparent text, and marked content as layers.
---

Export PDFs to HTML and configure image folders, page splitting, SVG graphics, background images, body markup, text, and layers.

Configure the Aspose.PDF for C++ SDK before running these functions. Pass an existing input file and a writable destination path; create any required output directories first. Each function is an independent example, and its options do not carry over to other examples.

## Convert PDF with default HTML options

Create HtmlSaveOptions and save the document with its default HTML export settings.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/htmlsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/HtmlSaveOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToHtml(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<HtmlSaveOptions>();
		document->Save(outputFile, options);
	}
}
```

## Choose an image folder

Set SpecialFolderForAllImages to an html_images directory beside the output file.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/htmlsaveoptions/).
1. Set `SpecialFolderForAllImages` to the output-relative directory described above in [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/htmlsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/HtmlSaveOptions.h>
#include <system/io/path.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToHtmlExternalImages(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<HtmlSaveOptions>();
		options->SpecialFolderForAllImages = System::IO::Path::Combine(System::IO::Path::GetDirectoryName(outputFile), u"html_images");
		document->Save(outputFile, options);
	}
}
```

## Choose an SVG folder

Set SpecialFolderForSvgImages to an html_svg directory beside the output file.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/htmlsaveoptions/).
1. Set `SpecialFolderForSvgImages` to the output-relative directory described above in [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/htmlsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/HtmlSaveOptions.h>
#include <system/io/path.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToHtmlExternalSvg(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<HtmlSaveOptions>();
		options->SpecialFolderForSvgImages = System::IO::Path::Combine(System::IO::Path::GetDirectoryName(outputFile), u"html_svg");
		document->Save(outputFile, options);
	}
}
```

## Compress SVG graphics

Set SpecialFolderForSvgImages to html_svg_compressed beside the output file and enable CompressSvgGraphicsIfAny.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/htmlsaveoptions/).
1. Set `CompressSvgGraphicsIfAny` to `true` in [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/htmlsaveoptions/).
1. Set `SpecialFolderForSvgImages` to the output-relative directory described above in [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/htmlsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/HtmlSaveOptions.h>
#include <system/io/path.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToHtmlCompressedSvg(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<HtmlSaveOptions>();
		options->SpecialFolderForSvgImages = System::IO::Path::Combine(System::IO::Path::GetDirectoryName(outputFile), u"html_svg_compressed");
		options->set_CompressSvgGraphicsIfAny(true);
		document->Save(outputFile, options);
	}
}
```

## Split HTML output by page

Enable SplitIntoPages to produce page-specific HTML output.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/htmlsaveoptions/).
1. Set `SplitIntoPages` to `true` in [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/htmlsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/HtmlSaveOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToHtmlSplitPages(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<HtmlSaveOptions>();
		options->set_SplitIntoPages(true);
		document->Save(outputFile, options);
	}
}
```

## Use PNG page backgrounds for raster images

Set RasterImagesSavingMode to AsEmbeddedPartsOfPngPageBackground.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/htmlsaveoptions/).
1. Set `RasterImagesSavingMode` to `HtmlSaveOptions::RasterImagesSavingModes::AsEmbeddedPartsOfPngPageBackground` in [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/htmlsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/HtmlSaveOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToHtmlPngBackground(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<HtmlSaveOptions>();
		options->RasterImagesSavingMode = HtmlSaveOptions::RasterImagesSavingModes::AsEmbeddedPartsOfPngPageBackground;
		document->Save(outputFile, options);
	}
}
```

## Export body content only

Set HtmlMarkupGenerationMode to WriteOnlyBodyContent and enable SplitIntoPages.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/htmlsaveoptions/).
1. Set `SplitIntoPages` to `true` in [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/htmlsaveoptions/).
1. Set `HtmlMarkupGenerationMode` to `HtmlSaveOptions::HtmlMarkupGenerationModes::WriteOnlyBodyContent` in [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/htmlsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/HtmlSaveOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToHtmlBodyContent(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<HtmlSaveOptions>();
		options->HtmlMarkupGenerationMode = HtmlSaveOptions::HtmlMarkupGenerationModes::WriteOnlyBodyContent;
		options->set_SplitIntoPages(true);
		document->Save(outputFile, options);
	}
}
```

## Preserve transparent text

Enable SaveTransparentTexts and SaveShadowedTextsAsTransparentTexts.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/htmlsaveoptions/).
1. Set `SaveTransparentTexts` to `true` in [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/htmlsaveoptions/).
1. Set `SaveShadowedTextsAsTransparentTexts` to `true` in [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/htmlsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/HtmlSaveOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToHtmlTransparentText(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<HtmlSaveOptions>();
		options->SaveTransparentTexts = true;
		options->SaveShadowedTextsAsTransparentTexts = true;
		document->Save(outputFile, options);
	}
}
```

## Convert marked content to layers

Enable ConvertMarkedContentToLayers for HTML export.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/htmlsaveoptions/).
1. Set `ConvertMarkedContentToLayers` to `true` in [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/htmlsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/HtmlSaveOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToHtmlLayers(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<HtmlSaveOptions>();
		options->set_ConvertMarkedContentToLayers(true);
		document->Save(outputFile, options);
	}
}
```

## Related conversion guides

- [PDF Conversion](/pdf/cpp/converting/)

