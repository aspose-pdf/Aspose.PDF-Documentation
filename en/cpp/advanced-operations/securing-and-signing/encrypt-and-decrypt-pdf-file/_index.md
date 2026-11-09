---
title: Encrypt and decrypt PDF files in C++
linktitle: Encrypt and Decrypt PDF
type: docs
weight: 10
url: /cpp/set-privileges-encrypt-and-decrypt-pdf-file/
description: Set PDF permissions, encrypt or decrypt documents, change passwords, and test supplied password candidates using Aspose.PDF for C++.
lastmod: "2026-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Manage PDF Passwords, Encryption, and Permissions in C++
Abstract: Learn how to apply password encryption and document privileges with Aspose.PDF for C++. The examples also remove encryption, change passwords, and test a fixed list of candidate passwords.
---

## Encrypt a PDF with passwords

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Select [Permissions](https://reference.aspose.com/pdf/cpp/aspose.pdf/permissions/)::ExtractContent and [CryptoAlgorithm](https://reference.aspose.com/pdf/cpp/aspose.pdf/cryptoalgorithm/)::AESx128.
1. Call [Encrypt()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/encrypt/) with the sample user and owner passwords.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Permissions.h>
#include <Aspose.PDF.Cpp/Security/CryptoAlgorithm.h>

using namespace System;
using namespace Aspose::Pdf;

namespace SecuringAndSigning {

    void EncryptPdfFile(System::String inputFile, System::String outputFile)
    {
        auto document = MakeObject<Document>(inputFile);

        document->Encrypt(u"user", u"owner", Permissions::ExtractContent, CryptoAlgorithm::AESx128);
        document->Save(outputFile);
    }

}
```

## Set document privileges

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Start with [DocumentPrivilege](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/documentprivilege/)::get_ForbidAll().
1. Enable AllowScreenReaders.
1. Call [Encrypt()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/encrypt/) with the passwords, privileges, AESx128, and false for encryptMetadata.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/DocumentPrivilege.h>
#include <Aspose.PDF.Cpp/Security/CryptoAlgorithm.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

namespace SecuringAndSigning {

// Port of SecuringAndSigningExamples.setPrivilegesOnExistingPdfFile.
void SetPrivilegesOnExistingPdfFile(System::String inputFile, System::String outputFile)
{
    {
        auto document = MakeObject<Document>(inputFile);

        auto documentPrivilege = DocumentPrivilege::get_ForbidAll();
        documentPrivilege->set_AllowScreenReaders(true);
        document->Encrypt(u"user", u"owner", documentPrivilege, CryptoAlgorithm::AESx128, false);
        document->Save(outputFile);
    }
}

}
```

## Decrypt a PDF

The literal password must match the input PDF. The explicit System::String selects the password constructor overload.

1. Open the [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) using the sample password wrapped in System::String.
1. Call [Decrypt()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/decrypt/).
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Document.h>

using namespace System;
using namespace Aspose::Pdf;

namespace SecuringAndSigning
{

    void DecryptPdfFile(System::String inputFile, System::String outputFile)
    {
        auto document = MakeObject<Document>(inputFile, String(u"password"));

        document->Decrypt();
        document->Save(outputFile);
    }

}
```

## Change user and owner passwords

1. Open the [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) with the existing owner password.
1. Call [ChangePasswords()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/changepasswords/) with the old owner password and the new user and owner passwords.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Document.h>

using namespace System;
using namespace Aspose::Pdf;

namespace SecuringAndSigning
{

    void ChangePassword(System::String inputFile, System::String outputFile)
    {

        auto document = MakeObject<Document>(inputFile, String(u"owner"));
        document->ChangePasswords(u"owner", u"newuser", u"newowner");
        document->Save(outputFile);
    }
}
```

## Test a fixed list of passwords

This sample logs candidate passwords. Its broad exception handler labels every caught System::Exception as an incorrect password, even when another error caused the failure.

1. Create [PdfFileInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileinfo/), print IsEncrypted, and close the facade.
1. Iterate through the supplied password candidates.
1. Attempt to open the [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) with each candidate.
1. Print the successful password and page count when at least one page is available.
1. Catch System::Exception and continue to the next candidate.

```cpp
#include <iostream>
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileInfo.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

namespace SecuringAndSigning
{

    void DetermineCorrectPasswordFromArray(System::String inputFile)
    {
        auto pdfFileInfo = MakeObject<PdfFileInfo>(inputFile);
        {
            std::cout << "File is password protected " << pdfFileInfo->get_IsEncrypted() << std::endl;

            pdfFileInfo->Close();
        }

        const String passwords[] = {u"test", u"test1", u"test2", u"test3", u"sample"};

        for (const auto &password : passwords)
        {
            try
            {
                auto document = MakeObject<Document>(inputFile, password);

                if (document->get_Pages()->get_Count() > 0)
                {
                    std::cout << "Password = " << password << " is correct" << std::endl;
                    std::cout << "Number of pages in document = " << document->get_Pages()->get_Count() << std::endl;
                    break;
                }
            }
            catch (const System::Exception &)
            {
                std::cout << "Password = " << password << " is not correct" << std::endl;
            }
        }
    }

}
```

## Password encryption in the PubSecEncryption sample

Despite its name, this function does not perform public-key encryption. The certificate parameters are only printed; they are not used to encrypt or decrypt the PDF.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) with metadata and a text page.
1. Call [Encrypt()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/encrypt/) with user and owner passwords, PrintDocument permissions, and the supplied algorithm.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).
1. Reopen the output with the user password and print its metadata and extracted text.
1. Call [Decrypt()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/decrypt/) and save pubsec_decrypted_out.pdf.
1. Print the certificate filenames and sample password.

```cpp
#include <iostream>
#include <system/exceptions.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/io/stream.h>
#include <system/io/path.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/DocumentInfo.h>
#include <Aspose.PDF.Cpp/Generator/Drawing/Path.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Permissions.h>
#include <Aspose.PDF.Cpp/Text/TextAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

namespace SecuringAndSigning {

// Port of SecuringAndSigningExamples.pubSecEncryption.
void PubSecEncryption(CryptoAlgorithm cryptoAlgorithm, System::String publicCertificate, System::String inputPfx, System::String outputFile)
{
    String pfxPassword = u"12345";

    {
        auto document = MakeObject<Document>();

        document->get_Info()->set_Title(u"TestTitle");
        document->get_Info()->set_Author(u"TestAuthor");
        auto page = document->get_Pages()->Add();
        page->get_Paragraphs()->Add(MakeObject<TextFragment>(u"Hello World!"));

        document->Encrypt(u"user", u"owner", Permissions::PrintDocument, cryptoAlgorithm);
        document->Save(outputFile);
    }

    {
        auto document = MakeObject<Document>(outputFile, String(u"user"));

        std::cout << document->get_Info()->get_Title() << std::endl;
        std::cout << document->get_Info()->get_Author() << std::endl;

        auto textAbsorber = MakeObject<TextAbsorber>();
        document->get_Pages()->idx_get(1)->Accept(textAbsorber);
        std::cout << textAbsorber->get_Text() << std::endl;

        document->Decrypt();
        document->Save(System::IO::Path::Combine(System::IO::Path::GetDirectoryName(outputFile), u"pubsec_decrypted_out.pdf"));
    }

    std::cout << "Used certificate files: " << System::IO::Path::GetFileName(publicCertificate)
    << ", " << System::IO::Path::GetFileName(inputPfx) << " with password " << pfxPassword << std::endl;
}

}
```
