---
title: PDF 파일에서 서명 확인
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ko/net/verify-signature-in-pdf/
description: 이 섹션에서는 PdfFileSignature 클래스를 사용하여 PDF 파일에서 서명을 확인하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Verify Signature in PDF File",
    "alternativeHeadline": "Verify Signatures in PDF Files Efficiently",
    "abstract": "이 기능은 사용자가 PdfFileSignature 클래스를 사용하여 PDF 파일 내에서 서명을 효율적으로 확인할 수 있도록 합니다. 서명의 존재와 유효성을 확인하는 방법을 통해 이 기능은 문서의 진위성과 무결성을 보장하는 과정을 단순화합니다. PDF의 보안을 원활하게 확인하여 문서 관리를 최적화하세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "313",
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
    "url": "/net/verify-signature-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/verify-signature-in-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## PDF 파일이 서명되었는지 확인하기

특정 서명을 사용하여 PDF 파일이 서명되었는지 확인하려면 [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 클래스의 VerifySigned 메서드를 사용하세요. 이 메서드는 서명 이름을 요구하며, PDF가 해당 서명 이름으로 서명된 경우 true를 반환합니다. 어떤 서명으로 서명되었는지 확인하지 않고도 [PDF가 서명되었는지](/pdf/ko/net/working-with-signature-in-a-pdf-file/) 확인할 수 있습니다.

### 주어진 서명으로 PDF가 서명되었는지 확인하기

다음 코드 조각은 주어진 서명을 사용하여 PDF가 서명되었는지 확인하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IsPdfSigned()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {      
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");
        if (pdFileSignature.ContainsSignature())
        {
            Console.WriteLine("Document Signed");
        }
    }
}
```

### PDF가 서명되었는지 확인하기

서명 이름을 제공하지 않고 파일이 서명되었는지 확인하려면 다음 코드를 사용하세요.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IsPdfSignedWithGivenSignature()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");
        if (pdFileSignature.VerifySignature("Signature1"))
        {
            Console.WriteLine("PDF Signed");
        }
    }
}
```

## 서명이 유효한지 확인하기

[VerifySignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/verifysignature) 메서드는 [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 클래스의 특정 서명을 검증할 수 있게 해줍니다. 이 메서드는 서명 이름을 입력으로 요구하며, 서명이 유효한 경우 true를 반환합니다. 다음 코드 조각은 서명을 검증하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IsPdfSignatureValid()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");
        if (pdFileSignature.VerifySignature("Signature1"))
        {
            Console.WriteLine("Signature Verified");
        }
    }
}
```