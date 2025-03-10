---
title: ملف استثناء التحكم PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ar/net/control-exception/
description: تعلم كيفية التعامل مع الاستثناءات في معالجة PDF وضمان سير العمليات بسلاسة أثناء العمل مع ملفات PDF باستخدام Aspose.PDF في .NET.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Control Exception PDF File",
    "alternativeHeadline": "Manage PDF Exception Handling with New Security Control",
    "abstract": "تتيح لك ميزة استثناء التحكم في فئة PdfFileSecurity إدارة معالجة الأخطاء عند فك تشفير ملفات PDF عن طريق تبديل خاصية AllowExceptions. يمكن للمستخدمين الاختيار بين تلقي نتائج بوليانية لنجاح فك التشفير أو استخدام كتل try-catch لإدارة الاستثناءات بشكل شامل، مما يعزز المرونة والتحكم في عمليات أمان PDF",
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
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

تتيح لك فئة [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) التحكم في الاستثناءات. للقيام بذلك، تحتاج إلى تعيين خاصية [AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) إلى false أو true. إذا قمت بتعيين العملية إلى false، فإن نتيجة [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile) ستعيد true أو false اعتمادًا على صحة كلمة المرور.

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

إذا قمت بتعيين خاصية [AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) إلى true، فيمكنك الحصول على نتيجة العملية باستخدام عامل try-catch.

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