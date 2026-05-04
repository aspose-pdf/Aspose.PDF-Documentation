---
title: Проверьте границы фигур в графах PDF с Python
type: docs
weight: 70
url: /python-net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Узнайте, как проверять границы фигур в коллекциях графов PDF на Python.
lastmod: "2026-04-16"
draft: false
TechArticle: true 
AlternativeHeadline: Руководство по проверке границ фигур в Shapes
Abstract: Эта статья предлагает всестороннее руководство по использованию функции проверки границ в коллекции Shapes, особенно в PDF‑документах с использованием Python. Эта функция помогает гарантировать, что графические элементы, такие как формы, правильно помещаются в свои родительские контейнеры. Её можно настроить так, чтобы при выходе компонента за пределы контейнера генерировалось исключение, обеспечивая надёжную обработку ошибок. Руководство пошагово описывает создание нового PDF‑документа, добавление страницы и создание графического элемента (прямоугольной формы) внутри объекта графа. Предоставлены подробные инструкции по созданию `Document`, добавлению `Page` и созданию объекта `Graph`. Описывается настройка формы `Rectangle` и установка `BoundsCheckMode` в значение `THROW_EXCEPTION_IF_DOES_NOT_FIT`, что гарантирует выброс исключения, если форма не помещается в заданные размеры графа. Процесс иллюстрируется примером кода на Python с использованием библиотеки Aspose.PDF, демонстрируя практическую реализацию этих возможностей.
---

В этой статье представлено подробное руководство по использованию функции проверки границ в коллекции Shapes. Эта функция гарантирует, что элементы помещаются в их родительский контейнер и может быть настроена для выбрасывания исключения, если компонент не помещается.

1. Создать новый PDF [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Добавить страницу
1. Создать [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/)
1. Создать прямоугольную фигуру
1. Режим проверки границ
1. Добавить [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) к Graph

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing
import sys
from os import path

def check_shape_bounds(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = ap.drawing.Graph(100, 100)
    graph.top = 10
    graph.left = 15
    graph.border = ap.BorderInfo(ap.BorderSide.BOX, 1, ap.Color.black)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(-1, 0, 50, 50)
    rect.graph_info.fill_color = ap.Color.tomato
    try:
        graph.shapes.update_bounds_check_mode(
            ap.BoundsCheckMode.THROW_EXCEPTION_IF_DOES_NOT_FIT
        )
        graph.shapes.add(rect)
    except Exception as e:
        print(e)
```

## Связанные темы графов

- [Работа с графами PDF в Python](/pdf/ru/python-net/working-with-graphs/)
- [Добавить прямоугольные фигуры в PDF на Python](/pdf/ru/python-net/add-rectangle/)
- [Добавить линейные фигуры в PDF с помощью Python](/pdf/ru/python-net/add-line/)
- [Добавить эллиптические фигуры в PDF на Python](/pdf/ru/python-net/add-ellipse/)
