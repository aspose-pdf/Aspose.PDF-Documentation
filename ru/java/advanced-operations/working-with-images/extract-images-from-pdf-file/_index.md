---
title: Извлечение изображений из PDF‑файла с использованием Java
linktitle: Извлечение изображений
type: docs
weight: 30
url: /ru/java/extract-images-from-pdf-file/
description: Узнайте, как извлекать встроенные изображения из PDF‑файлов на Java.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Извлечение изображений из PDF‑файлов с помощью Java
Abstract: В этой статье показано, как извлекать изображения из PDF‑документов с использованием Aspose.PDF for Java. В ней рассматривается сохранение конкретного ресурса изображения со страницы и экспорт изображений, находящихся внутри выбранного прямоугольного региона.
---
Aspose.PDF for Java поддерживает прямое извлечение ресурсов изображений и фильтрацию на основе размещения.

## Извлеките встроенное изображение по индексу

Используйте этот пример, когда необходимо сохранить конкретный ресурс изображения со страницы PDF.

1. Откройте исходный PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Получите доступ к целевому [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) из ресурсов страницы.
1. Сохраните поток изображения в выходной файл.

```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```

## Извлеките изображения из определённого региона страницы

Используйте этот пример, когда нужно экспортировать только изображения, размещённые внутри выбранного прямоугольника.

1. Определите цель [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) и откройте исходный PDF.
1. Используйте [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) для проверки размещения изображений на странице.
1. Сохраняйте только изображения, размещение которых попадает в выбранный регион.

```java
public static void extractImageFromSpecificRegion(Path inputFile, Path outputFile) throws Exception {
    Rectangle rectangle = new Rectangle(0, 0, 590, 590, true);

    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);
        int index = 1;
        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            Point point1 = new Point(imagePlacement.getRectangle().getLLX(), imagePlacement.getRectangle().getLLY());
            Point point2 = new Point(imagePlacement.getRectangle().getURX(), imagePlacement.getRectangle().getURX());
            if (rectangle.contains(point1, true) && rectangle.contains(point2, true)) {
                Path indexedOutputFile = Path.of(outputFile.toString().replace("index", String.valueOf(index)));
                try (OutputStream outputImage = Files.newOutputStream(indexedOutputFile)) {
                    imagePlacement.getImage().save(outputImage);
                }
                index++;
            }
        }
    }
}
```


