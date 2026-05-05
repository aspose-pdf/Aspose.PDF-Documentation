---
title: Добавить фигуры Arc в PDF на Python
linktitle: Добавить Arc
type: docs
weight: 10
url: /ru/python-net/add-arc/
description: Узнайте, как рисовать и заполнять формы дуг в PDF‑файлах на Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Добавление объекта Arc в PDF с использованием Python
Abstract: В статье представлено подробное руководство о том, как добавлять и настраивать объекты дуг в PDF‑документах с использованием Aspose.PDF for Python via .NET. Она подчёркивает возможность библиотеки включать графические элементы, такие как дуги, что важно для приложений, требующих динамического создания PDF‑контента, например технических схем и пользовательских иллюстраций. В статье содержатся пошаговые инструкции и фрагменты кода, демонстрирующие, как создать экземпляр `Document`, настроить объект `Drawing` с указанными размерами и свойствами границы, а также добавить объекты `Graph` и `Arc` на страницу PDF. Дополнительно рассматривается процесс заполнения объектов дуг цветом, показывается, как задать свойства заполнения для дуг и линий, и в конечном итоге сохранить PDF‑документ. Приведённые примеры служат практическим руководством для разработчиков, желающих использовать Aspose.PDF for Python via .NET для точных графических манипуляций в PDF‑файлах.
---

## Добавить объект Arc

Aspose.PDF for Python via .NET поддерживает возможность добавлять графические объекты (например граф, линию, прямоугольник и т.п.) в PDF‑документы. Он также предлагает возможность заполнять объект дуги определённым цветом.

В этом примере показано, как программно рисовать дуги в PDF‑документе с использованием Aspose.PDF for Python via .NET. Используя модуль рисования, разработчики могут создавать сложные графические элементы, такие как дуги, с точным контролем их внешнего вида и позиционирования. Эта возможность важна для приложений, требующих динамического создания графического контента в PDF, например технических схем, диаграмм или пользовательских иллюстраций.

Следуйте шагам ниже:

1. Создать [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) экземпляр.
1. Создать [Graph object](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) с определёнными размерами.
1. Установить [border](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) для объекта рисования.
1. Создать соответсвующий обьект дуги.
1. Добавить данный обьект в коллекцию Shapes в обьекте графов.
1. Добавить [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) объект в коллекцию абзацев страницы.
1. Сохраните наш PDF-файл.

Следующий фрагмент кода показывает, как добавить [Arc](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) объект.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing
import sys
from os import path

def add_arc(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    arc1 = drawing.Arc(100, 100, 95, 0, 90)
    arc1.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(arc1)

    arc2 = drawing.Arc(100, 100, 90, 70, 180)
    arc2.graph_info.color = ap.Color.dark_blue
    graph.shapes.add(arc2)

    arc3 = drawing.Arc(100, 100, 85, 120, 210)
    arc3.graph_info.color = ap.Color.red
    graph.shapes.add(arc3)

    page.paragraphs.add(graph)
    document.save(outfile)
```

## Создать заполненный объект Arc

Следующий пример показывает, как добавить объект Arc, заполненный цветом и определёнными размерами.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing
import sys
from os import path

def add_arc_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    arc = drawing.Arc(100, 100, 95, 0, 90)

    arc.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(arc)

    line = drawing.Line([195, 100, 100, 100, 100, 195])
    line.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(line)

    page.paragraphs.add(graph)
    document.save(outfile)
```

Посмотрим результат добавления заполненного Arc:

![Заполненный объект Arc](filled_arc.png)

## Связанные темы графов

- [Работа с графами PDF в Python](/pdf/ru/python-net/working-with-graphs/)
- [Добавление круглых фигур в PDF в Python](/pdf/ru/python-net/add-circle/)
- [Добавление кривых фигур в PDF в Python](/pdf/ru/python-net/add-curve/)
- [Добавить линейные фигуры в PDF с помощью Python](/pdf/ru/python-net/add-line/)