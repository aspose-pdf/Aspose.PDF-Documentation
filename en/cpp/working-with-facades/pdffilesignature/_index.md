---
title: Sign and inspect PDF signatures in C++
linktitle: PdfFileSignature Class
type: docs
weight: 120
url: /cpp/pdffilesignature-class/
description: Sign or certify PDF documents, inspect and verify signatures, extract certificates, and remove a signature using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create and Inspect PDF Digital Signatures in C++
Abstract: Use PdfFileSignature to sign PDFs with a certificate or certify them with modification permissions. Other examples inspect signature details, verify integrity and coverage, extract a certificate, and remove a signature.
---

Use [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/) to sign or certify PDF documents, inspect and verify signatures, extract certificates, and remove a signature.

Signing examples require a certificate file using the sample password Aspose2021. Inspection, extraction, verification, and removal examples select the first existing signature, so a signed input PDF is required. Use the appropriate certificate and password for your documents.

The snippets are independent example functions with their SDK includes and example namespaces. Configure the Aspose.PDF for C++ SDK, supply the input resources referenced by the sample, and choose writable output paths. The examples retain the source field names, page indexes, coordinates, and options.

## Certify PDF with mdp signature

Create a PKCS7 signature and certify page 1 with FillingInForms modification permissions and a visible signature.

