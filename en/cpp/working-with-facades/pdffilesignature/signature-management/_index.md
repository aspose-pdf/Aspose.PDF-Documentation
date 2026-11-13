---
title: Signature Management in C++
linktitle: Signature Management
type: docs
weight: 80
url: /cpp/signature-management/
description: Signature Management in C++ with the PdfFileSignature facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Signature Management with the PdfFileSignature Facade
Abstract: Remove the first signature and save the modified PDF.
---

Use [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/) for this task. The examples below retain the original C++ code and API Reference steps.

## Remove signature

Remove the first signature and save the modified PDF.

1. Create [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Read signature identifiers with [PdfFileSignature::GetSignatureNames()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/getsignaturenames/).
1. Remove the selected signature with [PdfFileSignature::RemoveSignature()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/removesignature/).
1. Save the resulting PDF with [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>
#include <Aspose.PDF.Cpp/Facades/SignatureName.h>
#include <system/collections/ilist.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileSignature
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void RemoveSignature(String inputFile, String outputFile)
{
    auto pdfSignature = MakeObject<PdfFileSignature>();
    pdfSignature->BindPdf(inputFile);
    auto signatureName = pdfSignature->GetSignatureNames()->idx_get(0);
    pdfSignature->RemoveSignature(signatureName);
    pdfSignature->Save(outputFile);
}
} // namespace Facades::Examples::PDF_FileSignature
```
