---
title: PDF 파일에서 서명 작업하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ko/net/working-with-signature-in-a-pdf-file/
description: 이 섹션에서는 PdfFileSignature 클래스를 사용하여 서명 정보를 추출하고, 서명에서 이미지를 추출하고, 언어를 변경하는 방법 등을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Signature in PDF File",
    "alternativeHeadline": "Extract Signature Details and Images from PDFs",
    "abstract": "Aspose.PDF for .NET의 새로운 기능은 사용자가 PdfFileSignature 클래스를 사용하여 서명 정보와 이미지를 추출할 수 있도록 하여 PDF 문서 보안을 강화합니다. 이 기능은 또한 디지털 서명을 사용자 정의하고, 위치 및 이유와 같은 특정 정보를 숨기며, 서명 텍스트의 언어 설정을 변경할 수 있는 기능을 포함하여 PDF 서명을 효율적으로 관리하기 위한 포괄적인 도구 세트를 제공합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "878",
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
    "url": "/net/working-with-signature-in-a-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-signature-in-a-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

## 서명 정보 추출 방법

Aspose.PDF for .NET는 PdfFileSignature 클래스를 사용하여 PDF 파일에 디지털 서명하는 기능을 지원합니다. 현재 인증서의 유효성을 확인할 수 있지만 전체 인증서를 추출할 수는 없습니다. 추출할 수 있는 정보는 공개 키, 지문 및 발급자 등입니다.

서명 정보를 추출하기 위해 PdfFileSignature 클래스에 ExtractCertificate(..) 메서드를 도입했습니다. PdfFileSignature 객체에서 인증서를 추출하는 단계를 보여주는 다음 코드 스니펫을 확인하십시오:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSignatureInfo()
{ 
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "signed_rsa.pdf");
        // Get list of signature names
        var sigNames = pdfFileSignature.GetSignatureNames();
        if (sigNames.Count > 0)
        {
            SignatureName sigName = sigNames[0];            
            // Extract signature certificate
            Stream cerStream = pdfFileSignature.ExtractCertificate(sigName);
            if (cerStream != null)
            {
                using (cerStream)
                {
                    using (FileStream fs = new FileStream(dataDir + "extracted_cert.pfx", FileMode.CreateNew))
                    {
                        cerStream.CopyTo(fs);
                    }
                }
            }
            
        }
    }
}
```

## 서명 필드에서 이미지 추출하기 (PdfFileSignature)

Aspose.PDF for .NET는 PdfFileSignature 클래스를 사용하여 PDF 파일에 디지털 서명하는 기능을 지원하며, 문서에 서명하는 동안 SignatureAppearance에 이미지를 설정할 수도 있습니다. 이제 이 API는 서명 필드와 관련된 이미지뿐만 아니라 서명 정보를 추출하는 기능도 제공합니다.

서명 정보를 추출하기 위해 PdfFileSignature 클래스에 ExtractImage(..) 메서드를 도입했습니다. PdfFileSignature 객체에서 이미지를 추출하는 단계를 보여주는 다음 코드 스니펫을 확인하십시오:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSignatureImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var signature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        signature.BindPdf(dataDir + "ExtractingImage.pdf");

        if (signature.ContainsSignature())
        {
            // Get list of signature names
            foreach (string sigName in signature.GetSignatureNames())
            {                
                // Extract signature image
                using (Stream imageStream = signature.ExtractImage(sigName))
                {
                    if (imageStream != null)
                    {
                        imageStream.Position = 0;
                        using (FileStream fs = new FileStream(dataDir + "ExtractImages_out.jpg", FileMode.OpenOrCreate))
                        {
                            imageStream.CopyTo(fs);
                        }
                    }
                }
            }
        }
    }
}
```

## 위치 및 이유 숨기기

