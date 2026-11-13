---
title: Signature Extraction in C++
linktitle: Signature Extraction
type: docs
weight: 50
url: /cpp/signature-extraction/
description: Signature Extraction in C++ with the PdfFileSignature facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Signature Extraction with the PdfFileSignature Facade
Abstract: Extract the certificate for the first signature and copy it to outputFile.
---

Use [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/) for this task. The examples below retain the original C++ code and API Reference steps.

## Extract signature certificate

Extract the certificate for the first signature and copy it to outputFile.

1. Create [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Read signature identifiers with [PdfFileSignature::GetSignatureNames()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/getsignaturenames/).
1. Extract the certificate stream with [PdfFileSignature::ExtractCertificate()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/extractcertificate/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>
#include <Aspose.PDF.Cpp/Facades/SignatureName.h>
#include <system/collections/ilist.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileSignature
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ExtractSignatureCertificate(String inputFile, String outputFile)
{
    auto pdfSignature = MakeObject<PdfFileSignature>();
    pdfSignature->BindPdf(inputFile);
    auto signatureName = pdfSignature->GetSignatureNames()->idx_get(0);
    auto inputStream = pdfSignature->ExtractCertificate(signatureName);
    auto outputStream = System::IO::File::Create(outputFile);

    inputStream->CopyTo(outputStream);
}
} // namespace Facades::Examples::PDF_FileSignature
```
