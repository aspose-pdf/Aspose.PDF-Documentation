---
title: Работа с векторной графикой
linktitle: Работа с векторной графикой
type: docs
weight: 120
url: /ru/net/working-with-vector-graphics/
description: Эта статья описывает особенности работы с инструментом GraphicsAbsorber с использованием C#.
lastmod: "2024-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Работа с GraphicsAbsorber",
    "alternativeHeadline": "Как получить позицию изображения в PDF файле",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, c#, GraphicsAbsorber в pdf",
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
    "url": "/net/working-with-vector-graphics/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-vector-graphics/"
    },
    "dateModified": "2022-02-04",
    "description": "Этот раздел описывает особенности работы с файлом PDF с использованием библиотеки C# GraphicsAbsorber."
}
</script>
В этой главе мы рассмотрим, как использовать мощный класс `GraphicsAbsorber` для взаимодействия с векторной графикой в документах PDF. Независимо от того, нужно ли вам перемещать, удалять или добавлять графику, это руководство покажет вам, как эффективно выполнять эти задачи. Давайте начнем!

## Введение<a name="introduction"></a>

Векторная графика является важным компонентом многих документов PDF, используемых для представления изображений, форм и других графических элементов. Aspose.PDF предоставляет класс `GraphicsAbsorber`, который позволяет разработчикам программно доступать и манипулировать этой графикой. Используя метод `Visit` класса `GraphicsAbsorber`, вы можете извлекать векторную графику с указанной страницы и выполнять различные операции, такие как перемещение, удаление или копирование её на другие страницы.

## 1. Извлечение графики с помощью `GraphicsAbsorber`<a name="extracting-graphics"></a>

Первый шаг в работе с векторной графикой - её извлечение из документа PDF. Вот как вы можете это сделать, используя класс `GraphicsAbsorber`:

```csharp
public static void UsingGraphicsAbsorber()
{
    // Шаг 1: Создайте объект Document.
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");

    // Шаг 2: Создайте экземпляр GraphicsAbsorber.
    var graphicsAbsorber = new GraphicsAbsorber();

    // Выберите первую страницу документа.
    var page = document.Pages[1];

    // Шаг 3: Используйте метод `Visit` для извлечения графики со страницы.
    graphicsAbsorber.Visit(page);

    // Отображение информации об извлеченных элементах.
    foreach (var element in graphicsAbsorber.Elements)
    {
        Console.WriteLine($"Номер страницы: {element.SourcePage.Number}");
        Console.WriteLine($"Позиция: ({element.Position.X}, {element.Position.Y})");
        Console.WriteLine($"Количество операторов: {element.Operators.Count}");
    }
}
```
### Объяснение:

1. **Создание объекта документа**: Создается новый объект `Document` с путем к целевому PDF-файлу.
2. **Создание экземпляра `GraphicsAbsorber`**: Этот класс захватывает все графические элементы с указанной страницы.
3. **Метод Visit**: Метод `Visit` вызывается на первой странице, что позволяет `GraphicsAbsorber` поглотить векторную графику.
4. **Итерация через извлеченные элементы**: Код проходит через каждый извлеченный элемент, выводя информацию, такую как номер страницы, позиция и количество графических операторов.

## 2. Перемещение графики<a name="moving-graphics"></a>

После извлечения графики вы можете переместить её в другое место на той же странице. Вот как это можно сделать:

```csharp
public static void MoveGraphics()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    graphicsAbsorber.Visit(page);

    // Временно приостановить обновления для повышения производительности.
    graphicsAbsorber.SuppressUpdate();

    foreach (var element in graphicsAbsorber.Elements)
    {
        var position = element.Position;
        // Переместить графику, сдвинув ее координаты X и Y.
        element.Position = new Point(position.X + 150, position.Y - 10);
    }

    // Возобновить обновления и применить изменения.
    graphicsAbsorber.ResumeUpdate();
    document.Save("test.pdf");
}
```
### Основные моменты:

