---
title: Convert PDF to other file formats in C++
linktitle: Convert PDF to Other Formats
type: docs
weight: 90
url: /cpp/convert-pdf-to-other-formats/
description: Export PDFs to EPUB, TeX, text, XPS, XML, Markdown, and MobiXML.
lastmod: "2026-11-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Export PDF to Other Formats Using C++
Abstract: Export PDFs with format-specific save options or SaveFormat values. The text example processes page 1 only, while the XML example expects tagged PDF input.
---

Export PDFs to EPUB, TeX, text, XPS, XML, Markdown, and MobiXML.

Configure the Aspose.PDF for C++ SDK before running these functions. Pass an existing input file and a writable destination path; create any required output directories first. Each function is an independent example, and its options do not carry over to other examples.

## Convert PDF to EPUB

Use SaveFormat::Epub with the SDK's default EPUB export settings.

1. Open the PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Select the [SaveFormat](https://reference.aspose.com/pdf/cpp/aspose.pdf/saveformat/) shown below.
1. Export the document with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/SaveFormat.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToEpub(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		document->Save(outputFile, SaveFormat::Epub);
	}
}
```

## Convert PDF to TeX

Save the PDF with TeXSaveOptions.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [TeXSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/texsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/TeXSaveOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToTex(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<TeXSaveOptions>();
		document->Save(outputFile, options);
	}
}
```

## Export text from the first page

Use TextDevice to process only page 1 into the output stream. The input must contain at least one page; this example does not extract text from subsequent pages.

1. Open the input PDF and create a [TextDevice](https://reference.aspose.com/pdf/cpp/aspose.pdf.devices/textdevice/).
1. Open the output FileStream in create mode.
1. Pass Pages[1] and the stream to [TextDevice](https://reference.aspose.com/pdf/cpp/aspose.pdf.devices/textdevice/)::Process(), then close the stream.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Devices/TextDevice.h>
#include <system/io/file_stream.h>

namespace ConvertingExamples
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Devices;

void ConvertPdfToText(String inputFile, String outputFile)
{
	auto document = MakeObject<Document>(inputFile);
	auto device = MakeObject<TextDevice>();
	auto output = MakeObject<System::IO::FileStream>(outputFile, System::IO::FileMode::Create);
	device->Process(document->get_Pages()->idx_get(1), output);
	output->Close();
}
}
```

## Convert PDF to XPS

Set XpsSaveOptions::UseEmbeddedTrueTypeFonts to true before saving.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [XpsSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/xpssaveoptions/).
1. Set `UseEmbeddedTrueTypeFonts` to `true` in [XpsSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/xpssaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/XpsSaveOptions.h>

namespace ConvertingExamples
{
using namespace System;
using namespace Aspose::Pdf;

void ConvertPdfToXps(String inputFile, String outputFile)
{
	auto document = MakeObject<Document>(inputFile);
	auto options = MakeObject<XpsSaveOptions>();
	options->set_UseEmbeddedTrueTypeFonts(true);
	document->Save(outputFile, options);
}
}
```

## Convert tagged PDF to XML

Use SaveFormat::Xml with a tagged PDF input. This is a document export example, not an OCR workflow or an arbitrary XML schema mapping.

1. Open the PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Select the [SaveFormat](https://reference.aspose.com/pdf/cpp/aspose.pdf/saveformat/) shown below.
1. Export the document with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/SaveFormat.h>

namespace ConvertingExamples
{
using namespace System;
using namespace Aspose::Pdf;

void ConvertPdfToXml(String inputFile, String outputFile)
{
	auto document = MakeObject<Document>(inputFile);
	document->Save(outputFile, SaveFormat::Xml);
}
}
```

## Convert PDF to Markdown

Set ResourcesDirectoryName to images and UseImageHtmlTag to true in MarkdownSaveOptions.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [MarkdownSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/markdownsaveoptions/).
1. Set `ResourcesDirectoryName` to `u"images"` in [MarkdownSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/markdownsaveoptions/).
1. Set `UseImageHtmlTag` to `true` in [MarkdownSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/markdownsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PdfToMarkdown/MarkdownOptions/MarkdownSaveOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToMarkdown(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<MarkdownSaveOptions>();
		options->set_ResourcesDirectoryName(u"images");
		options->set_UseImageHtmlTag(true);
		document->Save(outputFile, options);
	}
}
```

## Convert PDF to MobiXML

Use SaveFormat::MobiXml to export MobiXML content.

1. Open the PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Select the [SaveFormat](https://reference.aspose.com/pdf/cpp/aspose.pdf/saveformat/) shown below.
1. Export the document with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/SaveFormat.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToMobiXml(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		document->Save(outputFile, SaveFormat::MobiXml);
	}
}
```

## Related conversion guides

- [PDF Conversion](/pdf/cpp/converting/)

