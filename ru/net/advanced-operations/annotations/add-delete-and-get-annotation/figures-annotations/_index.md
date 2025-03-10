---
title: Добавление аннотаций фигур с использованием C#
linktitle: Аннотации фигур
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ru/net/figures-annotation/
description: Эта статья описывает, как добавлять, получать и удалять аннотации фигур из вашего PDF-документа с Aspose.PDF for .NET
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Figures Annotations using C#",
    "alternativeHeadline": "Enhance PDF Documents with Comprehensive Figure Annotations",
    "abstract": "Представляем новую функцию аннотаций фигур в Aspose.PDF for .NET, которая позволяет пользователям без труда добавлять, извлекать и удалять различные типы аннотаций, включая линии, квадраты, круги, многоугольники и полилинии в PDF-документах. Эта функциональность улучшает интерактивность документа, позволяя более четкому общению и визуальному разметке непосредственно в PDF-файлах. Оптимизируйте свои задачи редактирования PDF с помощью этого мощного набора инструментов аннотаций, предназначенного для разработчиков, использующих C#",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, figures annotations, line annotation, square annotation, circle annotation, polygon annotation, polyline annotation, free text annotation, ink annotation, Aspose.PDF for .NET",
    "wordcount": "2125",
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
    "url": "/net/figures-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/figures-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Эта статья описывает, как добавлять, получать и удалять аннотации фигур из вашего PDF-документа с Aspose.PDF for .NET"
}
</script>

Приложение для управления PDF-документами предоставляет различные инструменты для аннотирования документов. С точки зрения внутренней структуры PDF эти инструменты являются аннотациями. Мы поддерживаем следующие виды инструментов рисования.

* Аннотация линии - инструмент для рисования линий и стрелок.
* Аннотация квадрата - для рисования квадратов и прямоугольников.
* Аннотация круга - для овалов и кругов.
* Аннотация свободного текста - для комментариев Callout.
* Аннотация многоугольника - для многоугольников и облаков.
* Аннотация полилинии - для соединенных линий.

## Добавление фигур и форм на страницу

Подход к добавлению аннотации типичен для любого из них.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

1. Загрузите PDF-файл или создайте новый с помощью [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Создайте новую аннотацию и установите параметры (новый прямоугольник, новая точка, заголовок, цвет, ширина и т.д.).
1. Создайте новую [PopupAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/popupannotation/methods/index).
1. Свяжите всплывающую аннотацию с оригинальной.
1. Добавьте аннотацию на страницу.

## Добавление линий или стрелок

Цель аннотации линии - отобразить простую линию или стрелку на странице. Чтобы создать линию, нам нужно создать новый объект LineAnnotation.  
Конструктор класса LineAnnotation принимает четыре параметра:

* Страница, на которую будет добавлена аннотация.
* Прямоугольник, который определяет границы аннотации.
* Две точки, которые определяют начало и конец линии.

Также нам нужно инициализировать некоторые свойства:

* `Title` - обычно это имя пользователя, который сделал этот комментарий.
* `Subject` - может быть любой строкой, но в общих случаях это имя аннотации.

Чтобы стилизовать нашу линию, нам нужно установить цвет, ширину, стиль начала и стиль конца. Эти свойства контролируют, как аннотация будет выглядеть и вести себя в просмотрщике PDF. Например, свойства `StartingStyle` и `EndingStyle` определяют, какой вид будет нарисован на концах линии, например, открытая стрелка, закрытая стрелка, круг и т.д.

Следующий фрагмент кода показывает, как добавить аннотацию линии в PDF-файл:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLineAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments.pdf"))
    {
        // Create Line Annotation
        var lineAnnotation = new Aspose.Pdf.Annotations.LineAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(550, 93, 562, 439),
            new Aspose.Pdf.Point(556, 99), new Aspose.Pdf.Point(556, 443))
        {
            Title = "John Smith",
            Color = Aspose.Pdf.Color.Red,
            Width = 3,
            StartingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow,
            EndingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 124, 1021, 266))
        };

        // Add annotation to the page
        document.Pages[1].Annotations.Add(lineAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddLineAnnotation_out.pdf");
    }
}
```

## Добавление квадрата или круга

Аннотации [Square](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squareannotation) и [Circle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/circleannotation) будут отображать прямоугольник или эллипс на странице. При открытии они будут отображать всплывающее окно с текстом связанной заметки. Аннотации квадратов похожи на аннотации кругов (экземпляры класса Aspose. Pdf. Annotations. CircleAnnotation), за исключением формы.

### Добавление аннотации круга

Чтобы нарисовать новую аннотацию круга или эллипса, нам нужно создать новый объект CircleAnnotation. Конструктор класса `CircleAnnotation` принимает два параметра:

* Страница, на которую будет добавлена аннотация.
* Прямоугольник, который определяет границы аннотации.

Также мы можем установить некоторые свойства объекта `CircleAnnotation`, такие как заголовок, цвет, цвет заливки, непрозрачность. Эти свойства контролируют, как аннотация будет выглядеть и вести себя в просмотрщике PDF. Здесь и далее в квадрате цвет `InteriorColor` - это цвет заливки, а `Color` - цвет границы.

### Добавление аннотации квадрата

Рисование прямоугольника такое же, как и рисование круга. Следующий фрагмент кода показывает, как добавить аннотации круга и квадрата на страницу PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddCircleAndSquareAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "appartments.pdf"))
    {
        // Create Circle Annotation
        var circleAnnotation = new Aspose.Pdf.Annotations.CircleAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(270, 160, 483, 383))
        {
            Title = "John Smith",
            Subject = "Circle",
            Color = Aspose.Pdf.Color.Red,
            InteriorColor = Aspose.Pdf.Color.MistyRose,
            Opacity = 0.5,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 316, 1021, 459))
        };

        // Create Square Annotation
        var squareAnnotation = new Aspose.Pdf.Annotations.SquareAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(67, 317, 261, 459))
        {
            Title = "John Smith",
            Subject = "Rectangle",
            Color = Aspose.Pdf.Color.Blue,
            InteriorColor = Aspose.Pdf.Color.BlueViolet,
            Opacity = 0.25,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 196, 1021, 338))
        };

        // Add annotations to the page
        document.Pages[1].Annotations.Add(circleAnnotation);
        document.Pages[1].Annotations.Add(squareAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddCircleAndSquareAnnotations_out.pdf");
    }
}
```

