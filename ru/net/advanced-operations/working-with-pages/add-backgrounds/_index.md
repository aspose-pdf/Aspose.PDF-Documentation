---
title: Добавление фона в PDF
linktitle: Добавить фоны
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 110
url: /ru/net/add-backgrounds/
description: Добавьте фоновое изображение в ваш PDF-файл с помощью C#. Используйте объект BackgroundArtifact.
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
    "abstract": "Представляем возможность легко интегрировать фоновые изображения в ваши PDF-документы с помощью C# и Aspose.PDF для .NET. Эта функция использует объект BackgroundArtifact, предоставляя расширенные возможности оформления, такие как водяные знаки или тонкие текстуры, идеально подходящие для того, чтобы ваши PDF-файлы выделялись без особых усилий. Узнайте, как улучшить оформление ваших документов, легко добавляя индивидуальные фоны",
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
    "description": "Добавьте фоновое изображение в ваш PDF-файл с помощью C#. Используйте объект BackgroundArtifact"
}
</script>

Фоновые изображения можно использовать для добавления водяных знаков или других тонких элементов дизайна в документы. В Aspose.PDF for .NET каждый PDF-документ представляет собой набор страниц, и каждая страница содержит набор артефактов. Класс [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact) можно использовать для добавления фонового изображения к объекту страницы.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

Следующий фрагмент кода показывает, как добавить фоновое изображение на страницы PDF с помощью объекта BackgroundArtifact на C#.

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