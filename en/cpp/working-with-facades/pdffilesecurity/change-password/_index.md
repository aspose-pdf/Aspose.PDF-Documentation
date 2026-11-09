---
title: Change Password of PDF File in C++
linktitle: Change Password of PDF File
type: docs
weight: 10
url: /cpp/change-password/
description: Change Password of PDF File in C++ with the PdfFileSecurity facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Change Password of PDF File with the PdfFileSecurity Facade
Abstract: Change both passwords using the existing owner password and reset privileges to printing only with x128 key size. Change the user and owner passwords using the existing owner password. Check TryChangePassword and save only when it returns true; otherwise print a diagnostic.
---

Use [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/) for this task. The examples below retain the original C++ code and API Reference steps.

## Change password and reset security

Change both passwords using the existing owner password and reset privileges to printing only with x128 key size.

1. Configure the permission flags with [DocumentPrivilege](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/documentprivilege/).
1. Create [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Change passwords and security settings with [PdfFileSecurity::ChangePassword()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/changepassword/).
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

void ChangePasswordAndResetSecurity(String inputFile, String outputFile)
{
    auto fileSecurity = MakeObject<PdfFileSecurity>();
    fileSecurity->BindPdf(inputFile);
    auto privilege = DocumentPrivilege::get_ForbidAll();
    privilege->set_AllowPrint(true);
    fileSecurity->ChangePassword(u"owner_password", u"new_user_password", u"new_owner_password", privilege,
                                 KeySize::x128);
    fileSecurity->Save(outputFile);
    fileSecurity->Close();
}
} // namespace Facades::Examples::PDF_FileSecurity
```

## Change user and owner password

Change the user and owner passwords using the existing owner password.

1. Create [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Change passwords and security settings with [PdfFileSecurity::ChangePassword()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/changepassword/).
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

void ChangeUserAndOwnerPassword(String inputFile, String outputFile)
{
    auto fileSecurity = MakeObject<PdfFileSecurity>();
    fileSecurity->BindPdf(inputFile);
    fileSecurity->ChangePassword(u"owner_password", u"new_user_password", u"new_owner_password");
    fileSecurity->Save(outputFile);
    fileSecurity->Close();
}
} // namespace Facades::Examples::PDF_FileSecurity
```

## Try change password without exception

Check TryChangePassword and save only when it returns true; otherwise print a diagnostic.

1. Create [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Attempt the password change and check the result of [PdfFileSecurity::TryChangePassword()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/trychangepassword/).
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

void TryChangePasswordWithoutException(String inputFile, String outputFile)
{
    auto fileSecurity = MakeObject<PdfFileSecurity>();
    fileSecurity->BindPdf(inputFile);
    if (fileSecurity->TryChangePassword(u"owner_password", u"new_user_password", u"new_owner_password"))
    {
        fileSecurity->Save(outputFile);
    }
    else
    {
        std::cout << "Password change failed. Check owner password or document security." << std::endl;
    }
    fileSecurity->Close();
}
} // namespace Facades::Examples::PDF_FileSecurity
```
