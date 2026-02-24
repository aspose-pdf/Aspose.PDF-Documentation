---
title: Добавить объект дуги в PDF файл
linktitle: Добавить дугу
type: docs
weight: 10
url: /ru/python-net/add-arc/
description: В этой статье объясняется, как создать объект дуги в вашем PDF с помощью Aspose.PDF for Python via .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление объекта дуги в PDF с использованием Python
Abstract: Статья предоставляет подробное руководство по добавлению и настройке объектов дуги в PDF‑документах с использованием Aspose.PDF for Python via .NET. В ней подчеркивается возможность библиотеки включать графические элементы, такие как дуги, что важно для приложений, нуждающихся в динамической генерации PDF‑контента, например технических схем и пользовательских иллюстраций. В статье содержатся пошаговые инструкции и фрагменты кода, демонстрирующие, как создать экземпляр `Document`, настроить объект `Drawing` с заданными размерами и свойствами границы, а также добавить объекты `Graph` и `Arc` на страницу PDF. Кроме того, рассматривается процесс заполнения объектов дуги цветом, показывается, как задать свойства заливки для дуг и линий, и в итоге сохранить PDF‑документ. Приведённые примеры служат практическим руководством для разработчиков, желающих использовать Aspose.PDF для точных графических манипуляций в PDF‑файлах.
---

## Добавить объект дуги

Aspose.PDF for Python via .NET поддерживает возможность добавлять графические объекты (например граф, линию, прямоугольник и т.д.) в PDF‑документы. Он также предоставляет возможность заполнять объект дуги определённым цветом.

Этот пример иллюстрирует, как программно рисовать дуги в PDF‑документе с помощью Aspose.PDF for Python via .NET. Используя модуль рисования, разработчики могут создавать сложные графические элементы, такие как дуги, с точным контролем их внешнего вида и положения. Эта возможность важна для приложений, требующих динамической генерации графического контента в PDF, таких как технические схемы, диаграммы или пользовательские иллюстрации.

Следуйте инструкциям ниже:

1. Создать экземпляр [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .
1. Создать [Drawing object](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) с определенными размерами.
1. Установить [border](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) для объекта Drawing.
1. Добавить объект [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) в коллекцию абзацев страницы.
1. Сохранить наш PDF файл.

Следующий фрагмент кода показывает, как добавить объект [Arc](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) .

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create arcs and set their properties
    arc1 = drawing.Arc(100, 100, 95, 0, 90)
    arc1.graph_info = drawing.GraphInfo()
    arc1.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(arc1)

    arc2 = drawing.Arc(100, 100, 90, 70, 180)
    arc2.graph_info = drawing.GraphInfo()
    arc2.graph_info.color = ap.Color.dark_blue
    graph.shapes.add(arc2)

    arc3 = drawing.Arc(100, 100, 85, 120, 210)
    arc3.graph_info = drawing.GraphInfo()
    arc3.graph_info.color = ap.Color.red
    graph.shapes.add(arc3)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

## Создать заполненный объект дуги

Следующий пример показывает, как добавить объект дуги, заполненный цветом и заданными размерами.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create an arc and set fill color
    arc = drawing.Arc(100, 100, 95, 0, 90)
    arc.graph_info = drawing.GraphInfo()
    arc.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(arc)

    # Create a line and set fill color
    line = drawing.Line([195, 100, 100, 100, 100, 195])
    line.graph_info = drawing.GraphInfo()
    line.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(line)

    # Add Graph object to the paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

Посмотрим результат добавления заполненной дуги:

![Заполненная дуга](filled_arc.png)

