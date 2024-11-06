---
title: Создание ссылок в PDF-файле с помощью C#
linktitle: Создание ссылок
type: docs
weight: 10
url: ru/net/create-links/
description: В этом разделе объясняется, как создать ссылки в вашем PDF-документе с помощью C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Создание ссылок в PDF-файле с помощью C#",
    "alternativeHeadline": "Как создать ссылки в PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, создание ссылки в pdf",
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
    "url": "/net/create-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-links/"
    },
    "dateModified": "2022-02-04",
    "description": "В этом разделе объясняется, как создать ссылки в вашем PDF-документе с помощью C#."
}
</script>

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Создание ссылок

Добавив ссылку на приложение в документ, можно создать ссылки на приложения из документа. Это полезно, когда вы хотите, чтобы читатели предприняли определенные действия в конкретной точке учебного материала, например, или для создания документа с богатым функционалом. Чтобы создать ссылку на приложение:

1. [Создайте объект Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Получите [страницу](https://reference.aspose.com/pdf/net/aspose.pdf/page), к которой вы хотите добавить ссылку.
1. Создайте объект [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation), используя объекты Page и [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle).
1. Установите атрибуты ссылки с помощью объекта [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation).
1. При создании объекта [LaunchAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/launchaction) укажите приложение, которое хотите запустить.
1. Добавьте ссылку в свойство [Annotations](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/annotations) объекта Page.
1. Наконец, сохраните обновленный PDF с помощью метода [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) объекта Document.

Приведенный ниже фрагмент кода показывает, как создать ссылку на приложение в файле PDF.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// Открыть документ
Document document = new Document(dataDir + "CreateApplicationLink.pdf");

// Создать ссылку
Page page = document.Pages[1];
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
link.Action = new LaunchAction(document, dataDir + "CreateApplicationLink.pdf");
page.Annotations.Add(link);

dataDir = dataDir + "CreateApplicationLink_out.pdf";
// Сохранить обновленный документ
document.Save(dataDir);
```
### Создание ссылки на документ PDF в файле PDF

Aspose.PDF для .NET позволяет добавлять ссылку на внешний файл PDF, так что вы можете связывать несколько документов вместе. Чтобы создать ссылку на документ PDF:

1. Сначала создайте объект [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Затем получите конкретную [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page), на которую вы хотите добавить ссылку.
1. Создайте объект [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) с использованием объектов Page и [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle).
1. Установите атрибуты ссылки с помощью объекта [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation).
1. Установите свойство Action на объект [GoToRemoteAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoremoteaction).
1.
1. Добавьте ссылку в коллекцию аннотаций объекта Page.
1. Сохраните обновленный PDF с помощью метода [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) объекта Document.

Следующий фрагмент кода показывает, как создать ссылку в документе PDF.

 ```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Открыть документ
Document document = new Document(dataDir + "CreateDocumentLink.pdf");
// Создать ссылку
Page page = document.Pages[1];
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
link.Action = new GoToRemoteAction(dataDir + "RemoveOpenAction.pdf", 1);
page.Annotations.Add(link);
dataDir = dataDir + "CreateDocumentLink_out.pdf";
// Сохранить обновленный документ
document.Save(dataDir);
```

<script type="application/ld+json">

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

