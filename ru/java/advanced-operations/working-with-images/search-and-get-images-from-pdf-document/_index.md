---
title: Получать и искать изображения в PDF
linktitle: Получать и искать изображения
type: docs
weight: 40
url: /ru/java/search-and-get-images-from-pdf-document/
description: Узнайте, как искать и просматривать изображения в PDF‑документах на Java.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Ищите и просматривайте изображения в PDF‑файлах с помощью Java
Abstract: В этой статье показывается, как искать и проверять изображения в PDF‑документах с помощью Aspose.PDF for Java. Описывается чтение геометрии размещения изображений, определение типа цвета, извлечение альтернативного текста и вычисление эффективного разрешения изображения по операторам страницы.
---
Aspose.PDF for Java может проверять информацию о размещении изображений, а также данные низкоуровневого рисования.

## Получите параметры размещения изображения

Используйте этот пример, когда необходимо проверить геометрию изображения и его эффективное разрешение на странице.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Используйте [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) для сбора размещений изображений.
1. Выведите размер, координаты и разрешение для каждого размещённого изображения.

```java
public static void extractImageParams(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);

        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            System.out.println("image width: " + imagePlacement.getRectangle().getWidth());
            System.out.println("image height: " + imagePlacement.getRectangle().getHeight());
            System.out.println("image LLX: " + imagePlacement.getRectangle().getLLX());
            System.out.println("image LLY: " + imagePlacement.getRectangle().getLLY());
            System.out.println("image horizontal resolution: " + imagePlacement.getResolution().getX());
            System.out.println("image vertical resolution: " + imagePlacement.getResolution().getY());
        }
    }
}
```

## Определить типы цветов изображения

Используйте этот пример, когда вам нужно подсчитать изображения в градациях серого и RGB на странице PDF.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Используйте [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) для перебора изображений страниц.
1. Прочитать [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/colortype/) каждого изображения и вывести итоговые значения.

```java
public static void extractImageTypesFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        int grayscaled = 0;
        int rgb = 0;

        document.getPages().get_Item(1).accept(absorber);

        System.out.println("--------------------------------");
        System.out.println("Total Images = " + absorber.getImagePlacements().size());

        int imageCounter = 1;
        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            ColorType colorType = imagePlacement.getImage().getColorType();
            if (colorType == ColorType.Grayscale) {
                grayscaled++;
                System.out.println("Image " + imageCounter + " is Grayscale...");
            } else if (colorType == ColorType.Rgb) {
                rgb++;
                System.out.println("Image " + imageCounter + " is RGB...");
            }
            imageCounter++;
        }

        System.out.println("--------------------------------");
        System.out.println("Grayscale Images = " + grayscaled);
        System.out.println("RGB Images = " + rgb);
    }
}
```

## Извлеките альтернативный текст изображения

Используйте этот пример, когда нужно проверять текст доступности, связанный с изображениями на странице.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Используйте [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) для сбора размещений изображений.
1. Прочитайте альтернативный текст для каждого изображения и выведите результат.

```java
public static void extractImageAltText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);

        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            System.out.println("Name in collection: " + imagePlacement.getImage().getNameInCollection());
            List<String> lines = imagePlacement.getImage().getAlternativeText(document.getPages().get_Item(1));
            if (!lines.isEmpty()) {
                System.out.println("Alt Text: " + lines.get(0));
            } else {
                System.out.println("Alt Text: ");
            }
        }
    }
}
```

## Вычислить информацию об изображении из операторов страниц

Используйте этот пример, когда необходимо определить эффективный размер изображения и его разрешение из низкоуровневых операторов содержимого страницы.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и собрать имена ресурсов изображений.
1. Отслеживать состояние графики при итерации по операторам страницы.
1. Разобрать каждую операцию отрисовки изображения и вычислить её эффективные размеры и разрешение.

```java
public static void extractImageInformationFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int defaultResolution = 72;
        List<Matrix> graphicsState = new ArrayList<>();
        List<String> imageNames = Arrays.asList(document.getPages().get_Item(1).getResources().getImages().getNames());

        graphicsState.add(new Matrix(1, 0, 0, 1, 0, 0));

        for (Operator operator : document.getPages().get_Item(1).getContents()) {
            if (operator instanceof GSave) {
                graphicsState.add(new Matrix(graphicsState.get(graphicsState.size() - 1)));
            } else if (operator instanceof GRestore) {
                graphicsState.remove(graphicsState.size() - 1);
            } else if (operator instanceof ConcatenateMatrix concatenateMatrix) {
                Matrix current = graphicsState.get(graphicsState.size() - 1);
                graphicsState.set(graphicsState.size() - 1, current.multiply(concatenateMatrix.getMatrix()));
            } else if (operator instanceof Do doOperator) {
                if (imageNames.contains(doOperator.getName())) {
                    Matrix lastCtm = graphicsState.get(graphicsState.size() - 1);
                    int index = imageNames.indexOf(doOperator.getName()) + 1;
                    XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(index);

                    double scaledWidth = Math.sqrt(Math.pow(lastCtm.getA(), 2) + Math.pow(lastCtm.getB(), 2));
                    double scaledHeight = Math.sqrt(Math.pow(lastCtm.getC(), 2) + Math.pow(lastCtm.getD(), 2));

                    double originalWidth = image.getWidth();
                    double originalHeight = image.getHeight();

                    double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                    double resVertical = originalHeight * defaultResolution / scaledHeight;

                    String info = String.format(
                            "%s image %s (%.2f:%.2f): res %.2f x %.2f",
                            inputFile,
                            doOperator.getName(),
                            scaledWidth,
                            scaledHeight,
                            resHorizontal,
                            resVertical);
                    System.out.println(info);
                }
            }
        }
    }
}
```

