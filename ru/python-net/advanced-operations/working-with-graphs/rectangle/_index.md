---
title: Добавить Rectangle в PDF на Python
linktitle: Добавить Rectangle
type: docs
weight: 50
url: /ru/python-net/add-rectangle/
description: Узнайте, как рисовать и заполнять прямоугольные фигуры в PDF‑файлах на Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Добавление объекта прямоугольника в PDF с помощью Python
Abstract: Статья предоставляет всестороннее руководство по тому, как добавлять и управлять объектами Rectangle в PDF‑документах с использованием Aspose.PDF for Python via .NET. Она подробно описывает процесс создания Rectangle и интеграции его в PDF‑документ, включая установку границ и заполнение его сплошными цветами или градиентными заливками. В статье содержатся пошаговые инструкции с фрагментами кода, демонстрирующими создание PDF‑документа, добавление страниц и вставку объектов Rectangle с различными визуальными свойствами, такими как сплошные цветные заливки, градиентные заливки и прозрачность с использованием alpha channels. Кроме того, объясняется, как контролировать Z-Order объектов Rectangle для управления порядком их отображения, когда несколько фигур добавляются в один PDF. Каждый раздел сопровождается визуальными примерами, иллюстрирующими результат работы фрагментов кода.
---

## Добавить объект Rectangle

Aspose.PDF for Python via .NET поддерживает возможность добавления графических объектов (например граф, линия, прямоугольник и т.д.) в PDF‑документы. Вы также получаете возможность добавить [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) объект, который также предлагает возможность заполнить объект Rectangle.

Сначала давайте рассмотрим возможность создания объекта Rectangle.

Следуйте шагам ниже:

1. Создать новый PDF [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Добавить [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) к коллекции страниц PDF‑файла.
1. Добавить [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) к коллекции абзацев экземпляра страницы.
1. Создать [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) экземпляр.
1. Установить границу для [Drawing object](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/).
1. Добавить [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) объект в коллекцию фигур объекта Graph.
1. Добавьте объект graph в коллекцию абзацев экземпляра страницы.
1. Добавить [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) к коллекции абзацев экземпляра страницы.
1. И сохраните ваш PDF файл

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing
import sys
from os import path

def add_rectangle(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("Rectangle")
    page.paragraphs.add(text_fragment)

    graph = drawing.Graph(400, 300)
    page.paragraphs.add(graph)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    rect = drawing.Rectangle(20, 20, 350, 250)
    graph.shapes.add(rect)
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

![Создать rectangle](create_rectangle.png)

## Создать объект заполненного прямоугольника

Aspose.PDF for Python via .NET также предлагает возможность заполнить объект прямоугольника определённым цветом.

Следующий фрагмент кода показывает, как добавить [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) объект, заполненный цветом.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing
import sys
from os import path

def create_rectangle_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(100, 100, 200, 120)
    rect.graph_info.fill_color = ap.Color.red
    graph.shapes.add(rect)

    document.save(outfile)
```

Посмотрите на результат залитого сплошным цветом прямоугольника:

![Заполненный прямоугольник](fill_rectangle.png)

## Добавить рисунок с градиентным заполнением

Aspose.PDF for Python via .NET поддерживает возможность добавлять графические объекты в PDF‑документы, и иногда требуется заполнять графические объекты градиентным цветом.

Следующий фрагмент кода показывает, как добавить [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) объект, заполненный градиентным цветом.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing
import sys
from os import path

def add_drawing_with_gradient_fill(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(0, 0, 300, 300)
    gradient_color = ap.Color()
    gradient_settings = drawing.GradientAxialShading(ap.Color.red, ap.Color.blue)
    gradient_settings.start = ap.Point(0, 0)
    gradient_settings.end = ap.Point(350, 350)
    gradient_color.pattern_color_space = gradient_settings
    rect.graph_info.fill_color = gradient_color
    graph.shapes.add(rect)

    document.save(outfile)
```

![Градиентный Rectangle](gradient.png)

## Создать прямоугольник с альфа-каналом цвета

Aspose.PDF for Python .NET поддерживает заполнение объекта прямоугольника определённым цветом. Объект прямоугольника также может иметь альфа-канал цвета для создания прозрачного внешнего вида. Следующий фрагмент кода показывает, как добавить a [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) объект с альфа-каналом цвета.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing
import sys
from os import path

def create_rectangle_with_alpha_color_channel(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(100, 100, 200, 120)
    rect.graph_info.fill_color = ap.Color.from_argb(128, 244, 180, 0)
    graph.shapes.add(rect)

    rect1 = drawing.Rectangle(200, 150, 200, 100)
    rect1.graph_info.fill_color = ap.Color.from_argb(160, 120, 0, 120)
    graph.shapes.add(rect1)

    document.save(outfile)
```

![Цвет альфа-канала прямоугольника](rectangle_color.png)

## Управление Z-Order фигур

Aspose.PDF for .NET поддерживает возможность добавлять графические объекты (например граф, линию, прямоугольник и т.д.) в PDF-документы. При добавлении более чем одного экземпляра одного и того же объекта в PDF-файл мы можем управлять их отображением, указывая Z-Order. Z-Order также используется, когда необходимо отобразить объекты друг над другом.

Следующий фрагмент кода показывает шаги рендеринга [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) объекты друг над другом.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def _add_rectangle_to_page(
    page: ap.Page,
    x: float,
    y: float,
    width: float,
    height: float,
    color: ap.Color,
    zindex: int,
):
    graph = drawing.Graph(width, height)
    graph.is_change_position = False
    graph.left = x
    graph.top = y
    rect = drawing.Rectangle(0, 0, width, height)
    rect.graph_info.fill_color = color
    rect.graph_info.color = color
    graph.shapes.add(rect)
    graph.z_index = zindex
    page.paragraphs.add(graph)


def control_z_order_of_rectangle(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(375, 300)
    page.page_info.margin.left = 0
    page.page_info.margin.top = 0

    _add_rectangle_to_page(page, 50, 40, 60, 40, ap.Color.red, 2)
    _add_rectangle_to_page(page, 20, 20, 30, 30, ap.Color.blue, 1)
    _add_rectangle_to_page(page, 40, 40, 60, 30, ap.Color.green, 0)

    document.save(outfile)
```

![Управление Z Order](control.png)

## Связанные темы графов

- [Работа с графами PDF в Python](/pdf/ru/python-net/working-with-graphs/)
- [Проверьте границы фигур в графиках PDF с помощью Python](/pdf/ru/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/)
- [Добавить линейные фигуры в PDF с помощью Python](/pdf/ru/python-net/add-line/)
- [Добавить эллиптические фигуры в PDF на Python](/pdf/ru/python-net/add-ellipse/)