---
title: Проверка подписи в PDF файле
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ru/net/verify-signature-in-pdf/
description: Этот раздел объясняет, как проверить подпись в PDF файле с использованием класса PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Verify Signature in PDF File",
    "alternativeHeadline": "Verify Signatures in PDF Files Efficiently",
    "abstract": "Эта функция позволяет пользователям эффективно проверять подписи в PDF файлах с использованием класса PdfFileSignature. С методами для проверки как существования подписи, так и ее действительности, эта функциональность упрощает процесс обеспечения подлинности и целостности документа. Оптимизируйте управление документами, бесшовно подтверждая безопасность ваших PDF.",
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
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Проверьте, подписан ли PDF файл с использованием подписи

Чтобы проверить, подписан ли PDF файл с использованием [определенной подписи](/pdf/ru/net/working-with-signature-in-a-pdf-file/), используйте метод VerifySigned класса [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature). Этот метод требует имя подписи и возвращает true, если PDF подписан с использованием этого имени подписи. Также возможно проверить, что [PDF подписан](/pdf/ru/net/working-with-signature-in-a-pdf-file/), не проверяя, какой подписью он подписан.

### Проверка, что PDF подписан с использованием данной подписи

Следующий фрагмент кода показывает, как проверить, подписан ли PDF с использованием данной подписи.

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

### Проверка, что PDF подписан

Чтобы определить, подписан ли файл, не указывая имя подписи, используйте следующий код.

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

## Проверьте, действительна ли подпись

Метод [VerifySignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/verifysignature) класса [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) позволяет вам проверить действительность определенной подписи. Этот метод требует имя подписи в качестве входных данных и возвращает true, если подпись действительна. Следующий фрагмент кода показывает, как проверить подпись.

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