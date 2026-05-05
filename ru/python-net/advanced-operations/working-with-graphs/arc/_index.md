---
title: Добавить формы дуг в PDF на Python
linktitle: Добавить дугу
type: docs
weight: 10
url: /python-net/add-arc/
description: Узнайте, как рисовать и заливать формы дуг в PDF‑файлах на Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление объекта дуги в PDF с помощью Python
Abstract: Статья предоставляет подробное руководство по добавлению и настройке объектов дуг внутри PDF‑документов с использованием Aspose.PDF for Python via .NET. В ней подчеркивается возможность библиотеки включать графические элементы, такие как дуги, что имеет решающее значение для приложений, требующих динамического создания содержимого PDF, например технических схем и пользовательских иллюстраций. В статье содержатся пошаговые инструкции и фрагменты кода, демонстрирующие, как создать экземпляр `Document`, настроить объект `Drawing` с указанными размерами и свойствами границы, а также добавить объекты `Graph` и `Arc` на страницу PDF. Кроме того, рассматривается процесс заливки объектов дуг цветом, показывающий, как задать свойства заливки для дуг и линий, и в конечном итоге сохранить PDF‑документ. Приведённые примеры служат практическим руководством для разработчиков, желающих использовать Aspose.PDF для точных графических манипуляций в PDF‑файлах.
---

## Добавить объект дуги

Aspose.PDF for Python via .NET позволяет вам добавлять [Дуга](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) фигуры в страницы PDF с использованием [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) класс. Вы можете рисовать контурные дуги и заполненные сегменты дуг для схем и технических иллюстраций.

Выполните следующие шаги:

1. Создать [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) экземпляр.
1. Создать [Объект графа](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) с определенными размерами.
1. Установить [граница](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) для объекта Graph.
1. Создайте соответствующий объект дуги.
1. Добавьте этот объект в коллекцию Shapes в объекте graph.
1. Добавить [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) объект в коллекцию paragraphs страницы.
1. Сохраните наш PDF‑файл.

Следующий фрагмент кода показывает, как добавить [Дуга](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) объект.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

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

## Создать заполненный объект дуги

В этом примере показано, как добавить сегмент дуги, заполненный цветом.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

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

Результат добавления залитой дуги:

![Залитая дуга](filled_arc.png)

## Связанные темы графов

- [Работа с графами PDF в Python](/pdf/ru/python-net/working-with-graphs/)
- [Добавление круговых фигур в PDF с помощью Python](/pdf/ru/python-net/add-circle/)
- [Добавить кривые формы в PDF на Python](/pdf/ru/python-net/add-curve/)
- [Добавить линейные формы в PDF на Python](/pdf/ru/python-net/add-line/)