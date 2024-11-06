---
title: Работа с векторной графикой
linktitle: Работа с векторной графикой
type: docs
weight: 120
url: ru/net/working-with-vector-graphics/
description: В этой статье описаны возможности работы с инструментом GraphicsAbsorber с использованием C#.
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
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
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
    "url": "/net/working-with-vector-graphics/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-vector-graphics/"
    },
    "dateModified": "2022-02-04",
    "description": "Этот раздел описывает возможности работы с файлом PDF с использованием библиотеки C# GraphicsAbsorber."
}
</script>
В этой главе мы рассмотрим, как использовать мощный класс `GraphicsAbsorber` для взаимодействия с векторной графикой внутри PDF-документов. Независимо от того, нужно ли вам перемещать, удалять или добавлять графику, это руководство покажет вам, как эффективно выполнять эти задачи. Давайте начнем!

## Введение<a name="introduction"></a>

Векторная графика является важным компонентом многих PDF-документов, используемых для представления изображений, форм и других графических элементов. Aspose.PDF предоставляет класс `GraphicsAbsorber`, который позволяет разработчикам программно получать доступ к этой графике и управлять ею. Используя метод `Visit` класса `GraphicsAbsorber`, вы можете извлечь векторную графику с указанной страницы и выполнять различные операции, такие как перемещение, удаление или копирование на другие страницы.

## 1. Извлечение графики с помощью `GraphicsAbsorber`<a name="extracting-graphics"></a>

Первый шаг в работе с векторной графикой - извлечь ее из PDF-документа. Вот как вы можете это сделать с помощью класса `GraphicsAbsorber`:

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

    // Отобразите информацию о извлеченных элементах.
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
4. **Итерация через извлеченные элементы**: Код перебирает каждый извлеченный элемент, выводя информацию, такую как номер страницы, позиция и количество операторов рисования.

## 2. Перемещение графики<a name="moving-graphics"></a>

После извлечения графики, вы можете переместить ее на другую позицию на той же странице. Вот как это можно сделать:

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

- **SuppressUpdate**: Этот метод временно приостанавливает обновления для повышения производительности при внесении множественных изменений.
- **ResumeUpdate**: Этот метод возобновляет обновления и применяет сделанные изменения к позициям графики.
- **Позиционирование элементов**: Позиция каждой графики корректируется путем изменения её координат `X` и `Y`.

## 3. Удаление графики<a name="removing-graphics"></a>

Существуют сценарии, когда вы можете захотеть удалить определённые графические элементы со страницы. Aspose.PDF предлагает два метода для этого:

### Метод 1: Использование границ прямоугольника

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
        // Проверяем, попадает ли позиция графического элемента в прямоугольник.
        if (rectangle.Contains(element.Position))
        {
            element.Remove(); // Удаление графического элемента.
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

- **Граница прямоугольника**: Определите прямоугольную область для указания, какую графику удалить.
- **Приостановка и возобновление обновлений**: Обеспечивает эффективное удаление без промежуточной отрисовки.

## 4. Добавление графики на другую страницу<a name="adding-graphics"></a>

Графика, поглощенная с одной страницы, может быть добавлена на другую страницу в том же документе.
Графика, извлеченная с одной страницы, может быть добавлена на другую страницу в том же документе.

### Метод 1: Добавление графики по отдельности

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

- **SuppressUpdate и ResumeUpdate**: Эти методы помогают поддерживать производительность при выполнении массовых изменений.
- **AddOnPage против AddGraphics**: Используйте `AddOnPage` для отдельных добавлений и `AddGraphics` для массовых добавлений.

## Заключение

В этой главе мы рассмотрели, как использовать класс `GraphicsAbsorber` для извлечения, перемещения, удаления и добавления векторной графики в документах PDF с помощью Aspose.PDF. Овладев этими техниками, вы сможете значительно улучшить визуальное представление ваших PDF и создать динамичные, визуально привлекательные документы.

Не стесняйтесь экспериментировать с примерами кода и адаптировать их под свои конкретные случаи использования. Счастливого кодирования!

