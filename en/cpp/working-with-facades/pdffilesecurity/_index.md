---
title: Manage PDF passwords and permissions in C++
linktitle: PdfFileSecurity Class
type: docs
weight: 110
url: /cpp/pdffilesecurity-class/
description: Encrypt and decrypt PDF files, change passwords, and apply document privileges with direct or Try methods using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Configure PDF Encryption and Permissions in C++
Abstract: Use PdfFileSecurity to encrypt, decrypt, and update passwords and document privileges. The examples include explicit encryption settings and Try methods that check success before saving.
---

Use [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/) to encrypt and decrypt PDF files, change passwords, and apply document privileges with direct or Try methods.

The passwords in these examples are fixture values. Substitute the passwords for your own input and output documents. Permission examples configure DocumentPrivilege; Try methods save only when the operation succeeds.

The snippets are independent example functions with their SDK includes and example namespaces. Configure the Aspose.PDF for C++ SDK, supply the input resources referenced by the sample, and choose writable output paths. The examples retain the source field names, page indexes, coordinates, and options.

## Change password and reset security

Change both passwords using the existing owner password and reset privileges to printing only with x128 key size.

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

## Encrypt PDF with encryption algorithm

Encrypt with AES, x256 key size, and printing allowed.

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

## Set PDF privileges with passwords

Set printing allowed and copying disabled using the supplied sample passwords.

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

## Try set PDF privileges without exception

Check TrySetPrivilege and save only when it returns true; otherwise print a diagnostic.

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
