---
title: Добавление номера страницы в PDF с помощью C#
linktitle: Добавить номер страницы
type: docs
weight: 100
url: /net/add-page-number/
description: Aspose.PDF для .NET позволяет добавлять штамп с номером страницы в ваш PDF-файл с использованием класса PageNumber Stamp.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/get-and-set-page-properties/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Добавление номера страницы в PDF с помощью C#",
    "alternativeHeadline": "Как добавить штамп с номером страницы в PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, штамп с номером страницы",
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
    "url": "/net/add-page-number/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-page-number/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF для .NET позволяет добавлять штамп с номером страницы в ваш PDF-файл с использованием класса PageNumber Stamp."
}
</script>

Все документы должны иметь номера страниц. Номера страниц облегчают читателю поиск различных частей документа.
**Aspose.PDF для .NET** позволяет добавлять номера страниц с помощью PageNumberStamp.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

Вы можете использовать класс [PageNumberStamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp), чтобы добавить штамп с номером страницы в файл PDF.
Вы можете использовать класс [PageNumberStamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) для добавления штампа с номером страницы в PDF-файл.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Открыть документ
Document pdfDocument = new Document(dataDir+ "PageNumberStamp.pdf");

// Создать штамп с номером страницы
PageNumberStamp pageNumberStamp = new PageNumberStamp();
// Является ли штамп фоновым
pageNumberStamp.Background = false;
pageNumberStamp.Format = "Страница # из " + pdfDocument.Pages.Count;
pageNumberStamp.BottomMargin = 10;
pageNumberStamp.HorizontalAlignment = HorizontalAlignment.Center;
pageNumberStamp.StartingNumber = 1;
// Установить свойства текста
pageNumberStamp.TextState.Font = FontRepository.FindFont("Arial");
pageNumberStamp.TextState.FontSize = 14.0F;
pageNumberStamp.TextState.FontStyle = FontStyles.Bold;
pageNumberStamp.TextState.FontStyle = FontStyles.Italic;
pageNumberStamp.TextState.ForegroundColor = Color.Aqua;

// Добавить штамп на определённую страницу
pdfDocument.Pages[1].AddStamp(pageNumberStamp);

dataDir = dataDir + "PageNumberStamp_out.pdf";
// Сохранить выходной документ
pdfDocument.Save(dataDir);
```
## Пример вживую

[Добавление номеров страниц в PDF](https://products.aspose.app/pdf/page-number) - это бесплатное онлайн-приложение, которое позволяет изучить функциональность добавления номеров страниц.

[![Как добавить номер страницы в pdf с использованием C#](page_number.png)](https://products.aspose.app/pdf/page-number)

## Добавление/Удаление нумерации Бейтса

**Нумерация Бейтса** (также известная как штамповка Бейтса) используется в юридической, медицинской и бизнес-сферах для размещения идентификационных номеров и/или отметок даты/времени на изображениях и документах во время их сканирования или обработки, например, на стадии подготовки к судебному разбирательству или идентификации бизнес-квитанций. Этот процесс обеспечивает идентификацию, защиту и автоматическую последовательную нумерацию изображений или документов.

В настоящее время Aspose.PDF имеет ограниченную поддержку нумерации Бейтса. Эта функциональность будет обновлена согласно запросам клиентов.

### Как удалить нумерацию Бейтса

```csharp
static void Demo03()
{
    Document doc = new Document(@"C:\Samples\Sample-Document03.pdf");
    foreach (var page in doc.Pages)
    {
        var batesNum = page.Artifacts.First(ar => ar.CustomSubtype == "BatesN");
        page.Artifacts.Delete(batesNum);
    }
    doc.Save(@"C:\Samples\Sample-Document04.pdf");
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для .NET библиотеки",
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
    "applicationCategory": "Библиотека для манипулирования PDF для .NET",
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

