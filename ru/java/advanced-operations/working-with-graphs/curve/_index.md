---
title: Добавить криволинейные формы в PDF на Java
linktitle: Добавить кривую
type: docs
weight: 30
url: /ru/java/add-curve/
description: Узнайте, как рисовать и заполнять криволинейные формы в PDF‑файлах на Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Рисуйте криволинейные формы в PDF‑файлах с использованием Java
Abstract: В этой статье показано, как добавить криволинейные формы в PDF‑документы с помощью Aspose.PDF for Java. Описывается создание кривой из массивов координат и применение либо цвета контура, либо цвета заливки внутри контейнера Graph.
---
Кривые в Aspose.PDF for Java определяются массивом координат типа float, передаваемым в `Curve`.

## Добавьте контур кривой

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте [Граф](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) контейнер и добавить его на страницу.
1. Создайте [Кривую](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) форму и настроить её контрольные точки.
1. Добавьте [Кривую](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) к [Граф](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) контейнер.
1. Установите свойства фигуры, необходимые для примера, включая [Цвет](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. Сохраните результирующий PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

