---
title: Добавить Ellipse в PDF на Python
linktitle: Добавить Ellipse
type: docs
weight: 60
url: /python-net/add-ellipse/
description: Узнайте, как рисовать, заполнять и подписывать эллиптические формы в PDF‑файлах на Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Добавление Ellipse в PDF с помощью Python
Abstract: Статья предоставляет всестороннее руководство по использованию Aspose.PDF for Python via .NET для добавления и настройки объектов Ellipse в PDF‑документах. В ней объясняется процесс создания и манипуляции эллипсами, включая задавание их размеров, цветов и положения с помощью модуля рисования. Продемонстрировано, как рисовать эллипсы на странице PDF, показывая возможность контролировать их внешний вид и позицию. В примере показано задание свойств границы и добавление нескольких эллипсов в график. Иллюстрируется, как заполнять эллипсы определёнными цветами, приводя пример, где два эллипса заполнены разными цветами и добавлены в PDF‑документ. Объясняется, как вставлять текст внутрь объектов Ellipse, используя свойство text объекта Graph. В приведённом примере показано, как задавать свойства шрифта и добавлять текст к
---

## Добавить объект Ellipse

Aspose.PDF for Python via .NET поддерживает добавление [Ellipse](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) объекты в PDF документы. Также предлагает функцию заполнения ellipse  объекта определённым цветом.

Этот пример иллюстрирует, как программно рисовать и настраивать эллипсы в PDF‑документе с использованием Aspose.PDF for Python via .NET. Используя модуль рисования, разработчики могут создавать сложные графические элементы с точным контролем их внешнего вида и положения. Эта возможность важна для приложений, которым требуется динамическое создание графического контента внутри PDF, таких как технические схемы, диаграммы или пользовательские иллюстрации.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing
import sys
from os import path

def add_ellipse(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    ellipse1 = drawing.Ellipse(150, 100, 120, 60)
    ellipse1.graph_info.color = ap.Color.green_yellow
    ellipse1.text = ap.text.TextFragment("Ellipse")
    graph.shapes.add(ellipse1)

    ellipse2 = drawing.Ellipse(50, 50, 18, 300)
    ellipse2.graph_info.color = ap.Color.dark_red
    graph.shapes.add(ellipse2)

    page.paragraphs.add(graph)
    document.save(outfile)
```

![Добавить Ellipse](ellipse.png)

## Создать объект заполненного Ellipse

Следующий фрагмент кода показывает, как добавить [Ellipse](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) объект, заполненный цветом.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def create_ellipse_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    ellipse1 = drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(ellipse1)

    ellipse2 = drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red
    graph.shapes.add(ellipse2)

    page.paragraphs.add(graph)
    document.save(outfile)
```

![Заполненный Ellipse](fill_ellipse.png)

## Добавить текст внутри Ellipse

Aspose.PDF for Python via .NET поддерживает добавление текста внутри графического объекта. Свойство Text графического объекта предоставляет возможность задать текст графического объекта. Следующий фрагмент кода демонстрирует, как добавить текст внутри объекта Ellipse.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_text_inside_ellipse(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    text_fragment = ap.text.TextFragment("Ellipse")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Helvetica")
    text_fragment.text_state.font_size = 24

    ellipse1 = ap.drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow
    ellipse1.text = text_fragment
    graph.shapes.add(ellipse1)

    ellipse2 = ap.drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red
    ellipse2.text = text_fragment
    graph.shapes.add(ellipse2)

    page.paragraphs.add(graph)
    document.save(outfile)
```

![Текст внутри Ellipse](text_ellipse.png)

## Связанные темы графов

- [Работа с графами PDF в Python](/pdf/ru/python-net/working-with-graphs/)
- [Добавление круглых фигур в PDF в Python](/pdf/ru/python-net/add-circle/)
- [Добавление кривых фигур в PDF в Python](/pdf/ru/python-net/add-curve/)
- [Добавить прямоугольные фигуры в PDF на Python](/pdf/ru/python-net/add-rectangle/)
