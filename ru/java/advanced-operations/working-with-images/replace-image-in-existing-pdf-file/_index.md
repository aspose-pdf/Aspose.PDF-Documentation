---
title: Заменить изображение в существующем PDF‑файле с помощью Java
linktitle: Заменить изображение
type: docs
weight: 70
url: /ru/java/replace-image-in-existing-pdf-file/
description: Узнайте, как заменить встраиваемые изображения в существующих PDF‑файлах на Java.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Заменить изображения в существующих PDF‑файлах с помощью Java
Abstract: В этой статье показано, как заменять изображения в PDF‑документах с помощью Aspose.PDF for Java. Рассматривается замена изображения по индексу его ресурса и замена первого найденного подходящего размещения изображения с помощью ImagePlacementAbsorber.
---
Используйте либо коллекцию изображений страницы, либо поиск на основе размещения, в зависимости от того, насколько точно вам нужно найти изображение.

## Замените изображение по индексу ресурса

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Получите доступ к ресурсам изображений в целевом файле [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Замените целевой ресурс изображения новым файлом изображения.
1. Сохраните обновлённый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void replaceImage(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        document.getPages().get_Item(1).getResources().getImages().replace(1, imageStream);
        document.save(outputFile.toString());
    }
}
```

## Замените изображение с помощью `ImagePlacementAbsorber`

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) и посетить цель [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Получите цель [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacement/) и заменить его новым потоком изображения.
1. Сохраните обновлённый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void replaceImageWithAbsorber(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);

        if (absorber.getImagePlacements().size() > 0) {
            ImagePlacement imagePlacement = absorber.getImagePlacements().get_Item(1);
            try (InputStream imageStream = Files.newInputStream(imageFile)) {
                imagePlacement.replace(imageStream);
            }
        }

        document.save(outputFile.toString());
    }
}
```


