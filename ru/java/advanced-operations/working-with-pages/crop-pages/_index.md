---
title: Обрезка страниц PDF в Java
linktitle: Обрезка страниц PDF
type: docs
weight: 70
url: /ru/java/crop-pages/
description: Узнайте, как обрезать страницы PDF и корректировать crop, trim, bleed и media‑коробки в Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Обрезайте страницы и регулируйте коробки страниц в PDF‑файлах с помощью Java
Abstract: В этой статье объясняется, как обрезать страницы PDF с использованием Aspose.PDF for Java. Описывается назначение нового прямоугольника обрезки для crop, trim, art и bleed‑коробок, а также автоматическая обрезка страницы на основе обнаруженного графического содержимого.
---
Aspose.PDF for Java позволяет обрезать страницы либо с помощью явных координат коробки, либо на основе обнаруженного содержимого.

## Обрежьте страницу, установив границы страницы

Используйте этот пример, когда нужно применить одну и ту же область обрезки к основным границам страницы.

1. Откройте исходный PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте новую обрезку [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. Примените прямоугольник к областям страниц, связанным с обрезкой, и сохраните документ.

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

## Обрежьте страницу по обнаруженному содержимому

Используйте этот пример, когда область обрезки должна быть получена из первого обнаруженного изображения на странице.

1. Откройте исходный PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Используйте [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) для определения размещения изображений.
1. Установите crop box в прямоугольник изображения, если он найден, затем сохраните документ.

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


