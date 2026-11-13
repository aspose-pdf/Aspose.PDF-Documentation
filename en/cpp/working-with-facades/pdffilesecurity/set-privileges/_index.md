---
title: Set Privileges on an Existing PDF File in C++
linktitle: Set Privileges on an Existing PDF File
type: docs
weight: 40
url: /cpp/set-privileges/
description: Set Privileges on an Existing PDF File in C++ with the PdfFileSecurity facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Set Privileges on an Existing PDF File with the PdfFileSecurity Facade
Abstract: Set printing allowed and copying disabled using the supplied sample passwords. Set a printing-only privilege set using the overload without password arguments. Check TrySetPrivilege and save only when it returns true; otherwise print a diagnostic.
---

Use [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/) for this task. The examples below retain the original C++ code and API Reference steps.

## Set PDF privileges with passwords

Set printing allowed and copying disabled using the supplied sample passwords.

1. Configure the permission flags with [DocumentPrivilege](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/documentprivilege/).
1. Create [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Apply document privileges with [PdfFileSecurity::SetPrivilege()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/setprivilege/).
1. Save the resulting PDF with [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/)::`Save()`.
1. Close the facade with [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/)::`Close()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/DocumentPrivilege.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileSecurity.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileSecurity
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void SetPdfPrivilegesWithPasswords(String inputFile, String outputFile)
{
    auto fileSecurity = MakeObject<PdfFileSecurity>();
    fileSecurity->BindPdf(inputFile);
    auto privilege = DocumentPrivilege::get_ForbidAll();
    privilege->set_AllowPrint(true);
    privilege->set_AllowCopy(false);
    fileSecurity->SetPrivilege(u"user_password", u"owner_password", privilege);
    fileSecurity->Save(outputFile);
    fileSecurity->Close();
}
} // namespace Facades::Examples::PDF_FileSecurity
```

## Set PDF privileges without passwords

Set a printing-only privilege set using the overload without password arguments.

1. Configure the permission flags with [DocumentPrivilege](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/documentprivilege/).
1. Create [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Apply document privileges with [PdfFileSecurity::SetPrivilege()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/setprivilege/).
1. Save the resulting PDF with [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/)::`Save()`.
1. Close the facade with [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/)::`Close()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/DocumentPrivilege.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileSecurity.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileSecurity
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void SetPdfPrivilegesWithoutPasswords(String inputFile, String outputFile)
{
    auto fileSecurity = MakeObject<PdfFileSecurity>();
    fileSecurity->BindPdf(inputFile);
    auto privilege = DocumentPrivilege::get_ForbidAll();
    privilege->set_AllowPrint(true);
    fileSecurity->SetPrivilege(privilege);
    fileSecurity->Save(outputFile);
    fileSecurity->Close();
}
} // namespace Facades::Examples::PDF_FileSecurity
```

## Try set PDF privileges without exception

Check TrySetPrivilege and save only when it returns true; otherwise print a diagnostic.

1. Configure the permission flags with [DocumentPrivilege](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/documentprivilege/).
1. Create [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Attempt the privilege update and check the result of [PdfFileSecurity::TrySetPrivilege()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/trysetprivilege/).
1. Save the PDF with [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/)::`Save()` only after the operation succeeds.
1. Close the facade with [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/)::`Close()`.
1. Print the results or diagnostic messages shown in the example.

```cpp
#include <Aspose.PDF.Cpp/Facades/DocumentPrivilege.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileSecurity.h>
#include <iostream>
#include <system/string.h>

namespace Facades::Examples::PDF_FileSecurity
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void TrySetPdfPrivilegesWithoutException(String inputFile, String outputFile)
{
    auto fileSecurity = MakeObject<PdfFileSecurity>();
    fileSecurity->BindPdf(inputFile);
    auto privilege = DocumentPrivilege::get_ForbidAll();
    privilege->set_AllowPrint(true);
    if (fileSecurity->TrySetPrivilege(u"user_password", u"owner_password", privilege))
    {
        fileSecurity->Save(outputFile);
    }
    else
    {
        std::cout << "Setting privileges failed. Check passwords or document state." << std::endl;
    }
    fileSecurity->Close();
}
} // namespace Facades::Examples::PDF_FileSecurity
```
