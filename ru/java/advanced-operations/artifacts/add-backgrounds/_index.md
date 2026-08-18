---
title: Добавить фон PDF в Java
linktitle: Добавление фона
type: docs
weight: 20
url: /java/add-backgrounds/
description: Узнайте, как добавить фоновое изображение или цвет фона к страницам PDF на Java, используя `BackgroundArtifact` с Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить фон в PDF с помощью Java
Abstract: В этой статье объясняется, как добавить или удалить фон страницы PDF в Java с помощью Aspose.PDF. В нем рассматривается добавление фонового изображения, настройка непрозрачности изображения, применение цвета фона и удаление фоновых артефактов со страницы.
---
Фоновые артефакты позволяют размещать визуальные элементы, не являющиеся контентом, за содержимым главной страницы, не изменяя логический текст документа.

## Добавьте фоновое изображение в PDF-файл

Используйте этот пример, когда на странице должно отображаться изображение в качестве фонового артефакта.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и поток ввода изображения.
1. Создайте [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) и назначьте поток изображений.
1. Добавьте артефакт на целевую страницу и сохраните выходной PDF-файл.

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

## Добавьте фоновое изображение с непрозрачностью

В этом примере за содержимым страницы размещается полупрозрачное фоновое изображение.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и поток изображений.
1. Создайте [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/), назначьте изображение и установите непрозрачность.
1. Добавьте артефакт на страницу и сохраните документ.

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

## Добавьте цвет фона в PDF-файл

Используйте этот пример, когда на странице вместо изображения должен использоваться сплошной цвет фона.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) и назначьте цвет фона.
1. Добавьте артефакт на страницу и сохраните выходной файл.

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

## Удаление фоновых артефактов

Используйте этот подход, когда существующие фоновые артефакты необходимо удалить со страницы.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Перебирайте коллекцию артефактов страницы в обратном порядке.
1. Удалите артефакты, тип которых — нумерация страниц, а подтип — фон, а затем сохраните документ.

```java
public static void removeBackground(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Background) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```
