---
title: Проверка границ формы в коллекции Aspose.Pdf.Drawing.Graph.Shapes
type: docs
weight: 10
url: /ru/net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Узнайте, как проверить границы формы при вставке в коллекцию Aspose.Pdf.Drawing.Graph.Shapes, чтобы убедиться, что она помещается в родительский контейнер.
lastmod: "2025-02-28"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Checking Element Bounds in Aspose.Pdf.Drawing.Graph.Shapes Collection",
    "alternativeHeadline": "Configurable Bounds Checking for Aspose.PDF Shapes with Exception Mode",
    "abstract": "Функция проверки границ Aspose.PDF for .NET в коллекции `Drawing.Graph.Shapes` автоматически проверяет размеры элементов относительно родительских контейнеров, предотвращая переполнение макета. Она вызывает исключения, когда элементы превышают пределы контейнера, обеспечивая строгие ограничения по размеру во время вставки для точного форматирования PDF и повышения точности дизайна.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1000",
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
    "url": "/net/aspose-pdf-drawing-graph-shapes-bounds-check/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/aspose-pdf-drawing-graph-shapes-bounds-check/"
    },
    "dateModified": "2025-02-28",
    "description": ""
}
</script>

## Введение
Этот документ предоставляет подробное руководство по использованию функции проверки границ в коллекции Aspose.Pdf.Drawing.Graph.Shapes. Эта функция гарантирует, что элементы помещаются в родительский контейнер и может быть настроена на выброс исключения, если компонент не помещается. Мы пройдемся по шагам реализации этой функциональности и предоставим полный пример.

## Предварительные требования
Вам понадобятся следующие компоненты:
* Visual Studio 2019 или более поздняя версия
* Aspose.PDF for .NET 25.3 или более поздняя версия
* Пример PDF-файла, содержащего несколько страниц

Вы можете скачать библиотеку Aspose.PDF for .NET с официального сайта или установить ее с помощью диспетчера пакетов NuGet в Visual Studio.

## Шаги
Вот шаги для выполнения задачи:
1. Создайте новый документ и добавьте страницу.
2. Создайте объект `Graph` с заданными размерами.
3. Создайте объект `Shape` с заданными размерами.
4. Установите `BoundsCheckMode` в `ThrowExceptionIfDoesNotFit`.
5. Попытайтесь добавить форму в граф.

Давайте посмотрим, как реализовать эти шаги в коде C#.

### Шаг 1: Создайте новый документ и добавьте страницу
Сначала создайте новый PDF-документ и добавьте страницу в него.

```csharp
using (var doc = new Aspose.Pdf.Document())
{
    Aspose.Pdf.Page page = doc.Pages.Add();
}
```

### Шаг 2: Создайте объект Graph с заданными размерами
Затем создайте объект `Graph` с шириной и высотой 100 единиц. Разместите граф на 10 единиц от верхней части и на 15 единиц от левой стороны страницы. Добавьте черную рамку к графу.

```csharp
var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
{
    Top = 10,
    Left = 15,
    Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
};
page.Paragraphs.Add(graph);
```

### Шаг 3: Создайте объект Aspose.Pdf.Drawing.Shape (например, Aspose.Pdf.Drawing.Rectangle) с заданными размерами
Создайте объект Rectangle с шириной и высотой 50 единиц. Разместите прямоугольник в (-1, 0), что находится за пределами границ графа.

```csharp
Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
{
    GraphInfo =
    {
        FillColor = Aspose.Pdf.Color.Tomato
    }
};
```

### Шаг 4: Установите BoundsCheckMode в ThrowExceptionIfDoesNotFit
Установите `BoundsCheckMode` в `ThrowExceptionIfDoesNotFit`, чтобы гарантировать, что будет выброшено исключение, если прямоугольник не помещается в граф.

```csharp
graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);
```

### Шаг 5: Попытайтесь добавить прямоугольник в граф
Попытайтесь добавить прямоугольник в граф. Это вызовет `Aspose.Pdf.BoundsOutOfRangeException`, потому что прямоугольник не помещается в размеры графа.

```csharp
graph.Shapes.Add(rect);
```

## Вывод
После выполнения кода ожидаемый вывод будет `Aspose.Pdf.BoundsOutOfRangeException` с сообщением:

```
Bounds not fit. Container dimensions: 100x100
```

## Устранение неполадок
В случае возникновения проблем вот несколько советов:
* Убедитесь, что `BoundsCheckMode` установлен правильно.
* Проверьте, что размеры элемента и контейнера точны.
* Проверьте позиционирование элемента внутри контейнера.

## Полный пример
Ниже приведен полный пример, демонстрирующий все шаги в совокупности:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckShapeBounds()
{
    // Create a new document and add a page
    using (var doc = new Aspose.Pdf.Document())
    {
        Aspose.Pdf.Page page = doc.Pages.Add();
        
        // Create a Graph Object with Specified Dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
        {
            Top = 10,
            Left = 15,
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
        };
        page.Paragraphs.Add(graph);
        
        // Create a Aspose.Pdf.Drawing.Shape object (for example, Aspose.Pdf.Drawing.Rectangle) with specified dimensions
        Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
        {
            GraphInfo =
            {
                FillColor = Aspose.Pdf.Color.Tomato
            }
        };
        
        // Set the BoundsCheckMode to ThrowExceptionIfDoesNotFit
        graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);
        
        // Attempt to add the rectangle to the graph
        graph.Shapes.Add(rect);
    }
}```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckShapeBounds()
{
    // Create a new document and add a page
    using var doc = new Aspose.Pdf.Document();
    Aspose.Pdf.Page page = doc.Pages.Add();

    // Create a Graph Object with Specified Dimensions
    var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
    {
        Top = 10,
        Left = 15,
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
    };
    page.Paragraphs.Add(graph);

    // Create a Aspose.Pdf.Drawing.Shape object (for example, Aspose.Pdf.Drawing.Rectangle) with specified dimensions
    Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
    {
        GraphInfo =
        {
            FillColor = Aspose.Pdf.Color.Tomato
        }
    };

    // Set the BoundsCheckMode to ThrowExceptionIfDoesNotFit
    graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);

    // Attempt to add the rectangle to the graph
    graph.Shapes.Add(rect);
}
```
{{< /tab >}}
{{< /tabs >}}

## Заключение
Функция проверки границ в коллекции 'Aspose.Pdf.Drawing.Graph.Shapes' является мощным инструментом для обеспечения того, чтобы элементы помещались в родительские контейнеры. Вы можете предотвратить проблемы с макетом в ваших PDF-документах, установив BoundsCheckMode в ThrowExceptionIfDoesNotFit. Эта функция особенно полезна в сценариях, где критически важно точное позиционирование и размер элементов. Для получения дополнительных сведений посетите [официальную документацию](https://docs.aspose.com/pdf/net/).