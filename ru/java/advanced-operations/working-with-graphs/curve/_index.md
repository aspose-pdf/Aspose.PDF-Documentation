---
title: Добавить формы кривых в PDF в Java
linktitle: Добавить кривую
type: docs
weight: 30
url: /java/add-curve/
description: Узнайте, как рисовать и заполнять кривые в файлах PDF на Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Рисуйте формы кривых в файлах PDF с помощью Java
Abstract: В этой статье показано, как добавлять формы кривых в PDF-документы с помощью Aspose.PDF для Java. В нем рассматривается создание кривой из массивов координат и применение цвета обводки или цвета заливки внутри контейнера графика.
---
Кривые в Aspose.PDF для Java определяются массивом координат с плавающей запятой, передаваемым в `Curve`.

## Добавьте контур кривой

1. Создайте новый PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте контейнер [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) и добавьте его на страницу.
1. Создайте фигуру [Кривая](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) и настройте ее контрольные точки.
1. Добавьте [Кривую](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) в контейнер [График](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. Установите свойства фигуры, необходимые для примера, включая [Цвет](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. Сохраните выходной PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addCurve(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Curve curve1 = new Curve(new float[]{10, 10, 50, 60, 70, 10, 100, 120});
        curve1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(curve1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
