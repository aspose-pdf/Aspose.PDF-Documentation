---
title: Добавить объект круга в PDF-файл
linktitle: Добавить круг
type: docs
weight: 20
url: /ru/python-net/add-circle/
description: В этой статье объясняется, как создать объект круга в вашем PDF с помощью Aspose.PDF для Python через .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление объекта круга в PDF с использованием Python
Abstract: В статье предоставлено руководство по использованию Aspose.PDF для Python через .NET для создания объектов круга в PDF‑документах. Описывается процесс добавления как обведённых, так и заполненных графических кругов, подчёркивая, что круговые диаграммы могут быть полезным инструментом для отображения данных по нескольким категориям, когда данные представляют целое. Статья содержит пошаговые инструкции по созданию экземпляра `Document`, настройке объекта `Drawing` с определёнными размерами, применению границы и добавлению объекта `Graph` на страницу PDF. Примеры кода демонстрируют рисование простого круга и заполненного круга, с подробными инструкциями по установке цветов и добавлению текста в круг. Также представлены визуальные результаты этих операций, демонстрируя возможности Aspose.PDF по улучшению содержимого PDF с помощью динамических графических элементов.
---

## Добавить объект круга

Как и гистограммы, круговые диаграммы могут использоваться для отображения данных в нескольких отдельных категориях. Однако, в отличие от гистограмм, круговые диаграммы можно использовать только при наличии данных для всех категорий, составляющих целое. Итак, давайте рассмотрим добавление объекта [Круг](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/circle/) с помощью Aspose.PDF для Python .NET.

Этот пример демонстрирует, как программно нарисовать круг внутри PDF‑документа с использованием Aspose.PDF для Python через .NET. Используя модуль рисования, разработчики могут создавать сложные графические элементы с точным контролем над их внешним видом и позиционированием. Такая возможность необходима для приложений, требующих динамического создания графического контента в PDF, например технических схем, диаграмм или кастомных иллюстраций.

Следуйте инструкциям ниже:

1. Создайте экземпляр [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .
1. Создайте объект [Drawing](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) с определенными размерами.
1. Установите [границу](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) для объекта Drawing.
1. Добавьте объект [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) в коллекцию параграфов страницы.
1. Сохраните наш PDF-файл.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 200)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create a circle with the specified coordinates and radius
    circle = drawing.Circle(100, 100, 40)

    # Set the circle's color
    circle.graph_info = drawing.GraphInfo()
    circle.graph_info.color = ap.Color.green_yellow

    # Add the circle to the graph shapes
    graph.shapes.add(circle)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

Нарисованный нами круг будет выглядеть так:

![Рисунок круга](drawing_circle.png)

## Создать объект заполненного круга

Этот пример показывает, как добавить объект круга, заполненный цветом.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 200)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create a filled circle
    circle = drawing.Circle(100, 100, 40)
    circle.graph_info = drawing.GraphInfo()
    circle.graph_info.color = ap.Color.green_yellow
    circle.graph_info.fill_color = ap.Color.green
    circle.text = ap.text.TextFragment("Circle")

    # Add the circle to the graph shapes
    graph.shapes.add(circle)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

Посмотрим результат добавления заполненного круга:

![Заполненный круг](filled_circle.png)


