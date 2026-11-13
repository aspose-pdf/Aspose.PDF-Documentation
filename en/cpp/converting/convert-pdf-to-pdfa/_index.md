---
title: Convert PDF to PDF/A in C++
linktitle: Convert PDF to PDF/A
type: docs
weight: 100
url: /cpp/convert-pdf-to-pdfa/
description: Convert PDFs to PDF/A-1b, PDF/A-3a, or PDF/A-4 with logging, font substitution, attachments, and automatic tagging.
lastmod: "2026-11-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Export PDF to PDF/A Using C++
Abstract: Create PDF/A output with conversion reports and optional font substitution, attachment embedding, or automatic tagging. A separate example validates PDF/A-1b without saving a converted PDF.
---

Convert PDFs to PDF/A-1b, PDF/A-3a, or PDF/A-4 with logging, font substitution, attachments, and automatic tagging.

Configure the Aspose.PDF for C++ SDK before running these functions. Pass an existing input file and a writable destination path; create any required output directories first. Each function is an independent example, and its options do not carry over to other examples.

Conversion examples use `ConvertErrorAction::Delete`, which can remove elements that cannot conform to the selected standard. Review the conversion log and validate the saved PDF before relying on its compliance. The examples do not check the return value of `Convert()`.

## Convert PDF to PDF/A-1b

Convert to PDF_A_1B and write a .log.xml conversion report beside the output PDF.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Derive the `.log.xml` report path from `outputFile`.
1. Select `PdfFormat::PDF_A_1B` for [Document::Convert()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/convert/) and use `ConvertErrorAction::Delete`.
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

	void ConvertPdfToPdfA(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto logFile = System::IO::Path::ChangeExtension(outputFile, u".log.xml");
		document->Convert(logFile, PdfFormat::PDF_A_1B, ConvertErrorAction::Delete);
		document->Save(outputFile);
	}
}
```

## Substitute a missing font

Try to find AgencyFB. If it is missing, register a SimpleFontSubstitution from AgencyFB to Arial before converting to PDF/A-1b. Ensure Arial is installed.

1. Find AgencyFB with [FontRepository](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/fontrepository/). If it is missing, add a [SimpleFontSubstitution](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/simplefontsubstitution/) from AgencyFB to Arial.
1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Derive the conversion report path and select `PdfFormat::PDF_A_1B`.
1. Call [Document::Convert()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/convert/) with the selected format and `ConvertErrorAction::Delete`.
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/IO/ConvertStrategies/PdfFormat.h>
#include <Aspose.PDF.Cpp/IO/ConvertStrategies/ConvertErrorAction.h>
#include <system/io/path.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Exceptions/FontNotFoundException.h>
#include <Aspose.PDF.Cpp/CommonData/Text/Fonts/FontSubstitutions/SimpleFontSubstitution.h>
#include <Aspose.PDF.Cpp/CommonData/Text/Fonts/FontSubstitutions/FontSubstitutionCollection.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToPdfAWithFontSubstitution(String inputFile, String outputFile)
	{
		try {
			Aspose::Pdf::Text::FontRepository::FindFont(u"AgencyFB");
		}
		catch (FontNotFoundException&) {
			Aspose::Pdf::Text::FontRepository::get_Substitutions()->Add(MakeObject<Aspose::Pdf::Text::SimpleFontSubstitution>(u"AgencyFB", u"Arial"));
		}
		auto document = MakeObject<Document>(inputFile);
		auto logFile = System::IO::Path::ChangeExtension(outputFile, u".log.xml");
		document->Convert(logFile, PdfFormat::PDF_A_1B, ConvertErrorAction::Delete);
		document->Save(outputFile);
	}
}
```

## Convert PDF with an attachment

