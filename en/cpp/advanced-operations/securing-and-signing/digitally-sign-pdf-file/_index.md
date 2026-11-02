---
title: Digitally sign PDF files in C++
linktitle: Digitally Sign PDF
type: docs
weight: 20
url: /cpp/digitally-sign-pdf-file/
description: Sign PDF files with PKCS#7 or detached signatures and configure a timestamp server using Aspose.PDF for C++.
lastmod: "2026-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Apply PDF Digital Signatures and Timestamps in C++
Abstract: Learn how to sign the first PDF page using PFX credentials and Aspose.PDF for C++. The examples cover PKCS#7, detached SHA-256 signatures, an ECDSA sample, and timestamp settings.
---

## Sign with PKCS#7

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/) facade for the document.
1. Load [PKCS7](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/pkcs7/) from the PFX file with the sample password 12345.
1. Call [Sign()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/sign/) for page 1 with a visible signature rectangle.
1. Save the signed PDF with [PdfFileSignature::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/save/).

```cpp
#include <system/exceptions.h>
#include <drawing/rectangle.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/PKCS7.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Facades;

namespace SecuringAndSigning {

// Port of SecuringAndSigningExamples.signDocument.
void SignDocument(System::String inputFile, System::String outputFile, System::String pfxFile)
{
    {
        auto document = MakeObject<Document>(inputFile);
        auto signature = MakeObject<PdfFileSignature>(document);

        auto pkcs = MakeObject<PKCS7>(pfxFile, u"12345");
        signature->Sign(1, true, System::Drawing::Rectangle(300, 100, 400, 200), pkcs);
        signature->Save(outputFile);
    }
}

}
```

## Sign with a detached SHA-256 signature

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/) facade for the document.
1. Create [PKCS7Detached](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/pkcs7detached/) from the PFX path and password with [DigestHashAlgorithm](https://reference.aspose.com/pdf/cpp/aspose.pdf/digesthashalgorithm/)::Sha256.
1. Call [Sign()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/sign/) for page 1 with the supplied visible rectangle.
1. Save the signed PDF with [PdfFileSignature::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/save/).

```cpp
#include <system/exceptions.h>
#include <drawing/rectangle.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/PKCS7Detached.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Security/DigestHashAlgorithm.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Facades;

namespace SecuringAndSigning {

// Port of SecuringAndSigningExamples.signDocumentPkcs7Detached.
void SignDocumentPkcs7Detached(System::String inputFile, System::String outputFile, System::String pfxFile, System::String password)
{
    {
        auto document = MakeObject<Document>(inputFile);
        auto signature = MakeObject<PdfFileSignature>(document);

        auto pkcs = MakeObject<PKCS7Detached>(pfxFile, password, DigestHashAlgorithm::Sha256);
        signature->Sign(1, true, System::Drawing::Rectangle(300, 100, 400, 200), pkcs);
        signature->Save(outputFile);
    }
}

}
```

## ECDSA signing sample

The supplied README reports that SDK 26.7.0 rejected algorithm 1.2.840.10045.2.1 when running this example. The source calls are preserved; confirm support in your SDK before using this workflow.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/) facade for the document.
1. Load the supplied ECDSA PFX into [PKCS7Detached](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/pkcs7detached/) with SHA-256.
1. Call [Sign()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/sign/) for page 1.
1. Save the signed PDF with [PdfFileSignature::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/save/).

```cpp
#include <system/exceptions.h>
#include <drawing/rectangle.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/PKCS7Detached.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Security/DigestHashAlgorithm.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Facades;

namespace SecuringAndSigning {

// Port of SecuringAndSigningExamples.signEcdsa.
void SignEcdsa(System::String inputFile, System::String outputFile, System::String pfxFile, System::String password)
{
    {
        auto document = MakeObject<Document>(inputFile);
        auto signature = MakeObject<PdfFileSignature>(document);

        auto pkcs = MakeObject<PKCS7Detached>(pfxFile, password, DigestHashAlgorithm::Sha256);
        signature->Sign(1, true, System::Drawing::Rectangle(300, 100, 400, 200), pkcs);
        signature->Save(outputFile);
    }
}

}
```

## Sign using a timestamp server

Running this example contacts https://freetsa.org/tsr. It requires network access and a reachable timestamp service; the documentation-generation checks do not contact that service.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/) facade for the document.
1. Create a [PKCS7](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/pkcs7/) signature using the PFX path and password.
1. Assign [TimestampSettings](https://reference.aspose.com/pdf/cpp/aspose.pdf/timestampsettings/) using the sample server URL and SHA-256.
1. Call [Sign()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/sign/) for page 1 with the supplied reason, contact, location, and rectangle.
1. Save the signed PDF with [PdfFileSignature::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/save/).

```cpp
#include <system/exceptions.h>
#include <drawing/rectangle.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/PKCS7.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Signature.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/TimestampSettings.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Security/DigestHashAlgorithm.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Facades;

namespace SecuringAndSigning
{

    void SignWithTimeStampServer(System::String inputFile, System::String outputFile, System::String pfxFile, System::String password)
    {
        {
            auto document = MakeObject<Document>(inputFile);
            auto signature = MakeObject<PdfFileSignature>(document);

            auto pkcs = MakeObject<PKCS7>(pfxFile, password);
            pkcs->set_TimestampSettings(MakeObject<TimestampSettings>(u"https://freetsa.org/tsr", u"", DigestHashAlgorithm::Sha256));
            signature->Sign(1, u"Signature Reason", u"Contact", u"Location", true,
                            System::Drawing::Rectangle(100, 100, 200, 100), pkcs);
            signature->Save(outputFile);
        }
    }

}
```
