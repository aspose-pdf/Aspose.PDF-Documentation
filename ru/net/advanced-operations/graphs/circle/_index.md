---
title: Добавление объекта круга в файл PDF
linktitle: Добавление круга
type: docs
weight: 20
url: ru/net/add-circle/
description: Эта статья объясняет, как создать объект круга в вашем PDF с помощью Aspose.PDF для .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Добавление объекта круга в файл PDF",
    "alternativeHeadline": "Как создать объект круга в файле PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, круг в pdf",
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
    "url": "/net/add-circle/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-circle/"
    },
    "dateModified": "2022-02-04",
    "description": "Эта статья объясняет, как создать объект круга в вашем PDF с помощью Aspose.PDF для .NET."
}
</script>
Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Добавление объекта Circle

Как и столбчатые диаграммы, круговые диаграммы могут использоваться для отображения данных в ряде отдельных категорий. В отличие от столбчатых диаграмм, однако, круговые диаграммы можно использовать только тогда, когда у вас есть данные по всем категориям, которые составляют целое. Давайте рассмотрим добавление объекта [Circle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/circle) с Aspose.PDF для .NET.

Следуйте шагам ниже:

1. Создайте экземпляр [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)

1. Создайте [Drawing object](https://reference.aspose.com/pdf/net/aspose.pdf.drawing) с определенными размерами

1. Установите [Border](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) для Drawing object

1. Добавьте [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) объект в коллекцию абзацев страницы

1. Сохраните наш PDF файл

```csharp
        public static void Circle()
        {
            // Создайте экземпляр Document
            var document = new Document();

            // Добавьте страницу в коллекцию страниц PDF файла
            var page = document.Pages.Add();

            // Создайте Drawing object с определенными размерами
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);
            // Установите границу для Drawing object
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var circle = new Circle(100, 100, 40);

            circle.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(circle);

            // Добавьте Graph объект в коллекцию абзацев страницы
            page.Paragraphs.Add(graph);

            // Сохраните PDF файл
            document.Save(_dataDir + "DrawingCircle1_out.pdf");
        }
```
Наш нарисованный круг будет выглядеть так:

![Рисунок Круга](drawing_circle.png)

## Создание объекта закрашенного круга

Этот пример показывает, как добавить объект Круг, который заполнен цветом.

```csharp
        public static void CircleFilled()
        {
            // Создание экземпляра документа
            var document = new Document();

            // Добавление страницы в коллекцию страниц PDF файла
            var page = document.Pages.Add();

            // Создание объекта Рисование с определенными размерами
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

            // Установка границы для объекта Рисование
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var circle = new Circle(100, 100, 40);
            circle.GraphInfo.Color = Color.GreenYellow;
            circle.GraphInfo.FillColor = Color.Green;
            circle.Text = new TextFragment("Круг");

            graph.Shapes.Add(circle);

            // Добавление объекта Графика в коллекцию абзацев страницы
            page.Paragraphs.Add(graph);

            // Сохранение файла PDF
            document.Save(_dataDir + "DrawingCircle2_out.pdf");
        }
```
Давайте посмотрим на результат добавления закрашенного круга:

![Закрашенный круг](filled_circle.png)

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


