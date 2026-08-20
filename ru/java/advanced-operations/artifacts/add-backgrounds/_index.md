---
title: Добавление фонов PDF в Java
linktitle: Добавление фонов
type: docs
weight: 20
url: /ru/java/add-backgrounds/
description: Узнайте, как добавить фоновое изображение или фоновый цвет на страницы PDF в Java, используя `BackgroundArtifact` с Aspose.PDF.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить фон в PDF с помощью Java
Abstract: В этой статье объясняется, как добавлять или удалять фоновые элементы страниц PDF в Java с помощью Aspose.PDF. Рассматриваются добавление фонового изображения, регулировка непрозрачности изображения, применение фонового цвета и удаление фоновых артефактов со страницы.
---
Фоновые артефакты позволяют размещать визуальные элементы без содержания позади основного контента страницы без изменения логического текста документа.

## Добавьте фоновое изображение в PDF

Используйте этот пример, когда страница должна отображать изображение в качестве фонового артефакта.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и поток ввода изображения.
1. Создайте [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) и назначьте поток изображения.
1. Добавьте артефакт на целевую страницу и сохраните результирующий PDF.

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

Этот пример размещает полупрозрачное фоновое изображение за содержимым страницы.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и поток изображения.
1. Создайте [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/), назначьте изображение и задайте непрозрачность.
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

## Добавьте цвет фона в PDF

Используйте этот пример, когда страница должна использовать сплошной цвет фона вместо изображения.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) и задайте цвет фона.
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

## Удалите артефакты фона

Используйте этот подход, когда существующие артефакты фона должны быть удалены со страницы.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Итерировать коллекцию артефактов страницы в обратном порядке.
1. Удалите артефакты, тип которых – пагинация, а подтип – фон, затем сохранить документ.

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


