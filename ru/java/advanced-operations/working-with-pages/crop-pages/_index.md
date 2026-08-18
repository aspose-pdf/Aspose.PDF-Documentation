---
title: Обрезать PDF-страницы в Java
linktitle: Обрезка PDF-страниц
type: docs
weight: 70
url: /java/crop-pages/
description: Узнайте, как обрезать страницы PDF и настраивать рамки обрезки, обрезки, выпуска за обрез и медиа-поля в Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Обрезайте страницы и настраивайте страничные поля в файлах PDF с помощью Java.
Abstract: В этой статье объясняется, как обрезать страницы PDF с помощью Aspose.PDF для Java. В нем рассматривается назначение нового прямоугольника обрезки полям обрезки, обрезки, оформления и выпуска за обрез, а также автоматическая обрезка страницы на основе обнаруженного содержимого изображения.
---
Aspose.PDF для Java позволяет обрезать страницы либо по явным координатам поля, либо на основе обнаруженного содержимого.

## Обрезать страницу, установив рамки страницы

Используйте этот пример, когда вам нужно применить одну и ту же область обрезки к полям главной страницы.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте новую обрезку [Прямоугольник](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. Примените прямоугольник к полям страницы, связанным с обрезкой, и сохраните документ.

```java
public static void cropPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle newBox = new Rectangle(200, 220, 2170, 1520, true);
        document.getPages().get_Item(1).setCropBox(newBox);
        document.getPages().get_Item(1).setTrimBox(newBox);
        document.getPages().get_Item(1).setArtBox(newBox);
        document.getPages().get_Item(1).setBleedBox(newBox);
        document.save(outputFile.toString());
    }
}
```

## Обрезать страницу по обнаруженному содержимому

Используйте этот пример, когда область обрезки должна быть получена из первого обнаруженного изображения на странице.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Используйте [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) для определения размещения изображений.
1. Установите рамку обрезки на прямоугольник изображения, если он найден, затем сохраните документ.

```java
public static void cropPageByContent(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);
        if (absorber.getImagePlacements().size() > 0) {
            document.getPages().get_Item(1).setCropBox(absorber.getImagePlacements().get_Item(1).getRectangle());
        } else {
            System.out.println("No images found on the first page");
        }
        document.save(outputFile.toString());
    }
}
```
