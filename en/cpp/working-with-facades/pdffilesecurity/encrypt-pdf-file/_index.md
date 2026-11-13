---
title: Encrypt PDF File in C++
linktitle: Encrypt PDF File
type: docs
weight: 30
url: /cpp/encrypt-pdf-file/
description: Encrypt PDF File in C++ with the PdfFileSecurity facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Encrypt PDF File with the PdfFileSecurity Facade
Abstract: Encrypt with AES, x256 key size, and printing allowed. Encrypt with x128 key size while disabling printing and copying from an initially AllowAll privilege set. Encrypt with sample user and owner passwords, x128 key size, and printing allowed.
---

Use [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/) for this task. The examples below retain the original C++ code and API Reference steps.

## Encrypt PDF with encryption algorithm

Encrypt with AES, x256 key size, and printing allowed.

1. Configure the permission flags with [DocumentPrivilege](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/documentprivilege/).
1. Create [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Encrypt the bound PDF with [PdfFileSecurity::MfEncryptFile()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/mfencryptfile/).
1. Save the resulting PDF with [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/)::`Save()`.
1. Close the facade with [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/)::`Close()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/Algorithm.h>
#include <Aspose.PDF.Cpp/Facades/DocumentPrivilege.h>
#include <Aspose.PDF.Cpp/Facades/KeySize.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileSecurity.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileSecurity
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void EncryptPdfWithEncryptionAlgorithm(String inputFile, String outputFile)
{
    auto fileSecurity = MakeObject<PdfFileSecurity>();
    fileSecurity->BindPdf(inputFile);
    auto privilege = DocumentPrivilege::get_ForbidAll();
    privilege->set_AllowPrint(true);
    fileSecurity->MfEncryptFile(u"user_password", u"owner_password", privilege, KeySize::x256, Algorithm::AES);
    fileSecurity->Save(outputFile);
    fileSecurity->Close();
}
} // namespace Facades::Examples::PDF_FileSecurity
```

## Encrypt PDF with permissions

Encrypt with x128 key size while disabling printing and copying from an initially AllowAll privilege set.

1. Configure the permission flags with [DocumentPrivilege](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/documentprivilege/).
1. Create [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Encrypt the bound PDF with [PdfFileSecurity::MfEncryptFile()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/mfencryptfile/).
1. Save the resulting PDF with [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/)::`Save()`.
1. Close the facade with [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/)::`Close()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/DocumentPrivilege.h>
#include <Aspose.PDF.Cpp/Facades/KeySize.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileSecurity.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileSecurity
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void EncryptPdfWithPermissions(String inputFile, String outputFile)
{
    auto fileSecurity = MakeObject<PdfFileSecurity>();
    fileSecurity->BindPdf(inputFile);
    auto privilege = DocumentPrivilege::get_AllowAll();
    privilege->set_AllowPrint(false);
    privilege->set_AllowCopy(false);
    fileSecurity->MfEncryptFile(u"user_password", u"owner_password", privilege, KeySize::x128);
    fileSecurity->Save(outputFile);
    fileSecurity->Close();
}
} // namespace Facades::Examples::PDF_FileSecurity
```

## Encrypt PDF with user owner password

Encrypt with sample user and owner passwords, x128 key size, and printing allowed.

1. Configure the permission flags with [DocumentPrivilege](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/documentprivilege/).
1. Create [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Encrypt the bound PDF with [PdfFileSecurity::MfEncryptFile()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/mfencryptfile/).
1. Save the resulting PDF with [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/)::`Save()`.
1. Close the facade with [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/)::`Close()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/DocumentPrivilege.h>
#include <Aspose.PDF.Cpp/Facades/KeySize.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileSecurity.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileSecurity
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void EncryptPdfWithUserOwnerPassword(String inputFile, String outputFile)
{
    auto fileSecurity = MakeObject<PdfFileSecurity>();
    fileSecurity->BindPdf(inputFile);
    auto privilege = DocumentPrivilege::get_ForbidAll();
    privilege->set_AllowPrint(true);
    fileSecurity->MfEncryptFile(u"user_password", u"owner_password", privilege, KeySize::x128);
    fileSecurity->Save(outputFile);
    fileSecurity->Close();
}
} // namespace Facades::Examples::PDF_FileSecurity
```
