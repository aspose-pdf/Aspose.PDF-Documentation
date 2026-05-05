---
title: Проверка границ фигур в графах PDF с Python
linktitle: Проверить границы фигур
type: docs
weight: 70
url: /python-net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Узнайте, как проверять границы фигур в коллекциях графов PDF с помощью Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Проверяйте границы фигур графов в файлах PDF с использованием Python
Abstract: В этой статье показано, как проверять границы фигур в коллекциях Graph с помощью Aspose.PDF for Python via .NET. Описывается настройка BoundsCheckMode, обнаружение фигур за пределами диапазона и безопасная обработка исключений границ.
---

## Проверьте границы фигур в Graph

Когда вы добавляете фигуры к [Граф](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/), вы можете включить проверку границ, чтобы убедиться, что каждая фигура помещается в область графа.

Используйте [BoundsCheckMode](https://reference.aspose.com/pdf/python-net/aspose.pdf/boundscheckmode/) для определения поведения, когда фигура выходит за пределы. В этом примере, `THROW_EXCEPTION_IF_DOES_NOT_FIT` используется для вызова исключения.

Выполните следующие шаги:

1. Создайте новый PDF [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Добавьте [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Создайте [Граф](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) и добавить его на страницу.
1. Создайте [Прямоугольник](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) который выходит за пределы границ графика.
1. Установить режим проверки границ в `THROW_EXCEPTION_IF_DOES_NOT_FIT`.
1. Добавьте прямоугольник и обработайте исключение.
1. Сохраните документ.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def check_shape_bounds(outfile: str):
    document = ap.Document()
    page = document.pages.add()

    graph = drawing.Graph(100, 100)
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

    document.save(outfile)
```

## Примечания

- Используйте `THROW_EXCEPTION_IF_DOES_NOT_FIT` когда требуется строгая проверка макета.
- Для разрешительного поведения выберите другое `BoundsCheckMode` вариант в зависимости от ваших требований к макету.

## Связанные темы графов

- [Работа с графиками PDF в Python](/pdf/ru/python-net/working-with-graphs/)
- [Добавить прямоугольные фигуры в PDF в Python](/pdf/ru/python-net/add-rectangle/)
- [Добавить линейные фигуры в PDF в Python](/pdf/ru/python-net/add-line/)
- [Добавить эллиптические фигуры в PDF в Python](/pdf/ru/python-net/add-ellipse/)
