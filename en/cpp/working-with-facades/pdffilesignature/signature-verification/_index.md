---
title: Signature Verification in C++
linktitle: Signature Verification
type: docs
weight: 90
url: /cpp/signature-verification/
description: Signature Verification in C++ with the PdfFileSignature facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Signature Verification with the PdfFileSignature Facade
Abstract: Print the first signature's verification result and whether it covers the whole document.
---

Use [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/) for this task. The examples below retain the original C++ code and API Reference steps.

## Verify PDF signature

Print the first signature's verification result and whether it covers the whole document.

1. Create [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Read signature identifiers with [PdfFileSignature::GetSignatureNames()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/getsignaturenames/).
1. Verify the signature with [PdfFileSignature::VerifySignature()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/verifysignature/).
1. Check document coverage with [PdfFileSignature::CoversWholeDocument()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/coverswholedocument/).
1. Print the results or diagnostic messages shown in the example.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>
#include <Aspose.PDF.Cpp/Facades/SignatureName.h>
#include <iostream>
#include <system/collections/ilist.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileSignature
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void VerifyPdfSignature(String inputFile)
{
    auto pdfSignature = MakeObject<PdfFileSignature>();
    pdfSignature->BindPdf(inputFile);
    auto signatureName = pdfSignature->GetSignatureNames()->idx_get(0);
    std::cout << "Signature '" << signatureName->ToString()
              << "' is valid: " << pdfSignature->VerifySignature(signatureName) << std::endl;
    std::cout << "Signature covers whole document: " << pdfSignature->CoversWholeDocument(signatureName) << std::endl;
}
} // namespace Facades::Examples::PDF_FileSignature
```
