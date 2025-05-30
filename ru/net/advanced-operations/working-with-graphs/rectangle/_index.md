---
title: Добавление объекта прямоугольника в PDF-файл
linktitle: Добавить прямоугольник
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ru/net/add-rectangle/
description: В этой статье объясняется, как создать объект Rectangle в вашем PDF-файле с помощью Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Rectangle Object to PDF file",
    "alternativeHeadline": "Add Rectangle to PDF file",
    "abstract": "Новая функция в Aspose.PDF для .NET позволяет пользователям легко добавлять объекты Rectangle в PDF-документы. Эта функциональность включает возможности настройки прямоугольников с использованием сплошных цветов, градиентных заливок и прозрачности, обеспечивая улучшенную визуальную настройку и управление слоями для содержимого PDF",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Rectangle, PDF document generation, Aspose.PDF for .NET, Rectangle object, fill rectangle, gradient color fill, Z-Order control, alpha channel color, graph objects in PDF, create filled rectangle",
    "wordcount": "1263",
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
    "url": "/net/add-rectangle/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-rectangle/"
    },
    "dateModified": "2024-11-25",
    "description": "Этот статья объясняет, как создать объект Rectangle для вашего PDF-файла с помощью Aspose.PDF для .NET."
}
</script>

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Добавление объекта прямоугольника

