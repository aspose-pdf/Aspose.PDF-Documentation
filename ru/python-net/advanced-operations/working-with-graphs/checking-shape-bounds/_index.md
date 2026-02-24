---
title: Проверка границ фигур в коллекции Shapes с использованием Python
type: docs
weight: 70
url: /ru/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Узнайте, как проверять границы фигуры при вставке в коллекцию Shapes, чтобы убедиться, что она помещается в родительский контейнер.
lastmod: "2025-05-14"
draft: false
TechArticle: true
AlternativeHeadline: Руководство по проверке границ фигур в Shapes
Abstract: Эта статья предлагает всестороннее руководство по использованию функции проверки границ в коллекции Shapes, особенно в PDF‑документах с использованием Python. Функция помогает гарантировать, что графические элементы, такие как фигуры, правильно помещаются в свои родительские контейнеры. Ее можно настроить так, чтобы выбрасывать исключение, если компонент выходит за границы контейнера, обеспечивая надежную обработку ошибок. Руководство проходит процесс создания нового PDF‑документа, добавления страницы и создания графического элемента (прямоугольной фигуры) внутри объекта Graph. Предоставлены подробные инструкции по созданию `Document`, добавлению `Page` и созданию объекта `Graph`. Описывается настройка фигуры `Rectangle` и конфигурация `BoundsCheckMode` в значение `THROW_EXCEPTION_IF_DOES_NOT_FIT`, что обеспечивает выброс исключения, если фигура не помещается в указанные размеры графа. Процесс иллюстрируется примером кода на Python с использованием библиотеки Aspose.PDF, подчеркивая практическую реализацию этих функций.
---

Эта статья предоставляет подробное руководство по использованию функции проверки границ в коллекции Shapes. Эта функция гарантирует, что элементы помещаются в их родительский контейнер и может быть настроена для выброса исключения, если компонент не помещается.

1. Создайте новый PDF [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Добавьте страницу
1. Создайте [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/)
1. Создайте прямоугольную фигуру
1. Режим проверки границ
1. Добавьте [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) в Graph

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create a Graph object with specified dimensions
    graph = ap.drawing.Graph(100, 100)
    graph.top = 10
    graph.left = 15
    graph.border = ap.BorderInfo(ap.BorderSide.BOX, 1, ap.Color.black)
    page.paragraphs.add(graph)

    # Create a shape object(for example, Rectangle) with specified dimensions
    rect = drawing.Rectangle(-1, 0, 50, 50)
    rect.graph_info.fill_color = ap.Color.tomato

    # Set the BoundsCheck mode to THROW_EXCEPTION_IF_DOES_NOT_FIT
    graph.shapes.update_bounds_check_mode(ap.BoundsCheckMode.THROW_EXCEPTION_IF_DOES_NOT_FIT)

    # Add the rectangle to the graph
    graph.shapes.add(rect)
```            
