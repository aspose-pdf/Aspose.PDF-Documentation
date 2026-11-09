---
title: Get PDF Metadata in C++
linktitle: Get PDF Metadata
type: docs
weight: 20
url: /cpp/get-pdf-metadata/
description: Get PDF Metadata in C++ with the PdfFileInfo facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Get PDF Metadata with the PdfFileInfo Facade
Abstract: Print document information, file-status flags, and the custom Reviewer metadata value when available.
---

Use [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) for this task. The examples below retain the original C++ code and API Reference steps.

## Get PDF metadata

Print document information, file-status flags, and the custom Reviewer metadata value when available.

1. Create [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) with the input PDF path.
1. Read subject through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/).
1. Read title through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/).
1. Read keywords through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/).
1. Read creator through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/).
1. Read creation date through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/).
1. Read mod date through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/).
1. Read is pdf file through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/).
1. Read is encrypted through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/).
1. Read has open password through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/).
1. Read has edit password through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/).
1. Read has collection through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/).
1. Read custom metadata with [PdfFileInfo::GetMetaInfo()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/getmetainfo/).
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

void GetPdfMetadata(String inputFile)
{
    auto pdfInfo = MakeObject<PdfFileInfo>(inputFile);
    std::cout << "Subject: " << pdfInfo->get_Subject() << std::endl;
    std::cout << "Title: " << pdfInfo->get_Title() << std::endl;
    std::cout << "Keywords: " << pdfInfo->get_Keywords() << std::endl;
    std::cout << "Creator: " << pdfInfo->get_Creator() << std::endl;
    std::cout << "Creation Date: " << pdfInfo->get_CreationDate() << std::endl;
    std::cout << "Modification Date: " << pdfInfo->get_ModDate() << std::endl;
    std::cout << "Is Valid PDF: " << pdfInfo->get_IsPdfFile() << std::endl;
    std::cout << "Is Encrypted: " << pdfInfo->get_IsEncrypted() << std::endl;
    std::cout << "Has Open Password: " << pdfInfo->get_HasOpenPassword() << std::endl;
    std::cout << "Has Edit Password: " << pdfInfo->get_HasEditPassword() << std::endl;
    std::cout << "Is Portfolio: " << pdfInfo->get_HasCollection() << std::endl;
    auto reviewer = pdfInfo->GetMetaInfo(u"Reviewer");
    std::cout << "Reviewer: " << (reviewer.IsNullOrEmpty() ? u"No Reviewer metadata found." : reviewer) << std::endl;
    pdfInfo->Close();
}
} // namespace  Facades::Examples::PDF_FileInfo
```
