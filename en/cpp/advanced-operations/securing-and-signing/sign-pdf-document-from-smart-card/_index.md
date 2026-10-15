---
title: Sign PDFs with local certificates and smart cards in C++
linktitle: Local Certificates and Smart Cards
type: docs
weight: 50
url: /cpp/sign-pdf-document-from-smart-card/
description: Review the supplied local-certificate helper and the unsigned fallback behavior of signature-field and smart-card examples in Aspose.PDF for C++.
lastmod: "2026-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Integrate Certificate Selection into PDF Signing Examples in C++
Abstract: Review how the samples would use a selected certificate through ExternalSignature in Aspose.PDF for C++. The supplied certificate-selection helper returns nullptr, so the examples take their unsigned fallback paths until certificate selection is implemented.
---

## Certificate-selection placeholder

This is a placeholder, not an implementation that reads a certificate store or communicates with a smart card.

1. Inspect GetLocalCertificate() in the SecuringAndSigning namespace.
1. Observe that the helper returns nullptr.
1. Provide an application-specific certificate-selection implementation before expecting the dependent examples to sign a PDF.

```cpp
namespace SecuringAndSigning {

// Placeholder retained from SecuringAndSigningExamples.getLocalCertificate.
System::SharedPtr<System::Security::Cryptography::X509Certificates::X509Certificate2> GetLocalCertificate()
{
    return nullptr;
}

}
```

## Create a signature field with a certificate fallback

Despite its function name, this sample creates a signature field rather than extracting existing signature information. With the supplied helper, it saves an unsigned field.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [SignatureField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/signaturefield/) on page 1 using an Aspose::Pdf::Rectangle.
1. Call GetLocalCertificate().
1. When no certificate is returned, add the unsigned field, save the PDF, and return.
1. When a certificate is available, create an [ExternalSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/externalsignature/) and configure its properties.
1. Name and add the field, call its [Sign()](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/signaturefield/) method, and save the PDF.

```cpp
#include <iostream>
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/WidgetAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/ExternalSignature.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Field.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Form.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Signature.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/SignatureField.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

namespace SecuringAndSigning {

// Port of SecuringAndSigningExamples.getSignatureInfoUsingSignatureField.
void GetSignatureInfoUsingSignatureField(System::String inputFile, System::String outputFile)
{
    {
        auto document = MakeObject<Document>(inputFile);

        auto signatureField = MakeObject<SignatureField>(
        document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(100, 400, 110, 410, true));
        auto selectedCertificate = GetLocalCertificate();
        if (selectedCertificate == nullptr) {
            std::cout << "Local certificate was not found." << std::endl;
            document->get_Form()->Add(signatureField, 1);
            document->Save(outputFile);
            return;
        }

        auto externalSignature = MakeObject<ExternalSignature>(selectedCertificate);
        externalSignature->set_Authority(u"Me");
        externalSignature->set_Reason(u"Reason");
        externalSignature->set_ContactInfo(u"Contact");
        signatureField->set_PartialName(u"sig1");
        document->get_Form()->Add(signatureField, 1);
        signatureField->Sign(externalSignature);
        document->Save(outputFile);
    }
}

}
```

## Smart-card example with an unsigned fallback

The supplied code does not select or access a smart card. Implement certificate selection and make its private-key provider available before expecting a signed output.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/) facade for the document.
1. Call GetLocalCertificate().
1. When the helper returns nullptr, print a message, save an unsigned PDF, and return.
1. When a certificate is available, create an [ExternalSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/externalsignature/).
1. Set the PNG signature appearance, call [Sign()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/sign/), and save through [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/).

```cpp
#include <iostream>
#include <system/exceptions.h>
#include <drawing/rectangle.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/ExternalSignature.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Facades;

namespace SecuringAndSigning {

// Port of SecuringAndSigningExamples.signWithSmartCard.
void SignWithSmartCard(System::String inputFile, System::String outputFile, System::String pngFile)
{
    {
        auto document = MakeObject<Document>(inputFile);
        auto pdfSignature = MakeObject<PdfFileSignature>(document);

        auto selectedCertificate = GetLocalCertificate();
        if (selectedCertificate == nullptr) {
            std::cout << "Local certificate was not found." << std::endl;
            document->Save(outputFile);
            return;
        }

        auto externalSignature = MakeObject<ExternalSignature>(selectedCertificate);
        pdfSignature->set_SignatureAppearance(pngFile);
        pdfSignature->Sign(1, u"Reason", u"Contact", u"Location", true,
        System::Drawing::Rectangle(100, 100, 200, 200), externalSignature);
        pdfSignature->Save(outputFile);
    }
}

}
```
