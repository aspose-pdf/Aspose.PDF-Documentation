---
title: Добавить кривые формы в PDF на Python
linktitle: Добавить кривую
type: docs
weight: 30
url: /python-net/add-curve/
description: Узнайте, как рисовать и заполнять кривые формы в PDF‑файлах на Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Рисуйте кривые формы в PDF‑файлах с помощью Python
Abstract: Эта статья показывает, как добавить кривые формы в PDF‑документы с помощью Aspose.PDF for Python via .NET. В ней рассматривается создание обведённых кривых, заполнение объектов кривой и отрисовка пользовательских путей кривой в контейнере Graph.
---

## Добавить объект Curve

Aspose.PDF for Python via .NET позволяет добавлять [Кривая](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/curve/) фигуры на страницы PDF через [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) класс.

В этой статье показано, как создать как контурные, так и залитые кривые.

Следуйте приведённым ниже шагам:

1. Создать [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) экземпляр.
1. Создать объект [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) с определёнными размерами.
1. Установить [Border](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) для объекта Graph.
1. Добавить [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) объект в коллекцию абзацев страницы.
1. Сохранить наш PDF‑файл.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_curve(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(curve1)

    page.paragraphs.add(graph)
    document.save(outfile)
```

На следующем изображении показан результат, выполненный с помощью нашего фрагмента кода:

![Рисование кривой](drawing_curve.png)

## Создать объект заполненной кривой

Этот пример показывает, как добавить объект Curve, заполненный цветом.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def add_curve_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(curve1)

    page.paragraphs.add(graph)
    document.save(outfile)
```

Результат добавления заполненной кривой:

![Заполненная кривая](filled_curve.png)

## Связанные темы графиков

- [Работа с графиками PDF в Python](/pdf/ru/python-net/working-with-graphs/)
- [Добавление дуговых фигур в PDF с помощью Python](/pdf/ru/python-net/add-arc/)
- [Добавить линейные формы в PDF на Python](/pdf/ru/python-net/add-line/)
- [Добавить эллиптические формы в PDF на Python](/pdf/ru/python-net/add-ellipse/)