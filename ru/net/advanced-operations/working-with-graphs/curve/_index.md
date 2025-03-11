---
title: Добавление объекта кривой в PDF-файл
linktitle: Добавить кривую
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ru/net/add-curve/
description: В этой статье объясняется, как создать объект кривой в вашем PDF-файле с помощью Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Curve Object to PDF file",
    "alternativeHeadline": "Create Curves in PDFs",
    "abstract": "Новая функция в Aspose.PDF для .NET позволяет разработчикам создавать и управлять объектами кривых внутри PDF-документов, используя кривые Безье для плавной графики. Это улучшение упрощает создание как простых, так и заполненных кривых, предоставляя мощный инструмент для генерации сложных визуальных представлений в PDF-файлах с сохранением контроля над размерами и стилем",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Curve, Curve object, Bezier curves, Aspose.PDF for .NET, PDF document generation, Drawing object, Filled Curve, Graph object, PDF manipulation, ASP.NET PDF",
    "wordcount": "500",
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
    "url": "/net/add-curve/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-curve/"
    },
    "dateModified": "2024-11-25",
    "description": "Этот текст объясняет, как создать объект кривой в вашем PDF-файле с помощью Aspose.PDF для .NET."
}
</script>

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Добавление объекта кривой

Графический [объект кривой](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/curve) представляет собой связное объединение проективных линий, каждая из которых встречается с тремя другими в обычных двойных точках.

Aspose.PDF for .NET показывает, как использовать кривые Безье в ваших графиках.
Кривые Безье широко используются в компьютерной графике для моделирования плавных кривых. Кривая полностью содержится в выпуклой оболочке своих контрольных точек, точки могут быть графически отображены и использованы для интуитивного управления кривой.
Вся кривая содержится в четырёхугольнике, углы которого являются четырьмя заданными точками (их выпуклая оболочка).

В этой статье мы рассмотрим просто графические кривые и заполненные кривые, которые вы можете создать в своём PDF-документе.

Выполните следующие действия:

1. Создайте экземпляр [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Создайте [объект рисования](https://reference.aspose.com/pdf/net/aspose.pdf.drawing) с определёнными размерами.
1. Установите [границу](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) для объекта рисования.
1. Добавьте [графический](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) объект в коллекцию абзацев страницы.
1. Сохраните наш PDF-файл.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleCurve()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Drawing object with certain dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

        // Set border for Drawing object
        var borderInfo = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Green);
        graph.Border = borderInfo;

        // Create a curve and set its properties
        var curve1 = new Aspose.Pdf.Drawing.Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 })
        {
            GraphInfo = 
            { 
                Color = Aspose.Pdf.Color.GreenYellow 
            }
        };

        // Add the curve to the graph shapes
        graph.Shapes.Add(curve1);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "DrawingCurve1_out.pdf");
    }
}

```

На следующем рисунке показан результат выполнения нашего фрагмента кода:

![Рисование кривой](drawing_curve.png)

## Создание заполненного объекта кривой

Этот пример показывает, как добавить объект кривой, который заполнен цветом.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CurveFilled()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Drawing object with certain dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

        // Set border for Drawing object
        var borderInfo = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Green);
        graph.Border = borderInfo;

        // Create a curve and set fill color
        var curve1 = new Aspose.Pdf.Drawing.Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 })
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.GreenYellow 
            }
        };

        // Add the curve to the graph shapes
        graph.Shapes.Add(curve1);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "DrawingCurve2_out.pdf");
    }
}
```

Посмотрите на результат добавления заполненной кривой:

![Заполненная кривая](filled_curve.png)

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