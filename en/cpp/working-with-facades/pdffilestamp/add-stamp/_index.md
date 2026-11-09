---
title: Add Stamp to PDF in C++
linktitle: Add Stamp to PDF
type: docs
weight: 40
url: /cpp/add-stamp/
description: Add Stamp to PDF in C++ with the PdfFileStamp facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Stamp to PDF with the PdfFileStamp Facade
Abstract: Bind an image to a Stamp and apply it with PdfFileStamp.
---

Use [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/) for this task. The examples below retain the original C++ code and API Reference steps.

## Add stamp to PDF

Bind an image to a Stamp and apply it with PdfFileStamp.

1. Create [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Apply the configured stamp with [PdfFileStamp::AddStamp()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/addstamp/).
1. Save the resulting PDF with [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileStamp.h>
#include <Aspose.PDF.Cpp/Facades/Stamp.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileStamp
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Stamp = Aspose::Pdf::Facades::Stamp;

void AddStampToPdf(String inputFile, String imageFile, String outputFile)
{
    auto pdfStamper = MakeObject<PdfFileStamp>();
    pdfStamper->BindPdf(inputFile);
    auto stamp = MakeObject<Stamp>();
    stamp->BindImage(imageFile);
    pdfStamper->AddStamp(stamp);
    pdfStamper->Save(outputFile);
}
} // namespace Facades::Examples::PDF_FileStamp
```
