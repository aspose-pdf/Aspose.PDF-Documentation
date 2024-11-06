---
title: Добавление объекта Прямоугольник в PDF файл
linktitle: Добавить Прямоугольник
type: docs
weight: 50
url: ru/net/add-rectangle/
description: В этой статье объясняется, как создать объект Прямоугольник в вашем PDF с использованием Aspose.PDF для .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Добавление объекта Прямоугольник в PDF файл",
    "alternativeHeadline": "Как создать объект Прямоугольник в файле PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, прямоугольник в pdf",
    "wordcount": "302",
    "proficiencyLevel":"Начальный",
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
    "url": "/net/add-rectangle/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-rectangle/"
    },
    "dateModified": "2022-02-04",
    "description": "В этой статье объясняется, как создать объект Прямоугольник в вашем PDF с использованием Aspose.PDF для .NET."
}
</script>

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Добавление объекта Rectangle

Aspose.PDF для .NET поддерживает возможность добавления графических объектов (например, график, линия, прямоугольник и т.д.) в PDF документы. Вы также можете добавить объект [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle), который предоставляет возможность заполнить объект прямоугольника определенным цветом, управлять Z-порядком, добавить градиентное заполнение цветом и т.д.

Давайте сначала рассмотрим возможность создания объекта Rectangle.

Следуйте шагам ниже:

1. Создайте новый PDF [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)

2. Добавьте [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) в коллекцию страниц PDF файла

