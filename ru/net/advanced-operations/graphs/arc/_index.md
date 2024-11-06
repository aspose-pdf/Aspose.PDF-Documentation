---
title: Добавление объекта дуги в файл PDF
linktitle: Добавить дугу
type: docs
weight: 10
url: ru/net/add-arc/
description: Эта статья объясняет, как создать объект дуги в вашем PDF с помощью Aspose.PDF для .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Добавление объекта дуги в файл PDF",
    "alternativeHeadline": "Как создать дугу в файле PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, дуга в pdf",
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
    "url": "/net/add-arc/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-arc/"
    },
    "dateModified": "2022-02-04",
    "description": "Эта статья объясняет, как создать объект дуги в вашем PDF с помощью Aspose.PDF для .NET."
}
</script>

Следующий пример кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Добавление объекта дуги

Aspose.PDF для .NET поддерживает добавление графических объектов (например, граф, линия, прямоугольник и т.д.) в PDF-документы. Также предлагается функция заливки объекта дуги определенным цветом.

Следуйте шагам ниже:

1. Создайте экземпляр [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)

1. Создайте [графический объект](https://reference.aspose.com/pdf/net/aspose.pdf.drawing) с определенными размерами

1. Установите [границу](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) для графического объекта

1. Добавьте [графический объект](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) в коллекцию параграфов страницы

1. Сохраните наш PDF-файл

Следующий пример кода показывает, как добавить объект [дуги](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/arc).

```csharp
 public static void Arc()
        {
            // Создайте экземпляр Document
            var document = new Document();

            // Добавьте страницу в коллекцию страниц PDF-файла
            var page = document.Pages.Add();

            // Создайте графический объект с определенными размерами
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // Установите границу для графического объекта
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var arc1 = new Arc(100, 100, 95, 0, 90);
            arc1.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(arc1);

            var arc2 = new Arc(100, 100, 90, 70, 180);
            arc2.GraphInfo.Color = Color.DarkBlue;
            graph.Shapes.Add(arc2);

            var arc3 = new Arc(100, 100, 85, 120, 210);
            arc3.GraphInfo.Color = Color.Red;
            graph.Shapes.Add(arc3);

            // Добавьте графический объект в коллекцию параграфов страницы
            page.Paragraphs.Add(graph);

            // Сохраните PDF-файл
            document.Save(_dataDir + "DrawingArc_out.pdf");

        }
```
## Создание объекта закрашенной дуги

Следующий пример показывает, как добавить объект дуги, который закрашен цветом и имеет определенные размеры.

```csharp
        public static void ArcFilled()
        {
            // Создание экземпляра документа
            var document = new Document();

            // Добавление страницы в коллекцию страниц PDF файла
            var page = document.Pages.Add();

            // Создание объекта рисования с определенными размерами
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // Установка границ для объекта рисования
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var arc = new Arc(100, 100, 95, 0, 90);
            arc.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(arc);

            var line = new Line(new float[] { 195, 100, 100, 100, 100, 195 });
            line.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(line);

            // Добавление объекта графики в коллекцию абзацев страницы
            page.Paragraphs.Add(graph);

            // Сохранение PDF файла
            document.Save(_dataDir + "ExampleFilledArc_out.pdf");

        }
```
Давайте посмотрим на результат добавления закрашенной дуги:

![Закрашенная дуга](filled_arc.png)

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


