---
title: Заменить изображение в существующем PDF-файле с помощью Java
linktitle: Заменить изображение
type: docs
weight: 70
url: /java/replace-image-in-existing-pdf-file/
description: Узнайте, как заменить встроенные изображения в существующих PDF-файлах на Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Замените изображения в существующих файлах PDF с помощью Java.
Abstract: В этой статье показано, как заменить изображения в документах PDF с помощью Aspose.PDF для Java. Он охватывает замену изображения по его индексу ресурса и замену первого найденного соответствующего размещения изображения с помощью ImagePlacementAbsorber.
---
Используйте либо коллекцию изображений на странице, либо поиск по местам размещения в зависимости от того, насколько точно вам нужно настроить таргетинг на изображение.

## Заменить изображение по индексу ресурса

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Получите доступ к ресурсам изображений на целевой [Странице](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Замените целевой ресурс изображения новым файлом изображения.
1. Сохраните обновленный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void replaceImage(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        document.getPages().get_Item(1).getResources().getImages().replace(1, imageStream);
        document.save(outputFile.toString());
    }
}
```

## Замените изображение, используя `ImagePlacementAbsorber`

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) и посетите целевую [страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Получите целевой [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacement/) и замените его новым потоком изображений.
1. Сохраните обновленный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
