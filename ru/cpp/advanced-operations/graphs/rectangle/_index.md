---
title: Добавление объекта Прямоугольник в PDF файл
linktitle: Добавить Прямоугольник
type: docs
weight: 50
url: ru/cpp/add-rectangle/
description: В этой статье объясняется, как создать объект Прямоугольник в вашем PDF с помощью Aspose.PDF для C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Добавление объекта Прямоугольник

Aspose.PDF для C++ поддерживает возможность добавления графических объектов (например, график, линия, прямоугольник и т. д.) в PDF документы. Вы также можете добавить объект [Прямоугольник](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/), где также предлагается возможность заполнить объект прямоугольника определенным цветом, контролировать порядок наложения, добавить градиентную заливку и т. д.

Сначала давайте рассмотрим возможность создания объекта Прямоугольник.

Следуйте шагам ниже:

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/)

1. Добавьте [Страницу](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/) в коллекцию страниц PDF файла

1. Добавить [Text fragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/) в коллекцию абзацев экземпляра страницы

1. Создать экземпляр [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph/)

1. Установить границу для [Drawing object](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing)

1. Создать экземпляр Rectangle

1. Добавить объект [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) в коллекцию форм объекта Graph

1. Добавить графический объект в коллекцию абзацев экземпляра страницы

1. Добавить [Text fragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/) в коллекцию абзацев экземпляра страницы

1. И сохранить ваш PDF файл

```csharp
 private static void AddRectangle(Page page, float x, float y, float width, float height, Color color, int zindex)
        {
            // Создать графический объект с размерами, такими же, как указано для объекта Rectangle
            Aspose.Pdf.Drawing.Graph graph = new Aspose.Pdf.Drawing.Graph(width, height)
            {
                // Можно ли изменить позицию экземпляра графика
                IsChangePosition = false,
                // Установить координату Left для экземпляра Graph
                Left = x,
                // Установить координату Top для объекта Graph
                Top = y
            };
            // Добавить прямоугольник внутри "graph"
            Rectangle rect = new Rectangle(0, 0, width, height);
            // Установить цвет заливки прямоугольника
            rect.GraphInfo.FillColor = color;
            // Цвет графического объекта
            rect.GraphInfo.Color = color;
            // Добавить прямоугольник в коллекцию форм экземпляра графика
            graph.Shapes.Add(rect);
            // Установить Z-Index для объекта прямоугольника
            graph.ZIndex = zindex;
            // Добавить график в коллекцию абзацев объекта страницы
            page.Paragraphs.Add(graph);
        }
```
![Create Rectangle](create_rectangle.png)

## Создать объект заполненного прямоугольника

Aspose.PDF для C++ также предлагает функцию заполнения объекта прямоугольника определенным цветом.

Следующий фрагмент кода показывает, как добавить объект [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/), заполненный цветом.

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

            // Указать цвет заполнения для объекта графа
            rect.GraphInfo.FillColor = Color.Red;

            // Добавить объект прямоугольника в коллекцию форм объекта графа
            graph.Shapes.Add(rect);

            // Сохранить PDF файл
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

Посмотрите на результат прямоугольника, заполненного сплошным цветом:

![Заполненный Прямоугольник](fill_rectangle.png)

## Добавление Рисунка с Градиентной Заливкой

Aspose.PDF для C++ поддерживает возможность добавления графических объектов в PDF документы, и иногда требуется заполнить графические объекты градиентным цветом. Чтобы заполнить графические объекты градиентным цветом, нам нужно установить setPatterColorSpace с объектом gradientAxialShading, как показано ниже.

Следующий фрагмент кода показывает, как добавить объект [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/), который заполнен градиентным цветом.

