---
title: Verify PDF digital signatures in C++
linktitle: Verify Digital Signatures
type: docs
weight: 30
url: /cpp/verify-digital-signatures/
description: Verify PDF signatures, check certificate validation results, and inspect known signature-compromise indicators using Aspose.PDF for C++.
lastmod: "2026-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Check PDF Signatures, Certificates, and Signature Coverage in C++
Abstract: Learn how to verify PDF signatures with Aspose.PDF for C++ and inspect certificate validation results. The examples include public-certificate verification, ECDSA checks, and a detector for known signature-compromise methods.
---

## Verify signatures returned by the facade

The loop does not explicitly reject a document with no returned signature names. Function completion alone does not establish that the PDF contains a valid signature.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/) facade for the document.
1. Enumerate [GetSignatureNames(false)](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/).
1. Call [VerifySignature()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/verifysignature/) for each returned name.
1. Throw an exception when verification returns false.

```cpp
#include <stdexcept>
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

namespace SecuringAndSigning
{

    void Verify(System::String inputFile)
    {
        {
            auto document = MakeObject<Document>(inputFile);
            auto signature = MakeObject<PdfFileSignature>(document);

            for (const auto &signatureName : signature->GetSignatureNames(false))
            {
                if (!signature->VerifySignature(signatureName))
                {
                    throw std::runtime_error("Not verified");
                }
            }
        }
    }

}
```

## Verify an externally signed PDF

An empty signature-name collection causes no verification calls. This example does not explicitly require at least one signature.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/) facade for the document.
1. Enumerate [GetSignatureNames(true)](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/).
1. Call [VerifySignature()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/verifysignature/) for every returned name.
1. Throw an exception for a false result.

```cpp
#include <stdexcept>
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

namespace SecuringAndSigning
{

    void VerifyExternalSignature(System::String inputFile)
    {
        {
            auto document = MakeObject<Document>(inputFile);
            auto pdfSignature = MakeObject<PdfFileSignature>(document);

            for (const auto &signatureName : pdfSignature->GetSignatureNames(true))
            {
                if (!pdfSignature->VerifySignature(signatureName))
                {
                    throw std::runtime_error("Not verified");
                }
            }
        }
    }

}
```

## Verify an ECDSA signature

The supplied README reports that SDK 26.7.0 rejected algorithm 1.2.840.10045.4.3.2 in this example. Treat this as source-reported compatibility information rather than a result from a local documentation check.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/) facade for the document.
1. Call [ContainsSignature()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/) and throw when no signature exists.
1. Enumerate [GetSignatureNames(true)](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/).
1. Call [VerifySignature()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/verifysignature/) and throw for a false result.

```cpp
#include <stdexcept>
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

namespace SecuringAndSigning
{

    void VerifyEcdsa(System::String inputFile)
    {
        {
            auto document = MakeObject<Document>(inputFile);
            auto signature = MakeObject<PdfFileSignature>(document);

            if (!signature->ContainsSignature())
            {
                throw std::runtime_error("Document does not contain a signature");
            }

            for (const auto &signatureName : signature->GetSignatureNames(true))
            {
                if (!signature->VerifySignature(signatureName))
                {
                    throw std::runtime_error("Not verified");
                }
            }
        }
    }

}
```

## Verify with certificate checks

Certificate-chain and revocation checks can require network access. Inspect both the returned Boolean and the validation status; finishing without an exception is not a successful-verification result.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/) facade for the document.
1. Enumerate the signature names.
1. Create [ValidationOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.security/validationoptions/) with Strict mode, Auto method, certificate-chain checking, and a 20000-millisecond timeout.
1. Call [VerifySignature()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/verifysignature/) with the options and an output [ValidationResult](https://reference.aspose.com/pdf/cpp/aspose.pdf.security/validationresult/).
1. Print the validation status when present and the verification Boolean.

```cpp
#include <iostream>
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>
#include <Aspose.PDF.Cpp/Security/CertificateValidation/ValidationMethod.h>
#include <Aspose.PDF.Cpp/Security/CertificateValidation/ValidationMode.h>
#include <Aspose.PDF.Cpp/Security/CertificateValidation/ValidationOptions.h>
#include <Aspose.PDF.Cpp/Security/CertificateValidation/ValidationResult.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using namespace Aspose::Pdf::Security;

namespace SecuringAndSigning
{

    void VerifySignatureWithCertificateCheck(System::String inputFile)
    {
        {
            auto document = MakeObject<Document>(inputFile);
            auto signature = MakeObject<PdfFileSignature>(document);

            for (const auto &signatureName : signature->GetSignatureNames(true))
            {
                auto options = MakeObject<ValidationOptions>();
                options->set_ValidationMode(ValidationMode::Strict);
                options->set_ValidationMethod(ValidationMethod::Auto);
                options->set_CheckCertificateChain(true);
                options->set_RequestTimeout(20000);
                SharedPtr<ValidationResult> validationResult;
                bool verified = signature->VerifySignature(signatureName, options, validationResult);
                if (validationResult != nullptr)
                {
                    std::cout << "Certificate validation result: " << static_cast<int>(validationResult->get_Status()) << std::endl;
                }
                std::cout << "Is verified: " << verified << std::endl;
            }
        }
    }

}
```

## Verify using a supplied public certificate

The document must have at least one returned signature name. This overload uses the supplied certificate; the sample does not configure the strict validation options from the previous example.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/) facade for the document.
1. Select signature-name index 0.
1. Read the certificate file into an [X509Certificate2](https://reference.aspose.com/pdf/cpp/system.security.cryptography.x509certificates/x509certificate2/).
1. Call [VerifySignature()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/verifysignature/) with the selected name and certificate.
1. Print the returned Boolean.

```cpp
#include <iostream>
#include <system/exceptions.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/io/stream.h>
#include <system/io/path.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>
#include <Aspose.PDF.Cpp/Facades/SignatureName.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using namespace System::Security::Cryptography::X509Certificates;

namespace SecuringAndSigning
{

    void VerifyWithPublicKeyCertificate(System::String certificate, System::String inputFile)
    {
        {
            auto document = MakeObject<Document>(inputFile);
            auto fileSign = MakeObject<PdfFileSignature>(document);

            auto signatureName = fileSign->GetSignatureNames(true)->idx_get(0);
            auto certificate2 =
                MakeObject<X509Certificate2>(
                    System::IO::File::ReadAllBytes(certificate));
            std::cout << fileSign->VerifySignature(signatureName, certificate2) << std::endl;
        }
    }

}
```

## Extract a certificate and then verify

The extracted certificate stream is not passed to VerifySignature(). This sample uses the signature-name-only overload after extraction and does not independently establish trust in the extracted certificate.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/) facade for the document.
1. Select signature-name index 0.
1. Call [TryExtractCertificate()](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/signaturefield/) and print its success message when extraction succeeds.
1. Call [VerifySignature()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/verifysignature/) for the selected name, or print false when extraction fails.

