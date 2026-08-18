---
title: Add Arc Shapes to PDF in Java
linktitle: Добавить дугу
type: docs
weight: 10
url: /java/add-arc/
description: Узнайте, как рисовать и заполнять дуги в файлах PDF на Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Рисование дуг в файлах PDF с помощью Java
Abstract: В этой статье показано, как добавлять формы дуг в документы PDF с помощью Aspose.PDF для Java. Он охватывает рисование нескольких очерченных дуг разными цветами и создание заполненного сегмента дуги путем объединения дуги с замыкающей линией.
---
Aspose.PDF для Java использует `Graph` вместе с объектами фигур, такими как `Arc` и `Line`, для рендеринга векторной графики.

## Добавьте контуры дуг

1. Создайте новый PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте контейнер [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) и добавьте его на страницу.
1. Создайте фигуру [Дуга](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) и настройте ее геометрию.
1. Добавьте [Дугу](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) в контейнер [График](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. Установите свойства фигуры, необходимые для примера, включая [Цвет](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. Сохраните выходной PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addArc(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Arc arc1 = new Arc(100, 100, 95, 0, 90);
        arc1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(arc1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```

В полном примере к одному графику добавляются три дуги с разными радиусами, углами и цветами.

## Добавьте сегмент заполненной дуги

1. Создайте новый PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте контейнер [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) и добавьте его на страницу.
1. Создайте фигуру [Линия](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) и настройте ее координаты.
1. Создайте фигуру [Дуга](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) и настройте ее геометрию.
1. Добавьте [Линию](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) и [Дугу](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) в контейнер [График](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. Сохраните выходной PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addArcFilled(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Arc arc = new Arc(100, 100, 95, 0, 90);
        arc.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().addItem(arc);

        Line line = new Line(new float[]{195, 100, 100, 100, 100, 195});
        line.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().addItem(line);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
