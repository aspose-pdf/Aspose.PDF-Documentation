---
title: Проверка границ формы в графиках PDF с помощью Java
linktitle: Проверьте границы формы
type: docs
weight: 70
url: /java/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Узнайте, как проверять границы фигур в коллекциях графов PDF на Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Проверка границ формы графика в файлах PDF с помощью Java
Abstract: В этой статье показано, как проверить границы фигур в коллекциях Graph с помощью Aspose.PDF для Java. В нем рассматривается включение строгой проверки границ, попытка добавить фигуру, выходящую за пределы допустимого диапазона, и обработка полученного исключения при сохранении документа.
---
Используйте `BoundsCheckMode`, когда вам нужно убедиться, что фигуры помещаются внутри контейнера графа.

## Проверка границ формы графика

1. Создайте новый PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте контейнер [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) и добавьте его на страницу.
1. Создайте фигуру [Прямоугольник](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) и настройте ее геометрию.
1. Включите строгую проверку границ и попробуйте добавить фигуру в коллекцию графиков с помощью `BoundsCheckMode`.
1. Обработайте исключение, если фигура не подходит.
1. Сохраните выходной PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
