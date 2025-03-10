---
title: 제어 예외 PDF 파일
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ko/net/control-exception/
description: Aspose.PDF를 사용하여 PDF 처리 중 예외를 처리하고 원활한 작업을 보장하는 방법을 알아보세요.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Control Exception PDF File",
    "alternativeHeadline": "Manage PDF Exception Handling with New Security Control",
    "abstract": "PdfFileSecurity 클래스의 제어 예외 기능을 사용하면 AllowExceptions 속성을 전환하여 PDF 파일을 해독할 때 오류 처리를 관리할 수 있습니다. 사용자는 해독 성공에 대한 부울 결과를 받거나 포괄적인 예외 관리를 위해 try-catch 블록을 활용하는 것 중에서 선택할 수 있으며, 이는 PDF 보안 작업에 대한 유연성과 제어를 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "224",
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
    "url": "/net/control-exception/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/control-exception/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 단순하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

[PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) 클래스는 예외를 제어할 수 있게 해줍니다. 이를 위해 [AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) 속성을 false 또는 true로 설정해야 합니다. 작업을 false로 설정하면 [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile)의 결과는 비밀번호의 정확성에 따라 true 또는 false를 반환합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ControlExceptionPDFFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "sample_encrypted.pdf");
        // Disallow exceptions
        fileSecurity.AllowExceptions = false;
        
        // Decrypt PDF document
        if (!fileSecurity.DecryptFile("IncorrectPassword"))
        {
            Console.WriteLine("Something wrong...");
            Console.WriteLine($"Last exception: {fileSecurity.LastException.Message}");
        }
        // Save PDF document
        fileSecurity.Save(dataDir + "SampleDecrtypted_out.pdf");
    }
}
```

[AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) 속성을 true로 설정하면 try-catch 연산자를 사용하여 작업의 결과를 얻을 수 있습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ControlExceptionPDFFile2()
{   
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "sample_encrypted.pdf");
        // Allow exceptions
        fileSecurity.AllowExceptions = true;
        try
        {
            // Decrypt PDF document
            fileSecurity.DecryptFile("IncorrectPassword");
        }
        catch (Exception ex)
        {
            Console.WriteLine("Something wrong...");
            Console.WriteLine($"Exception: {ex.Message}");
        }
        // Save PDF document
        fileSecurity.Save(dataDir + "SampleDecrtypted_out.pdf");
    }
}
```