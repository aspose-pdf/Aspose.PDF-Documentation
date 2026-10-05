---
title: Добавление эллиптических фигур в PDF на Java
linktitle: Добавление эллипса
type: docs
weight: 60
url: /ru/java/add-ellipse/
description: Узнайте, как рисовать, заполнять и подписывать эллиптические фигуры в PDF файлах на Java.
lastmod: "2026-09-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Рисуйте эллиптические фигуры в PDF файлах с помощью Java
Abstract: В этой статье показано, как добавить эллиптические фигуры в PDF‑документы с использованием Aspose.PDF for Java. Рассматриваются контурные эллипсы, заполненные эллипсы и размещение текстовых фрагментов внутри эллиптических фигур.
---
## Добавление контуров эллипсов

1. Создайте новый PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте контейнер [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) и добавьте его на страницу.
1. Создайте фигуру [Ellipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) и настройте её геометрию.
1. Добавьте [Ellipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) в контейнер [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. Установите свойства фигуры, необходимые для примера, включая [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) и [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. Сохраните выходной PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addEllipse(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Ellipse ellipse1 = new Ellipse(150, 100, 120, 60);
        ellipse1.getGraphInfo().setColor(Color.getGreenYellow());
        ellipse1.setText(new TextFragment("Ellipse"));
        graph.getShapes().addItem(ellipse1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```

Полный пример добавляет два разных контурных эллипса к одному и тому же графу.

## Добавление заполненных эллипсов

`createEllipseFilled` заполняет два эллипса `Color.getGreenYellow()` и `Color.getDarkRed()`.

## Добавление текста внутри эллипсов

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) и установите необходимые параметры форматирования текста.
1. Создайте контейнер [Граф](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) и добавьте его на страницу.
1. Создайте фигуру [Эллипс](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) и настройте её геометрию.
1. Добавьте [Эллипс](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) в контейнер [Граф](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. Сохраните выходной PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addTextInsideEllipse(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        TextFragment textFragment = new TextFragment("Ellipse");
        textFragment.getTextState().setFont(FontRepository.findFont("Helvetica"));
        textFragment.getTextState().setFontSize(24);

        Ellipse ellipse1 = new Ellipse(100, 100, 120, 180);
        ellipse1.getGraphInfo().setFillColor(Color.getGreenYellow());
        ellipse1.setText(textFragment);
        graph.getShapes().addItem(ellipse1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```


