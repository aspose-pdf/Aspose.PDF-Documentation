---
title: إضافة خلفية إلى PDF
linktitle: إضافة خلفيات
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 110
url: /ar/net/add-backgrounds/
description: إضافة صورة خلفية إلى ملف PDF الخاص بك باستخدام C#. استخدم كائن BackgroundArtifact.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add background to PDF",
    "alternativeHeadline": "Add Custom Backgrounds to PDFs with C#",
    "abstract": "تقديم القدرة على دمج صور الخلفية بسلاسة في مستندات PDF الخاصة بك باستخدام C# مع Aspose.PDF for .NET. هذه الميزة تستخدم كائن BackgroundArtifact، مما يسمح بخيارات تصميم محسّنة مثل العلامات المائية أو التمويه الخفيف، مما يجعل PDFs الخاصة بك تبرز بأقل جهد. اكتشف كيفية رفع تخطيطات مستنداتك من خلال إضافة خلفيات مخصصة بسهولة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add background to PDF, BackgroundArtifact object, PDF manipulation, C# PDF library, watermark in PDF, Aspose.PDF for .NET, add background image, PDF document generation, PDF artifacts, document background settings",
    "wordcount": "228",
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
    "url": "/net/add-backgrounds/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-backgrounds/"
    },
    "dateModified": "2024-11-26",
    "description": "إضافة صورة خلفية إلى ملف PDF الخاص بك باستخدام C#. استخدم كائن BackgroundArtifact."
}
</script>

يمكن استخدام صور الخلفية لإضافة علامة مائية، أو تصميم خفيف آخر، إلى المستندات. في Aspose.PDF for .NET، كل مستند PDF هو مجموعة من الصفحات وكل صفحة تحتوي على مجموعة من الآثار. يمكن استخدام فئة [BackgroundArtifact](https://reference.aspose.com/pdf/ar/net/aspose.pdf/backgroundartifact) لإضافة صورة خلفية إلى كائن الصفحة.

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

تظهر مقتطفات الشيفرة التالية كيفية إضافة صورة خلفية إلى صفحات PDF باستخدام كائن BackgroundArtifact مع C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBackgroundToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Image for background artifact object
        using (var image = File.OpenRead(dataDir + "aspose-total-for-net.jpg"))
        {
            // Add page
            Page page = document.Pages.Add();
            // Create Background Artifact object
            var background = new Aspose.Pdf.BackgroundArtifact();
            // Specify the image for background artifact object
            background.BackgroundImage = image;
            // Add background artifact to artifacts collection of page
            page.Artifacts.Add(background);
            // Save PDF document
            document.Save(dataDir + "ImageAsBackground_out.pdf");
        }
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>