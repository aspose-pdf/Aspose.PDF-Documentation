---
title: Работа с артефактами в .NET
linktitle: Работа с артефактами
type: docs
weight: 110
url: /net/artifacts/
description: Aspose.PDF для .NET позволяет добавлять фоновое изображение на страницы PDF и получать каждый водяной знак с использованием класса Artifact.
lastmod: "2024-01-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Работа с артефактами в .NET",
    "alternativeHeadline": "Артефакты в документе PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, артефакты в pdf",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Команда документации Aspose.PDF",
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
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/artifacts/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/artifacts/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF для .NET позволяет добавлять фоновое изображение на страницы PDF и получать каждый водяной знак с использованием класса Artifact."
}
</script>
Артефакты в PDF - это графические объекты или другие элементы, которые не являются частью фактического содержимого документа. Обычно они используются для декоративных целей, макета или фона. Примеры артефактов включают заголовки страниц, колонтитулы, разделители или изображения, которые не несут смысловой нагрузки.

Цель артефактов в PDF заключается в том, чтобы позволить различать элементы содержания и несодержательные элементы. Это важно для доступности, поскольку экранные читалки и другие вспомогательные технологии могут игнорировать артефакты и сосредотачиваться на релевантном содержимом. Артефакты также могут улучшить производительность и качество документов PDF, так как их можно опустить при печати, поиске или копировании.

Для создания элемента в виде артефакта в PDF, вам необходимо использовать класс [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact).
Он содержит следующие полезные свойства:

- **Artifact.Type** – получает тип артефакта (поддерживает значения перечисления Artifact.ArtifactType, куда входят Background, Layout, Page, Pagination и Undefined).
- **Artifact.Type** – получает тип артефакта (поддерживает значения перечисления Artifact.ArtifactType, к которым относятся Background, Layout, Page, Pagination и Undefined).
- **Artifact.Subtype** – получает подтип артефакта (поддерживает значения перечисления Artifact.ArtifactSubtype, к которым относятся Background, Footer, Header, Undefined, Watermark).
- **Artifact.Image** – получает изображение артефакта (если изображение присутствует, иначе null).
- **Artifact.Text** – получает текст артефакта.
- **Artifact.Contents** – получает коллекцию внутренних операторов артефакта. Поддерживаемый тип - System.Collections.ICollection.
- **Artifact.Form** – получает XForm артефакта (если используется XForm). Артефакты с водяными знаками, заголовками и нижними колонтитулами содержат XForm, который отображает все содержимое артефакта.
- **Artifact.Rectangle** – получает позицию артефакта на странице.
- **Artifact.Rotation** – получает вращение артефакта (в градусах, положительное значение указывает на вращение против часовой стрелки).
- **Artifact.Opacity** – получает непрозрачность артефакта.
- **Artifact.Opacity** – Получает прозрачность артефакта.

Следующие классы также могут быть полезны для работы с артефактами:

- [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection)
- [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/watermarkartifact/)

## Работа с существующими водяными знаками

Водяной знак, созданный с помощью Adobe Acrobat, называется артефактом (как описано в разделе 14.8.2.2 Реальное содержание и артефакты спецификации PDF).

Для получения всех водяных знаков на определенной странице класс [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) имеет свойство Artifacts.

Следующий фрагмент кода показывает, как получить все водяные знаки на первой странице PDF-файла.

_Примечание:_ Этот код также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).
_Примечание:_ Этот код также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample-w.pdf"));
var watermarks = document.Pages[1].Artifacts
    .Where(artifact =>
    artifact.Type == Artifact.ArtifactType.Pagination
    && artifact.Subtype == Artifact.ArtifactSubtype.Watermark);
foreach (WatermarkArtifact item in watermarks.Cast<WatermarkArtifact>())
{
    Console.WriteLine($"{item.Text} {item.Rectangle}");
}
```

## Работа с фонами как с артефактами

Фоновые изображения могут использоваться для добавления водяного знака или другого тонкого дизайна в документы. В Aspose.PDF для .NET каждый документ PDF представляет собой коллекцию страниц, и каждая страница содержит коллекцию артефактов. Класс [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact) можно использовать для добавления фонового изображения на объект страницы.

Следующий фрагмент кода показывает, как добавить фоновое изображение на страницы PDF с использованием объекта BackgroundArtifact.

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var background = new BackgroundArtifact()
{
    BackgroundImage = System.IO.File.OpenRead(System.IO.Path.Combine(_dataDir, "background.jpg"))
};
document.Pages[1].Artifacts.Add(background);
document.Save(System.IO.Path.Combine(_dataDir, "sample_artifacts_background.pdf"));
```
Если вы по какой-то причине хотите использовать однотонный фон, пожалуйста, измените предыдущий код следующим образом:

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var background = new BackgroundArtifact()
{
    BackgroundColor = Color.DarkKhaki,
};
document.Pages[1].Artifacts.Add(background);
document.Save(System.IO.Path.Combine(_dataDir, "sample_artifacts_background.pdf"));
```

## Подсчет артефактов определенного типа

Для расчета общего количества артефактов определенного типа (например, общее количество водяных знаков), используйте следующий код:

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var paginationArtifacts = document.Pages[1].Artifacts.Where(artifact => artifact.Type == Artifact.ArtifactType.Pagination);
Console.WriteLine("Водяные знаки: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Watermark));
Console.WriteLine("Фоны: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Background));
Console.WriteLine("Заголовки: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Header));
Console.WriteLine("Подвалы: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Footer));
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
                "areaServed": "США",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "Великобритания",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "Австралия",
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

