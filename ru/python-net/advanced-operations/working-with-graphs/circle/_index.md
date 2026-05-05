---
title: Добавить Circle в PDF с помощью Python
linktitle: Добавить Circle
type: docs
weight: 20
url: /ru/python-net/add-circle/
description: Узнайте, как рисовать и заполнять круговые формы в PDF‑файлах с помощью Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Добавление объекта Circle в PDF с использованием Python
Abstract: В статье представлено руководство по использованию Aspose.PDF for Python via .NET для создания объектов круга в PDF‑документах. Описывается процесс добавления как контурных, так и заполненных графических элементов круга, подчёркивая, как круговые диаграммы могут быть полезным инструментом для отображения данных по нескольким категориям, когда данные представляют собой целое. В статье содержатся пошаговые инструкции по созданию экземпляра `Document`, настройке объекта `Drawing` с определёнными размерами, применению границы и добавлению объекта `Graph` на страницу PDF. Примеры кода демонстрируют рисование простого круга и заполненного круга, с подробными инструкциями по установке цветов и добавлению текста в круг. Также представлены визуальные результаты этих операций, демонстрирующие возможности Aspose.PDF по улучшению содержимого PDF с помощью динамических графических элементов.
---

## Добавить объект Circle

Как и столбчатые графики, круговые графики могут использоваться для отображения данных в нескольких отдельных категориях. Однако, в отличие от столбчатых графиков, круговые графики можно использовать только тогда, когда у вас есть данные для всех категорий, составляющих целое. Итак, давайте посмотрим, как добавить [Circle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/circle/) объект с Aspose.PDF for Python .NET.

Этот пример демонстрирует, как программно нарисовать круг в PDF‑документе с использованием Aspose.PDF for Python via .NET. Используя модуль рисования, разработчики могут создавать сложные графические элементы с точным контролем их внешнего вида и позиционирования. Эта возможность важна для приложений, которым требуется динамическое создание графического контента в PDF, таких как технические схемы, диаграммы или пользовательские иллюстрации.

Следуйте шагам ниже:

1. Создать [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) экземпляр.
1. Создать [Drawing object](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) с определёнными размерами.
1. Установить [border](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) для объекта рисования.
1. Добавить [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) объект в коллекцию абзацев страницы.
1. Сохраните наш PDF-файл.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing
import sys
from os import path

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

![Рисование Circle](drawing_circle.png)

## Создать объект заполненного Circle

Этот пример показывает, как добавить объект Circle, заполненный цветом.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing
import sys
from os import path

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

Посмотрим результат добавления заполненного Circle:

![Заполненный Circle](filled_circle.png)

## Связанные темы графов

- [Работа с графами PDF в Python](/pdf/ru/python-net/working-with-graphs/)
- [Добавить дуговые формы в PDF на Python](/pdf/ru/python-net/add-arc/)
- [Добавить эллиптические фигуры в PDF на Python](/pdf/ru/python-net/add-ellipse/)
- [Добавить прямоугольные фигуры в PDF на Python](/pdf/ru/python-net/add-rectangle/)