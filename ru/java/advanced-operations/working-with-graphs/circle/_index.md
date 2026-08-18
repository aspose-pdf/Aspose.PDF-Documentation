---
title: Добавить формы круга в PDF в Java
linktitle: Добавить круг
type: docs
weight: 20
url: /java/add-circle/
description: Узнайте, как рисовать и заполнять круги в файлах PDF на Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Рисование кругов в файлах PDF с помощью Java
Abstract: В этой статье показано, как добавлять формы кругов в PDF-документы с помощью Aspose.PDF для Java. Он охватывает рисование контуров кругов, заливку кругов цветом и размещение текста внутри круга.
---
## Добавьте контур круга

1. Создайте новый PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте контейнер [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) и добавьте его на страницу.
1. Создайте фигуру [Круг](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) и настройте ее геометрию.
1. Добавьте [Круг](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) в контейнер [График](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. Установите свойства фигуры, необходимые для примера, включая [Цвет](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. Сохраните выходной PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

1. Создайте новый PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте контейнер [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) и добавьте его на страницу.
1. Создайте фигуру [Круг](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) и настройте ее геометрию.
1. Добавьте [Круг](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) в контейнер [График](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. Установите свойства фигуры, необходимые для примера, включая [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) и [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. Сохраните выходной PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
