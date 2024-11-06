---
title: تدوير صفحات PDF برمجيًا
linktitle: تدوير صفحات PDF
type: docs
weight: 60
url: ar/java/rotate-pages/
description: تغيير اتجاه الصفحة وتناسب محتوى الصفحة مع الاتجاه الجديد للصفحة باستخدام Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## تغيير اتجاه الصفحة

تصف هذه المقالة كيفية تحديث أو تغيير اتجاه الصفحات في ملف PDF موجود.

تحتوي Aspose.PDF for Java على ميزة لتغيير اتجاه الصفحة من العرضي إلى الطولي والعكس صحيح. لتغيير اتجاه الصفحة، قم بتعيين [MediaBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#setMediaBox-com.aspose.pdf.Rectangle-) باستخدام الجزء البرمجي التالي.

يمكنك أيضًا تغيير اتجاه الصفحة عن طريق تعيين زاوية الدوران باستخدام طريقة Rotate().

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleRotatePDFPages  {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RotatePages() {
        // فتح المستند
        Document pdfDocument = new Document(_dataDir + "sample2.pdf");

        for (Page page : pdfDocument.getPages())
        {            
            // Rectangle r = page.getMediaBox();
            // double newHeight = r.getWidth();
            // double newWidth = r.getHeight();
            // double newLLX = r.getLLX();
            // // يجب علينا تحريك الصفحة لأعلى لتعويض تغيير حجم الصفحة
            // // (الحافة السفلية للصفحة هي 0,0 وعادة ما يتم وضع المعلومات من
            // // أعلى الصفحة. لهذا السبب نقوم بتحريك الحافة السفلية لأعلى بفارق بين
            // // الارتفاع القديم والجديد.
            // double newLLY = r.getLLY() + (r.getHeight() - newHeight);
            // page.setMediaBox (new Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));
            // // أحيانًا نحتاج أيضًا إلى تعيين CropBox (إذا كان محددًا في الملف الأصلي)
            // page.setCropBox(new Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));

            // تعيين زاوية دوران الصفحة
            page.setRotate(Rotation.on90);
        }

        _dataDir = _dataDir + "ChangeOrientation_out.pdf";
        // حفظ الملف الناتج
        pdfDocument.save(_dataDir);
    }    
}
```