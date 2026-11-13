---
title: Convert and validate PDF/E in C++
linktitle: Convert PDF to PDF/E
type: docs
weight: 110
url: /cpp/convert-pdf-to-pdfe/
description: Convert PDFs to PDF/E-1 and validate documents against the PDF/E-1 standard.
lastmod: "2026-11-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Export PDF to PDF/E Using C++
Abstract: Convert a document to PDF/E-1 with a conversion report. Validate an existing PDF against PDF/E-1 and print the result without modifying it.
---

Convert PDFs to PDF/E-1 and validate documents against the PDF/E-1 standard.

Configure the Aspose.PDF for C++ SDK before running these functions. Pass an existing input file and a writable destination path; create any required output directories first. Each function is an independent example, and its options do not carry over to other examples.

Conversion examples use `ConvertErrorAction::Delete`, which can remove elements that cannot conform to the selected standard. Review the conversion log and validate the saved PDF before relying on its compliance. The examples do not check the return value of `Convert()`.

## Convert PDF to PDF/E-1

Use PdfFormat::PDF_E_1, write a .log.xml conversion report, and save the resulting PDF.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Derive the `.log.xml` report path from `outputFile`.
1. Convert to `PdfFormat::PDF_E_1` with [Document::Convert()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/convert/) and `ConvertErrorAction::Delete`.
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/IO/ConvertStrategies/PdfFormat.h>
#include <Aspose.PDF.Cpp/IO/ConvertStrategies/ConvertErrorAction.h>
#include <system/io/path.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToPdfE(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto logFile = System::IO::Path::ChangeExtension(outputFile, u".log.xml");
		document->Convert(logFile, PdfFormat::PDF_E_1, ConvertErrorAction::Delete);
		document->Save(outputFile);
	}
}
```

## Validate PDF/E-1 compliance

Call Validate() for PDF_E_1 and print its Boolean result. outputFile names the validation report, not a converted PDF. The input document is not saved or modified.

1. Open the input PDF.
1. Call [Document::Validate()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/validate/) with the report path and [PdfFormat](https://reference.aspose.com/pdf/cpp/aspose.pdf/pdfformat/)::PDF_E_1.
1. Print whether the document conforms.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/IO/ConvertStrategies/PdfFormat.h>
#include <iostream>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ValidatePdfE(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		const bool isValid = document->Validate(outputFile, PdfFormat::PDF_E_1);
		std::cout << (isValid ? "Conforms to PDF/E." : "Does not conform to PDF/E.") << std::endl;
	}
}
```

## Related conversion guides

- [PDF Conversion](/pdf/cpp/converting/)

