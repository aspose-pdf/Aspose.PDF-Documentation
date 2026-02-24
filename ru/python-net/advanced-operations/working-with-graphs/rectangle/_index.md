---
title: Добавить объект Rectangle в PDF файл
linktitle: Добавить Rectangle
type: docs
weight: 50
url: /ru/python-net/add-rectangle/
description: В этой статье объясняется, как создать объект Rectangle в вашем PDF с помощью Aspose.PDF для Python через .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление объекта Rectangle в PDF с использованием Python
Abstract: Статья предоставляет всестороннее руководство по добавлению и манипулированию объектами Rectangle в PDF‑документах с использованием Aspose.PDF для Python через .NET. В ней подробно описан процесс создания Rectangle и его интеграции в PDF‑документ, включая установку границ и заполнение сплошными цветами или градиентными заливками. Статья содержит пошаговые инструкции с примерами кода, демонстрирующими создание PDF‑документа, добавление страниц и вставку объектов Rectangle с различными визуальными свойствами, такими как сплошные цветовые заливки, градиентные заливки и прозрачность с использованием альфа‑каналов. Кроме того, объясняется, как управлять Z‑Order объектов Rectangle для контроля порядка их отрисовки, когда в один PDF добавляется несколько фигур. Каждый раздел сопровождается визуальными примерами, иллюстрирующими результат работы кода.
---

## Добавить объект Rectangle

Aspose.PDF для Python через .NET поддерживает функцию добавления графических объектов (например граф, линия, прямоугольник и т.д.) в PDF‑документы. Вы также можете добавить объект [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/), который предлагает возможность заполнения прямоугольника.

Сначала посмотрим возможность создания объекта Rectangle.

Следуйте инструкциям ниже:

1. Создать новый PDF [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Добавить [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) в коллекцию страниц PDF‑файла.
1. Добавить [Text fragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) в коллекцию абзацев экземпляра страницы.
1. Создать экземпляр [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/).
1. Установить границу для [Drawing object](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/).
1. Добавить объект [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) в коллекцию фигур объекта Graph.
1. Добавить графический объект в коллекцию абзацев экземпляра страницы.
1. Добавить [Text fragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) в коллекцию абзацев экземпляра страницы.
1. И сохранить ваш PDF‑файл

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("Rectangle")

    # Add Text fragment to paragraphs collection of page instance
    page.paragraphs.add(text_fragment)

    # Create Graph instance
    graph = drawing.Graph(400, 300)

    # Add graph object to paragraphs collection of page instance
    page.paragraphs.add(graph)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)
    graph.border = border_info

    # Create Rectangle instance
    rect = drawing.Rectangle(20, 20, 350, 250)

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(rect)

    # Add Text fragment to paragraphs collection of page instance
    page.paragraphs.add(text_fragment)

    # Save PDF file
    document.save(path_outfile)
```

![Создать прямоугольник](create_rectangle.png)

## Создать заполненный объект Rectangle

Aspose.PDF для Python через .NET также предлагает возможность заполнить объект прямоугольника определённым цветом.

В следующем фрагменте кода показано, как добавить объект [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/), заполненный цветом.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add a page
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(100, 400)

    # Add graph object to the paragraphs collection of the page instance
    page.paragraphs.add(graph)

    # Create Rectangle instance with specified dimensions
    rect = drawing.Rectangle(100, 100, 200, 120)

    # Specify fill color for the Rectangle object
    rect.graph_info.fill_color = ap.Color.red

    # Add rectangle object to the shapes collection of the Graph object
    graph.shapes.add(rect)

    # Save PDF document
    document.save(path_outfile)
```

Посмотрите результат прямоугольника, заполненного сплошным цветом:

![Заполненный прямоугольник](fill_rectangle.png)

## Добавить рисунок с градиентной заливкой

Aspose.PDF для Python через .NET поддерживает возможность добавления графических объектов в PDF‑документы, и иногда требуется заполнить графические объекты градиентным цветом.

В следующем фрагменте кода показано, как добавить объект [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/), заполненный градиентным цветом.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(400, 400)

    # Add graph object to paragraphs collection of page instance
    page.paragraphs.add(graph)

    # Create Rectangle instance
    rect = drawing.Rectangle(0, 0, 300, 300)

    # Specify fill color for Graph object
    gradient_color = ap.Color()
    gradient_settings = drawing.GradientAxialShading(ap.Color.red, ap.Color.blue)
    gradient_settings.start = ap.Point(0, 0)
    gradient_settings.end = ap.Point(350, 350)
    gradient_color.pattern_color_space = gradient_settings
    rect.graph_info.fill_color = gradient_color

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(rect)

    # Save PDF file
    document.save(output_file)
```

![Градиентный прямоугольник](gradient.png)

## Создать прямоугольник с альфа‑каналом цвета

Aspose.PDF для Python .NET поддерживает заполнение объекта прямоугольника определённым цветом. Объект прямоугольника также может иметь альфа‑канал цвета, чтобы придать прозрачный вид. В следующем фрагменте кода показано, как добавить объект [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) с альфа‑каналом цвета.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(100, 400)

    # Add graph object to paragraphs collection of page instance
    page.paragraphs.add(graph)

    # Create Rectangle instance
    rect = drawing.Rectangle(100, 100, 200, 120)

    # Specify fill color for Graph object
    rect.graph_info.fill_color = ap.Color.from_argb(128, 244, 180, 0)

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(rect)

    # Create second rectangle object
    rect1 = drawing.Rectangle(200, 150, 200, 100)
    rect1.graph_info.fill_color = ap.Color.from_argb(160, 120, 0, 120)
    graph.shapes.append(rect1)

    # Save PDF file
    document.save(output_file)
```

![Прямоугольник с альфа‑каналом цвета](rectangle_color.png)

## Управление Z‑Order фигур

Aspose.PDF для .NET поддерживает возможность добавления графических объектов (например граф, линия, прямоугольник и т.д.) в PDF‑документы. При добавлении более одного экземпляра одного и того же объекта в PDF‑файл мы можем управлять их отрисовкой, указывая Z‑Order. Z‑Order также используется, когда необходимо отображать объекты друг над другом.

В следующем фрагменте кода показаны шаги по отрисовке объектов [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) друг над другом.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Set size of PDF page
    page.set_page_size(375, 300)

    # Set left margin for page object as 0
    page.page_info.margin.left = 0

    # Set top margin of page object as 0
    page.page_info.margin.top = 0

    # Create a new rectangle with Color as Red, Z-Order as 0 and certain dimensions
    add_rectangle(page, 50, 40, 60, 40, ap.Color.red, 2)

    # Create a new rectangle with Color as Blue, Z-Order as 0 and certain dimensions
    add_rectangle_to_page(page, 20, 20, 30, 30, ap.Color.blue, 1)

    # Create a new rectangle with Color as Green, Z-Order as 0 and certain dimensions
    add_rectangle_to_page(page, 40, 40, 60, 30, ap.Color.green, 0)

    # Save resultant PDF file
    document.save(output_file)
```

![Управление Z‑Order](control.png)
