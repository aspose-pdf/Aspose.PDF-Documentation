---
title: Добавление водяного знака в PDF с использованием C#
linktitle: Добавить водяной знак
type: docs
weight: 90
url: /ru/net/add-watermarks/
description: Эта статья объясняет особенности работы с артефактами и получения водяных знаков в PDF файлах с использованием C# программно.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/working-with-existing-watermarks/
    - /net/adding-multi-line-watermark-to-existing-pdf/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Добавление водяного знака в PDF с использованием C#",
    "alternativeHeadline": "Как добавить водяной знак в PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, c#, добавить водяной знак",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "dateModified": "2022-02-04",
    "description": "Эта статья объясняет особенности работы с артефактами и получения водяных знаков в PDF файлах с использованием C# программно."
}
</script>
**Aspose.PDF для .NET** позволяет добавлять водяные знаки в ваш PDF документ с использованием Артефактов. Пожалуйста, ознакомьтесь с этой статьей для решения вашей задачи.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

Водяной знак, созданный с помощью Adobe Acrobat, называется артефактом (как описано в 14.8.2.2 Реальное содержимое и Артефакты спецификации PDF). Для работы с артефактами, Aspose.PDF имеет два класса: [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) и [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection).

Для получения всех артефактов на конкретной странице, класс [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) имеет свойство Artifacts. Эта тема объясняет, как работать с артефактом в файлах PDF.

## Работа с Артефактами

Класс [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) содержит следующие свойства:

**Artifact.Type** – получает тип артефакта (поддерживает значения перечисления Artifact.ArtifactType, куда входят Background, Layout, Page, Pagination и Undefined).
**Artifact.Type** – получает тип артефакта (поддерживает значения перечисления Artifact.ArtifactType, включающие Background, Layout, Page, Pagination и Undefined).  
**Artifact.Subtype** – получает подтип артефакта (поддерживает значения перечисления Artifact.ArtifactSubtype, включающие Background, Footer, Header, Undefined, Watermark).  

{{% alert color="primary" %}}

Обратите внимание, что водяные знаки, созданные с помощью Adobe Acrobat, имеют тип Pagination и подтип Watermark.

{{% /alert %}}

**Artifact.Contents** – получает коллекцию внутренних операторов артефакта. Поддерживаемый тип — System.Collections.ICollection.  
**Artifact.Form** – получает XForm артефакта (если используется XForm). Артефакты водяных знаков, заголовок и нижний колонтитул содержат XForm, который отображает все содержимое артефакта.  
**Artifact.Image** – получает изображение артефакта (если изображение присутствует, иначе null).  
**Artifact.Text** – получает текст артефакта.  
**Artifact.Rectangle** – получает позицию артефакта на странице.  
**Artifact.Rotation** – получает вращение артефакта (в градусах, положительное значение указывает на вращение против часовой стрелки).  
**Artifact.Rotation** – Получает угол поворота артефакта (в градусах, положительное значение указывает на поворот против часовой стрелки).
**Artifact.Opacity** – Получает непрозрачность артефакта. Возможные значения находятся в диапазоне от 0 до 1, где 1 полностью непрозрачен.

## Примеры программирования: Как добавить водяной знак на PDF файлы

Следующий фрагмент кода показывает, как получить каждый водяной знак на первой странице PDF файла на C#.

```csharp
public static void AddWatermarks()
{
    Document document = new Document(_dataDir + "text.pdf");
    WatermarkArtifact artifact = new WatermarkArtifact();
    artifact.SetTextAndState(
        "WATERMARK",
        new TextState()
        {
            FontSize = 72,
            ForegroundColor = Color.Blue,
            Font = FontRepository.FindFont("Courier")
        });
    artifact.ArtifactHorizontalAlignment = HorizontalAlignment.Center;
    artifact.ArtifactVerticalAlignment = VerticalAlignment.Center;
    artifact.Rotation = 45;
    artifact.Opacity = 0.5;
    artifact.IsBackground = true;
    document.Pages[1].Artifacts.Add(artifact);
    document.Save(_dataDir + "watermark.pdf");
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для библиотеки .NET",
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
                "contactType": "продажи",
                "areaServed": "US",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "GB",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "AU",
                "availableLanguage": "английский"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для работы с PDF для .NET",
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
```

