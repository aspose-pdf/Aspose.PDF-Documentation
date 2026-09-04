---
title: Добавить формы дуги в PDF на Java
linktitle: Добавить дугу
type: docs
weight: 10
url: /ru/java/add-arc/
description: Узнайте, как рисовать и заполнять формы дуг в PDF‑файлах на Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Рисовать формы дуг в PDF‑файлах с использованием Java
Abstract: В этой статье показано, как добавить формы дуг в PDF‑документы с помощью Aspose.PDF for Java. Описывается рисование нескольких контурных дуг разного цвета и создание заполненного сегмента дуги путем комбинирования дуги с закрывающей линией.
---
Aspose.PDF for Java использует `Graph` вместе с объектами формы, такими как `Arc` и `Line` для рендеринга векторной графики.

## Добавьте контуры дуги

1. Создайте новый PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте [Граф](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) контейнер и добавить его на страницу.
1. Создайте [Дуга](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) фигуру и настроить её геометрию.
1. Добавьте [Дуга](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) к [Граф](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) контейнер.
1. Установите свойства фигуры, необходимые для примера, включая [Цвет](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. Сохраните выходной PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

Полный пример добавляет три дуги с разными радиусами, углами и цветами в один и тот же график.

## Добавьте заполненный сегмент дуги

1. Создайте новый PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) контейнер и добавить его на страницу.
1. Создайте [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) фигуру и настроить её координаты.
1. Создайте [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) фигуру и настроить её геометрию.
1. Добавьте [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) и [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) к [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) контейнер.
1. Сохраните выходной PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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


