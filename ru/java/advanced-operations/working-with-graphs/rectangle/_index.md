---
title: Добавить прямоугольные фигуры в PDF в Java
linktitle: Добавить прямоугольник
type: docs
weight: 50
url: /java/add-rectangle/
description: Узнайте, как рисовать и заполнять прямоугольные формы в файлах PDF на Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Рисование прямоугольников в файлах PDF с помощью Java
Abstract: В этой статье показано, как добавлять прямоугольные формы в PDF-документы с помощью Aspose.PDF для Java. Он охватывает очерченные прямоугольники, сплошные заливки, градиентные заливки, альфа-прозрачность и управление z-порядком для перекрывающихся фигур.
---
## Добавляем контур прямоугольника

1. Создайте новый PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте контейнер [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) и добавьте его на страницу.
1. Создайте фигуру [Прямоугольник](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) и настройте ее геометрию.
1. Добавьте [Прямоугольник](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) в контейнер [График](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. Сохраните выходной PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addRectangle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 300.0);
        page.getParagraphs().add(graph);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        Rectangle rectangle = new Rectangle(20, 20, 350, 250);
        graph.getShapes().addItem(rectangle);

        document.save(outputFile.toString());
    }
}
```

## Залейте прямоугольник сплошным или градиентным цветом.

Примеры прямоугольников включают в себя:

- `createRectangleFilled` для сплошной заливки `Color.getRed()`
- `addDrawingWithGradientFill` для заливки `GradientAxialShading`

## Используйте альфа-прозрачность

`createRectangleWithAlphaColorChannel` применяет полупрозрачные цвета с помощью `Color.fromArgb(...)`, поэтому перекрывающиеся прямоугольники остаются видимыми.

## Управлять z-порядком прямоугольников

1. Создайте новый PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Установите необходимый размер [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Добавьте настроенные фигуры [Прямоугольник](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) на целевую страницу с необходимым Z-порядком.
1. Сохраните выходной PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void controlZOrderOfRectangle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.setPageSize(375, 300);
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setTop(0);

        addRectangleToPage(page, 50, 40, 60, 40, Color.getRed(), 2);
        addRectangleToPage(page, 20, 20, 30, 30, Color.getBlue(), 1);
        addRectangleToPage(page, 40, 40, 60, 30, Color.getGreen(), 0);

        document.save(outputFile.toString());
    }
}
```
