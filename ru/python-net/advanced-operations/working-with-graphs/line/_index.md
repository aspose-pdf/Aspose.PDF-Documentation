---
title: Добавить Line в PDF на Python
linktitle: Добавить Line
type: docs
weight: 40
url: /ru/python-net/add-line/
description: Узнайте, как рисовать линейные фигуры и стилизованные линии в PDF‑файлах с помощью Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Добавление объекта линии в PDF с помощью Python
Abstract: В статье рассматривается, как добавить объекты линии в PDF‑документ с использованием Aspose.PDF for Python via .NET. Описывается процесс создания экземпляра `Document` и добавления в PDF объекта `Graph`. В статье приведены подробные шаги по созданию и настройке объекта `Line`, включая указание его шаблона штриховки и цвета. В ней содержатся фрагменты кода, демонстрирующие, как добавить простую линию, пунктирную линию и как рисовать линии по странице, образуя крестообразный узор. Каждый раздел сопровождается визуальным представлением полученного PDF. Этот руководитель служит практическим ресурсом для разработчиков, желающих улучшить свои PDF‑документы графическими элементами с помощью Aspose.PDF.
---

## Добавить объект Line

Aspose.PDF for Python via .NET поддерживает возможность добавления графических объектов (например граф, линия, прямоугольник и т.д.) в PDF‑документы. Вы также получаете возможность добавить [Line](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) объект, в котором вы также можете указать шаблон пунктирной линии, цвет и другое форматирование для элемента Line.

Следуйте шагам ниже:

1. Создать [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) экземпляр.
1. Создать объект Graph
1. Добавить [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) объект в коллекцию абзацев страницы.
1. Создать и настроить линию
1. Добавить [Line](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) к Graph
1. Сохраните наш PDF-файл.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def add_line(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    line = drawing.Line([100, 100, 200, 100])
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1
    graph.shapes.add(line)

    document.save(outfile)
```

![Добавить Line](add_line.png)

## Как добавить пунктирно‑точечную Line в ваш PDF‑документ

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing
import sys
from os import path

def add_dotted_dashed_line(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    line = drawing.Line([100, 100, 200, 100])
    line.graph_info.color = ap.Color.red
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1
    graph.shapes.add(line)

    document.save(outfile)
```

Давайте проверим результат:

![Пунктирная Line](dash_line.png)

## Нарисовать Line через страницу

Мы также можем использовать объект Line, чтобы нарисовать крест, начиная от Left-Bottom к Right-Upper и от Left-Top к Bottom-Right.

Пожалуйста, просмотрите следующий фрагмент кода, чтобы выполнить это требование.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing
import sys
from os import path

def draw_line_across_page(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    page.page_info.margin.left = 0
    page.page_info.margin.right = 0
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0

    graph = drawing.Graph(page.page_info.width, page.page_info.height)
    line = drawing.Line([page.rect.llx, 0, page.page_info.width, page.rect.ury])
    graph.shapes.add(line)
    line2 = drawing.Line([0, page.rect.ury, page.page_info.width, page.rect.llx])
    graph.shapes.add(line2)
    page.paragraphs.add(graph)

    document.save(outfile)
```

![Рисование Line](draw_line.png)

## Связанные темы графов

- [Работа с графами PDF в Python](/pdf/ru/python-net/working-with-graphs/)
- [Добавление кривых фигур в PDF в Python](/pdf/ru/python-net/add-curve/)
- [Добавить прямоугольные фигуры в PDF на Python](/pdf/ru/python-net/add-rectangle/)
- [Проверьте границы фигур в графиках PDF с помощью Python](/pdf/ru/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/)
