---
title: Добавление объекта Эллипс в файл PDF
linktitle: Добавить Эллипс
type: docs
weight: 60
url: ru/net/add-ellipse/
description: Эта статья объясняет, как создать объект Эллипс в вашем PDF с использованием Aspose.PDF для .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Добавление объекта Эллипс в файл PDF",
    "alternativeHeadline": "Как создать объект Эллипс в файле PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, эллипс в pdf",
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
    "url": "/net/add-ellipse/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-ellipse/"
    },
    "dateModified": "2022-02-04",
    "description": "Эта статья объясняет, как создать объект Эллипс в вашем PDF с использованием Aspose.PDF для .NET."
}
</script>
Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Добавление объекта Ellipse

Aspose.PDF для .NET поддерживает добавление объектов [Ellipse](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/ellipse) в документы PDF. Также предлагается функция заливки объекта эллипса определенным цветом.

```csharp
 public static void Ellipse()
        {
            // Создание экземпляра документа
            var document = new Document();

            // Добавление страницы в коллекцию страниц PDF файла
            var page = document.Pages.Add();

            // Создание объекта Drawing с определенными размерами
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);

            // Установка границы для объекта Drawing
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var ellipse1 = new Ellipse(150, 100, 120, 60);
            ellipse1.GraphInfo.Color = Color.GreenYellow;
            ellipse1.Text = new TextFragment("Ellipse");
            graph.Shapes.Add(ellipse1);

            var ellipse2 = new Ellipse(50, 50, 18, 300);
            ellipse2.GraphInfo.Color = Color.DarkRed;

            graph.Shapes.Add(ellipse2);

            // Добавление объекта Graph в коллекцию параграфов страницы
            page.Paragraphs.Add(graph);

            // Сохранение файла PDF
            document.Save(_dataDir + "DrawingEllipse_out.pdf");

        }
```
![Добавить эллипс](ellipse.png)

## Создание объекта закрашенного эллипса

Следующий фрагмент кода показывает, как добавить объект [Ellipse](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/ellipse), который закрашен цветом.

```csharp
     public static void EllipseFilled()
        {
            // Создание экземпляра документа
            var document = new Document();

            // Добавление страницы в коллекцию страниц PDF файла
            var page = document.Pages.Add();

            // Создание объекта рисования с определенными размерами
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);

            // Установка границы для объекта рисования
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var ellipse1 = new Ellipse(100, 100, 120, 180);
            ellipse1.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(ellipse1);

            var ellipse2 = new Ellipse(200, 150, 180, 120);
            ellipse2.GraphInfo.FillColor = Color.DarkRed;
            graph.Shapes.Add(ellipse2);

            // Добавление объекта графики в коллекцию абзацев страницы
            page.Paragraphs.Add(graph);

            // Сохранение PDF файла
            document.Save(_dataDir + "DrawingEllipse_out.pdf");
        }
```
![Заполненный Эллипс](fill_ellipse.png)

## Добавление текста внутрь эллипса

Aspose.PDF для .NET поддерживает добавление текста внутрь графического объекта. Свойство Text графического объекта предоставляет возможность установить текст графического объекта. Следующий код показывает, как добавить текст внутрь объекта Прямоугольник.

```csharp
        public static void EllipseWithText()
        {
            // Создание экземпляра документа
            var document = new Document();

            // Добавление страницы в коллекцию страниц PDF файла
            var page = document.Pages.Add();

            // Создание объекта Рисование с определенными размерами
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // Установка границы для объекта Рисование
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var textFragment = new TextFragment("Эллипс");
            textFragment.TextState.Font = FontRepository.FindFont("Helvetica");
            textFragment.TextState.FontSize = 24;

            var ellipse1 = new Ellipse(100, 100, 120, 180);
            ellipse1.GraphInfo.FillColor = Color.GreenYellow;
            ellipse1.Text = textFragment;
            graph.Shapes.Add(ellipse1);


            var ellipse2 = new Ellipse(200, 150, 180, 120);
            ellipse2.GraphInfo.FillColor = Color.DarkRed;
            ellipse2.Text = textFragment;
            graph.Shapes.Add(ellipse2);

            // Добавление объекта Графика в коллекцию параграфов страницы
            page.Paragraphs.Add(graph);

            // Сохранение файла PDF
            document.Save(_dataDir + "DrawingEllipseText_out.pdf");

        }
 ```

![Текст внутри Эллипса](text_ellipse.png)

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

