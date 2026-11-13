---
title: Convert PDF to DOC and DOCX in C++
linktitle: Convert PDF to Word
type: docs
weight: 10
url: /cpp/convert-pdf-to-word/
description: Export PDFs to DOC or DOCX and configure text recognition, line endings, bullet recognition, and image resolution.
lastmod: "2026-11-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Export PDF to Word Using C++
Abstract: Create DOC and DOCX files with DocSaveOptions. Separate examples configure enhanced flow recognition, line-end returns, bullet recognition, and 300-DPI image resolution.
---

Export PDFs to DOC or DOCX and configure text recognition, line endings, bullet recognition, and image resolution.

Configure the Aspose.PDF for C++ SDK before running these functions. Pass an existing input file and a writable destination path; create any required output directories first. Each function is an independent example, and its options do not carry over to other examples.

## Convert PDF to DOC

Select DocSaveOptions::DocFormat::Doc for Word DOC output.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [DocSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/docsaveoptions/).
1. Set `Format` to `DocSaveOptions::DocFormat::Doc` in [DocSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/docsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/DocSaveOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToDoc(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<DocSaveOptions>();
		options->set_Format(DocSaveOptions::DocFormat::Doc);
		document->Save(outputFile, options);
	}
}
```

## Convert PDF to DOCX

Select DocSaveOptions::DocFormat::DocX for DOCX output.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [DocSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/docsaveoptions/).
1. Set `Format` to `DocSaveOptions::DocFormat::DocX` in [DocSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/docsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/DocSaveOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToDocx(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<DocSaveOptions>();
		options->set_Format(DocSaveOptions::DocFormat::DocX);
		document->Save(outputFile, options);
	}
}
```

## Use enhanced flow recognition

Set RecognitionMode::EnhancedFlow to configure how the converter reconstructs flowing text.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [DocSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/docsaveoptions/).
1. Set `Format` to `DocSaveOptions::DocFormat::DocX` in [DocSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/docsaveoptions/).
1. Set `Mode` to `DocSaveOptions::RecognitionMode::EnhancedFlow` in [DocSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/docsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/DocSaveOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToDocxEnhancedFlow(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<DocSaveOptions>();
		options->set_Format(DocSaveOptions::DocFormat::DocX);
		options->set_Mode(DocSaveOptions::RecognitionMode::EnhancedFlow);
		document->Save(outputFile, options);
	}
}
```

## Add returns at line ends

Set AddReturnToLineEnd to true when exporting DOCX.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [DocSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/docsaveoptions/).
1. Set `Format` to `DocSaveOptions::DocFormat::DocX` in [DocSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/docsaveoptions/).
1. Set `AddReturnToLineEnd` to `true` in [DocSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/docsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/DocSaveOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToDocxWithLineBreaks(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<DocSaveOptions>();
		options->set_Format(DocSaveOptions::DocFormat::DocX);
		options->set_AddReturnToLineEnd(true);
		document->Save(outputFile, options);
	}
}
```

## Recognize bullets

Enable RecognizeBullets for DOCX output.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [DocSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/docsaveoptions/).
1. Set `Format` to `DocSaveOptions::DocFormat::DocX` in [DocSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/docsaveoptions/).
1. Set `RecognizeBullets` to `true` in [DocSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/docsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/DocSaveOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToDocxWithBullets(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<DocSaveOptions>();
		options->set_Format(DocSaveOptions::DocFormat::DocX);
		options->set_RecognizeBullets(true);
		document->Save(outputFile, options);
	}
}
```

## Set DOCX image resolution

Set ImageResolutionX and ImageResolutionY to 300 for exported images.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [DocSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/docsaveoptions/).
1. Set `Format` to `DocSaveOptions::DocFormat::DocX` in [DocSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/docsaveoptions/).
1. Set `ImageResolutionX` to `300` in [DocSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/docsaveoptions/).
1. Set `ImageResolutionY` to `300` in [DocSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/docsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/DocSaveOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToDocxImageResolution(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<DocSaveOptions>();
		options->set_Format(DocSaveOptions::DocFormat::DocX);
		options->set_ImageResolutionX(300);
		options->set_ImageResolutionY(300);
		document->Save(outputFile, options);
	}
}
```

## Related conversion guides

- [PDF Conversion](/pdf/cpp/converting/)

