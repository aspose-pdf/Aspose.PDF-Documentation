---
title: Добавить линейные фигуры в PDF на Java
linktitle: Добавить линию
type: docs
weight: 40
url: /ru/java/add-line/
description: Узнайте, как рисовать линейные фигуры и стилизованные линии в PDF‑файлах на Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Рисовать линейные фигуры в PDF‑файлах с помощью Java
Abstract: В этой статье показано, как добавить линейные фигуры в PDF‑документы с использованием Aspose.PDF for Java. Описывается создание линий из массивов координат, применение пунктирного стиля и цвета, а также рисование линий по всей площади страницы.
---
## Добавьте пунктирную линию

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте [Граф](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) контейнер и добавить его на страницу.
1. Создайте [Линия](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) форму и настроить её координаты.
1. Добавьте [Линия](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) к [Граф](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) контейнер.
1. Сохраните выходной PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addLine(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(100.0, 400.0);
        page.getParagraphs().add(graph);

        Line line = new Line(new float[]{100, 100, 200, 100});
        line.getGraphInfo().setDashArray(new int[]{0, 1, 0});
        line.getGraphInfo().setDashPhase(1);
        graph.getShapes().addItem(line);

        document.save(outputFile.toString());
    }
}
```

## Добавьте цветную пунктирную или штриховую линию

`addDottedDashedLine` использует те же координаты и настройки пунктиров, но также применяет `Color.getRed()`.

## Рисовать линии по всей странице

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте [Граф](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) контейнер и добавить его на страницу.
1. Создайте [Линия](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) форму и настроить её координаты.
1. Добавьте [Линия](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) к [Граф](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) контейнер.
1. Сохраните выходной PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void drawLineAcrossPage(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);

        Graph graph = new Graph(page.getPageInfo().getWidth(), page.getPageInfo().getHeight());
        Line line = new Line(new float[]{
                (float) page.getRect().getLLX(),
                0,
                (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getURY()
        });
        graph.getShapes().addItem(line);
        page.getParagraphs().add(graph);

        document.save(outputFile.toString());
    }
}
```

