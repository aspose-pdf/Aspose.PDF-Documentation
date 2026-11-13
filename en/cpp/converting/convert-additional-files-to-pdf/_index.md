---
title: Convert OFD, EPS, and PCL to PDF in C++
linktitle: Convert OFD, EPS, and PCL to PDF
type: docs
weight: 85
url: /cpp/convert-additional-files-to-pdf/
description: Load OFD, EPS, and PCL files with format-specific options and save them as PDF.
lastmod: "2026-11-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Export OFD, EPS, and PCL to PDF Using C++
Abstract: Use dedicated load options for OFD and PCL input or PostScript load options for EPS. The PCL example enables error suppression before saving the PDF.
---

Load OFD, EPS, and PCL files with format-specific options and save them as PDF.

Configure the Aspose.PDF for C++ SDK before running these functions. Pass an existing input file and a writable destination path; create any required output directories first. Each function is an independent example, and its options do not carry over to other examples.

For text, LaTeX, Markdown, PostScript, XPS, and XML with XSL-FO, see [Convert Other File Formats to PDF](/pdf/cpp/convert-other-files-to-pdf/).

## Convert OFD to PDF

Use OfdLoadOptions to load the OFD document.

1. Create [OfdLoadOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/ofdloadoptions/).
1. Load `inputFile` into a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) using the load options.
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).


```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/OFD/OfdLoadOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertOfdToPdf(String inputFile, String outputFile)
	{
		auto options = MakeObject<OfdLoadOptions>();
		auto document = MakeObject<Document>(inputFile, options);
		document->Save(outputFile);
	}
}
```

## Convert EPS to PDF

Use PsLoadOptions to load the Encapsulated PostScript document.

1. Create [PsLoadOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/psloadoptions/).
1. Load `inputFile` into a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) using the load options.
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PsLoadOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertEpsToPdf(String inputFile, String outputFile)
	{
		auto options = MakeObject<PsLoadOptions>();
		auto document = MakeObject<Document>(inputFile, options);
		document->Save(outputFile);
	}
}
```

## Convert PCL to PDF

Set PclLoadOptions::SupressErrors to true before loading the PCL file. The supplied example suppresses PCL conversion errors.

1. Create [PclLoadOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/pclloadoptions/).
1. Set `SupressErrors` to `true` in [PclLoadOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/pclloadoptions/).
1. Load `inputFile` into a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) using the load options.
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PclLoadOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPclToPdf(String inputFile, String outputFile)
	{
		auto options = MakeObject<PclLoadOptions>();
		options->SupressErrors = true;
		auto document = MakeObject<Document>(inputFile, options);
		document->Save(outputFile);
	}
}
```

## Related conversion guides

- [PDF Conversion](/pdf/cpp/converting/)

