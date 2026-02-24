---
title: Добавить объект эллипса в PDF‑файл
linktitle: Добавить эллипс
type: docs
weight: 60
url: /ru/python-net/add-ellipse/
description: В этой статье объясняется, как создать объект Эллипс в вашем PDF, используя Aspose.PDF для Python через .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление объекта эллипса в PDF с помощью Python
Abstract: Статья представляет собой всестороннее руководство по использованию Aspose.PDF для Python через .NET для добавления и настройки объектов Эллипс в PDF‑документах. В ней объясняется процесс создания и манипулирования эллипсами, включая задание их размеров, цветов и позиционирования с помощью модуля рисования. Демонстрируется, как рисовать эллипсы на странице PDF, показывая возможность управлять их внешним видом и расположением. В примере показана настройка свойств рамки и добавление нескольких эллипсов в график. Иллюстрируется заполнение эллипсов конкретными цветами, приводится пример, где два эллипса заполнены разными цветами и добавлены в PDF‑документ. Описывается, как вставлять текст внутрь объектов Эллипс, используя свойство text объекта Graph. Приведённый пример показывает, как установить свойства шрифта и добавить текст в
---

## Добавить объект эллипса

Aspose.PDF для Python через .NET поддерживает добавление объектов [Эллипс](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) в PDF‑документы. Он также предоставляет возможность заполнять объект эллипса определённым цветом.

Этот пример иллюстрирует, как программно рисовать и настраивать эллипсы в PDF‑документе с использованием Aspose.PDF для Python через .NET. Используя модуль рисования, разработчики могут создавать сложные графические элементы с точным контролем их внешнего вида и позиционирования. Эта возможность важна для приложений, требующих динамического создания графического контента в PDF, таких как технические схемы, диаграммы или пользовательские иллюстрации.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add a page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create first ellipse with specified coordinates and radii
    ellipse1 = drawing.Ellipse(150, 100, 120, 60)
    ellipse1.graph_info.color = ap.Color.green_yellow
    ellipse1.text = ap.TextFragment("Ellipse")

    # Add first ellipse to graph
    graph.shapes.add(ellipse1)

    # Create second ellipse with different dimensions and color
    ellipse2 = drawing.Ellipse(50, 50, 18, 300)
    ellipse2.graph_info.color = ap.Color.dark_red

    # Add second ellipse to graph
    graph.shapes.add(ellipse2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)

```

![Добавить эллипс](ellipse.png)

## Создать заполненный объект эллипса

Следующий фрагмент кода показывает, как добавить объект [Эллипс](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/), заполненный цветом.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add a page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create first ellipse and set its fill color
    ellipse1 = drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow

    # Add first ellipse to graph
    graph.shapes.add(ellipse1)

    # Create second ellipse and set its fill color
    ellipse2 = drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red

    # Add second ellipse to graph
    graph.shapes.add(ellipse2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

![Заполненный эллипс](fill_ellipse.png)

## Добавить текст внутрь эллипса

Aspose.PDF для Python через .NET поддерживает добавление текста внутрь объекта Graph. Свойство Text объекта Graph предоставляет возможность установить текст объекта Graph. Следующий фрагмент кода показывает, как добавить текст внутрь объекта Эллипс.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    text_fragment = ap.text.TextFragment("Ellipse")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Helvetica")
    text_fragment.text_state.font_size = 24

    ellipse1 = ap.drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow
    ellipse1.text = text_fragment
    graph.shapes.append(ellipse1)

    ellipse2 = ap.drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red
    ellipse2.text = text_fragment
    graph.shapes.append(ellipse2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF file
    document.save(path_outfile)
```

![Текст внутри эллипса](text_ellipse.png)

