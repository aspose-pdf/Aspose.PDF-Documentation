---
title: Добавить объект линии в PDF файл
linktitle: Добавить линию
type: docs
weight: 40
url: /ru/python-net/add-line/
description: В этой статье объясняется, как создать объект линии в вашем PDF, используя Aspose.PDF для Python через .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление объекта линии в PDF с помощью Python
Abstract: В статье рассматривается, как добавить объекты линии в PDF‑документ с помощью Aspose.PDF для Python через .NET. Описывается процесс создания экземпляра `Document` и добавления объекта `Graph` в PDF. Статья предоставляет подробные шаги по созданию и настройке объекта `Line`, включая указание его шаблона штриховки и цвета. В ней представлены фрагменты кода, демонстрирующие, как добавить простую линию, пунктирно‑штриховую линию и как нарисовать линии по всей странице, образуя крест. Каждый раздел сопровождается визуальным представлением полученного PDF. Это руководство служит практическим ресурсом для разработчиков, желающих улучшить свои PDF‑документы графическими элементами с использованием Aspose.PDF.
---

## Добавить объект линии

Aspose.PDF for Python via .NET поддерживает возможность добавлять графические объекты (например граф, линия, прямоугольник и т.д.) в PDF‑документы. Вы также получаете возможность добавить объект [Линия](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/), где можно указать шаблон штриховки, цвет и другое форматирование элемента линии.

Следуйте инструкциям ниже:

1. Создать экземпляр [Документ](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .
1. Создать объект Graph
1. Добавить объект [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) в коллекцию абзацев страницы.
1. Создать и настроить объект Line
1. Добавить [Line](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) в Graph
1. Сохранить наш PDF‑файл.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(100, 400)

    # Add graph object to paragraphs collection of page instance
    page.paragraphs.add(graph)

    # Create Rectangle instance
    line = drawing.Line([100, 100, 200, 100])

    # Specify fill color for Graph object
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(line)

    # Save PDF file
    document.save(path_outfile)
```

![Добавить линию](add_line.png)

## Как добавить пунктирно‑штриховую линию в ваш PDF‑документ

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(100, 400)

    # Add graph object to paragraphs collection of page instance
    page.paragraphs.add(graph)

    # Create Rectangle instance
    line = drawing.Line([100, 100, 200, 100])

    # Set color for Line object
    line.graph_info.color = ap.Color.red

    # Specify fill color for Graph object
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(line)

    # Save PDF file
    document.save(path_outfile)
```

Давайте проверим результат:

![Пунктирная линия](dash_line.png)

## Нарисовать линию по всей странице

Мы также можем использовать объект линии, чтобы нарисовать крест, начиная от левого нижнего угла к правому верхнему и от левого верхнего угла к правому нижнему.

Пожалуйста, посмотрите следующий фрагмент кода, чтобы выполнить это требование.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Set page margin on all sides as 0
    page.page_info.margin.left = 0
    page.page_info.margin.right = 0
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0

    # Create Graph object with Width and Height equal to page dimensions
    graph = drawing.Graph(page.page_info.width, page.page_info.height)

    # Create first line object starting from Lower-Left to Top-Right corner of page
    line = drawing.Line([page.rect.llx, 0, page.page_info.width, page.rect.ury])

    # Add line to shape collection of Graph object
    graph.shapes.append(line)

    # Draw line from Top-Left corner of page to Bottom-Right corner of page
    line2 = drawing.Line([0, page.rect.ury, page.page_info.width, page.rect.llx])

    # Add line to shape collection of Graph object
    graph.shapes.append(line2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF file
    document.save(path_outfile)
```

![Рисование линии](draw_line.png)