```cpp
#include <iostream>
#include <system/exceptions.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/io/stream.h>
#include <system/io/path.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>
#include <Aspose.PDF.Cpp/Facades/SignatureName.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

namespace SecuringAndSigning
{

    void VerifyWithPublicKeyCertificateFromSignature(System::String inputFile)
    {
        {
            auto document = MakeObject<Document>(inputFile);
            auto fileSign = MakeObject<PdfFileSignature>(document);

            auto signatureName = fileSign->GetSignatureNames(true)->idx_get(0);
            SharedPtr<System::IO::Stream> certificate;
            if (fileSign->TryExtractCertificate(signatureName, certificate))
            {
                std::cout << "The certificate extraction succeeded" << std::endl;
                std::cout << fileSign->VerifySignature(signatureName) << std::endl;
            }
            else
            {
                std::cout << false << std::endl;
            }
        }
    }

}
```

## Check known signature-compromise indicators

The detector checks known compromise methods. A result with no detected compromise is not a guarantee against unknown methods; see the API reference for the detector's scope.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [SignaturesCompromiseDetector](https://reference.aspose.com/pdf/cpp/aspose.pdf/signaturescompromisedetector/).
1. Call [Check()](https://reference.aspose.com/pdf/cpp/aspose.pdf/signaturescompromisedetector/) with an output CompromiseCheckResult.
1. Return when [Check()](https://reference.aspose.com/pdf/cpp/aspose.pdf/signaturescompromisedetector/) reports no detected compromise.
1. Otherwise, print compromised signature names and the signature-coverage classification.

```cpp
#include <iostream>
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/SignatureName.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Signature.h>
#include <Aspose.PDF.Cpp/Security/Impl/Signatures/Sanitization/CompromiseCheckResult.h>
#include <Aspose.PDF.Cpp/Security/Impl/Signatures/Sanitization/SignaturesCompromiseDetector.h>
#include <Aspose.PDF.Cpp/Security/Impl/Signatures/Sanitization/SignaturesCoverage.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Signatures;

namespace SecuringAndSigning
{

    void Check(System::String inputFile)
    {

        auto document = MakeObject<Document>(inputFile);
        auto detector = MakeObject<SignaturesCompromiseDetector>(document);
        SharedPtr<CompromiseCheckResult> result;

        if (detector->Check(result))
        {
            std::cout << "No signature compromise detected" << std::endl;
            return;
        }

        if (result->get_HasCompromisedSignatures())
        {
            std::cout << "Count of compromised signatures: " << result->CompromisedSignatures->get_Count() << std::endl;
            for (const auto &signatureName : result->CompromisedSignatures)
            {
                std::cout << "Signature name: " << signatureName->FullName << std::endl;
            }
        }

        switch (result->get_SignaturesCoverage())
        {
        case SignaturesCoverage::EntirelySigned:
            std::cout << "All signatures are covered" << std::endl;
            break;
        case SignaturesCoverage::PartiallySigned:
            std::cout << "Some signatures are covered" << std::endl;
            break;
        case SignaturesCoverage::Undefined:
        {
            std::cout << "Unknown or undefined signatures coverage" << std::endl;
            break;
        }
        default:
        {
            std::cout << "Unknown signatures coverage" << std::endl;
            break;
        }
        }
    }
}
```
