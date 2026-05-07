---
title: Добавить эллиптические формы в PDF на Python
linktitle: Добавить эллипс
type: docs
weight: 60
url: /python-net/add-ellipse/
description: Узнайте, как рисовать, заполнять и подписывать эллиптические формы в PDF‑файлах на Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Рисовать эллиптические формы в PDF‑файлах с помощью Python.
Abstract: Эта статья показывает, как добавлять формы эллипсов в PDF‑документы с помощью Aspose.PDF for Python via .NET. В ней рассматриваются контурные эллипсы, заполненные эллипсы и добавление текста внутрь объектов эллипса.
---

## Добавить объект Ellipse

Aspose.PDF for Python via .NET позволяет добавлять [Ellipse](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) формы в PDF‑страницы с [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) класс. Вы можете рисовать контуры эллипсов, применять цвета заливки и размещать текст внутри объектов эллипсов.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

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

![Добавить эллипс](ellipse.png)

## Создать заполненный объект эллипса

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

![Заполненный Эллипс](fill_ellipse.png)

## Добавить текст внутри Эллипса

Aspose.PDF for Python via .NET также позволяет размещать текст внутри объектов фигур. Следующий пример добавляет текст к фигурам-эллипсам.

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

![Текст внутри эллипса](text_ellipse.png)

## Связанные темы графов

- [Работа с графами PDF в Python](/pdf/ru/python-net/working-with-graphs/)
- [Добавить формы круга в PDF в Python](/pdf/ru/python-net/add-circle/)
- [Добавить формы кривой в PDF в Python](/pdf/ru/python-net/add-curve/)
- [Добавьте прямоугольные фигуры в PDF на Python](/pdf/ru/python-net/add-rectangle/)