В качестве примера мы увидим следующий результат добавления аннотаций квадрата и круга в PDF-документ:

## Добавление аннотаций многоугольников и полилиний

Инструмент Poly позволяет создавать фигуры и контуры с произвольным количеством сторон на документе.

**Аннотации многоугольников** представляют многоугольники на странице. Они могут иметь любое количество вершин, соединенных прямыми линиями.  
**Аннотации полилиний** также похожи на многоугольники, единственное отличие в том, что первая и последняя вершины не соединены.

### Добавление аннотации многоугольника

PolygonAnnotation отвечает за аннотации многоугольников. Конструктор класса PolygonAnnotation принимает три параметра:

* Страница, на которую будет добавлена аннотация.
* Прямоугольник, который определяет границы аннотации.
* Массив точек, которые определяют вершины многоугольника.

`Color` и `InteriorColor` используются для цвета границы и заливки соответственно.

### Добавление аннотации полилинии

PolygonAnnotation отвечает за аннотации многоугольников. Конструктор класса PolygonAnnotation принимает три параметра:

* Страница, на которую будет добавлена аннотация.
* Прямоугольник, который определяет границы аннотации.
* Массив точек, которые определяют вершины многоугольника.

Вместо `PolygonAnnotation` мы не можем заполнить эту фигуру, поэтому нам не нужно использовать `InteriorColor`.

Следующий фрагмент кода показывает, как добавить аннотации многоугольников и полилиний в PDF-файл:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPolygonAndPolylineAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "appartments.pdf"))
    {
        // Create Polygon Annotation
        var polygonAnnotation = new Aspose.Pdf.Annotations.PolygonAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(270, 193, 571, 383),
            new Aspose.Pdf.Point[] {
                new Aspose.Pdf.Point(274, 381),
                new Aspose.Pdf.Point(555, 381),
                new Aspose.Pdf.Point(555, 304),
                new Aspose.Pdf.Point(570, 304),
                new Aspose.Pdf.Point(570, 195),
                new Aspose.Pdf.Point(274, 195)
            })
        {
            Title = "John Smith",
            Color = Aspose.Pdf.Color.Blue,
            InteriorColor = Aspose.Pdf.Color.BlueViolet,
            Opacity = 0.25,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 196, 1021, 338))
        };

        // Create Polyline Annotation
        var polylineAnnotation = new Aspose.Pdf.Annotations.PolylineAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(270, 193, 571, 383),
            new Aspose.Pdf.Point[] {
                new Aspose.Pdf.Point(545, 150),
                new Aspose.Pdf.Point(545, 190),
                new Aspose.Pdf.Point(667, 190),
                new Aspose.Pdf.Point(667, 110),
                new Aspose.Pdf.Point(626, 111)
            })
        {
            Title = "John Smith",
            Color = Aspose.Pdf.Color.Red,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 196, 1021, 338))
        };

        // Add annotations to the page
        document.Pages[1].Annotations.Add(polygonAnnotation);
        document.Pages[1].Annotations.Add(polylineAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddPolygonAndPolylineAnnotations_out.pdf");
    }
}
```

## Получение фигур

Все аннотации хранятся в коллекции `Annotations`. Любая аннотация может определить свой тип через свойство `AnnotationType`. Поэтому мы можем сделать запрос LINQ для фильтрации нужных аннотаций.

### Получение аннотаций линий

Пример ниже объясняет, как получить все аннотации линий с первой страницы PDF-документа.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReadLineAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all line annotations from the first page
        var lineAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Line)
            .Cast<Aspose.Pdf.Annotations.LineAnnotation>();

        // Iterate through each line annotation and print its coordinates
        foreach (var la in lineAnnotations)
        {
            Console.WriteLine($"[{la.Starting.X},{la.Starting.Y}]-[{la.Ending.X},{la.Ending.Y}]");
        }
    }
}
```

