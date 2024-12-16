---
title: Добавление аннотаций к фигурам с помощью C#
linktitle: Аннотации к фигурам
type: docs
weight: 30
url: /ru/net/figures-annotation/
description: Эта статья описывает, как добавлять, получать и удалять аннотации к фигурам в вашем PDF-документе с помощью Aspose.PDF для .NET
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Добавление аннотаций к фигурам с помощью C#",
    "alternativeHeadline": "Как добавить аннотации к фигурам в PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, аннотации к фигурам, аннотация полигона, аннотация линии, аннотация квадрата, аннотация круга",
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
    "url": "/net/figures-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/figures-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Эта статья описывает, как добавлять, получать и удалять аннотации к фигурам в вашем PDF-документе с помощью Aspose.PDF для .NET"
}
</script>

Приложение для управления документами PDF предоставляет различные инструменты для аннотирования документов. С точки зрения внутренней структуры PDF, эти инструменты являются аннотациями. Мы поддерживаем следующие виды инструментов для рисования.

* Аннотация Линия - инструмент для рисования линий и стрелок
* Аннотация Квадрат - для рисования квадратов и прямоугольников
* Аннотация Круг - для овалов и кругов
* Аннотация Свободный текст - для комментариев-выносок
* Аннотация Многоугольник - для многоугольников и облаков
* Аннотация Полилиния - для соединенных линий

## Добавление фигур и форм на страницу

Подход к добавлению аннотации типичен для любой из них.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

