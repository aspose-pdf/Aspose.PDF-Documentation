---
title: Добавление штампов изображений в PDF в Java
linktitle: Штампы изображений в PDF-файле
type: docs
weight: 10
url: /java/image-stamps-in-pdf-page/
description: Узнайте, как добавлять штампы изображений на страницы PDF в Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавляйте штампы изображений и фоновые изображения на страницы PDF с помощью Java
Abstract: В этой статье объясняется, как добавлять штампы изображений в файлы PDF с помощью Aspose.PDF для Java. Он охватывает штампы изображений с позиционированием, вращением, непрозрачностью и контролем качества, а также использует изображение в качестве фона плавающего блока.
---
Aspose.PDF для Java поддерживает штампы изображений в виде наложений и элементов макета на основе изображений.

## Добавьте штамп изображения

Используйте этот пример, когда на странице должен отображаться штамп изображения с произвольным размещением и непрозрачностью.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp/) и настройте его внешний вид.
1. Добавьте штамп на страницу и сохраните документ.

```java
public static void addImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImageStamp imageStamp = new ImageStamp(imageFile.toString());
        imageStamp.setBackground(true);
        imageStamp.setXIndent(100);
        imageStamp.setYIndent(100);
        imageStamp.setHeight(300);
        imageStamp.setWidth(300);
        imageStamp.setRotate(Rotation.on270);
        imageStamp.setOpacity(0.5);

        document.getPages().get_Item(1).addStamp(imageStamp);
        document.save(outputFile.toString());
    }
}
```

## Добавьте штамп изображения с контролем качества

Используйте этот пример, если вам нужно настроить качество рендеринга штампа изображения.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp/) и установите значение качества.
1. Добавьте штамп на страницу и сохраните результат.

```java
public static void addImageStampWithQualityControl(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImageStamp imageStamp = new ImageStamp(imageFile.toString());
        imageStamp.setQuality(10);
        document.getPages().get_Item(1).addStamp(imageStamp);
        document.save(outputFile.toString());
    }
}
```

## Используйте изображение в качестве фона плавающего блока.

Используйте этот пример, когда изображение должно служить фоном контейнера стилизованного макета.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и получите доступ к целевой странице.
1. Создайте [FloatingBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/floatingbox/) с настройками текста и границ.
1. Установите фоновое изображение, добавьте поле на страницу и сохраните документ.

```java
public static void addImageAsBackgroundInFloatingBox(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        FloatingBox box = new FloatingBox(200.0f, 100.0f);
        box.setLeft(40);
        box.setTop(80);
        box.setHorizontalAlignment(HorizontalAlignment.Center);
        box.getParagraphs().add(new TextFragment("Text in Floating Box"));
        box.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        Image image = new Image();
        image.setFile(imageFile.toString());
        box.setBackgroundImage(image);
        box.setBackgroundColor(Color.getYellow());
        page.getParagraphs().add(box);

        document.save(outputFile.toString());
    }
}
```
