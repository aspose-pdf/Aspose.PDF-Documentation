---
title: Convert PDF to PDF/X in C++
linktitle: Convert PDF to PDF/X
type: docs
weight: 115
url: /cpp/convert-pdf-to-pdfx/
description: Convert PDFs to PDF/X-4 using conversion options, an output intent, and an optional ICC profile.
lastmod: "2026-11-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Export PDF to PDF/X Using C++
Abstract: Configure PDF/X-4 conversion with a FOGRA39 output intent. The example uses an ICC profile when the expected file exists beside the input PDF.
---

Convert PDFs to PDF/X-4 using conversion options, an output intent, and an optional ICC profile.

Configure the Aspose.PDF for C++ SDK before running these functions. Pass an existing input file and a writable destination path; create any required output directories first. Each function is an independent example, and its options do not carry over to other examples.

Conversion examples use `ConvertErrorAction::Delete`, which can remove elements that cannot conform to the selected standard. Review the conversion log and validate the saved PDF before relying on its compliance. The examples do not check the return value of `Convert()`.

## Convert PDF to PDF/X-4

Configure PDF_X_4 conversion and a FOGRA39 output intent. If ISOcoated_v2_eci.icc exists beside the input PDF, assign it as the ICC profile; otherwise the example leaves IccProfileFileName unset.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [PdfFormatConversionOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/pdfformatconversionoptions/) with the report path, `PDF_X_4`, and `ConvertErrorAction::Delete`.
1. If `ISOcoated_v2_eci.icc` exists beside the input file, assign its path to `IccProfileFileName`.
1. Set `OutputIntent` to a new [OutputIntent](https://reference.aspose.com/pdf/cpp/aspose.pdf/outputintent/) initialized with `FOGRA39`.
1. Pass the options to [Document::Convert()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/convert/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/IO/ConvertStrategies/PdfFormat.h>
#include <Aspose.PDF.Cpp/IO/ConvertStrategies/ConvertErrorAction.h>
#include <system/io/path.h>
#include <Aspose.PDF.Cpp/OutputIntent.h>
#include <system/io/file.h>
#include <Aspose.PDF.Cpp/PdfFormatConversionOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToPdfX(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto logFile = System::IO::Path::ChangeExtension(outputFile, u".log.xml");
		auto options = MakeObject<PdfFormatConversionOptions>(logFile, PdfFormat::PDF_X_4, ConvertErrorAction::Delete);
		auto profile = System::IO::Path::Combine(System::IO::Path::GetDirectoryName(inputFile), u"ISOcoated_v2_eci.icc");
		if (System::IO::File::Exists(profile)) {
			options->set_IccProfileFileName(profile);
		}
		options->set_OutputIntent(MakeObject<OutputIntent>(u"FOGRA39"));
		document->Convert(options);
		document->Save(outputFile);
	}
}
```

## Related conversion guides

- [PDF Conversion](/pdf/cpp/converting/)

