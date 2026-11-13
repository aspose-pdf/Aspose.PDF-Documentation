---
title: Decrypt PDF File in C++
linktitle: Decrypt PDF File
type: docs
weight: 20
url: /cpp/decrypt-pdf-file/
description: Decrypt PDF File in C++ with the PdfFileSecurity facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Decrypt PDF File with the PdfFileSecurity Facade
Abstract: Decrypt the PDF using the owner password and save the result. Check TryDecryptFile and save only when it returns true; otherwise print a diagnostic.
---

Use [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/) for this task. The examples below retain the original C++ code and API Reference steps.

## Decrypt PDF with owner password

Decrypt the PDF using the owner password and save the result.

1. Create [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Decrypt the bound PDF with [PdfFileSecurity::MfDecryptFile()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/mfdecryptfile/).
1. Save the resulting PDF with [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/)::`Save()`.
1. Close the facade with [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/)::`Close()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileSecurity.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileSecurity
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void DecryptPdfWithOwnerPassword(String inputFile, String outputFile)
{
    auto fileSecurity = MakeObject<PdfFileSecurity>();
    fileSecurity->BindPdf(inputFile);
    fileSecurity->MfDecryptFile(u"owner_password");
    fileSecurity->Save(outputFile);
    fileSecurity->Close();
}
} // namespace Facades::Examples::PDF_FileSecurity
```

## Try decrypt PDF without exception

Check TryDecryptFile and save only when it returns true; otherwise print a diagnostic.

1. Create [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Attempt decryption and check the result of [PdfFileSecurity::TryDecryptFile()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/trydecryptfile/).
1. Save the PDF with [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/)::`Save()` only after the operation succeeds.
1. Close the facade with [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/)::`Close()`.
1. Print the results or diagnostic messages shown in the example.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileSecurity.h>
#include <iostream>
#include <system/string.h>

namespace Facades::Examples::PDF_FileSecurity
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void TryDecryptPdfWithoutException(String inputFile, String outputFile)
{
    auto fileSecurity = MakeObject<PdfFileSecurity>();
    fileSecurity->BindPdf(inputFile);
    if (fileSecurity->TryDecryptFile(u"owner_password"))
    {
        fileSecurity->Save(outputFile);
    }
    else
    {
        std::cout << "Decryption failed. Check password or document security." << std::endl;
    }
    fileSecurity->Close();
}
} // namespace Facades::Examples::PDF_FileSecurity
```