Aspose.PDF 기능은 디지털 서명 인스턴스에 대한 유연한 구성을 허용합니다. [PdfFileSignature](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilesignature) 클래스는 PDF 파일에 서명할 수 있는 기능을 제공합니다. 서명 메서드 구현은 PDF에 서명하고 이 클래스에 특정 서명 객체를 전달할 수 있도록 합니다. 서명 메서드는 출력 디지털 서명의 사용자 지정을 위한 속성 집합을 포함합니다. 결과 서명에서 일부 텍스트 속성을 숨기려면 해당 속성을 비워둘 수 있습니다. 다음 코드 스니펫은 서명 블록에서 위치와 이유 두 줄을 숨기는 방법을 보여줍니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SupressLocationReason()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "input.pdf");

        // Create a rectangle for signature location
        System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
        // Set signature appearance
        pdfFileSignature.SignatureAppearance = dataDir + "aspose-logo.png";

        // Create any of the three signature types
        var signature = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1

        pdfFileSignature.Sign(1, string.Empty, "test01@aspose-pdf-demo.local", string.Empty, true, rect, signature);
        // Save PDF document
        pdfFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```

## 디지털 서명을 위한 사용자 정의 기능

Aspose.PDF for .NET는 디지털 서명을 위한 사용자 정의 기능을 허용합니다. [SignatureCustomAppearance](https://reference.aspose.com/pdf/ko/net/aspose.pdf.forms/signaturecustomappearance) 클래스의 서명 메서드는 편리한 사용을 위해 6개의 오버로드를 구현합니다. 예를 들어, SignatureCustomAppearance 클래스 인스턴스와 그 속성 값을 사용하여 결과 서명을 구성할 수 있습니다. 다음 코드 스니펫은 PDF의 출력 디지털 서명에서 "디지털 서명한 사람" 캡션을 숨기는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CustomizationFeaturesForDigitalSign()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "input.pdf");

        // Create a rectangle for signature location
        System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);

        // Create any of the three signature types
        var signature = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1
        // Create signature appearance
        var signatureCustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance
        {
            FontSize = 6,
            FontFamilyName = "Times New Roman",
            DigitalSignedLabel = "Signed by:"
        };
        // Set signature appearance
        signature.CustomAppearance = signatureCustomAppearance;

        pdfFileSignature.Sign(1, true, rect, signature);
        // Save PDF document
        pdfFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```

## 디지털 서명 텍스트의 언어 변경

Aspose.PDF for .NET API를 사용하면 다음 세 가지 유형의 서명 중 하나를 사용하여 PDF 파일에 서명할 수 있습니다:

- PKCS#1.
- PKCS#7.
- PKCS#12.

제공된 각 서명은 귀하의 편의를 위해 구현된 구성 속성 집합을 포함합니다(지역화, 날짜 시간 형식, 글꼴 패밀리 등). [SignatureCustomAppearance](https://reference.aspose.com/pdf/ko/net/aspose.pdf.forms/signaturecustomappearance) 클래스는 해당 기능을 제공합니다. 다음 코드 스니펫은 디지털 서명 텍스트의 언어를 변경하는 방법을 보여줍니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangeLanguageInDigitalSignText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();   
    
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "input.pdf");
        // Create a rectangle for signature location
        System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);

        // Create any of the three signature types
        var pkcs = new Aspose.Pdf.Forms.PKCS7(dataDir + "rsa_cert.pfx", "12345")
        {
            Reason = "Pruebas Firma",
            ContactInfo = "Contacto Pruebas",
            Location = "Población (Provincia)",
            Date = DateTime.Now
        };
        
        var signatureCustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance
        {
            DateSignedAtLabel = "Fecha",
            DigitalSignedLabel = "Digitalmente firmado por",
            ReasonLabel = "Razón",
            LocationLabel = "Localización",
            FontFamilyName = "Arial",
            FontSize = 10d,
            Culture = System.Globalization.CultureInfo.InvariantCulture,
            DateTimeFormat = "yyyy.MM.dd HH:mm:ss"
        };
        // Set signature appearance
        pkcs.CustomAppearance = signatureCustomAppearance;
        // Sign the PDF file
        pdfFileSignature.Sign(1, true, rect, pkcs);
        // Save PDF document
        pdfFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```