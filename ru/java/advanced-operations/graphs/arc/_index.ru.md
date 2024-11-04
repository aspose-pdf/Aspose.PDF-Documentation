---
title: Добавить объект дуги в PDF файл
linktitle: Добавить дугу
type: docs
weight: 10
url: /java/add-arc/
description: В этой статье объясняется, как создать объект дуги в вашем PDF с использованием Aspose.PDF для Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Добавить объект дуги

Aspose.PDF для Java поддерживает возможность добавления графических объектов (например, график, линия, прямоугольник и т.д.) в документы PDF. Он также предлагает возможность заполнения объекта дуги определенным цветом.

Следуйте шагам ниже:

1. Создайте экземпляр [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)

1. Создайте [Drawing object](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame) с определенными размерами

1. Установите [Border](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-) для объекта Drawing

1. Добавьте объект [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) в коллекцию абзацев страницы

1. Сохраните наш PDF файл

Следующий фрагмент кода показывает, как добавить объект [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Arc).

```java
    public static void ExampleArc() {
        // Создать экземпляр документа
        Document pdfDocument = new Document();
        // Добавить страницу в коллекцию страниц PDF файла
        Page page = pdfDocument.getPages().add();

        // Создать объект Drawing с определенными размерами
        Graph graph = new Graph(400, 400);
        // Установить границу для объекта Drawing
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Arc arc1 = new Arc(100, 100, 95, 0, 90);
        arc1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(arc1);

        Arc arc2 = new Arc(100, 100, 90, 70, 180);
        arc2.getGraphInfo().setColor(Color.getDarkBlue());
        graph.getShapes().add(arc2);

        Arc arc3 = new Arc(100, 100, 85, 120, 210);
        arc3.getGraphInfo().setColor(Color.getRed());
        graph.getShapes().add(arc3);

        // Добавить объект Graph в коллекцию параграфов страницы
        page.getParagraphs().add(graph);

        // Сохранить PDF файл
        pdfDocument.save(_dataDir + "DrawingArc_out.pdf");

    }
```


## Создание заполненного объекта дуги

Следующий пример показывает, как добавить объект дуги, заполненный цветом и имеющий определенные размеры.

```java
    public static void ExampleFilledArc() {
        // Создайте экземпляр документа
        Document pdfDocument = new Document();
        // Добавьте страницу в коллекцию страниц PDF-файла
        Page page = pdfDocument.getPages().add();

        // Создайте объект Drawing с определенными размерами
        Graph graph = new Graph(400, 400);
        // Установите границу для объекта Drawing
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Arc arc = new Arc(100, 100, 95, 0, 90);
        arc.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(arc);

        Line line = new Line(new float[] { 195, 100, 100, 100, 100, 195 });
        line.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(line);

        // Добавьте объект Graph в коллекцию абзацев страницы
        page.getParagraphs().add(graph);

        // Сохраните PDF-файл
        pdfDocument.save(_dataDir + "DrawingArc_out.pdf");

    }
```


Let's see the result of adding a filled Arс:

![Заполненная дуга](filled_arc.png)