---
title: Добавить эллиптические фигуры в PDF в Java
linktitle: Добавить эллипс
type: docs
weight: 60
url: /java/add-ellipse/
description: Узнайте, как рисовать, заполнять и маркировать эллипсы в файлах PDF на Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Рисование эллипсов в файлах PDF с помощью Java
Abstract: В этой статье показано, как добавить формы эллипса в PDF-документы с помощью Aspose.PDF для Java. Он охватывает очерченные эллипсы, заполненные эллипсы и размещение фрагментов текста внутри эллипсов.
---
## Добавьте контуры эллипса

1. Создайте новый PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте контейнер [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) и добавьте его на страницу.
1. Создайте фигуру [Эллипс](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) и настройте ее геометрию.
1. Добавьте [Эллипс](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) в контейнер [График](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. Установите свойства фигуры, необходимые для примера, включая [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) и [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. Сохраните выходной PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

В полном примере к одному графику добавляются два разных контурных эллипса.

## Добавьте заполненные эллипсы

`createEllipseFilled` заполняет два эллипса `Color.getGreenYellow()` и `Color.getDarkRed()`.

## Добавьте текст внутри эллипсов

1. Создайте новый PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) и установите необходимые параметры форматирования текста.
1. Создайте контейнер [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) и добавьте его на страницу.
1. Создайте фигуру [Эллипс](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) и настройте ее геометрию.
1. Добавьте [Эллипс](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) в контейнер [График](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. Сохраните выходной PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
