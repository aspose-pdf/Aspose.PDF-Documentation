---
title: Clear PDF Metadata in C++
linktitle: Clear PDF Metadata
type: docs
weight: 10
url: /cpp/clear-pdf-metadata/
description: Clear PDF Metadata in C++ with the PdfFileInfo facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Clear PDF Metadata with the PdfFileInfo Facade
Abstract: Clear document information, save the output, and close PdfFileInfo.
---

Use [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) for this task. The examples below retain the original C++ code and API Reference steps.

## Clear PDF metadata

Clear document information, save the output, and close PdfFileInfo.

1. Create [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) with the input PDF path.
1. Clear document information with [PdfFileInfo::ClearInfo()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/clearinfo/).
1. Save the resulting PDF with [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/)::`Save()`.
1. Close the facade with [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/)::`Close()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileInfo.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileInfo
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Facades;

	void ClearPdfMetadata(String inputFile, String outputFile)
	{
		auto pdfInfo = MakeObject<PdfFileInfo>(inputFile);
		pdfInfo->ClearInfo();
		pdfInfo->Save(outputFile);
		pdfInfo->Close();
	}
} // namespace Facades::Examples::PDF_FileInfo
```