Open attachmentFile, embed it with its original file name and the description Image attachment, then convert to PDF_A_3A. Keep the attachment stream available until saving.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Derive the conversion report path and open `attachmentFile` as a readable stream.
1. Create a [FileSpecification](https://reference.aspose.com/pdf/cpp/aspose.pdf/filespecification/) with the original attachment name and add it to the document's [EmbeddedFileCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/embeddedfilecollection/).
1. Convert to `PdfFormat::PDF_A_3A` with [Document::Convert()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/convert/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/IO/ConvertStrategies/PdfFormat.h>
#include <Aspose.PDF.Cpp/IO/ConvertStrategies/ConvertErrorAction.h>
#include <system/io/path.h>
#include <Aspose.PDF.Cpp/FileSpecification.h>
#include <Aspose.PDF.Cpp/EmbeddedFileCollection.h>
#include <system/io/file.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToPdfAWithAttachment(String inputFile, String attachmentFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto logFile = System::IO::Path::ChangeExtension(outputFile, u".log.xml");
		auto attachment = System::IO::File::OpenRead(attachmentFile);
		auto attachmentName = System::IO::Path::GetFileName(attachmentFile);
		document->get_EmbeddedFiles()->Add(MakeObject<FileSpecification>(attachment, attachmentName, u"Image attachment"));
		document->Convert(logFile, PdfFormat::PDF_A_3A, ConvertErrorAction::Delete);
		document->Save(outputFile);
	}
}
```

## Enable automatic tagging

Configure PdfFormatConversionOptions for PDF_A_1B, enable AutoTaggingSettings, and choose HeadingRecognitionStrategy::Auto before conversion.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [PdfFormatConversionOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/pdfformatconversionoptions/) with the report path, `PDF_A_1B`, and `ConvertErrorAction::Delete`.
1. Create [AutoTaggingSettings](https://reference.aspose.com/pdf/cpp/aspose.pdf/autotaggingsettings/), set `EnableAutoTagging` to `true`, and select `HeadingRecognitionStrategy::Auto`.
1. Assign the tagging settings to the conversion options and pass the options to [Document::Convert()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/convert/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/IO/ConvertStrategies/PdfFormat.h>
#include <Aspose.PDF.Cpp/IO/ConvertStrategies/ConvertErrorAction.h>
#include <system/io/path.h>
#include <Aspose.PDF.Cpp/IO/ConvertStrategies/AutoTaggingSettings.h>
#include <Aspose.PDF.Cpp/PdfToMarkdown/MarkdownOptions/HeadingRecognitionStrategy.h>
#include <Aspose.PDF.Cpp/PdfFormatConversionOptions.h>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ConvertPdfToPdfAWithAutomaticTagging(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto logFile = System::IO::Path::ChangeExtension(outputFile, u".log.xml");
		auto options = MakeObject<PdfFormatConversionOptions>(logFile, PdfFormat::PDF_A_1B, ConvertErrorAction::Delete);
		auto tagging = MakeObject<AutoTaggingSettings>();
		tagging->set_EnableAutoTagging(true);
		tagging->set_HeadingRecognitionStrategy(HeadingRecognitionStrategy::Auto);
		options->set_AutoTaggingSettings(tagging);
		document->Convert(options);
		document->Save(outputFile);
	}
}
```

## Convert PDF to PDF/A-4

Convert first to PDF version 2.0 and then to PDF_A_4. The example writes separate .pdf20.log.xml and .log.xml reports.

1. Open the input PDF as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Derive separate `.pdf20.log.xml` and `.log.xml` report paths from `outputFile`.
1. Call [Document::Convert()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/convert/) for `PdfFormat::v_2_0`, then for `PdfFormat::PDF_A_4`, using `ConvertErrorAction::Delete` for both calls.
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

	void ConvertPdfToPdfA4(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		auto logFile = System::IO::Path::ChangeExtension(outputFile, u".log.xml");
		document->Convert(System::IO::Path::ChangeExtension(outputFile, u".pdf20.log.xml"), PdfFormat::v_2_0, ConvertErrorAction::Delete);
		document->Convert(logFile, PdfFormat::PDF_A_4, ConvertErrorAction::Delete);
		document->Save(outputFile);
	}
}
```

## Validate PDF/A-1b compliance

Call Validate() for PDF_A_1B and print its Boolean result. Here outputFile is the validation report path, not a PDF file; the example does not modify or save the input PDF.

1. Open the input PDF.
1. Call [Document::Validate()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/validate/) with the report path and [PdfFormat](https://reference.aspose.com/pdf/cpp/aspose.pdf/pdfformat/)::PDF_A_1B.
1. Print whether the validation succeeded.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/IO/ConvertStrategies/PdfFormat.h>
#include <iostream>

namespace ConvertingExamples
{
	using namespace System;
	using namespace Aspose::Pdf;

	void ValidatePdfA(String inputFile, String outputFile)
	{
		auto document = MakeObject<Document>(inputFile);
		const bool isValid = document->Validate(outputFile, PdfFormat::PDF_A_1B);
		std::cout << (isValid ? "Conforms to PDF/A." : "Does not conform to PDF/A.") << std::endl;
	}
}
```

## Related conversion guides

- [PDF Conversion](/pdf/cpp/converting/)
- [Remove PDF/A Compliance Information](/pdf/cpp/convert-pdfa-to-pdf/)

