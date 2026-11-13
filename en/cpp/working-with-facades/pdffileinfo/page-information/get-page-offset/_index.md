---
title: Get Page Offset in C++
linktitle: Get Page Offset
type: docs
weight: 20
url: /cpp/get-page-offset/
description: Get Page Offset in C++ with the PdfFileInfo facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Get Page Offset with the PdfFileInfo Facade
Abstract: Print page 1 X and Y offsets in inches.
---

Use [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) for this task. The examples below retain the original C++ code and API Reference steps.

## Get page offsets

Print page 1 X and Y offsets in inches.

1. Create [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) with the input PDF path.
1. Read the X offset with [PdfFileInfo::GetPageXOffset()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/getpagexoffset/).
1. Read the Y offset with [PdfFileInfo::GetPageYOffset()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/getpageyoffset/).
1. Close the facade with [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/)::`Close()`.
1. Print the results or diagnostic messages shown in the example.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileInfo.h>
#include <iostream>
#include <system/string.h>

namespace Facades::Examples::PDF_FileInfo
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Facades;

	void GetPageOffsets(String inputFile)
	{
		auto pdfInfo = MakeObject<PdfFileInfo>(inputFile);
		std::cout << "Page X Offset: " << (pdfInfo->GetPageXOffset(1) / 72.0) << " inches" << std::endl;
		std::cout << "Page Y Offset: " << (pdfInfo->GetPageYOffset(1) / 72.0) << " inches" << std::endl;
		pdfInfo->Close();
	}
} // namespace Facades::Examples::PDF_FileInfo
```
