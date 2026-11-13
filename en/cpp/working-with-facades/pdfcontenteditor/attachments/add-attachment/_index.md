---
title: Add Attachment in C++
linktitle: Add Attachment
type: docs
weight: 10
url: /cpp/add-attachment/
description: Add Attachment in C++ with the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Attachment with the PdfContentEditor Facade
Abstract: Attach the supplied file stream using its filename and a sample description.
---

Use [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/) for this task. The examples below retain the original C++ code and API Reference steps.

## Add attachment

Attach the supplied file stream using its filename and a sample description.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Attach the file with [PdfContentEditor::AddDocumentAttachment()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/adddocumentattachment/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/io/path.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Facades;

	void AddAttachment(String inputFile, String attachmentFile, String outputFile)
	{
		auto editor = MakeObject<PdfContentEditor>();
		auto attachmentStream = System::IO::File::OpenRead(attachmentFile);

		editor->BindPdf(inputFile);
		editor->AddDocumentAttachment(attachmentStream, System::IO::Path::GetFileName(attachmentFile),
			u"Sample attachment.");
		editor->Save(outputFile);
	}
} // namespace Facades::Examples::PDF_ContentEditor
```
