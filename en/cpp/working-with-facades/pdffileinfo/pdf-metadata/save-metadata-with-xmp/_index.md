---
title: Save Metadata with XMP in C++
linktitle: Save Metadata with XMP
type: docs
weight: 30
url: /cpp/save-metadata-with-xmp/
description: Save Metadata with XMP in C++ with the PdfFileInfo facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Save Metadata with XMP with the PdfFileInfo Facade
Abstract: Set subject, title, keywords, and creator and save the updated document information with XMP.
---

Use [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) for this task. The examples below retain the original C++ code and API Reference steps.

## Save info with XMP

Set subject, title, keywords, and creator and save the updated document information with XMP.

1. Create [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) with the input PDF path.
1. Set subject through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) using the example values.
1. Set title through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) using the example values.
1. Set keywords through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) using the example values.
1. Set creator through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) using the example values.
1. Save document information and XMP with [PdfFileInfo::SaveNewInfoWithXmp()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/savenewinfowithxmp/).
1. Close the facade with [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/)::`Close()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileInfo.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileInfo
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Facades;

	void SaveInfoWithXmp(String inputFile, String outputFile)
	{
		auto pdfInfo = MakeObject<PdfFileInfo>(inputFile);
		pdfInfo->set_Subject(u"Aspose PDF for C++");
		pdfInfo->set_Title(u"Aspose PDF for C++");
		pdfInfo->set_Keywords(u"Aspose, PDF, C++");
		pdfInfo->set_Creator(u"Aspose Team");
		pdfInfo->SaveNewInfoWithXmp(outputFile);
		pdfInfo->Close();
	}
} // namespace Facades::Examples::PDF_FileInfo
```