3. Добавьте [Text fragment](https://reference.aspose.com/pdf/net/aspose.pdf/texfragment) в коллекцию параграфов экземпляра страницы

4. Создайте экземпляр [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph)
1. Создайте экземпляр Rectangle

1. Добавьте объект [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) в коллекцию форм объекта Graph

1. Добавьте объект графики в коллекцию абзацев экземпляра страницы

1. Добавьте [фрагмент текста](https://reference.aspose.com/pdf/net/aspose.pdf/texfragment) в коллекцию абзацев экземпляра страницы

1. И сохраните ваш PDF файл

```csharp
 private static void AddRectangle(Page page, float x, float y, float width, float height, Color color, int zindex)
        {
            // Создайте объект графики с размерами, указанными для объекта Rectangle
            Aspose.Pdf.Drawing.Graph graph = new Aspose.Pdf.Drawing.Graph(width, height)
            {
                // Можем ли мы изменить положение экземпляра графики
                IsChangePosition = false,
                // Установите левую координату положения для экземпляра графики
                Left = x,
                // Установите верхнюю координату положения для объекта графики
                Top = y
            };
            // Добавьте прямоугольник внутри "графики"
            Rectangle rect = new Rectangle(0, 0, width, height);
            // Установите цвет заливки прямоугольника
            rect.GraphInfo.FillColor = color;
            // Цвет объекта графики
            rect.GraphInfo.Color = color;
            // Добавьте прямоугольник в коллекцию форм экземпляра графики
            graph.Shapes.Add(rect);
            // Установите Z-индекс для объекта прямоугольника
            graph.ZIndex = zindex;
            // Добавьте графику в коллекцию абзацев объекта страницы
            page.Paragraphs.Add(graph);
        }
```
![Создать прямоугольник](create_rectangle.png)

## Создание объекта заполненного прямоугольника

Aspose.PDF для .NET также предлагает функцию заполнения объекта прямоугольника определенным цветом.

Следующий фрагмент кода показывает, как добавить объект [Прямоугольник](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle), который заполнен цветом.

```csharp
    {
        private const string _dataDir = "C:\\Samples\\";
        public static void RectangleFilled()
        {
            // Создать экземпляр документа
            var doc = new Document();

            // Добавить страницу в коллекцию страниц PDF файла
            var page = doc.Pages.Add();
            // Создать экземпляр графа
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

            // Добавить объект графа в коллекцию абзацев экземпляра страницы
            page.Paragraphs.Add(graph);

            // Создать экземпляр прямоугольника
            var rect = new Rectangle(100, 100, 200, 120);

            // Указать цвет заливки для объекта графа
            rect.GraphInfo.FillColor = Color.Red;

            // Добавить объект прямоугольника в коллекцию форм объекта графа
            graph.Shapes.Add(rect);

            // Сохранить PDF файл
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```
Посмотрите на результат закрашенного прямоугольника:

![Закрашенный прямоугольник](fill_rectangle.png)

## Добавление рисунка с градиентной заливкой

Aspose.PDF для .NET поддерживает возможность добавления графических объектов в документы PDF и иногда требуется заливать графические объекты градиентным цветом. Чтобы залить графические объекты градиентным цветом, нам нужно установить setPatterColorSpace с объектом gradientAxialShading следующим образом.

Следующий фрагмент кода показывает, как добавить объект [Прямоугольник](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle), который заполнен градиентным цветом.

```csharp
 public static void CreateFilledRectangletGradientFill()
        {
            // Создать экземпляр документа
            var doc = new Document();

            // Добавить страницу в коллекцию страниц PDF файла
            var page = doc.Pages.Add();
            // Создать экземпляр графа
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // Добавить графический объект в коллекцию абзацев экземпляра страницы
            page.Paragraphs.Add(graph);
            // Создать экземпляр прямоугольника
            var rect = new Rectangle(0, 0, 300, 300);
            // Указать цвет заливки для графического объекта
            var gradientColor = new Color();
            var gradientSettings = new GradientAxialShading(Color.Red, Color.Blue)
            {
                Start = new Point(0, 0),
                End = new Point(350, 350)
            };
            gradientColor.PatternColorSpace = gradientSettings;
            rect.GraphInfo.FillColor = gradientColor;

            // Добавить объект прямоугольника в коллекцию форм графического объекта
            graph.Shapes.Add(rect);

            // Сохранить PDF файл
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```
![Градиентный прямоугольник](gradient.png)

## Создание прямоугольника с альфа-каналом цвета

Aspose.PDF для .NET поддерживает заполнение объекта прямоугольник определенным цветом. Объект прямоугольника также может иметь альфа-канал цвета для создания прозрачного вида. Следующий фрагмент кода показывает, как добавить объект [Прямоугольник](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) с альфа-каналом цвета.

Пиксели изображения могут хранить информацию о своей прозрачности вместе с цветовым значением. Это позволяет создавать изображения с прозрачными или полупрозрачными областями.

Вместо того, чтобы делать цвет прозрачным, каждый пиксель хранит информацию о том, насколько он непрозрачен. Эти данные о непрозрачности называются альфа-каналом и обычно хранятся после цветовых каналов пикселя.

```csharp
     public static void RectangleFilled_AlphaChannel()
        {
            // Создать экземпляр документа
            var doc = new Document();

            // Добавить страницу в коллекцию страниц PDF файла
            var page = doc.Pages.Add();
            // Создать экземпляр графа
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);
            // Добавить объект графа в коллекцию параграфов экземпляра страницы
            page.Paragraphs.Add(graph);
            // Создать экземпляр прямоугольника
            var rect = new Rectangle(100, 100, 200, 120);
            // Указать цвет заливки для объекта графа
            rect.GraphInfo.FillColor = Color.FromArgb(128, 244, 180, 0);

            // Добавить объект прямоугольника в коллекцию форм объекта графа
            graph.Shapes.Add(rect);

            // Создать второй объект прямоугольника
            var rect1 = new Rectangle(200, 150, 200, 100);
            rect1.GraphInfo.FillColor = Color.FromArgb(160, 120, 0, 120);
            graph.Shapes.Add(rect1);

            // Добавить экземпляр графа в коллекцию параграфов объекта страницы
            page.Paragraphs.Add(graph);

            // Сохранить PDF файл
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```
![Прямоугольник Альфа-канал Цвет](rectangle_color.png)

## Контроль Z-порядка прямоугольника

Aspose.PDF для .NET поддерживает возможность добавления графических объектов (например, график, линия, прямоугольник и т.д.) в PDF документы. При добавлении более одного экземпляра одного и того же объекта внутри PDF файла, мы можем контролировать их рендеринг, указывая Z-порядок. Z-порядок также используется, когда нам нужно рендерить объекты один поверх другого.

Следующий фрагмент кода показывает шаги для рендеринга объектов [Прямоугольник](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) друг на друга.

```csharp
 public static void AddRectangleZOrder()
        {
            // Создаем объект класса Document
            Document doc1 = new Document();
            /// Добавляем страницу в коллекцию страниц PDF файла
            Page page1 = doc1.Pages.Add();
            // Устанавливаем размер PDF страницы
            page1.SetPageSize(375, 300);
            // Устанавливаем левый отступ для объекта страницы как 0
            page1.PageInfo.Margin.Left = 0;
            // Устанавливаем верхний отступ объекта страницы как 0
            page1.PageInfo.Margin.Top = 0;
            // Создаем новый прямоугольник с Цветом как Красный, Z-порядком как 0 и определенными размерами
            AddRectangle(page1, 50, 40, 60, 40, Color.Red, 2);
            // Создаем новый прямоугольник с Цветом как Синий, Z-порядком как 0 и определенными размерами
            AddRectangle(page1, 20, 20, 30, 30, Color.Blue, 1);
            // Создаем новый прямоугольник с Цветом как Зеленый, Z-порядком как 0 и определенными размерами
            AddRectangle(page1, 40, 40, 60, 30, Color.Green, 0);
            // Сохраняем результирующий PDF файл
            doc1.Save(_dataDir + "ControlRectangleZOrder_out.pdf");
        }
```
![Управление порядком Z](control.png)

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
    "applicationCategory": "Библиотека для манипуляции PDF для .NET",
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