- **SuppressUpdate**: Этот метод временно приостанавливает обновления для повышения производительности при выполнении множественных изменений.
- **ResumeUpdate**: Этот метод возобновляет обновления и применяет внесенные изменения к позициям графики.
- **Позиционирование элементов**: Позиция каждого графического элемента корректируется путем изменения его координат `X` и `Y`.

## 3. Удаление графики<a name="removing-graphics"></a>

Существуют сценарии, при которых вам может потребоваться удалить определенные графические элементы со страницы. Aspose.PDF предлагает два метода для достижения этого:

### Метод 1: Использование прямоугольной границы

```csharp
public static void RemoveGraphicsMethod1()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    graphicsAbsorber.Visit(page);
    var rectangle = new Rectangle(70, 248, 170, 252);

    graphicsAbsorber.SuppressUpdate();
    foreach (var element in graphicsAbsorber.Elements)
    {
        // Проверяем, находится ли позиция графики в пределах прямоугольника.
        if (rectangle.Contains(element.Position))
        {
            element.Remove(); // Удаляем графический элемент.
        }
    }
    graphicsAbsorber.ResumeUpdate();
    document.Save("test.pdf");
}
```
### Метод 2: Использование коллекции удаленных элементов

```csharp
public static void RemoveGraphicsMethod2()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    var rectangle = new Rectangle(70, 248, 170, 252);

    graphicsAbsorber.Visit(page);
    var removedElementsCollection = new GraphicElementCollection();
    foreach (var item in graphicsAbsorber.Elements.Where(el => rectangle.Contains(el.Position)))
    {
        removedElementsCollection.Add(item);
    }

    page.Contents.SuppressUpdate();
    page.DeleteGraphics(removedElementsCollection);
    page.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```

### Объяснение:

- **Граница прямоугольника**: Определите область прямоугольника, чтобы указать, какую графику удалить.
- **Приостановка и возобновление обновлений**: Обеспечьте эффективное удаление без промежуточного рендеринга.

## 4. Добавление графики на другую страницу<a name="adding-graphics"></a>

Графика, поглощенная с одной страницы, может быть добавлена на другую страницу в том же документе.
Графика, извлеченная с одной страницы, может быть добавлена на другую страницу в том же документе.

### Метод 1: Добавление графики по одному элементу

```csharp
public static void AddToAnotherPageMethod1()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page1 = document.Pages[1];
    var page2 = document.Pages[2];

    graphicsAbsorber.Visit(page1);
    page2.Contents.SuppressUpdate();
    foreach (var element in graphicsAbsorber.Elements)
    {
        element.AddOnPage(page2); // Добавить каждый графический элемент на вторую страницу.
    }
    page2.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```

### Метод 2: Добавление графики как коллекции

```csharp
public static void AddToAnotherPageMethod2()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page1 = document.Pages[1];
    var page2 = document.Pages[2];

    graphicsAbsorber.Visit(page1);
    page2.Contents.SuppressUpdate();
    page2.AddGraphics(graphicsAbsorber.Elements); // Добавить всю графику сразу.
    page2.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```
### Основные моменты:

- **SuppressUpdate и ResumeUpdate**: Эти методы помогают поддерживать производительность при массовых изменениях.
- **AddOnPage против AddGraphics**: Используйте `AddOnPage` для индивидуальных добавлений и `AddGraphics` для массовых добавлений.

## Заключение

В этой главе мы рассмотрели, как использовать класс `GraphicsAbsorber` для извлечения, перемещения, удаления и добавления векторной графики в документах PDF с помощью Aspose.PDF. Овладев этими техниками, вы сможете значительно улучшить визуальное представление ваших PDF и создать динамичные, визуально привлекательные документы.

Не стесняйтесь экспериментировать с примерами кода и адаптировать их к своим конкретным случаям использования. Счастливого кодирования!

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


