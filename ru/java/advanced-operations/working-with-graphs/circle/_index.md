---
title: Добавить круговые фигуры в PDF на Java
linktitle: Добавить круг
type: docs
weight: 20
url: /ru/java/add-circle/
description: Узнайте, как рисовать и заполнять круговые формы в PDF‑файлах на Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Рисовать круговые формы в PDF‑файлах с помощью Java
Abstract: В этой статье показано, как добавить круговые формы в PDF‑документы с использованием Aspose.PDF for Java. Описывается рисование контуров кругов, заполнение кругов цветом и размещение текста внутри круговой формы.
---
## Добавьте контур круга

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте [Граф](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) контейнер и добавить его на страницу.
1. Создайте [Круг](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) фигуру и настроить её геометрию.
1. Добавьте [Круг](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) к [Граф](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) контейнер.
1. Установите свойства фигуры, требуемые примером, включая [Цвет](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. Сохраните выходной PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addCircle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Circle circle = new Circle(100, 100, 40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(circle);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```

## Добавьте заполненный круг с текстом

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте [Граф](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) контейнер и добавить его на страницу.
1. Создайте [Круг](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) фигуру и настроить её геометрию.
1. Добавьте [Круг](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) к [Граф](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) контейнер.
1. Установите свойства фигуры, требуемые примером, включая [Цвет](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) и [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. Сохраните выходной PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addCircleFilled(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Circle circle = new Circle(100, 100, 40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());
        circle.getGraphInfo().setFillColor(Color.getGreen());
        circle.setText(new TextFragment("Circle"));
        graph.getShapes().addItem(circle);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```


