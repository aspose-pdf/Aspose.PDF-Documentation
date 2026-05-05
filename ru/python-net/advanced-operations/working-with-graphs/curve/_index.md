---
title: Добавить Curve в PDF на Python
linktitle: Добавить Curve
type: docs
weight: 30
url: /ru/python-net/add-curve/
description: Узнайте, как рисовать и заполнять формы кривых в PDF‑файлах на Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Добавление объекта кривой в PDF с помощью Python
Abstract: В статье рассматривается реализация графических кривых в PDF‑документах с использованием библиотеки Aspose.PDF для Python via .NET. Представлена концепция графической кривой, представляющей собой объединение проективных линий, а также подробно описан процесс создания как простых, так и заполненных Bézier‑кривых программным способом. В статье представлены пошаговые инструкции и фрагменты кода для рисования кривых внутри PDF, с акцентом на манипуляцию графическими элементами с помощью модуля рисования Aspose.PDF. Процесс включает создание экземпляра `Document`, определение объекта `Drawing` с заданными размерами, установку границ и добавление объекта `Graph` на страницу PDF. Визуальные результаты этих примеров кода иллюстрируются изображениями, показывающими полученные кривые. В статье также исследуется создание заполненных объектов кривой, демонстрируя, как задавать цвета заливки для кривых, что имеет решающее значение для генерации динамического графического контента, такого как технические диаграммы, графики или пользовательские иллюстрации в PDF.
---

## Добавить объект кривой

Граф [Curve](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/curve/) является соединённым объединением проективных прямых, каждая из которых пересекает три другие в обычных двойных точках.

В этой статье мы исследуем простые графовые кривые и заполненные кривые, которые вы можете создать в своем PDF‑документе.

Этот пример демонстрирует, как программно нарисовать кривую Бéзье внутри PDF‑документа с помощью Aspose.PDF for Python via .NET. Используя модуль рисования, разработчики могут создавать сложные графические элементы с точным контролем их внешнего вида и позиционирования. Эта возможность важна для приложений, требующих динамической генерации графического контента в PDF, таких как технические схемы, диаграммы или пользовательские иллюстрации.

Следуйте шагам ниже:

1. Создать [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) экземпляр.
1. Создать [Drawing object](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) с определёнными размерами.
1. Установить [border](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) для объекта рисования.
1. Добавить [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) объект в коллекцию абзацев страницы.
1. Сохраните наш PDF-файл.

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

Следующее изображение показывает результат, полученный при выполнении нашего фрагмента кода:

![Drawing Curve](drawing_curve.png)

## Создать объект заполненной Curve

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

Посмотрите результат добавления заполненного Curve:

![Заполненный Curve](filled_curve.png)

## Связанные темы графов

- [Работа с графами PDF в Python](/pdf/ru/python-net/working-with-graphs/)
- [Добавить дуговые формы в PDF на Python](/pdf/ru/python-net/add-arc/)
- [Добавить линейные фигуры в PDF с помощью Python](/pdf/ru/python-net/add-line/)
- [Добавить эллиптические фигуры в PDF на Python](/pdf/ru/python-net/add-ellipse/)