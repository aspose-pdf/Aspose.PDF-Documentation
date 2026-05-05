---
title: Добавить линейные фигуры в PDF на Python
linktitle: Добавить линию
type: docs
weight: 40
url: /python-net/add-line/
description: Узнайте, как рисовать линейные фигуры и стилизованные линии в PDF‑файлах на Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Рисовать линейные фигуры в PDF‑файлах используя Python
Abstract: В этой статье показано, как добавить формы линий в PDF‑документы с помощью Aspose.PDF for Python via .NET. Она охватывает создание базовых линий, настройку пунктирных стилей линий и рисование линий по всей странице.
---

## Добавить объект Line

Aspose.PDF for Python via .NET позволяет вам добавить [Линия](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) формы в страницы PDF с использованием [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) класс. Вы можете управлять цветом линии, пунктирным шаблоном и размещением.

Выполните следующие шаги:

1. Создать [Документ](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) экземпляр.
1. Создать объект Graph
1. Добавить [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) объект в коллекцию абзацев страницы.
1. Создать и настроить строку
1. Добавить [Линия](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) к графу
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

![Добавить линию](add_line.png)

## Как добавить пунктирно‑штриховую линию в ваш PDF‑документ

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

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

Результат добавления пунктирно‑точечной линии:

![Пунктирная линия](dash_line.png)

## Нарисовать линию поперек страницы

Вы также можете нарисовать линии поперек страницы, чтобы сформировать крест.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

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

![Рисование линии](draw_line.png)

## Связанные темы графов

- [Работа с графиками PDF в Python](/pdf/ru/python-net/working-with-graphs/)
- [Добавить кривые формы в PDF в Python](/pdf/ru/python-net/add-curve/)
- [Добавить прямоугольные формы в PDF в Python](/pdf/ru/python-net/add-rectangle/)
- [Проверьте границы фигур в графиках PDF с помощью Python](/pdf/ru/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/)
