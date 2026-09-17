---
title: Добавление прямоугольных форм в PDF на Java
linktitle: Добавление прямоугольника
type: docs
weight: 50
url: /ru/java/add-rectangle/
description: Узнайте, как рисовать и заполнять прямоугольные формы в PDF‑файлах на Java.
lastmod: "2026-09-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Рисовать прямоугольные формы в PDF‑файлах с использованием Java
Abstract: В этой статье показано, как добавить прямоугольные формы в PDF‑документы с помощью Aspose.PDF for Java. Рассматриваются обведённые прямоугольники, сплошные заливки, градиентные заливки, альфа‑прозрачность и управление порядком наложения (z‑order) для перекрывающихся фигур.
---
## Добавление контура прямоугольника

1. Создайте новый PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте контейнер [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) и добавьте его на страницу.
1. Создайте фигуру [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) и настройте её геометрию.
1. Добавьте [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) в контейнер [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. Сохраните выходной PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

## Заполнение прямоугольника сплошным или градиентным цветом

Примеры прямоугольников включают:

- `createRectangleFilled` для сплошной заливки с `Color.getRed()`
- `addDrawingWithGradientFill` для заливки с помощью `GradientAxialShading`

## Использование альфа-прозрачности

`createRectangleWithAlphaColorChannel` применяет полупрозрачные цвета с `Color.fromArgb(...)`, чтобы перекрывающиеся прямоугольники оставались видимыми.

## Управление порядком наложения прямоугольников

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Установите требуемый размер страницы [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Добавьте настроенные фигуры [Прямоугольник](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) на целевую страницу в требуемом порядке наложения.
1. Сохраните выходной PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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


