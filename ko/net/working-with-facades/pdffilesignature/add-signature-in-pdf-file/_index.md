---
title: PDF 파일에 서명 추가
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/add-signature-in-pdf/
description: 이 섹션에서는 PdfFileSignature 클래스를 사용하여 PDF 파일에 서명을 추가하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Signature in PDF File",
    "alternativeHeadline": "Add Custom Digital Signatures to PDF Files",
    "abstract": "PdfFileSignature 클래스를 사용하여 디지털 서명을 추가하는 새로운 기능으로 PDF 문서를 향상시키세요. 이 기능은 사용자가 PKCS#1, PKCS#7 및 PKCS#7Detached를 포함한 다양한 서명 유형을 적용할 수 있게 하며, 이미지 및 특정 속성을 사용하여 서명의 모양을 사용자 정의할 수 있습니다. 여러 페이지에 여러 서명을 쉽게 통합하여 문서 검증 프로세스를 간소화하세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "838",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/add-signature-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-signature-in-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## PDF 파일에 디지털 서명 추가

[PdfFileSignature](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilesignature) 클래스는 PDF 파일에 서명을 추가할 수 있게 해줍니다. 입력 및 출력 PDF 파일을 사용하여 [PdfFileSignature](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilesignature) 클래스의 객체를 생성해야 합니다. 서명을 추가할 위치에 [Rectangle](https://reference.aspose.com/pdf/ko/net/aspose.pdf/rectangle) 객체를 생성해야 하며, 서명의 모양을 설정하기 위해 [PdfFileSignature](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilesignature) 객체의 [SignatureAppearance](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilesignature/properties/signatureappearance) 속성을 사용하여 이미지를 지정할 수 있습니다. Aspose.Pdf.Facades는 PKCS#1, PKCS#7 및 PKCS#7Detached와 같은 다양한 서명 유형도 제공합니다. 특정 유형의 서명을 생성하려면 인증서 파일과 비밀번호를 사용하여 **PKCS1**, **PKCS7** 또는 **PKCS7Detached**와 같은 특정 클래스의 객체를 생성해야 합니다.

특정 서명 유형의 객체가 생성되면, [PdfFileSignature](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilesignature) 클래스의 [Sign](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilesignature/methods/sign/index) 메서드를 사용하여 PDF에 서명하고 이 클래스에 특정 서명 객체를 전달할 수 있습니다. 이 메서드에 대한 다른 속성도 지정할 수 있습니다. 마지막으로, [PdfFileSignature](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilesignature) 클래스의 [Save](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/methods/save/index) 메서드를 사용하여 서명된 PDF를 저장해야 합니다. 다음 코드 스니펫은 PDF 파일에 서명을 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPdfFileSignature()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "input.pdf");

        // Create a rectangle for signature location
        System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
    
        // Set signature appearance
        pdFileSignature.SignatureAppearance = dataDir + "aspose-logo.png";

        // Create any of the three signature types
        var signature = new PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1

        pdFileSignature.Sign(1, "I'm document author", "test01@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect, signature);
        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```

다음 코드 예제는 두 개의 서명으로 문서에 서명할 수 있는 기능을 보여줍니다. 우리의 예제에서는 첫 번째 페이지에 첫 번째 서명을, 두 번째 페이지에 두 번째 서명을 추가합니다. 필요한 페이지를 지정할 수 있습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTwoSignature()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "input.pdf");

        // Create a rectangle for 1st signature location
        System.Drawing.Rectangle rect1 = new System.Drawing.Rectangle(10, 10, 300, 50);

        // Create 1st signature object
        var signature1 = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1

        pdFileSignature.Sign(1, "I'm document author", "test@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect1, signature1);
        pdFileSignature.Save(dataDir + "DigitallySign_out.pdf");

        // Sign with 2nd signature
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "DigitallySign_out.pdf");

        // Create a rectangle for 2nd signature location
        System.Drawing.Rectangle rect2 = new System.Drawing.Rectangle(10, 10, 300, 50);

        // Create 2nd signature object
        var signature2 = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1

        pdFileSignature.Sign(2, "I'm document reviewer", "test02@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect2, signature2);

        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign2_out.pdf");
    }
}
```

서명해야 하는 양식 또는 아크로폼이 있는 문서의 경우, 다음 예제를 참조하세요. 입력 및 출력 PDF 파일을 사용하여 [PdfFileSignature](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilesignature) 클래스의 객체를 생성해야 합니다. 바인딩을 위해 [BindPdf](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades.pdffilesignature/bindpdf/methods/1)를 사용하세요. 필요한 속성을 추가할 수 있는 서명을 생성하세요. 우리의 예제에서는 'Reason'과 'CustomAppearance'가 있습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPdfFileSignatureField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "input.pdf");

        // Create any of the three signature types
        var signature = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345")
        {
            Reason = "Sign as Author",
            CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance
            {
                FontSize = 6,
                FontFamilyName = "Calibri"
            }
        }; // PKCS#1
        
        pdFileSignature.Sign("Signature1", signature);
        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```

문서에 두 개의 필드가 있는 경우, 서명하는 알고리즘은 첫 번째 예제와 유사합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPdfFileSignatureField2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "input.pdf");

        // Create any of the three signature types
        var signature1 = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345")
        {
            Reason = "Sign as Author",
            CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance
            {
                FontSize = 6
            }
        }; // PKCS#1
        pdFileSignature.Sign("Signature1", signature1);
        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign_out.pdf");
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "DigitallySign_out.pdf");

        // Create any of the three signature types
        var signature2 = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345")
        {
            Reason = "Sign as Reviwer",
            CustomAppearance = new SignatureCustomAppearance
            {
                FontSize = 6
            }
        }; // PKCS#1
        
        pdFileSignature.Sign("Signature2", signature2);
        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign2_out.pdf");
    }
}
```