### Получение аннотаций кругов

Пример ниже объясняет, как получить все аннотации полилиний с первой страницы PDF-документа.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReadCircleAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all circle annotations from the first page
        var circleAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Circle)
            .Cast<Aspose.Pdf.Annotations.CircleAnnotation>();

        // Iterate through each circle annotation and print its rectangle
        foreach (var ca in circleAnnotations)
        {
            Console.WriteLine($"[{ca.Rect}]");
        }
    }
}
```

### Получение аннотаций квадратов

Пример ниже объясняет, как получить все аннотации полилиний с первой страницы PDF-документа.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReadSquareAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all square annotations from the first page
        var squareAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Square)
            .Cast<Aspose.Pdf.Annotations.SquareAnnotation>();

        // Iterate through each square annotation and print its rectangle
        foreach (var sq in squareAnnotations)
        {
            Console.WriteLine($"[{sq.Rect}]");
        }
    }
}
```

### Получение аннотаций полилиний

Пример ниже объясняет, как получить все аннотации полилиний с первой страницы PDF-документа.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReadPolylineAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all polyline annotations from the first page
        var polyAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.PolyLine)
            .Cast<Aspose.Pdf.Annotations.PolylineAnnotation>();

        // Iterate through each polyline annotation and print its rectangle
        foreach (var pa in polyAnnotations)
        {
            Console.WriteLine($"[{pa.Rect}]");
        }
    }
}
```

### Получение аннотаций многоугольников

Пример ниже объясняет, как получить все аннотации многоугольников с первой страницы PDF-документа.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReadPolygonAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all polygon annotations from the first page
        var polyAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Polygon)
            .Cast<Aspose.Pdf.Annotations.PolygonAnnotation>();

        // Iterate through each polygon annotation and print its rectangle
        foreach (var pa in polyAnnotations)
        {
            Console.WriteLine($"[{pa.Rect}]");
        }
    }
}
```

## Удаление фигур

Подход к удалению аннотации из PDF довольно прост:

* Выберите аннотации для удаления (создайте коллекцию).
* Переберите коллекцию с помощью цикла foreach и удалите каждую аннотацию из коллекции аннотаций с помощью метода Delete.

### Удаление аннотации линии

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteLineAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all line annotations from the first page
        var lineAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Line)
            .Cast<Aspose.Pdf.Annotations.LineAnnotation>();

        // Iterate through each line annotation and delete it
        foreach (var la in lineAnnotations)
        {
            document.Pages[1].Annotations.Delete(la);
        }

        // Save PDF document
        document.Save(dataDir + "DeleteLineAnnotations_out.pdf");
    }
}
```

### Удаление аннотаций кругов и квадратов

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteCircleAndSquareAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all circle and square annotations from the first page
        var figures = document.Pages[1].Annotations
            .Where(a =>
                a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Circle
                || a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Square);

        // Iterate through each figure annotation and delete it
        foreach (var fig in figures)
        {
            document.Pages[1].Annotations.Delete(fig);
        }

        // Save PDF document
        document.Save(dataDir + "DeleteCircleAndSquareAnnotations_out.pdf");
    }
}
```

### Удаление аннотаций многоугольников и полилиний

