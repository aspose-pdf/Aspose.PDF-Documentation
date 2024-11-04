---
title: استخراج الصور من ملف PDF
linktitle: استخراج الصور
type: docs
weight: 30
url: /java/extract-images-from-pdf-file/
description: يوضح هذا القسم كيفية استخراج الصور من ملف PDF باستخدام مكتبة Java.
lastmod: "2021-06-05"
---

كل صفحة تحتوي على مجموعة [الموارد](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources)، وهذه بدورها تحتوي على مجموعة الصور، حيث يتم الاحتفاظ بجميع الصور في الصفحة. يحصل كائن [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) على صورة معينة في مجموعة الصور.

لاستخراج صورة من صفحة:

احصل على الصورة من مجموعة الصور باستخدام فهرس الصورة.  
استخدم طريقة الكائن [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) `save(..)` لحفظ الصورة المستخرجة.

يوضح مقتطف الشيفرة التالي كيفية استخراج الصور من ملف PDF.

```java
package com.aspose.pdf.examples;

import java.io.FileOutputStream;
import java.io.IOException;

import com.aspose.pdf.*;
import com.aspose.pdf.internal.html.rendering.image.ImageFormat;

public class ExampleExtractImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExtractImages() throws IOException {

        // فتح الوثيقة
        Document pdfDocument = new Document(_dataDir + "ExtractImages.pdf");

        // استخراج صورة معينة
        XImage xImage = pdfDocument.getPages().get_Item(1).getResources().getImages().get_Item(1);

        FileOutputStream outputImage = new FileOutputStream(_dataDir + "output.jpg");

        // حفظ الصورة الناتجة
        xImage.save(outputImage, ImageFormat.Jpeg);
        outputImage.close();

        // حفظ ملف PDF المحدث
        pdfDocument.save(_dataDir + "ExtractImages_out.pdf");
    }
}
```