1. Load the certificate and configure a [PKCS7](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/pkcs7/) signature object.
1. Set the certification permissions with [DocMDPSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/docmdpsignature/).
1. Create [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Apply the certification signature with [PdfFileSignature::Certify()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/certify/).
1. Save the resulting PDF with [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/DocMDPAccessPermissions.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/DocMDPSignature.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/PKCS7.h>
#include <drawing/rectangle.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileSignature
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Facades;
	using PKCS7 = Aspose::Pdf::Forms::PKCS7;
	using DocMDPSignature = Aspose::Pdf::Forms::DocMDPSignature;
	using DocMDPAccessPermissions = Aspose::Pdf::Forms::DocMDPAccessPermissions;

	void CertifyPdfWithMdpSignature(String inputFile, String certificateFile, String outputFile)
	{
		auto certificateSignature = MakeObject<PKCS7>(certificateFile, u"Aspose2021");
		certificateSignature->set_Reason(u"Certified for form filling and signing");
		certificateSignature->set_ContactInfo(u"qa@example.com");
		certificateSignature->set_Location(u"New York, USA");
		certificateSignature->set_Authority(u"Aspose.PDF Example");

		auto pdfSignature = MakeObject<PdfFileSignature>();
		pdfSignature->BindPdf(inputFile);
		auto signature = MakeObject<DocMDPSignature>(certificateSignature, DocMDPAccessPermissions::FillingInForms);
		pdfSignature->Certify(1, u"Certified for form filling and signing", u"security@example.com", u"New York, USA", true,
			System::Drawing::Rectangle(10, 10, 200, 60), signature);
		pdfSignature->Save(outputFile);
	}
} // namespace Facades::Examples::PDF_FileSignature
```

## Extract signature certificate

Extract the certificate for the first signature and copy it to outputFile.

1. Create [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Read signature identifiers with [PdfFileSignature::GetSignatureNames()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/getsignaturenames/).
1. Extract the certificate stream with [PdfFileSignature::ExtractCertificate()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/extractcertificate/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>
#include <Aspose.PDF.Cpp/Facades/SignatureName.h>
#include <system/collections/ilist.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileSignature
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ExtractSignatureCertificate(String inputFile, String outputFile)
{
    auto pdfSignature = MakeObject<PdfFileSignature>();
    pdfSignature->BindPdf(inputFile);
    auto signatureName = pdfSignature->GetSignatureNames()->idx_get(0);
    auto inputStream = pdfSignature->ExtractCertificate(signatureName);
    auto outputStream = System::IO::File::Create(outputFile);

    inputStream->CopyTo(outputStream);
}
} // namespace Facades::Examples::PDF_FileSignature
```

## Get signature information

List signature names and print the first signature's signer, date, reason, and location.

1. Create [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Read signature identifiers with [PdfFileSignature::GetSignatureNames()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/getsignaturenames/).
1. List signature names with [PdfFileSignature::GetSignNames()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/getsignnames/).
1. Read the signer name with [PdfFileSignature::GetSignerName()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/getsignername/).
1. Read the signing date with [PdfFileSignature::GetDateTime()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/getdatetime/).
1. Read the signing reason with [PdfFileSignature::GetReason()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/getreason/).
1. Read the signing location with [PdfFileSignature::GetLocation()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/getlocation/).
1. Print the results or diagnostic messages shown in the example.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>
#include <Aspose.PDF.Cpp/Facades/SignatureName.h>
#include <iostream>
#include <system/collections/ilist.h>
#include <system/date_time.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileSignature
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void GetSignatureInformation(String inputFile)
{
    auto pdfSignature = MakeObject<PdfFileSignature>();
    pdfSignature->BindPdf(inputFile);
    auto signatureName = pdfSignature->GetSignatureNames()->idx_get(0);
    for (const auto &name : pdfSignature->GetSignNames())
        std::cout << "Signature Name: " << name << std::endl;
    std::cout << "Signer: " << pdfSignature->GetSignerName(signatureName) << std::endl;
    std::cout << "Date: " << pdfSignature->GetDateTime(signatureName).ToString() << std::endl;
    std::cout << "Reason: " << pdfSignature->GetReason(signatureName) << std::endl;
    std::cout << "Location: " << pdfSignature->GetLocation(signatureName) << std::endl;
}
} // namespace Facades::Examples::PDF_FileSignature
```

## Remove signature

Remove the first signature and save the modified PDF.

1. Create [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Read signature identifiers with [PdfFileSignature::GetSignatureNames()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/getsignaturenames/).
1. Remove the selected signature with [PdfFileSignature::RemoveSignature()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/removesignature/).
1. Save the resulting PDF with [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>
#include <Aspose.PDF.Cpp/Facades/SignatureName.h>
#include <system/collections/ilist.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileSignature
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void RemoveSignature(String inputFile, String outputFile)
{
    auto pdfSignature = MakeObject<PdfFileSignature>();
    pdfSignature->BindPdf(inputFile);
    auto signatureName = pdfSignature->GetSignatureNames()->idx_get(0);
    pdfSignature->RemoveSignature(signatureName);
    pdfSignature->Save(outputFile);
}
} // namespace Facades::Examples::PDF_FileSignature
```

## Sign PDF with basic parameters

Set the certificate and sign page 1 with approval details and the visible flag set to false.

1. Create [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Set the signing certificate with [PdfFileSignature::SetCertificate()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/setcertificate/).
1. Apply the digital signature with [PdfFileSignature::Sign()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/sign/).
1. Save the resulting PDF with [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>
#include <drawing/rectangle.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileSignature
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void SignPdfWithBasicParameters(String inputFile, String certificateFile, String outputFile)
{
    auto pdfSignature = MakeObject<PdfFileSignature>();
    pdfSignature->BindPdf(inputFile);
    pdfSignature->SetCertificate(certificateFile, u"Aspose2021");
    pdfSignature->Sign(1, u"Document approval", u"qa@example.com", u"New York, USA", false,
                       System::Drawing::Rectangle(10, 10, 200, 60));
    pdfSignature->Save(outputFile);
}
} // namespace Facades::Examples::PDF_FileSignature
```

## Sign PDF with certificate object

Configure a PKCS7 certificate object and sign page 1 with the visible flag set to false.

1. Load the certificate and configure a [PKCS7](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/pkcs7/) signature object.
1. Create [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Apply the digital signature with [PdfFileSignature::Sign()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/sign/).
1. Save the resulting PDF with [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/PKCS7.h>
#include <drawing/rectangle.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileSignature
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using PKCS7 = Aspose::Pdf::Forms::PKCS7;

void SignPdfWithCertificateObject(String inputFile, String certificateFile, String outputFile)
{
    auto certificateSignature = MakeObject<PKCS7>(certificateFile, u"Aspose2021");
    certificateSignature->set_Reason(u"Document approval");
    certificateSignature->set_ContactInfo(u"qa@example.com");
    certificateSignature->set_Location(u"New York, USA");
    certificateSignature->set_Authority(u"Aspose.PDF Example");

    auto pdfSignature = MakeObject<PdfFileSignature>();
    pdfSignature->BindPdf(inputFile);
    pdfSignature->Sign(1, false, System::Drawing::Rectangle(10, 10, 200, 60), certificateSignature);
    pdfSignature->Save(outputFile);
}
} // namespace Facades::Examples::PDF_FileSignature
```

## Verify PDF signature

Print the first signature's verification result and whether it covers the whole document.

1. Create [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Read signature identifiers with [PdfFileSignature::GetSignatureNames()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/getsignaturenames/).
1. Verify the signature with [PdfFileSignature::VerifySignature()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/verifysignature/).
1. Check document coverage with [PdfFileSignature::CoversWholeDocument()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/coverswholedocument/).
1. Print the results or diagnostic messages shown in the example.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileSignature.h>
#include <Aspose.PDF.Cpp/Facades/SignatureName.h>
#include <iostream>
#include <system/collections/ilist.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileSignature
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void VerifyPdfSignature(String inputFile)
{
    auto pdfSignature = MakeObject<PdfFileSignature>();
    pdfSignature->BindPdf(inputFile);
    auto signatureName = pdfSignature->GetSignatureNames()->idx_get(0);
    std::cout << "Signature '" << signatureName->ToString()
              << "' is valid: " << pdfSignature->VerifySignature(signatureName) << std::endl;
    std::cout << "Signature covers whole document: " << pdfSignature->CoversWholeDocument(signatureName) << std::endl;
}
} // namespace Facades::Examples::PDF_FileSignature
```
