---
title: Извлечение изображений из PDF-файла с помощью Java
linktitle: Извлечь изображения
type: docs
weight: 30
url: /java/extract-images-from-pdf-file/
description: Узнайте, как извлечь внедренные изображения из файлов PDF в Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Извлечение изображений из файлов PDF с помощью Java
Abstract: В этой статье показано, как извлекать изображения из PDF-документов с помощью Aspose.PDF для Java. Он охватывает сохранение определенного ресурса изображения со страницы и экспорт изображений, попадающих в выбранную прямоугольную область.
---
Aspose.PDF для Java поддерживает прямое извлечение ресурсов изображения и фильтрацию на основе размещения.

## Извлеките встроенное изображение по индексу

Используйте этот пример, когда вам нужно сохранить определенный ресурс изображения со страницы PDF.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Получите доступ к целевому [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) из ресурсов страницы.
1. Сохраните поток изображений в выходной файл.

```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```

## Извлечение изображений из определенной области страницы

Используйте этот пример, когда необходимо экспортировать только изображения, помещенные внутри выбранного прямоугольника.

1. Определите целевой [Прямоугольник](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) и откройте исходный PDF-файл.
1. Используйте [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/), чтобы проверить размещение изображений на странице.
1. Сохраняйте только те изображения, размещение которых соответствует выбранной области.

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