Aspose.PDF for .NET поддерживает функцию добавления графических объектов (например, графика, линии, прямоугольника и т.д.) в PDF-документы. Вы также получаете возможность добавить объект [Rectangle](https://reference.aspose.com/pdf/ru/net/aspose.pdf.drawing/rectangle), где вам также предлагается возможность заполнить объект прямоугольника определённым цветом, управлять Z-порядком, добавить градиентную заливку цветом и т. д.

Давайте сначала рассмотрим возможность создания объекта Rectangle.

Выполните следующие шаги:

1. Создайте новый PDF [документ](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document).
1. Добавьте [страницу](https://reference.aspose.com/pdf/ru/net/aspose.pdf/page) в коллекцию страниц PDF-файла.
1. Добавьте фрагмент [текста](https://reference.aspose.com/pdf/ru/net/aspose.pdf/texfragment) в коллекцию абзацев экземпляра страницы.
1. Создайте экземпляр [Graph](https://reference.aspose.com/pdf/ru/net/aspose.pdf.drawing/graph).
1. Установите границу для [рисунка](https://reference.aspose.com/pdf/ru/net/aspose.pdf.drawing).
1. Создайте объект Rectangle.

1. Добавьте объект [Rectangle](https://reference.aspose.com/pdf/ru/net/aspose.pdf.drawing/rectangle) в коллекцию фигур объекта Graph.
1. Добавьте графический объект в коллекцию абзацев экземпляра страницы.
1. Добавьте фрагмент [текста](https://reference.aspose.com/pdf/ru/net/aspose.pdf/texfragment) в коллекцию абзацев экземпляра страницы.

1. Сохраните ваш PDF-файл.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRectangle(Aspose.Pdf.Page page, float x, float y, float width, float height, Aspose.Pdf.Color color, int zIndex)
{
    // Create a Graph object with dimensions matching the specified rectangle
    var graph = new Aspose.Pdf.Drawing.Graph(width, height)
    {
        // Prevent the graph from repositioning automatically
        IsChangePosition = false,
        // Set the Left coordinate position for the Graph instance
        Left = x,
        // Set the Top coordinate position for the Graph instance
        Top = y
    };

    // Create a Rectangle object inside the Graph
    var rect = new Aspose.Pdf.Drawing.Rectangle(0, 0, width, height)
    {
        // Set the fill color of the rectangle
        GraphInfo =
        {
            FillColor = color,
            // Set the border color of the rectangle
            Color = color
        }
    };

    // Add the rectangle to the Shapes collection of the Graph
    graph.Shapes.Add(rect);

    // Set the Z-Index for the Graph object to control layering
    graph.ZIndex = zIndex;

    // Add the Graph object to the Paragraphs collection of the page
    page.Paragraphs.Add(graph);
}
```

![Создание прямоугольника](/create_rectangle.png)

## Создание заполненного объекта прямоугольника

Aspose.PDF for .NET также предлагает возможность заполнения объекта прямоугольника определённым цветом.

В следующем фрагменте кода показано, как добавить объект [Rectangle](https://reference.aspose.com/pdf/ru/net/aspose.pdf.drawing/rectangle), который заполнен цветом.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RectangleFilled()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Graph instance
        var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

        // Add graph object to paragraphs collection of page instance
        page.Paragraphs.Add(graph);

        // Create Rectangle instance with specified dimensions
        var rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 200, 120)
        {
            // Specify fill color for the Rectangle object
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.Red 
            }
        };

        // Add rectangle object to shapes collection of Graph object
        graph.Shapes.Add(rect);

        // Save PDF document
        document.Save(dataDir + "CreateFilledRectangle_out.pdf");
    }
}
```

Посмотрите на результат заполнения прямоугольника сплошным цветом:

![Заполненный прямоугольник](/fill_rectangle.png)

## Добавление рисунка с градиентной заливкой

Aspose.PDF for .NET поддерживает возможность добавления графических объектов в PDF-документы, и иногда требуется заполнить графические объекты градиентом цвета. Чтобы заполнить графические объекты градиентом цвета, нам нужно установить setPatterColorSpace с объектом gradientAxialShading следующим образом.

В следующем фрагменте кода показано, как добавить объект [Rectangle](https://reference.aspose.com/pdf/ru/net/aspose.pdf.drawing/rectangle), который заполнен градиентом цвета.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateFilledRectangleGradientFill()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Graph instance
        var graph = new Aspose.Pdf.Drawing.Graph(400, 400);

        // Add graph object to paragraphs collection of page instance
        page.Paragraphs.Add(graph);

        // Create Rectangle instance
        var rect = new Aspose.Pdf.Drawing.Rectangle(0, 0, 300, 300);

        // Create a gradient fill color
        var gradientColor = new Aspose.Pdf.Color();
        var gradientSettings = new Aspose.Pdf.Drawing.GradientAxialShading(Aspose.Pdf.Color.Red, Aspose.Pdf.Color.Blue)
        {
            Start = new Aspose.Pdf.Point(0, 0),
            End = new Aspose.Pdf.Point(350, 350)
        };
        gradientColor.PatternColorSpace = gradientSettings;

        // Apply gradient fill color to the rectangle
        rect.GraphInfo.FillColor = gradientColor;

        // Add rectangle object to shapes collection of Graph object
        graph.Shapes.Add(rect);

        // Save PDF document
        document.Save(dataDir + "CreateFilledRectangleGradient_out.pdf");
    }
}
```

![Градиентный прямоугольник](/gradient.png)

## Создание прямоугольника с альфа-каналом цвета

Aspose.PDF for .NET поддерживает заполнение объекта прямоугольника определённым цветом. Объект прямоугольника также может иметь альфа-канал цвета для придания прозрачного вида. В следующем фрагменте кода показано, как добавить объект [Rectangle](https://reference.aspose.com/pdf/ru/net/aspose.pdf.drawing/rectangle) с альфа-каналом цвета.

Пиксели изображения могут хранить информацию об их непрозрачности вместе со значением цвета. Это позволяет создавать изображения с прозрачными или полупрозрачными областями.

Вместо того чтобы делать цвет прозрачным, каждый пиксель хранит информацию о том, насколько он непрозрачен. Эти данные о непрозрачности называются альфа-каналом и обычно хранятся после цветовых каналов пикселя.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RectangleFilled_AlphaChannel()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Graph instance
        var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

        // Add graph object to paragraphs collection of page instance
        page.Paragraphs.Add(graph);

        // Create first rectangle with alpha channel fill color
        var rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 200, 120)
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.FromArgb(128, 244, 180, 0) 
            }
        };

        // Add the first rectangle to the shapes collection of the Graph object
        graph.Shapes.Add(rect);

        // Create second rectangle with different alpha channel fill color
        var rect1 = new Aspose.Pdf.Drawing.Rectangle(200, 150, 200, 100)
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.FromArgb(160, 120, 0, 120) 
            }
        };

        // Add the second rectangle to the shapes collection of the Graph object
        graph.Shapes.Add(rect1);

        // Save PDF document
        document.Save(dataDir + "CreateFilledRectangle_out.pdf");
    }
}
```

![Прямоугольник с альфа-каналом цвета](rectangle_color.png)

## Управление порядком Z объекта прямоугольника

Aspose.PDF for .NET поддерживает функцию добавления графических объектов (например, график, линия, прямоугольник и т.д.) в PDF-документы. При добавлении более одного экземпляра одного и того же объекта внутрь PDF-файла мы можем управлять их рендерингом, указывая порядок Z. Порядок Z также используется, когда нам нужно отобразить объекты друг над другом.

В следующем фрагменте кода показаны шаги для отображения объектов [Rectangle](https://reference.aspose.com/pdf/ru/net/aspose.pdf.drawing/rectangle) друг над другом.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRectangleZOrder()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Set size of PDF page
        page.SetPageSize(375, 300);

        // Set left and top margins for the page object as 0
        page.PageInfo.Margin.Left = 0;
        page.PageInfo.Margin.Top = 0;

        // Create rectangles with different colors and Z-Order values
        AddRectangle(page, 50, 40, 60, 40, Aspose.Pdf.Color.Red, 2);
        AddRectangle(page, 20, 20, 30, 30, Aspose.Pdf.Color.Blue, 1);
        AddRectangle(page, 40, 40, 60, 30, Aspose.Pdf.Color.Green, 0);

        // Save PDF document
        document.Save(dataDir + "ControlRectangleZOrder_out.pdf");
    }
}
```

![Управление порядком Z](control.png)

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