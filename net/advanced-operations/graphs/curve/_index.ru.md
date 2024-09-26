---
title: Добавление объекта кривой в файл PDF
linktitle: Добавление кривой
type: docs
weight: 30
url: /net/add-curve/
description: Эта статья объясняет, как создать объект кривой в вашем PDF с использованием Aspose.PDF для .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Добавление объекта кривой в файл PDF",
    "alternativeHeadline": "Как создать объект кривой в файле PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, .net, кривая в pdf",
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
    "url": "/net/add-curve/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-curve/"
    },
    "dateModified": "2022-02-04",
    "description": "Эта статья объясняет, как создать объект кривой в вашем PDF с использованием Aspose.PDF для .NET."
}
</script>

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Добавить объект Curve

Граф [Curve](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/curve) представляет собой соединённое объединение проективных линий, каждая из которых пересекает три другие в обычных двойных точках.

Aspose.PDF для .NET показывает, как использовать кривые Безье в ваших графиках.
Кривые Безье широко используются в компьютерной графике для моделирования плавных кривых. Кривая полностью содержится в выпуклой оболочке её контрольных точек, точки могут быть визуально отображены и использованы для интуитивного управления кривой.
Вся кривая содержится в четырёхугольнике, углы которого являются четырьмя данными точками (их выпуклая оболочка).

В этой статье мы рассмотрим простые графические кривые и заполненные кривые, которые вы можете создать в вашем PDF-документе.

Следуйте шагам ниже:

1. Создайте экземпляр [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. Установите [границу](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) для объекта Drawing

1. Добавьте объект [График](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) в коллекцию параграфов страницы

1. Сохраните наш PDF файл

```csharp
 public static void ExampleCurve()
        {
            // Создание экземпляра документа
            var document = new Document();

            // Добавление страницы в коллекцию страниц PDF файла
            var page = document.Pages.Add();

            // Создание объекта Drawing с определенными размерами
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

            // Установка границ для объекта Drawing
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 });
            curve1.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(curve1);

            // Добавление объекта График в коллекцию параграфов страницы
            page.Paragraphs.Add(graph);

            // Сохранение PDF файла
            document.Save(_dataDir + "DrawingCurve1_out.pdf");
        }
```
Следующее изображение показывает результат, выполненный с помощью нашего фрагмента кода:

![Рисунок Кривой](drawing_curve.png)

## Создание объекта Заполненной Кривой

Этот пример показывает, как добавить объект Кривая, который заполнен цветом.

```csharp
      public static void CurveFilled()
        {
            // Создание экземпляра Document
            var document = new Document();

            // Добавление страницы в коллекцию страниц PDF файла
            var page = document.Pages.Add();

            // Создание объекта Рисования с определенными размерами
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

            // Установка границ для объекта Рисования
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 });
            curve1.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(curve1);

            // Добавление объекта Графика в коллекцию параграфов страницы
            page.Paragraphs.Add(graph);

            // Сохранение PDF файла
            document.Save(_dataDir + "DrawingCurve2_out.pdf");
        }
```
Посмотрите на результат добавления заполненной кривой:

![Заполненная кривая](filled_curve.png)

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Библиотека Aspose.PDF для .NET",
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

