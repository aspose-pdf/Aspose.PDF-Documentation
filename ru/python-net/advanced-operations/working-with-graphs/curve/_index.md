---
title: Добавить объект кривой в PDF файл
linktitle: Добавить кривую
type: docs
weight: 30
url: /ru/python-net/add-curve/
description: В этой статье объясняется, как создать объект кривой в вашем PDF с помощью Aspose.PDF для Python через .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление объекта кривой в PDF с использованием Python
Abstract: В статье рассматривается реализация графических кривых в PDF‑документах с использованием библиотеки Aspose.PDF для Python через .NET. Представлена концепция графической кривой, представляющей собой объединение проектных линий, а также подробно описан процесс создания как простых, так и заполненных кривых Безье программным способом. В статье даны пошаговые инструкции и фрагменты кода для рисования кривых в PDF, с акцентом на манипуляцию графическими элементами с помощью модуля рисования Aspose.PDF. Процесс включает создание экземпляра `Document`, определение объекта `Drawing` с указанными размерами, установку границ и добавление объекта `Graph` на страницу PDF. Визуальные результаты этих примеров кода иллюстрируются изображениями, показывающими полученные кривые. Статья также исследует создание заполненных объектов кривой, демонстрируя, как задавать цвет заливки для кривых, что имеет важное значение для генерации динамического графического контента, такого как технические схемы, диаграммы или пользовательские иллюстрации в PDF.
---

## Добавить объект кривой

Графическая [кривая](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/curve/) представляет собой соединённое объединение проектных линий, каждая из которых пересекается с тремя другими в обычных двойных точках.

В этой статье мы исследуем простые графические кривые и заполненные кривые, которые вы можете создать в своем PDF‑документе.

Этот пример иллюстрирует, как программно нарисовать кривую Безье в PDF‑документе с помощью Aspose.PDF для Python через .NET. Используя модуль рисования, разработчики могут создавать сложные графические элементы с точным контролем их внешнего вида и позиционирования. Эта возможность важна для приложений, требующих динамического создания графического контента в PDF, таких как технические схемы, диаграммы или пользовательские иллюстрации.

Следуйте инструкциям ниже:

1. Создайте экземпляр [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Создайте [объект Drawing](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) с определёнными размерами.
1. Установите [границу](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) для объекта Drawing.
1. Добавьте объект [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) в коллекцию абзацев страницы.
1. Сохраните наш PDF‑файл.

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

    # Create a curve and set its properties
    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info = drawing.GraphInfo()
    curve1.graph_info.color = ap.Color.green_yellow

    # Add the curve to the graph shapes
    graph.shapes.add(curve1)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

Следующее изображение показывает результат, полученный с помощью нашего фрагмента кода:

![Рисование кривой](drawing_curve.png)

## Создать заполненный объект кривой

Этот пример показывает, как добавить объект Curve, заполненный цветом.

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

    # Create a curve and set fill color
    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info = drawing.GraphInfo()
    curve1.graph_info.fill_color = ap.Color.green_yellow

    # Add the curve to the graph shapes
    graph.shapes.add(curve1)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

Посмотрите результат добавления заполненной Curve:

![Заполненная кривая](filled_curve.png)