Следующий фрагмент кода показывает, как удалить аннотации многоугольников и полилиний из PDF-файла.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeletePolylineAndPolygonAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all polyline and polygon annotations from the first page
        var polyAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.PolyLine
                        || a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Polygon);

        // Iterate through each polyline or polygon annotation and delete it
        foreach (var pa in polyAnnotations)
        {
            document.Pages[1].Annotations.Delete(pa);
        }

        // Save PDF document
        document.Save(dataDir + DeletePolylineAndPolygonAnnotations_out.pdf");
    }
}
```

## Как добавить аннотацию чернила в PDF-файл

Аннотация чернила представляет собой свободный "каракули", состоящий из одного или нескольких несвязанных путей. При открытии она будет отображать всплывающее окно с текстом связанной заметки.

[InkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) представляет собой свободные каракули, состоящие из одной или нескольких несвязанных точек. Пожалуйста, попробуйте использовать следующий фрагмент кода для добавления InkAnnotation в PDF-документ.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddInkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "appartments.pdf"))
    {
        // Get first page
        var page = document.Pages[1];

        // Define the rectangle for the ink annotation
        var arect = new Aspose.Pdf.Rectangle(156.574, 521.316, 541.168, 575.703);

        // Create a list of ink paths
        IList<Aspose.Pdf.Point[]> inkList = new List<Aspose.Pdf.Point[]>();
        var arrpt = new[]
        {
            new Aspose.Pdf.Point(209.727, 542.263),
            new Aspose.Pdf.Point(209.727, 541.94),
            new Aspose.Pdf.Point(209.727, 541.616)
        };
        inkList.Add(arrpt);

        // Create the ink annotation
        var ia = new Aspose.Pdf.Annotations.InkAnnotation(page, arect, inkList)
        {
            Title = "John Smith",
            Subject = "Pencil",
            Color = Aspose.Pdf.Color.LightBlue,
            CapStyle = Aspose.Pdf.Annotations.CapStyle.Rounded,
            Opacity = 0.5
        };

        // Set the border for the annotation
        var border = new Aspose.Pdf.Annotations.Border(ia)
        {
            Width = 25
        };
        ia.Border = border;

        // Add the annotation to the page
        page.Annotations.Add(ia);

        // Save PDF document
        document.Save(dataDir + "AddInkAnnotation_out.pdf");
    }
}
```

### Установка ширины линии InkAnnotation

Ширину [InkAnnottion](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) можно изменить с помощью объектов LineInfo и Border.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddInkAnnotationWithLineWidth()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create a list of ink paths
        IList<Aspose.Pdf.Point[]> inkList = new List<Aspose.Pdf.Point[]>();

        // Define line information
        var lineInfo = new Aspose.Pdf.Facades.LineInfo
        {
            VerticeCoordinate = new float[] { 55, 55, 70, 70, 70, 90, 150, 60 },
            Visibility = true,
            LineColor = System.Drawing.Color.Red,
            LineWidth = 2
        };

        // Convert line coordinates to Aspose.Pdf.Point array
        int length = lineInfo.VerticeCoordinate.Length / 2;
        var gesture = new Aspose.Pdf.Point[length];
        for (int i = 0; i < length; i++)
        {
            gesture[i] = new Aspose.Pdf.Point(lineInfo.VerticeCoordinate[2 * i], lineInfo.VerticeCoordinate[2 * i + 1]);
        }

        // Add the gesture to the ink list
        inkList.Add(gesture);

        // Create the ink annotation
        var a1 = new Aspose.Pdf.Annotations.InkAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), inkList)
        {
            Subject = "Test",
            Title = "Title",
            Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green)
        };

        // Set the border for the annotation
        var border = new Aspose.Pdf.Annotations.Border(a1)
        {
            Width = 3,
            Effect = Aspose.Pdf.Annotations.BorderEffect.Cloudy,
            Dash = new Aspose.Pdf.Annotations.Dash(1, 1),
            Style = Aspose.Pdf.Annotations.BorderStyle.Solid
        };
        a1.Border = border;

        // Add the annotation to the page
        page.Annotations.Add(a1);

        // Save PDF document
        document.Save(dataDir + "lnkAnnotationLineWidth_out.pdf");
    }
}
```

### Удаление аннотации круга

Следующий фрагмент кода показывает, как удалить аннотацию круга из PDF-файла.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteCircleAnnotation()
{
	// The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
	
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        var circleAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == AnnotationType.Circle)
            .Cast<Aspose.Pdf.Annotations.CircleAnnotation>();

        foreach (var ca in circleAnnotations)
        {
            document.Pages[1].Annotations.Delete(ca);
        }

        // Save PDF document
        document.Save(dataDir + "DeleteCircleAnnotation_out.pdf");
    }
}
```

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