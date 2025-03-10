---
title: Работа с артефактами в .NET
linktitle: Работа с артефактами
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 170
url: /ru/net/artifacts/
description: «Aspose.PDF for .NET» позволяет добавлять фоновое изображение на страницы PDF и получать каждый водяной знак с помощью класса Artifact.
lastmod: "2024-01-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Artifacts in .NET",
    "alternativeHeadline": "Add and Manage Artifacts in PDF Documents",
    "abstract": "Aspose.PDF для .NET представляет класс Artifact, позволяющий разработчикам эффективно управлять не содержательными элементами, такими как фоновые изображения и водяные знаки, в PDF-документах. Эта функциональность улучшает структуру документа, а также его доступность и производительность, поскольку вспомогательные технологии могут игнорировать артефакты. Пользователи могут легко управлять этими элементами для создания визуально привлекательных PDF-файлов благодаря настраиваемым параметрам типов и свойств.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Artifacts, PDF document generation, Aspose.PDF for .NET, BackgroundArtifact, WatermarkArtifact, Artifact class, PDF artifacts, Artifact types, Accessibility in PDF, PDF watermark handling",
    "wordcount": "779",
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
    "url": "/net/artifacts/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/artifacts/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF для .NET позволяет добавлять фоновое изображение на страницы PDF и получать каждый водяной знак с помощью класса Artifact."
}
</script>

Артефакты в PDF — это графические объекты или другие элементы, которые не являются частью фактического содержимого документа. Обычно они используются для украшения, макета или фона. Примерами артефактов являются заголовки страниц, нижние колонтитулы, разделители или изображения, не несущие никакого смысла.

Цель артефактов в PDF — позволить различать содержимое и не относящиеся к нему элементы. Это важно для обеспечения доступности, поскольку программы чтения с экрана и другие вспомогательные технологии могут игнорировать артефакты и сосредоточиться на соответствующем содержимом. Артефакты также могут повысить производительность и качество PDF-документов, поскольку их можно исключить из печати, поиска или копирования.

Чтобы создать элемент в качестве артефакта в PDF, необходимо использовать класс [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact). Он содержит следующие полезные свойства:

* **Artifact.Type** — получает тип артефакта (поддерживает значения перечисления Artifact.ArtifactType, включая Background, Layout, Page, Pagination и Undefined).
* **Artifact.Subtype** — получает подтип артефакта (поддерживает значения перечисления Artifact.ArtifactSubtype, включая Background, Footer, Header, Undefined, Watermark).
* **Artifact.Image** — Получает изображение артефакта (если изображение присутствует, иначе null).
* **Artifact.Text** — Получает текст артефакта.
* **Artifact.Contents** — Получает коллекцию внутренних операторов артефакта. Поддерживаемый тип — System.Collections.ICollection.
* **Artifact.Form** — Получает XForm артефакта (если используется XForm). Артефакты водяных знаков, заголовка и нижнего колонтитула содержат XForm, который показывает всё содержимое артефакта.
* **Artifact.Rectangle** — Получает положение артефакта на странице.
* **Artifact.Rotation** — Получает поворот артефакта (в градусах, положительное значение указывает на вращение против часовой стрелки).
* **Artifact.Opacity** — Получает непрозрачность артефакта. Возможные значения находятся в диапазоне от 0 до 1, где 1 — полностью непрозрачный.

Для работы с артефактами также могут быть полезны следующие классы:

* [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection)
* [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact/)
* [HeaderArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/headerartifact/)
* [FooterArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/footerartifact/)
* [WatermarkArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/watermarkartifact/)

## Работа с существующими водяными знаками

Водяной знак, созданный с помощью Adobe Acrobat, называется артефактом (как описано в 14.8.2.2 Реальное содержимое и артефакты спецификации PDF).

Чтобы получить все водяные знаки на определённой странице, класс [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) имеет свойство Artifacts.

Следующий фрагмент кода показывает, как получить все водяные знаки на первой странице PDF-файла.

Примечание: Этот код также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractWatermarkFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample-w.pdf"))
    {
        // Get the watermarks from the first page artifacts
        var watermarks = document.Pages[1].Artifacts
            .Where(artifact =>
                artifact.Type == Aspose.Pdf.Artifact.ArtifactType.Pagination
                && artifact.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Watermark);

        // Iterate through the found watermark artifacts and print details
        foreach (Aspose.Pdf.WatermarkArtifact item in watermarks.Cast<Aspose.Pdf.WatermarkArtifact>())
        {
            Console.WriteLine($"{item.Text} {item.Rectangle}");
        }
    }
}
```

## Использование фонов в качестве артефактов

Фоновые изображения можно использовать для добавления водяных знаков или другого ненавязчивого оформления документов. В «Aspose.PDF for .NET» каждый PDF-документ представляет собой набор страниц, и каждая страница содержит набор артефактов. Класс [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact) можно использовать для добавления фонового изображения к объекту страницы.

Следующий фрагмент кода показывает, как добавить фоновое изображение на страницы PDF с помощью объекта BackgroundArtifact.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBackgroundImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Create a new BackgroundArtifact and set the background image
        var background = new Aspose.Pdf.BackgroundArtifact()
        {
            BackgroundImage = File.OpenRead(dataDir + "background.jpg")
        };

        // Add the background image to the first page's artifacts
        document.Pages[1].Artifacts.Add(background);

        // Save PDF document with the added background
        document.Save(dataDir + "SampleArtifactsBackground_out.pdf");
    }
}
```

Если вы по какой-то причине хотите использовать сплошной цветовой фон, измените предыдущий код следующим образом:

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

 private static void AddBackgroundColorToPDF()
 {
    // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
     {
         // Create a new BackgroundArtifact and set the background color
         var background = new Aspose.Pdf.BackgroundArtifact()
         {
             BackgroundColor = Aspose.Pdf.Color.DarkKhaki
         };

         // Add the background color to the first page's artifacts
         document.Pages[1].Artifacts.Add(background);

         // Save PDF document
         document.Save(dataDir + "SampleArtifactsBackground_out.pdf");
     }
 }
```

## Подсчёт артефактов определённого типа

Чтобы вычислить общее количество артефактов определённого типа (например, общее количество водяных знаков), используйте следующий код:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CountPDFArtifacts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Get pagination artifacts from the first page
        var paginationArtifacts = document.Pages[1].Artifacts
            .Where(artifact => artifact.Type == Aspose.Pdf.Artifact.ArtifactType.Pagination);

        // Count and display the number of each artifact type
        Console.WriteLine("Watermarks: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Watermark));
        Console.WriteLine("Backgrounds: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Background));
        Console.WriteLine("Headers: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Header));
        Console.WriteLine("Footers: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Footer));
    }
}
```

<!-- 6525752351 -->
<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type":
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