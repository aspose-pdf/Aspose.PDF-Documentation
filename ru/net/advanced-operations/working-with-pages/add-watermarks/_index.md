---
title: Добавление водяного знака в PDF с помощью C#
linktitle: Добавить водяной знак
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /ru/net/add-watermarks/
description: В этой статье рассказывается о возможностях работы с артефактами и получении водяных знаков в файлах PDF с использованием программирования на языке C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add watermark to PDF using C#",
    "alternativeHeadline": "Add Custom Watermarks to PDF with C#",
    "abstract": "Новая функция в Aspose.PDF для .NET позволяет разработчикам программно добавлять настраиваемые водяные знаки в PDF-документы с помощью функции Artifact. Эта функция улучшает управление документами, поддерживая различные свойства артефактов, включая тип, непрозрачность, поворот и настройку текста, что позволяет пользователям легко создавать профессиональные и узнаваемые PDF-файлы",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "462",
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
    "url": "/net/add-watermarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-watermarks/"
    },
    "dateModified": "2024-11-26",
    "description": "Эта статья объясняет особенности работы с артефактами и получения водяных знаков в PDF-файлах с помощью программирования на C#."
}
</script>

**Aspose.PDF for .NET** позволяет добавлять водяные знаки к вашему PDF-документу с помощью артефактов. Пожалуйста, ознакомьтесь с этой статьёй для решения вашей задачи.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

Водяной знак, созданный в Adobe Acrobat, называется артефактом (как описано в разделе 14.8.2.2 Реальное содержимое и артефакты спецификации PDF). Для работы с артефактами в Aspose.PDF есть два класса: [Artifact](https://reference.aspose.com/pdf/ru/net/aspose.pdf/artifact) и [ArtifactCollection](https://reference.aspose.com/pdf/ru/net/aspose.pdf/artifactcollection).

Чтобы получить все артефакты на определённой странице, класс [Page](https://reference.aspose.com/pdf/ru/net/aspose.pdf/page) имеет свойство Artifacts. Этот раздел объясняет, как работать с артефактами в файлах PDF.

## Работа с артефактами

Класс [Artifact](https://reference.aspose.com/pdf/ru/net/aspose.pdf/artifact) содержит следующие свойства:

- **Тип артефакта**: получает тип артефакта (поддерживает значения перечисления Artifact.ArtifactType, где значения включают Background, Layout, Page, Pagination и Undefined).
- **Подтип артефакта**: получает подтип артефакта (поддерживает значения перечисления Artifact.ArtifactSubtype, где значения включают Background, Footer, Header, Undefined, Watermark).

{{% alert color="primary" %}}

Обратите внимание, что водяные знаки, созданные в Adobe Acrobat, имеют тип Pagination и подтип Watermark.

{{% /alert %}}

- **Содержимое артефакта**: Получает коллекцию внутренних операторов артефакта. Поддерживаемый тип — System.Collections.ICollection.
- **Форма артефакта**: Получает XForm артефакта (если используется XForm). Артефакты водяных знаков, заголовков и нижних колонтитулов содержат XForm, который показывает всё содержимое артефакта.
- **Изображение артефакта**: Получает изображение артефакта (если присутствует изображение, иначе null).
- **Текст артефакта**: Получает текст артефакта.
- **Прямоугольник артефакта**: Получает положение артефакта на странице.
- **Поворот артефакта**: Получает поворот артефакта (в градусах, положительное значение указывает на вращение против часовой стрелки).
- **Непрозрачность артефакта**: Получает непрозрачность артефакта. Возможные значения находятся в диапазоне от 0 до 1, где 1 полностью непрозрачный.

## Как добавить водяной знак в файлы PDF

Следующий фрагмент кода показывает, как получить каждый водяной знак на первой странице файла PDF с помощью C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddWatermarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddWatermarksInput.pdf"))
    {
        // Create a new watermark artifact
        var artifact = new Aspose.Pdf.WatermarkArtifact();
        artifact.SetTextAndState(
            "WATERMARK",
            new Aspose.Pdf.Text.TextState()
            {
                FontSize = 72,
                ForegroundColor = Aspose.Pdf.Color.Blue,
                Font = Aspose.Pdf.Text.FontRepository.FindFont("Courier")
            });
        // Set watermark properties
        artifact.ArtifactHorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        artifact.ArtifactVerticalAlignment = Aspose.Pdf.VerticalAlignment.Center;
        artifact.Rotation = 45;
        artifact.Opacity = 0.5;
        artifact.IsBackground = true;
        // Add watermark artifact to the first page
        document.Pages[1].Artifacts.Add(artifact);
        // Save PDF document
        document.Save(dataDir + "AddWatermarks_out.pdf");
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