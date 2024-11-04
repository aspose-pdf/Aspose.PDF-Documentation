---
title: Поиск и Извлечение Изображений из PDF Документа
linktitle: Поиск и Извлечение Изображений
type: docs
weight: 60
url: /java/search-and-get-images-from-pdf-document/
description: Этот раздел объясняет, как искать и извлекать изображения из PDF документа с помощью библиотеки Aspose.PDF для Java.
lastmod: "2021-06-05"
---

[ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber) позволяет искать изображения на всех страницах в PDF документе.

Чтобы искать изображения во всем документе:

1. Вызовите метод Accept коллекции [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection). Метод Accept принимает объект [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber) в качестве параметра. Это возвращает коллекцию объектов [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement).
1. Переберите объекты ImagePlacements и получите их свойства (Изображение, размеры, разрешение и так далее).

Следующий фрагмент кода показывает, как искать все изображения в документе.

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import com.aspose.pdf.*;

public class ExampleSearchAndGet {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void SearchImages() throws IOException {
        // Открыть документ
        Document doc = new Document(_dataDir + "SearchAndGetImages.pdf");

        // Создать объект ImagePlacementAbsorber для выполнения поиска размещения изображений
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

        // Принять абсорбер для всех страниц
        doc.getPages().accept(abs);

        // Перебрать все ImagePlacements, получить изображение и свойства ImagePlacement
        for (ImagePlacement imagePlacement : abs.getImagePlacements()) {
            // Получить изображение с использованием объекта ImagePlacement
            // XImage image = imagePlacement.getImage();

            // Отобразить свойства размещения изображений для всех размещений
            System.out.println("ширина изображения:" + imagePlacement.getRectangle().getWidth());
            System.out.println("высота изображения:" + imagePlacement.getRectangle().getHeight());
            System.out.println("LLX изображения:" + imagePlacement.getRectangle().getLLX());
            System.out.println("LLY изображения:" + imagePlacement.getRectangle().getLLY());
            System.out.println("горизонтальное разрешение изображения:" + imagePlacement.getResolution().getX());
            System.out.println("вертикальное разрешение изображения:" + imagePlacement.getResolution().getY());
        }

    }
}
```

To get an image from an individual page, use the following code:

```java
Чтобы получить изображение с отдельной страницы, используйте следующий код:

doc.getPages().get_Item(1).accept(abs)
```