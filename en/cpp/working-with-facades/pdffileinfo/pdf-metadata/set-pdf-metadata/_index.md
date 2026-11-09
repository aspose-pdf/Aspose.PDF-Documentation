---
title: Set PDF Metadata in C++
linktitle: Set PDF Metadata
type: docs
weight: 50
url: /cpp/set-pdf-metadata/
description: Set PDF Metadata in C++ with the PdfFileInfo facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Set PDF Metadata with the PdfFileInfo Facade
Abstract: Set standard document information and the custom CustomKey value.
---

Use [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) for this task. The examples below retain the original C++ code and API Reference steps.

## Set PDF metadata

Set standard document information and the custom CustomKey value.

1. Create [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) with the input PDF path.
1. Set subject through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) using the example values.
1. Set title through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) using the example values.
1. Set keywords through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) using the example values.
1. Set creator through [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/) using the example values.
1. Set custom metadata with [PdfFileInfo::SetMetaInfo()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/setmetainfo/).
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

void SetPdfMetadata(String inputFile, String outputFile)
{
    auto pdfInfo = MakeObject<PdfFileInfo>(inputFile);
    pdfInfo->set_Subject(u"Aspose PDF for C++");
    pdfInfo->set_Title(u"Aspose PDF for C++");
    pdfInfo->set_Keywords(u"Aspose, PDF, C++");
    pdfInfo->set_Creator(u"Aspose Team");
    pdfInfo->SetMetaInfo(u"CustomKey", u"CustomValue");
    pdfInfo->Save(outputFile);
    pdfInfo->Close();
}
} // namespace Facades::Examples::PDF_FileInfo
```
