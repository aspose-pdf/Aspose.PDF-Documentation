---
title: Sign PDF Documents in C++
linktitle: Sign PDF Documents
type: docs
weight: 10
url: /cpp/pdf-signing/
description: Sign PDF Documents in C++ with the PdfFileSignature facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Sign PDF Documents with the PdfFileSignature Facade
Abstract: Set the certificate and sign page 1 with approval details and the visible flag set to false. Configure a PKCS7 certificate object and sign page 1 with the visible flag set to false.
---

Use [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/) for this task. The examples below retain the original C++ code and API Reference steps.

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
