---
title: Добавить круглые формы в PDF на Python
linktitle: Добавить круг
type: docs
weight: 20
url: /python-net/add-circle/
description: Узнайте, как рисовать и заполнять формы кругов в PDF‑файлах на Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Рисовать формы кругов в PDF‑файлах, используя Python
Abstract: В этой статье показано, как добавить формы кругов в PDF‑документы с помощью Aspose.PDF for Python via .NET. Описывается создание контурных кругов, заполнение кругов цветом и размещение текста внутри объектов круга.
---

## Добавить объект круга

Aspose.PDF for Python via .NET позволяет вам добавлять [Круг](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/circle/) фигуры на страницы PDF через [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) class. Используйте круги для схем, аннотаций и простых визуальных элементов.

Следуйте указаниям ниже:

1. Создайте [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) экземпляр.
1. Создайте объект [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) с определенными размерами.
1. Установите [Border](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) для объекта Graph.
1. Добавьте [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) объект в коллекцию абзацев страницы.
1. Сохраните наш PDF-файл.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_circle(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    circle = drawing.Circle(100, 100, 40)
    circle.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(circle)

    page.paragraphs.add(graph)
    document.save(outfile)
```

Нарисованный нами круг будет выглядеть так:

![Рисование круга](drawing_circle.png)

## Создать объект заполненного круга

Этот пример показывает, как добавить круг и заполнить его цветом.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_circle_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    circle = drawing.Circle(100, 100, 40)
    circle.graph_info.color = ap.Color.green_yellow
    circle.graph_info.fill_color = ap.Color.green
    circle.text = ap.text.TextFragment("Circle")
    graph.shapes.add(circle)

    page.paragraphs.add(graph)
    document.save(outfile)
```

Результат добавления заполненного круга:

![Заполненный круг](filled_circle.png)

## Связанные темы графиков

- [Работа с графиками PDF в Python](/pdf/ru/python-net/working-with-graphs/)
- [Добавление дуговых фигур в PDF на Python](/pdf/ru/python-net/add-arc/)
- [Добавить эллипсные фигуры в PDF на Python](/pdf/ru/python-net/add-ellipse/)
- [Добавить прямоугольные фигуры в PDF на Python](/pdf/ru/python-net/add-rectangle/)