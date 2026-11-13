---
title: Get Page Information in C++
linktitle: Get Page Information
type: docs
weight: 10
url: /cpp/get-page-info/
description: Get Page Information in C++ with the PdfFileInfo facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Get Page Information with the PdfFileInfo Facade
Abstract: Print page 1 width, height, and rotation.
---

Use [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) for this task. The examples below retain the original C++ code and API Reference steps.

## Get page information

Print page 1 width, height, and rotation.

1. Create [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) with the input PDF path.
1. Read the page width with [PdfFileInfo::GetPageWidth()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/getpagewidth/).
1. Read the page height with [PdfFileInfo::GetPageHeight()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/getpageheight/).
1. Read the page rotation with [PdfFileInfo::GetPageRotation()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/getpagerotation/).
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

void GetPageInformation(String inputFile)
{
    auto pdfInfo = MakeObject<PdfFileInfo>(inputFile);
    std::cout << "Page Width: " << pdfInfo->GetPageWidth(1) << std::endl;
    std::cout << "Page Height: " << pdfInfo->GetPageHeight(1) << std::endl;
    std::cout << "Page Rotation: " << pdfInfo->GetPageRotation(1) << std::endl;
    pdfInfo->Close();
}
} // namespace  Facades::Examples::PDF_FileInfo
```
