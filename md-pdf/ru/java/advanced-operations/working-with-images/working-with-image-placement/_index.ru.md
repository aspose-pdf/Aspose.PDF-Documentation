---
title: Работа с размещением изображений
linktitle: Размещение изображений
type: docs
weight: 50
url: /java/working-with-image-placement/
description: Этот раздел описывает функции работы с размещением изображений в PDF файле с использованием Java библиотеки.
lastmod: "2021-06-05"
---

Aspose.PDF for Java представил классы [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement), [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber) и [ImagePlacementCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementCollection), которые предоставляют аналогичную возможность как вышеописанные классы для получения разрешения и положения изображения в PDF документе.

- ImagePlacementAbsorber выполняет поиск использования изображения как коллекция объектов ImagePlacement.
- ImagePlacement предоставляет члены Resolution и Rectangle, которые возвращают фактические значения размещения изображения.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;


import javax.imageio.ImageIO;

public class ExampleWorkingWithImagePlacement {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void WorkingWithImagePlacement() throws IOException {
        // Загрузить исходный PDF файл
        Document doc = new Document(_dataDir + "ImageInformation.pdf");
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

        // Загрузить содержимое первой страницы
        doc.getPages().get_Item(1).accept(abs);
        for (ImagePlacement imagePlacement : abs.getImagePlacements()) {
            // Получить свойства изображения
            System.out.println("ширина изображения:" + imagePlacement.getRectangle().getWidth());
            System.out.println("высота изображения:" + imagePlacement.getRectangle().getHeight());
            System.out.println("LLX изображения:" + imagePlacement.getRectangle().getLLX());
            System.out.println("LLY изображения:" + imagePlacement.getRectangle().getLLY());
            System.out.println("горизонтальное разрешение изображения:" + imagePlacement.getResolution().getX());
            System.out.println("вертикальное разрешение изображения:" + imagePlacement.getResolution().getY());

            // Извлечь изображение с видимыми размерами
            // Bitmap scaledImage;
            // Извлечь изображение из ресурсов
            ByteArrayOutputStream imageStream = new ByteArrayOutputStream();
            imagePlacement.getImage().save(imageStream, ImageType.getPng());

            // Bitmap resourceImage = (Bitmap)Bitmap.FromStream(imageStream);
            BufferedImage resourceImage = ImageIO.read(new ByteArrayInputStream(imageStream.toByteArray()));

            // Создать bitmap с фактическими размерами
            BufferedImage scaledImage = toBufferedImage( 
            resourceImage.getScaledInstance((int) imagePlacement.getRectangle().getWidth(),
                    (int) imagePlacement.getRectangle().getHeight(), java.awt.Image.SCALE_SMOOTH));

            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            ImageIO.write(scaledImage, "jpg", baos);
            ByteArrayInputStream fis = new ByteArrayInputStream(baos.toByteArray());

            imagePlacement.getImage().replace(fis);
        }
    }
    
    public static BufferedImage toBufferedImage(java.awt.Image img) {
        if (img instanceof BufferedImage) {
            return (BufferedImage) img;
        }

        // Создать буферное изображение с прозрачностью
        BufferedImage bimage = new BufferedImage(img.getWidth(null), img.getHeight(null), BufferedImage.TYPE_INT_ARGB);

        // Нарисовать изображение на буферном изображении
        Graphics2D bGr = bimage.createGraphics();
        bGr.drawImage(img, 0, 0, null);
        bGr.dispose();

        // Вернуть буферное изображение
        return bimage;
    }
}
```