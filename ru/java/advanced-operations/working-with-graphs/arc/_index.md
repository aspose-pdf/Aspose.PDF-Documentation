---
title: Добавление форм дуги в PDF на Java
linktitle: Добавление дуги
type: docs
weight: 10
url: /ru/java/add-arc/
description: Узнайте, как рисовать и заполнять формы дуг в PDF‑файлах на Java.
lastmod: "2026-09-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Рисовать формы дуг в PDF‑файлах с использованием Java
Abstract: В этой статье показано, как добавить формы дуг в PDF‑документы с помощью Aspose.PDF for Java. Описывается рисование нескольких контурных дуг разного цвета и создание заполненного сегмента дуги путем комбинирования дуги с закрывающей линией.
---
Aspose.PDF for Java использует `Graph` вместе с объектами формы, такими как `Arc` и `Line`, для рендеринга векторной графики.

## Добавление контуров дуги

1. Создайте новый PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте контейнер [Граф](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) и добавьте его на страницу.
1. Создайте фигуру [Дуга](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) и настройте её геометрию.
1. Добавьте [Дуга](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) в контейнер [Граф](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
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

## Добавление заполненного сегмента дуги

1. Создайте новый PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте контейнер [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) и добавьте его на страницу.
1. Создайте фигуру [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) и настройте её координаты.
1. Создайте фигуру [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) и настройте её геометрию.
1. Добавьте [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) и [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) в контейнер [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
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