```csharp
 public static void CreateFilledRectangletGradientFill()
        {
            // Создать экземпляр документа
            var doc = new Document();

            // Добавить страницу в коллекцию страниц PDF файла
            var page = doc.Pages.Add();
            // Создать экземпляр Graph
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // Добавить графический объект в коллекцию абзацев экземпляра страницы
            page.Paragraphs.Add(graph);
            // Создать экземпляр Rectangle
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

![Gradient Rectangle](gradient.png)

## Создание прямоугольника с альфа-каналом цвета

Aspose.PDF для C++ поддерживает заполнение объекта прямоугольника определённым цветом. Объект прямоугольника также может иметь альфа-канал цвета для создания прозрачного вида. Следующий фрагмент кода показывает, как добавить объект [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) с альфа-каналом цвета.

Пиксели изображения могут хранить информацию об их непрозрачности вместе со значением цвета. Это позволяет создавать изображения с прозрачными или полупрозрачными областями.

Вместо того чтобы делать цвет прозрачным, каждый пиксель хранит информацию о том, насколько он непрозрачен. Эти данные о непрозрачности называются альфа-каналом и обычно хранятся после цветовых каналов пикселя.

```csharp
     public static void RectangleFilled_AlphaChannel()
        {
            // Создать экземпляр документа
            var doc = new Document();

            // Добавить страницу в коллекцию страниц PDF-файла
            var page = doc.Pages.Add();
            // Создать экземпляр графики
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);
            // Добавить объект графики в коллекцию абзацев экземпляра страницы
            page.Paragraphs.Add(graph);
            // Создать экземпляр прямоугольника
            var rect = new Rectangle(100, 100, 200, 120);
            // Указать цвет заливки для объекта графики
            rect.GraphInfo.FillColor = Color.FromArgb(128, 244, 180, 0);

            // Добавить объект прямоугольника в коллекцию форм объекта графики
            graph.Shapes.Add(rect);

            // Создать второй объект прямоугольника
            var rect1 = new Rectangle(200, 150, 200, 100);
            rect1.GraphInfo.FillColor = Color.FromArgb(160, 120, 0, 120);
            graph.Shapes.Add(rect1);

            // Добавить экземпляр графики в коллекцию абзацев объекта страницы
            page.Paragraphs.Add(graph);

            // Сохранить PDF-файл
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

![Rectangle Alpha Channel Color](rectangle_color.png)

## Управление порядком наложения прямоугольников

Aspose.PDF для C++ поддерживает возможность добавления графических объектов (например, графиков, линий, прямоугольников и т.д.) в PDF-документы. При добавлении нескольких экземпляров одного и того же объекта в PDF-файл мы можем управлять их отображением, указывая порядок наложения (Z-Order). Порядок наложения также используется, когда нам нужно отобразить объекты друг на друге.

Следующий фрагмент кода показывает шаги для отображения объектов [Прямоугольник](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) друг на друге.

```csharp
 public static void AddRectangleZOrder()
        {
            // Создать экземпляр класса Document
            Document doc1 = new Document();
            /// Добавить страницу в коллекцию страниц PDF-файла
            Page page1 = doc1.Pages.Add();
            // Установить размер страницы PDF
            page1.SetPageSize(375, 300);
            // Установить левое поле объекта страницы в 0
            page1.PageInfo.Margin.Left = 0;
            // Установить верхнее поле объекта страницы в 0
            page1.PageInfo.Margin.Top = 0;
            // Создать новый прямоугольник с цветом Красный, порядком наложения 0 и определенными размерами
            AddRectangle(page1, 50, 40, 60, 40, Color.Red, 2);
            // Создать новый прямоугольник с цветом Синий, порядком наложения 0 и определенными размерами
            AddRectangle(page1, 20, 20, 30, 30, Color.Blue, 1);
            // Создать новый прямоугольник с цветом Зеленый, порядком наложения 0 и определенными размерами
            AddRectangle(page1, 40, 40, 60, 30, Color.Green, 0);
            // Сохранить результирующий PDF-файл
            doc1.Save(_dataDir + "ControlRectangleZOrder_out.pdf");
        }
```


![Контроль порядка отображения](control.png)
```