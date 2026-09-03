---
title: Добавить штампы изображений в PDF на Java
linktitle: Штампы изображений в PDF‑файле
type: docs
weight: 10
url: /ru/java/image-stamps-in-pdf-page/
description: Узнайте, как добавить штампы изображений на страницы PDF с помощью Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавьте штампы изображений и фоновые изображения на страницы PDF с помощью Java
Abstract: В этой статье объясняется, как добавить штамп‑изображение в PDF‑файлы с помощью Aspose.PDF for Java. Рассматриваются штампы‑изображения с позиционированием, вращением, непрозрачностью и контролем качества, а также использование изображения в качестве фона плавающего блока.
---
Aspose.PDF for Java поддерживает штампы‑изображения в качестве наложений и элементов макета, основанных на изображении.

## Добавьте штамп‑изображение

Используйте этот пример, когда странице нужно отобразить штамп‑изображение с пользовательским расположением и непрозрачностью.

1. Откройте исходный PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
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

Используйте этот пример, когда вам нужно отрегулировать качество отображения штампа изображения.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp/) и установить значение качества.
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

## Используйте изображение в качестве фона плавающего блока

Используйте этот пример, когда изображение должно служить фоном стилизованного контейнера макета.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и получите доступ к целевой странице.
1. Создайте [FloatingBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/floatingbox/) с настройками текста и границ.
1. Установите фоновое изображение, добавьте коробку на страницу и сохраните документ.

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


