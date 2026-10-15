---
title: Extract PDF signature information in C++
linktitle: Extract Signature Information
type: docs
weight: 40
url: /cpp/extract-image-and-signature-information/
description: Read signature algorithm details, extract a certificate or signature appearance image, and check certificate extraction using Aspose.PDF for C++.
lastmod: "2026-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Read PDF Signature Details and Export Signature Resources in C++
Abstract: Learn how to inspect signature information and extract resources from PDF signature fields with Aspose.PDF for C++. The examples save the first available certificate or appearance image and show a separate certificate-extraction success check.
---

## Print signature algorithm information

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/) facade for the document.
1. Call [GetSignaturesInfo()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/).
1. Print ToString() for each returned information object.

```cpp
#include <iostream>
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>
#include <Aspose.PDF.Cpp/Security/SignatureAlgorithmInfo.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

namespace SecuringAndSigning {

// Port of SecuringAndSigningExamples.getSignaturesInfo.
void GetSignaturesInfo(System::String inputFile)
{
    {
        auto document = MakeObject<Document>(inputFile);
        auto signature = MakeObject<PdfFileSignature>(document);

        for (const auto& signatureInfo : signature->GetSignaturesInfo()) {
            std::cout << signatureInfo->ToString() << std::endl;
        }
    }
}

}
```

## Save a certificate from a signature field

The function can finish without creating a file if no field supplies a certificate. It saves only the first available result.

1. Open the [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) with the sample owner password.
1. Iterate through the form fields and select [SignatureField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/signaturefield/) objects.
1. Call [ExtractCertificate()](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/signaturefield/) and skip null streams.
1. Copy the first available certificate stream to outputFile, close the output, and return.

```cpp
#include <system/exceptions.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/io/stream.h>
#include <system/io/path.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/WidgetAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Field.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Form.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/SignatureField.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

namespace SecuringAndSigning {

// Port of SecuringAndSigningExamples.extractCertificate.
void ExtractCertificate(System::String inputFile, System::String outputFile)
{
    {
        auto document = MakeObject<Document>(inputFile, String(u"owner"));

        for (const auto& field : document->get_Form()) {
            if (!System::DynamicCast_noexcept<SignatureField>(field)) {
                continue;
            }

            auto signatureField = System::DynamicCast<SignatureField>(field);
            {
                auto certificateStream = signatureField->ExtractCertificate();

                if (certificateStream == nullptr) {
                    continue;
                }
                auto output = System::IO::File::Create(outputFile);
                certificateStream->CopyTo(output);
                output->Close();
                return;
            }
        }
    }
}

}
```

## Check certificate extraction

This sample receives a certificate stream but does not write it to a file.

1. Open the [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) with the sample owner password.
1. Create a [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/) facade for the document.
1. Enumerate the signature names.
1. Call Try[ExtractCertificate()](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/signaturefield/) for each name.
1. Print a message when extraction succeeds.

```cpp
#include <iostream>
#include <system/exceptions.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/io/stream.h>
#include <system/io/path.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

namespace SecuringAndSigning {

// Port of SecuringAndSigningExamples.extractCertificateTryExtractCertificateMethod.
void ExtractCertificateTryExtractCertificateMethod(System::String inputFile)
{
    {
        auto document = MakeObject<Document>(inputFile, String(u"owner"));
        auto signature = MakeObject<PdfFileSignature>(document);

        for (const auto& signatureName : signature->GetSignatureNames(true)) {
            SharedPtr<System::IO::Stream> certificate;
            if (signature->TryExtractCertificate(signatureName, certificate)) {
                std::cout << "The certificate extraction succeeded" << std::endl;
            }
        }
    }
}

}
```

## Save a signature appearance image

An appearance image is a visual signature resource, not proof of cryptographic validity. No file is created when no matching image stream is found.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Iterate through form fields and select [SignatureField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/signaturefield/) objects.
1. Call [ExtractImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/signaturefield/) with JPEG format and skip null streams.
1. Copy the first available image stream to outputFile, close the output, and return.

```cpp
#include <system/exceptions.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/io/stream.h>
#include <system/io/path.h>
#include <drawing/imaging/image_format.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/WidgetAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Field.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Form.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/SignatureField.h>
#include <Aspose.PDF.Cpp/Presentation/IndependentImpl/ImageFormat.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

namespace SecuringAndSigning {

// Port of SecuringAndSigningExamples.extractImagesFromSignatureField.
void ExtractImagesFromSignatureField(System::String inputFile, System::String outputFile)
{
    {
        auto document = MakeObject<Document>(inputFile);

        for (const auto& field : document->get_Form()) {
            if (!System::DynamicCast_noexcept<SignatureField>(field)) {
                continue;
            }

            auto signatureField = System::DynamicCast<SignatureField>(field);
            {
                auto imageStream = signatureField->ExtractImage(System::Drawing::Imaging::ImageFormat::get_Jpeg());

                if (imageStream == nullptr) {
                    continue;
                }
                auto output = System::IO::File::Create(outputFile);
                imageStream->CopyTo(output);
                output->Close();
                return;
            }
        }
    }
}

}
```
