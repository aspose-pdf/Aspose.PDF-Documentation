---
title: Добавление фона в PDF на Java
linktitle: Добавление фона
type: docs
weight: 20
url: /ru/java/add-backgrounds/
description: Добавить изображения и одноцветные фоны на страницы PDF в Java и отрегулировать непрозрачность изображения.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление фона в PDF на Java
Abstract: Добавить изображения и одноцветные фоны на страницы PDF в Java и отрегулировать непрозрачность изображения.
---
Фоновые артефакты позволяют размещать визуальные элементы, не являющиеся содержимым, за основным содержимым страницы, не изменяя логический текст документа.

## Добавление фонового изображения в PDF

Используйте этот пример, когда страница должна отображать изображение в качестве фонового артефакта.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Откройте поток чтения изображения.
1. Создайте [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/).
1. Задайте поток изображения.
1. Добавьте артефакт на целевую страницу.
1. Сохраните результирующий PDF.

```java
public static void addBackgroundImageToPdf(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundImage(imageStream);
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## Настройка непрозрачности фонового изображения

Этот пример размещает полупрозрачное фоновое изображение за содержимым страницы.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Откройте поток чтения изображения.
1. Создайте [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/).
1. Назначьте изображение.
1. Установите непрозрачность.
1. Добавьте артефакт на страницу.
1. Сохраните документ.

```java
public static void addBackgroundImageWithOpacityToPdf(Path inputFile, Path imageFile, Path outputFile)
        throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundImage(imageStream);
        artifact.setOpacity(0.5);
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## Добавление сплошного фона в PDF

Используйте этот пример, когда страница должна использовать сплошной цвет фона вместо изображения.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/).
1. Назначьте цвет фона.
1. Добавьте артефакт на страницу.
1. Сохраните выходной файл.

```java
public static void addBackgroundColorToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundColor(Color.getDarkKhaki().toRgb());
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## См. также

- [Удаление фона](/pdf/ru/java/remove-backgrounds/)
- [Работа с PDF-артефактами](/pdf/ru/java/artifacts/)
