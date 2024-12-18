---
title: Добавление объекта линии в PDF-файл
linktitle: Добавить линию
type: docs
weight: 40
url: /ru/net/add-line/
description: Эта статья объясняет, как создать объект линии в вашем PDF с использованием Aspose.PDF для .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Добавление объекта линии в PDF-файл",
    "alternativeHeadline": "Как создать объект линии в PDF-файле",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, c#, линия в pdf",
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
    "url": "/net/add-line/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-line/"
    },
    "dateModified": "2022-02-04",
    "description": "Эта статья объясняет, как создать объект линии в вашем PDF с использованием Aspose.PDF для .NET."
}
</script>

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Добавление объекта Line

Aspose.PDF для .NET поддерживает возможность добавления графических объектов (например, граф, линия, прямоугольник и т.д.) в PDF-документы. Вы также можете добавить объект [Line](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/line), где можно указать шаблон пунктира, цвет и другие параметры форматирования для элемента Line.

Следуйте следующим шагам:

1. Создайте новый PDF [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)

1. Добавьте [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) в коллекцию страниц PDF-файла

1. Создайте экземпляр [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph).

1. Добавьте объект Graph в коллекцию абзацев экземпляра страницы.

1. Создайте экземпляр [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle).

1. Установите ширину линии.
1. Сохраните ваш PDF файл.

Следующий фрагмент кода показывает, как добавить объект [Прямоугольник](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle), который заполнен цветом.

```csharp
        public static void AddLineObjectToPDF()
        {
            // Создать экземпляр документа
            var document = new Document();

            // Добавить страницу в коллекцию страниц PDF файла
            var page = document.Pages.Add();

            // Создать экземпляр графа
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

            // Добавить объект графа в коллекцию параграфов экземпляра страницы
            page.Paragraphs.Add(graph);

            // Создать экземпляр прямоугольника
            var line = new Line(new float[] { 100, 100, 200, 100 });

            // Указать цвет заливки для объекта графа
            line.GraphInfo.DashArray = new int[] { 0, 1, 0 };
            line.GraphInfo.DashPhase = 1;

            // Добавить объект прямоугольника в коллекцию форм объекта графа
            graph.Shapes.Add(line);

            // Сохранить PDF файл
            document.Save(_dataDir + "AddLineObject_out.pdf");
        }
```
![Add Line](add_line.png)

## Как добавить пунктирную пунктирную линию в ваш PDF документ

```csharp
        public static void DashLengthInBlackAndDashLengthInWhite()
        {
            // Создать экземпляр документа
            var document = new Document();

            // Добавить страницу в коллекцию страниц PDF файла
            var page = document.Pages.Add();

            // Создать объект рисования с определенными размерами
            var canvas = new Aspose.Pdf.Drawing.Graph(100, 400);
            // Добавить объект рисования в коллекцию параграфов экземпляра страницы
            page.Paragraphs.Add(canvas);

            // Создать объект линии
            var line = new Line(new float[] { 100, 100, 200, 100 });
            // Установить цвет для объекта линии
            line.GraphInfo.Color = Color.Red;
            // Указать массив чередования для объекта линии
            line.GraphInfo.DashArray = new int[] { 0, 1, 0 };
            // Установить фазу чередования для экземпляра линии
            line.GraphInfo.DashPhase = 1;
            // Добавить линию в коллекцию форм объекта рисования
            canvas.Shapes.Add(line);
            // Сохранить PDF файл
            document.Save(_dataDir + "DashLengthInBlackAndDashLengthInWhite_out.pdf");
        }
```
![Пунктирная линия](dash_line.png)

## Рисуем линию через всю страницу

Мы также можем использовать объект линии, чтобы нарисовать крест, начиная с левого нижнего угла до правого верхнего и с левого верхнего угла до правого нижнего.

Пожалуйста, ознакомьтесь с следующим фрагментом кода, чтобы выполнить это требование.

```csharp
   public static void ExampleLineAcrossPage()
        {

            // Создаем экземпляр документа
            var document = new Document();

            // Добавляем страницу в коллекцию страниц PDF файла
            var page = document.Pages.Add();
            // Устанавливаем поля страницы со всех сторон равными 0

            page.PageInfo.Margin.Left = 0;
            page.PageInfo.Margin.Right = 0;
            page.PageInfo.Margin.Bottom = 0;
            page.PageInfo.Margin.Top = 0;

            // Создаем объект Graph с шириной и высотой, равными размерам страницы
            var graph = new Aspose.Pdf.Drawing.Graph(
                (float)page.PageInfo.Width,
                (float)page.PageInfo.Height);

            // Создаем первый объект линии, начиная с нижнего левого угла до верхнего правого угла страницы
            var line = new Line(
                    new float[]{
                        (float)page.Rect.LLX, 0,
                        (float)page.PageInfo.Width,
                        (float)page.Rect.URY });

            // Добавляем линию в коллекцию форм объекта Graph
            graph.Shapes.Add(line);
            // Рисуем линию от верхнего левого угла страницы до нижнего правого угла
            var line2 = new Line(
                new float[]{ 0,
                    (float) page.Rect.URY,
                    (float) page.PageInfo.Width,
                    (float) page.Rect.LLX });

            // Добавляем линию в коллекцию форм объекта Graph
            graph.Shapes.Add(line2);

            // Добавляем объект Graph в коллекцию абзацев страницы
            page.Paragraphs.Add(graph);

            // Сохраняем PDF файл
            document.Save(_dataDir + "ExampleLineAcrossPage_out.pdf");
        }
```
![Рисунок Линии](draw_line.png)

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
    "applicationCategory": "Библиотека для обработки PDF для .NET",
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


