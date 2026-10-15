---
title: Encrypt and decrypt PDF files in C++
linktitle: Encrypt and decrypt PDF files
type: docs
weight: 70
url: /cpp/protect-pdf-file/
description: Encrypt and decrypt PDFs in C++, set permissions, change passwords, and check password protection.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Manage PDF Encryption, Permissions, and Passwords in C++
Abstract: Learn how to encrypt and decrypt PDF files with Aspose.PDF for C++ and configure document permissions. The examples also change user and owner passwords, inspect encryption, and test candidate passwords.
---

Manage PDF encryption and passwords through the [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) API.

A user password is used to open a protected document. An owner password controls access to restricted operations. The sample password constants below illustrate API usage; supply your own password values for your documents.

## Encrypt a PDF with restricted permissions

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Forbid all operations with [DocumentPrivilege::get_ForbidAll()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/documentprivilege/).
1. Enable screen reader access on the [DocumentPrivilege](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/documentprivilege/) object.
1. Call [Encrypt()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/encrypt/) with user and owner passwords, the privileges, and [CryptoAlgorithm](https://reference.aspose.com/pdf/cpp/aspose.pdf/cryptoalgorithm/) set to AESx128.
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Security/CryptoAlgorithm.h>
#include <Aspose.PDF.Cpp/Facades/DocumentPrivilege.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileInfo.h>

constexpr auto USER_PASSWORD = u"userpassword";
constexpr auto OWNER_PASSWORD = u"ownerpassword";

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void EncryptPassword(System::String path_infile, System::String path_outfile)
{
    const auto document = MakeObject<Document>(path_infile);

    auto documentPrivilege = DocumentPrivilege::get_ForbidAll();
    documentPrivilege->set_AllowScreenReaders(true);

    document->Encrypt(
        USER_PASSWORD,
        OWNER_PASSWORD,
        documentPrivilege,
        CryptoAlgorithm::AESx128,
        false);
    document->Save(path_outfile);
}
```

## Encrypt a PDF with all permissions allowed

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Allow all operations with [DocumentPrivilege::get_AllowAll()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/documentprivilege/).
1. Call [Encrypt()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/encrypt/) with user and owner passwords, the privileges, and [CryptoAlgorithm](https://reference.aspose.com/pdf/cpp/aspose.pdf/cryptoalgorithm/) set to RC4x128.
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Security/CryptoAlgorithm.h>
#include <Aspose.PDF.Cpp/Facades/DocumentPrivilege.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileInfo.h>

constexpr auto USER_PASSWORD = u"userpassword";
constexpr auto OWNER_PASSWORD = u"ownerpassword";

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void EncryptPdfFile(String path_infile, String path_outfile) {
    const auto document = MakeObject<Document>(path_infile);
    document->Encrypt(
        USER_PASSWORD,
        OWNER_PASSWORD,
        DocumentPrivilege::get_AllowAll(),
        CryptoAlgorithm::RC4x128,
        false);
    document->Save(path_outfile);
}
```

## Decrypt a PDF

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) using its user password.
1. Remove encryption with [Decrypt()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Save the unencrypted document with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Security/CryptoAlgorithm.h>
#include <Aspose.PDF.Cpp/Facades/DocumentPrivilege.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileInfo.h>

constexpr auto USER_PASSWORD = u"userpassword";
constexpr auto OWNER_PASSWORD = u"ownerpassword";

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void DecryptPdfFile(String path_infile, String path_outfile) {
    const auto document = MakeObject<Document>(path_infile, USER_PASSWORD);
    document->Decrypt();
    document->Save(path_outfile);
}
```

## Change user and owner passwords

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) using the current owner password.
1. Call [ChangePasswords()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) with the current owner password, the new user password, and the new owner password.
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Security/CryptoAlgorithm.h>
#include <Aspose.PDF.Cpp/Facades/DocumentPrivilege.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileInfo.h>

constexpr auto USER_PASSWORD = u"userpassword";
constexpr auto OWNER_PASSWORD = u"ownerpassword";

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ChangePassword(String path_infile, String path_outfile) {
    const auto document = MakeObject<Document>(path_infile, OWNER_PASSWORD);
    document->ChangePasswords(OWNER_PASSWORD, u"newuser", u"newowner");
    document->Save(path_outfile);

}
```

## Check encryption and test candidate passwords

1. Check whether the file is encrypted with [PdfFileInfo::get_IsEncrypted()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/get_isencrypted/).
1. Create a list of candidate passwords.
1. For each candidate, open a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) inside the try block.
1. Read the page count with [PageCollection::get_Count()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/get_count/).
1. Report the candidate as correct if the document contains at least one page.
1. Catch [InvalidPasswordException](https://reference.aspose.com/pdf/cpp/aspose.pdf/) and report an incorrect candidate.

```cpp
#include <iostream>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Security/CryptoAlgorithm.h>
#include <Aspose.PDF.Cpp/Facades/DocumentPrivilege.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileInfo.h>
#include <Aspose.PDF.Cpp/Exceptions/InvalidPasswordException.h>

constexpr auto USER_PASSWORD = u"userpassword";
constexpr auto OWNER_PASSWORD = u"ownerpassword";

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void DetermineCorrectPasswordFromList(String path_infile) {
    const auto info = MakeObject<PdfFileInfo>(path_infile);

    std::cout << "File is password protected: " << info->get_IsEncrypted() << std::endl;

    auto passwords = MakeArray<String>({ u"test", u"test1", u"test2", u"test3", USER_PASSWORD });
    for (auto& password : passwords) {

        try {
            const auto document = MakeObject<Document>(path_infile, password);
            int pageCount = document->get_Pages()->get_Count();
            if (pageCount > 0) {
                std::cout << "Password '" << password << "' is correct. Pages: " << pageCount << std::endl;
            }
        }

        catch (InvalidPasswordException& ex) {
            std::cout << "Wrong password: " << password << std::endl;
        }
    }
}
```
