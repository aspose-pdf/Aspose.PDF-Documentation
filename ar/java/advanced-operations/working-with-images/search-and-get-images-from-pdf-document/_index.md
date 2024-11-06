---
title: البحث والحصول على الصور من مستند PDF
linktitle: البحث والحصول على الصور
type: docs
weight: 60
url: ar/java/search-and-get-images-from-pdf-document/
description: يشرح هذا القسم كيفية البحث والحصول على الصور من مستند PDF باستخدام مكتبة Aspose.PDF for Java.
lastmod: "2021-06-05"
---

يسمح لك [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber) بالبحث بين الصور على جميع الصفحات في مستند PDF.

للبحث في مستند كامل عن الصور:

1. قم باستدعاء طريقة Accept الخاصة بمجموعة [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection). تأخذ طريقة Accept كائن [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber) كمعامل. هذا يعيد مجموعة من كائنات [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement).
2. قم بالتكرار عبر كائنات ImagePlacements واحصل على خصائصها (الصورة، الأبعاد، الدقة وهكذا).

يعرض المقتطف البرمجي التالي كيفية البحث في مستند عن جميع صوره.

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import com.aspose.pdf.*;

public class ExampleSearchAndGet {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void SearchImages() throws IOException {
        // فتح المستند
        Document doc = new Document(_dataDir + "SearchAndGetImages.pdf");

        // إنشاء كائن ImagePlacementAbsorber لأداء البحث عن موضع الصورة
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

        // قبول جهاز الامتصاص لجميع الصفحات
        doc.getPages().accept(abs);

        // تكرار جميع مواضع الصور، الحصول على الصورة وخصائص موضع الصورة
        for (ImagePlacement imagePlacement : abs.getImagePlacements()) {
            // الحصول على الصورة باستخدام كائن ImagePlacement
            // XImage image = imagePlacement.getImage();

            // عرض خصائص موضع الصورة لجميع المواضع
            System.out.println("عرض الصورة:" + imagePlacement.getRectangle().getWidth());
            System.out.println("ارتفاع الصورة:" + imagePlacement.getRectangle().getHeight());
            System.out.println("LLX للصورة:" + imagePlacement.getRectangle().getLLX());
            System.out.println("LLY للصورة:" + imagePlacement.getRectangle().getLLY());
            System.out.println("دقة الصورة الأفقية:" + imagePlacement.getResolution().getX());
            System.out.println("دقة الصورة العمودية:" + imagePlacement.getResolution().getY());
        }

    }
}
```

To get an image from an individual page, use the following code:

```java
doc.getPages().get_Item(1).accept(abs)
```