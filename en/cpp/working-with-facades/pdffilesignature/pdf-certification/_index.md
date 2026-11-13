---
title: PDF Certification in C++
linktitle: PDF Certification
type: docs
weight: 30
url: /cpp/pdf-certification/
description: PDF Certification in C++ with the PdfFileSignature facade in Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF Certification with the PdfFileSignature Facade
Abstract: Create a PKCS7 signature and certify page 1 with FillingInForms modification permissions and a visible signature.
---

Use [PdfFileSignature](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesignature/) for this task. The examples below retain the original C++ code and API Reference steps.

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
