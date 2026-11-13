---
title: Convert PDF to PowerPoint in C++
linktitle: Convert PDF to PowerPoint
type: docs
weight: 50
url: /cpp/convert-pdf-to-powerpoint/
description: Export PDFs to PPTX with default settings, image-based slides, or a configured image resolution.
lastmod: "2026-11-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Export PDF to PowerPoint Using C++
Abstract: Use PptxSaveOptions to export PDF content to PowerPoint. Compare default output with image-based slides and a separate image-resolution setting.
---

Export PDFs to PPTX with default settings, image-based slides, or a configured image resolution.

Configure the Aspose.PDF for C++ SDK before running these functions. Pass an existing input file and a writable destination path; create any required output directories first. Each function is an independent example, and its options do not carry over to other examples.

## Convert PDF to PPTX

Save the document using PptxSaveOptions.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [PptxSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/pptxsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PptxSaveOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToPptx(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<PptxSaveOptions>();
		document->Save(outputFile, options);
	}
}
```

## Export slides as images

Set SlidesAsImages to true to export slide content as images.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [PptxSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/pptxsaveoptions/).
1. Set `SlidesAsImages` to `true` in [PptxSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/pptxsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PptxSaveOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToPptxSlidesAsImages(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<PptxSaveOptions>();
		options->set_SlidesAsImages(true);
		document->Save(outputFile, options);
	}
}
```

## Set PPTX image resolution

Set ImageResolution to 300. This variant does not enable SlidesAsImages.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [PptxSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/pptxsaveoptions/).
1. Set `ImageResolution` to `300` in [PptxSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/pptxsaveoptions/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/), passing the output path and options.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PptxSaveOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToPptxImageResolution(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto options = MakeObject<PptxSaveOptions>();
		options->set_ImageResolution(300);
		document->Save(outputFile, options);
	}
}
```

## Related conversion guides

- [PDF Conversion](/pdf/cpp/converting/)

