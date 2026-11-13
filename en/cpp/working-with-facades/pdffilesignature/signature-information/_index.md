---
title: Signature Information in C++
linktitle: Signature Information
type: docs
weight: 60
url: /cpp/signature-information/
description: Signature Information in C++ with the PdfFileSignature facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Signature Information with the PdfFileSignature Facade
Abstract: List signature names and print the first signature's signer, date, reason, and location.
---

Use [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/) for this task. The examples below retain the original C++ code and API Reference steps.

## Get signature information

List signature names and print the first signature's signer, date, reason, and location.

1. Create [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Read signature identifiers with [PdfFileSignature::GetSignatureNames()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/getsignaturenames/).
1. List signature names with [PdfFileSignature::GetSignNames()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/getsignnames/).
1. Read the signer name with [PdfFileSignature::GetSignerName()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/getsignername/).
1. Read the signing date with [PdfFileSignature::GetDateTime()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/getdatetime/).
1. Read the signing reason with [PdfFileSignature::GetReason()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/getreason/).
1. Read the signing location with [PdfFileSignature::GetLocation()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/getlocation/).
1. Print the results or diagnostic messages shown in the example.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>
#include <Aspose.PDF.Cpp/Facades/SignatureName.h>
#include <iostream>
#include <system/collections/ilist.h>
#include <system/date_time.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileSignature
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void GetSignatureInformation(String inputFile)
{
    auto pdfSignature = MakeObject<PdfFileSignature>();
    pdfSignature->BindPdf(inputFile);
    auto signatureName = pdfSignature->GetSignatureNames()->idx_get(0);
    for (const auto &name : pdfSignature->GetSignNames())
        std::cout << "Signature Name: " << name << std::endl;
    std::cout << "Signer: " << pdfSignature->GetSignerName(signatureName) << std::endl;
    std::cout << "Date: " << pdfSignature->GetDateTime(signatureName).ToString() << std::endl;
    std::cout << "Reason: " << pdfSignature->GetReason(signatureName) << std::endl;
    std::cout << "Location: " << pdfSignature->GetLocation(signatureName) << std::endl;
}
} // namespace Facades::Examples::PDF_FileSignature
```