1. Загрузите PDF-файл или создайте новый с помощью [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Создайте новую аннотацию и установите параметры (новый Rectangle, новый Point, заголовок, цвет, ширина и т.д).
1. Свяжите всплывающую аннотацию с оригинальной.
1. Добавьте аннотацию на страницу

## Добавление линий или стрелок

Цель аннотации линии - отобразить прямую линию или стрелку на странице.
Для создания линии нам нужен новый объект LineAnnotation.  
Конструктор класса LineAnnotation принимает четыре параметра:

* страница, на которую будет добавлена аннотация,
* прямоугольник, определяющий границы аннотации,
* и две точки, определяющие начало и конец линии.

Также нам нужно инициализировать некоторые свойства:

* `Title` - обычно это имя пользователя, который сделал этот комментарий
* `Subject` - может быть любой строкой, но обычно это название аннотации

Для стилизации нашей линии необходимо установить цвет, ширину, стиль начала и стиль окончания.
Для стилизации нашей линии нам нужно установить цвет, ширину, начальный стиль и конечный стиль.

Следующий фрагмент кода показывает, как добавить аннотацию линии в файл PDF:

```csharp
// Загрузить файл PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments.pdf"));

// Создать аннотацию линии
var lineAnnotation = new LineAnnotation(
    document.Pages[1],
    new Rectangle(550, 93, 562, 439),
    new Point(556, 99), new Point(556, 443))
{
    Title = "Джон Смит",
    Color = Color.Red,
    Width = 3,
    StartingStyle = LineEnding.OpenArrow,
    EndingStyle = LineEnding.OpenArrow,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 124, 1021, 266))
};

// Добавить аннотацию на страницу
document.Pages[1].Annotations.Add(lineAnnotation);
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
```

## Добавление квадрата или круга

Аннотации [Square](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squareannotation) и [Circle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/circleannotation) отобразят прямоугольник или эллипс на странице.
[Square](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squareannotation) и [Circle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/circleannotation) аннотации отображают прямоугольник или эллипс на странице.

### Добавление аннотации Circle

Чтобы нарисовать новую круглую или эллиптическую аннотацию, нам нужно создать новый объект CircleAnnotation. Конструктор класса `CircleAnnotation` принимает два параметра:

* страницу, на которую будет добавлена аннотация,
* и прямоугольник, который определяет границы аннотации

Также мы можем установить некоторые свойства объекта `CircleAnnotation`, такие как название, цвет, внутренний цвет, прозрачность. Эти свойства контролируют внешний вид и поведение аннотации в PDF-просмотрщике. Здесь и далее в Square `InteriorColor` - это цвет заливки, а `Color` - цвет границы.

### Добавление аннотации Square

Рисование прямоугольника происходит так же, как и рисование круга.
Рисование прямоугольника такое же, как рисование круга.

```csharp
var dataDir = "<path-to-file>";
// Загрузить файл PDF
Document document = new Document(System.IO.Path.Combine(dataDir, "appartments.pdf"));

// Создать аннотацию Круг
var circleAnnotation = new CircleAnnotation(document.Pages[1], new Rectangle(270, 160, 483, 383))
{
    Title = "John Smith",
    Subject = "Круг",
    Color = Color.Red,
    InteriorColor = Color.MistyRose,
    Opacity = 0.5,        
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 316, 1021, 459))
};

// Создать аннотацию Квадрат
var squareAnnotation = new SquareAnnotation(document.Pages[1], new Rectangle(67, 317, 261, 459))
{
    Title = "John Smith",
    Subject = "Прямоугольник",
    Color = Color.Blue,
    InteriorColor = Color.BlueViolet,
    Opacity = 0.25,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// Добавить аннотацию на страницу
document.Pages[1].Annotations.Add(circleAnnotation);
document.Pages[1].Annotations.Add(squareAnnotation);
document.Save(System.IO.Path.Combine(dataDir, "appartments_mod.pdf"));
```
В качестве примера мы увидим следующий результат добавления аннотаций Квадрат и Круг к документу PDF:

![Демонстрация аннотаций Круг и Квадрат](circle_demo.png)

## Добавление аннотаций Полигон и Полилиния

Инструмент Poly- позволяет создавать фигуры и контуры с произвольным количеством сторон на документе.

**Аннотации Полигон** представляют собой полигоны на странице. Они могут иметь любое количество вершин, соединенных прямыми линиями.
**Аннотации Полилиния** также похожи на полигоны, единственное отличие в том, что первая и последняя вершины не соединены неявно.

### Добавление аннотации Полигон

PolygonAnnotation отвечает за аннотации полигонов. Конструктор класса PolygonAnnotation принимает три параметра:

* страница, на которой будет добавлена аннотация,
* прямоугольник, который определяет границы аннотации,
* и массив точек, определяющих вершины полигона.

`Color` и `InteriorColor` используются соответственно для цвета границы и цвета заливки.

### Добавление аннотации Полилиния
### Добавление аннотации полилинии

PolygonAnnotation отвечает за аннотации в виде полигонов. Конструктор класса PolygonAnnotation принимает три параметра:

* страницу, на которую будет добавлена аннотация,
* прямоугольник, который определяет границы аннотации,
* и массив точек, которые определяют вершины полигона.

Вместо `PolygonAnnotation` мы не можем заполнить эту форму, поэтому нам не нужно использовать `InteriorColor`.

Следующий пример кода показывает, как добавить аннотации Polygon и Polyline в файл PDF:

```csharp
// Загрузить файл PDF
Document document = new Document(System.IO.Path.Combine(dataDir, "appartments.pdf"));

// Создать аннотацию Polygon
var polygonAnnotation = new PolygonAnnotation(document.Pages[1],
    new Rectangle(270, 193, 571, 383),
    new Point[] {
        new Point(274, 381),
        new Point(555, 381),
        new Point(555, 304),
        new Point(570, 304),
        new Point(570, 195),
        new Point(274, 195)})
{
    Title = "John Smith",
    Color = Color.Blue,
    InteriorColor = Color.BlueViolet,
    Opacity = 0.25,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// Создать аннотацию Polyline
var polylineAnnotation = new PolylineAnnotation(document.Pages[1],
    new Rectangle(270, 193, 571, 383),
    new Point[] {
        new Point(545,150),
        new Point(545,190),
        new Point(667,190),
        new Point(667,110),
        new Point(626,111)
        })
{
    Title = "John Smith",
    Color = Color.Red,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// Добавить аннотацию на страницу
document.Pages[1].Annotations.Add(polygonAnnotation);
document.Pages[1].Annotations.Add(polylineAnnotation);
document.Save(System.IO.Path.Combine(dataDir, "appartments_mod.pdf"));
```
## Получение данных

Все аннотации хранятся в коллекции `Annotations`. Любая аннотация может указывать свой тип через свойство `AnnotationType`. Следовательно, мы можем выполнить запрос LINQ, чтобы отфильтровать нужные аннотации.

### Получение аннотаций линий

Пример ниже объясняет, как получить все аннотации линий с первой страницы документа PDF.

```csharp
// Загрузка файла PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var lineAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<LineAnnotation>();
foreach (var la in lineAnnotations)
{
    Console.WriteLine($"[{la.Starting.X},{la.Starting.Y}]-[{la.Ending.X},{la.Ending.Y}]");
}   
```

### Получение аннотаций окружностей

Пример ниже объясняет, как получить все аннотации полилиний с первой страницы документа PDF.

```csharp
// Загрузка файла PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var circleAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<CircleAnnotation>();
foreach (var ca in circleAnnotations)
{
    Console.WriteLine($"[{ca.Rect}]");
}   
```
### Получение аннотаций в виде квадратов

Пример ниже объясняет, как получить все аннотации в виде квадратов на первой странице PDF документа.

```csharp
// Загрузка PDF файла
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var squareAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Square)
    .Cast<SquareAnnotation>();
foreach (var sq in squareAnnotations)
{
    Console.WriteLine($"[{sq.Rect}]");
}
```

### Получение аннотаций в виде полилиний

Пример ниже объясняет, как получить все аннотации в виде полилиний на первой странице PDF документа.

```csharp
// Загрузка PDF файла
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.PolyLine)
    .Cast<PolylineAnnotation>();
foreach (var pa in polyAnnotations)
{
    Console.WriteLine($"[{pa.Rect}]");
}     
```

### Получение аннотаций в виде полигонов
Пример ниже объясняет, как получить все аннотации-полигоны с первой страницы PDF-документа.

```csharp
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Polygon)
    .Cast<PolygonAnnotation>();
foreach (var pa in polyAnnotations)
{
    Console.WriteLine($"[{pa.Rect}]");
} 
```

## Удаление фигур

Подход к удалению аннотации из PDF довольно прост:

* Выберите аннотации для удаления (создайте некоторую коллекцию)
* Итерируйте по коллекции с помощью цикла foreach и удаляйте каждую аннотацию из коллекции аннотаций с использованием метода Delete.

### Удаление аннотации-линии

```csharp
// Загрузите файл PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var lineAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<LineAnnotation>();

foreach (var la in lineAnnotations)
{
    document.Pages[1].Annotations.Delete(la);
}
```
### Удаление аннотаций Круг и Квадрат

```csharp
// Загрузка файла PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var figures = document.Pages[1].Annotations
    .Where(a =>
        a.AnnotationType == AnnotationType.Circle
        || a.AnnotationType == AnnotationType.Square);

foreach (var fig in figures)
{
    document.Pages[1].Annotations.Delete(fig);
}
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_del.pdf"));
```

### Удаление аннотаций Полигон и Полилиния

В следующем примере кода показано, как удалить аннотации Полигон и Полилиния из файла PDF.

```csharp
// Загрузка файла PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
                .Where(a => a.AnnotationType == AnnotationType.PolyLine
                || a.AnnotationType == AnnotationType.Polygon);

foreach (var pa in polyAnnotations)
{
    document.Pages[1].Annotations.Delete(pa);
}
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_del.pdf"));
```
## Как добавить аннотацию чернилами в файл PDF

Аннотация чернилами представляет собой свободный "набросок", состоящий из одного или нескольких разрозненных путей. При открытии она должна отображать всплывающее окно с текстом связанной заметки.

[InkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) представляет собой свободный набросок, состоящий из одного или нескольких разрозненных точек. Пожалуйста, попробуйте использовать следующий фрагмент кода для добавления аннотации чернилами в документ PDF.

```csharp
// Загрузить файл PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "appartments.pdf"));
Page page = document.Pages[1];

Rectangle arect = new Rectangle(156.574, 521.316, 541.168, 575.703);

IList<Point[]> inkList = new List<Point[]>();
Point[] arrpt = new[]
{
    new Point(209.727,542.263),
    new Point(209.727,541.94),
    new Point(209.727,541.616)
};
inkList.Add(arrpt);

InkAnnotation ia = new InkAnnotation(page, arect, inkList)
{
    Title = "John Smith",
    Subject = "Pencil",
    Color = Color.LightBlue,
    CapStyle = CapStyle.Rounded,
    Opacity = 0.5
};
Border border = new Border(ia)
{
    Width = 25
};
ia.Border = border;
page.Annotations.Add(ia);

// Сохранить выходной файл
document.Save(System.IO.Path.Combine(_dataDir, "appartments_mod.pdf"));
```
### Установка ширины линии InkAnnotation

Ширину [InkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) можно изменить с помощью объектов LineInfo и Border.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Document doc = new Document();
doc.Pages.Add();
IList<Point[]> inkList = new List<Point[]>();
LineInfo lineInfo = new LineInfo();
lineInfo.VerticeCoordinate = new float[] { 55, 55, 70, 70, 70, 90, 150, 60 };
lineInfo.Visibility = true;
lineInfo.LineColor = System.Drawing.Color.Red;
lineInfo.LineWidth = 2;
int length = lineInfo.VerticeCoordinate.Length / 2;
Aspose.Pdf.Point[] gesture = new Aspose.Pdf.Point[length];
for (int i = 0; i < length; i++)
{
   gesture[i] = new Aspose.Pdf.Point(lineInfo.VerticeCoordinate[2 * i], lineInfo.VerticeCoordinate[2 * i + 1]);
}

inkList.Add(gesture);
InkAnnotation a1 = new InkAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), inkList);
a1.Subject = "Test";
a1.Title = "Title";
a1.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
Border border = new Border(a1);
border.Width = 3;
border.Effect = BorderEffect.Cloudy;
border.Dash = new Dash(1, 1);
border.Style = BorderStyle.Solid;
doc.Pages[1].Annotations.Add(a1);

dataDir = dataDir + "lnkAnnotationLineWidth_out.pdf";
// Сохранить выходной файл
doc.Save(dataDir);
```

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
### Удаление аннотации с кругом

Следующий фрагмент кода показывает, как удалить аннотацию с кругом из файла PDF.

```csharp
public static void DeleteCircleAnnotation()
{
    // Загрузить файл PDF
    Document document = new Document(System.IO.Path.Combine(dataDir, "Appartments_mod.pdf"));
    var circleAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Circle)
        .Cast<CircleAnnotation>();

    foreach (var ca in circleAnnotations)
    {
        document.Pages[1].Annotations.Delete(ca);
    }
    document.Save(System.IO.Path.Combine(dataDir, "Appartments_del.pdf"));
}
```
