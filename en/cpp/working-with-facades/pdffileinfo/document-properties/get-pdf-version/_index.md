---
title: Get PDF Version in C++
linktitle: Get PDF Version
type: docs
weight: 20
url: /cpp/get-pdf-version/
description: Get PDF Version in C++ with the PdfFileInfo facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Get PDF Version with the PdfFileInfo Facade
Abstract: Print the PDF version.
---

Use [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) for this task. The examples below retain the original C++ code and API Reference steps.

## Get PDF version

Print the PDF version.

1. Create [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) with the input PDF path.
1. Read the PDF version with [PdfFileInfo::GetPdfVersion()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/getpdfversion/).
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

void GetPdfVersion(String inputFile)
{
    auto pdfInfo = MakeObject<PdfFileInfo>(inputFile);
    std::cout << std::endl;
    std::cout << String(u"PDF Version: ") << pdfInfo->GetPdfVersion() << std::endl;
    pdfInfo->Close();
}
} // namespace Facades::Examples::PDF_FileInfo
```
