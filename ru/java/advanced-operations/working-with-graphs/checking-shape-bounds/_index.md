---
title: Проверка границ фигур в графах PDF с помощью Java
linktitle: Проверка границ фигур
type: docs
weight: 70
url: /ru/java/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Узнайте, как проверять границы фигур в коллекциях графов PDF на Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Проверяйте границы фигур графов в PDF‑файлах с помощью Java
Abstract: В этой статье показано, как проверять границы фигур в коллекциях Graph с использованием Aspose.PDF for Java. Описывается включение строгой проверки границ, попытка добавить форму за пределами диапазона и обработка возникающего исключения при сохранении документа.
---
Использовать `BoundsCheckMode` когда вам нужно убедиться, что фигуры помещаются внутри контейнера графика.

## Проверьте границы формы графа

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте [Граф](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) контейнер и добавить его на страницу.
1. Создайте [Прямоугольник](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) фигуру и настроить её геометрию.
1. Включить строгую проверку границ и попытаться добавить форму в коллекцию графов с `BoundsCheckMode`.
1. Обработайте исключение, если форма не помещается.
1. Сохраните выходной PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void checkShapeBounds(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(100.0, 100.0);
        graph.setTop(10);
        graph.setLeft(15);
        graph.setBorder(new BorderInfo(BorderSide.Box, 1, Color.getBlack()));
        page.getParagraphs().add(graph);

        Rectangle rectangle = new Rectangle(-1, 0, 50, 50);
        rectangle.getGraphInfo().setFillColor(Color.getTomato());
        try {
            graph.getShapes().updateBoundsCheckMode(BoundsCheckMode.ThrowExceptionIfDoesNotFit);
            graph.getShapes().addItem(rectangle);
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }

        document.save(outputFile.toString());
    }
}
```

