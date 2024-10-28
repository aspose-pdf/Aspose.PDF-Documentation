---
title: العمل مع وضع الصور
linktitle: وضع الصور
type: docs
weight: 50
url: /java/working-with-image-placement/
description: يصف هذا القسم ميزات العمل مع وضع الصور في ملف PDF باستخدام مكتبة Java.
lastmod: "2021-06-05"
---

قدمت Aspose.PDF for Java فئات تسمى [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement)، [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber) و [ImagePlacementCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementCollection) والتي توفر قدرة مشابهة للفئات المذكورة أعلاه للحصول على دقة الصورة وموقعها في مستند PDF.

- يقوم ImagePlacementAbsorber بالبحث عن استخدام الصورة كمجموعة من كائنات ImagePlacement.
- يوفر ImagePlacement الأعضاء Resolution وRectangle التي تعيد القيم الفعلية لوضع الصورة.

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
        // تحميل ملف PDF المصدر
        Document doc = new Document(_dataDir + "ImageInformation.pdf");
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

        // تحميل محتويات الصفحة الأولى
        doc.getPages().get_Item(1).accept(abs);
        for (ImagePlacement imagePlacement : abs.getImagePlacements()) {
            // الحصول على خصائص الصورة
            System.out.println("عرض الصورة:" + imagePlacement.getRectangle().getWidth());
            System.out.println("ارتفاع الصورة:" + imagePlacement.getRectangle().getHeight());
            System.out.println("LLX للصورة:" + imagePlacement.getRectangle().getLLX());
            System.out.println("LLY للصورة:" + imagePlacement.getRectangle().getLLY());
            System.out.println("الدقة الأفقية للصورة:" + imagePlacement.getResolution().getX());
            System.out.println("الدقة الرأسية للصورة:" + imagePlacement.getResolution().getY());

            // استرجاع الصورة بالأبعاد الظاهرة
            // Bitmap scaledImage;
            // استرجاع الصورة من الموارد
            ByteArrayOutputStream imageStream = new ByteArrayOutputStream();
            imagePlacement.getImage().save(imageStream, ImageType.getPng());

            // Bitmap resourceImage = (Bitmap)Bitmap.FromStream(imageStream);
            BufferedImage resourceImage = ImageIO.read(new ByteArrayInputStream(imageStream.toByteArray()));

            // إنشاء صورة نقطية بأبعاد فعلية
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

        // إنشاء صورة نقطية مع الشفافية
        BufferedImage bimage = new BufferedImage(img.getWidth(null), img.getHeight(null), BufferedImage.TYPE_INT_ARGB);

        // رسم الصورة على الصورة النقطية
        Graphics2D bGr = bimage.createGraphics();
        bGr.drawImage(img, 0, 0, null);
        bGr.dispose();

        // إرجاع الصورة النقطية
        return bimage;
    }
}
```