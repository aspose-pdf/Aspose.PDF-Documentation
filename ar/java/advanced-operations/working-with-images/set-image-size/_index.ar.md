---
title: ضبط حجم الصورة
linktitle: ضبط حجم الصورة
type: docs
weight: 80
url: /java/set-image-size/
description: يصف هذا القسم كيفية ضبط حجم الصورة في ملف PDF باستخدام مكتبة Java.
lastmod: "2021-06-05"
---

من الممكن ضبط حجم الصورة التي يتم إضافتها إلى ملف PDF. لضبط الحجم، يمكنك استخدام الطريقتين [setFixWidth](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image#setFixWidth-double-) و [setFixHeight](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image#setFixHeight-double-) من فئة com.aspose.pdf.Image.

يظهر مقتطف الشيفرة التالي كيفية ضبط حجم الصورة:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleSetImageSize {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Replace() {
        // إنشاء كائن مستند
        Document doc = new Document();
        // إضافة صفحة إلى مجموعة صفحات ملف PDF
        Page page = doc.getPages().add();
        // إنشاء مثيل للصورة
        Image img = new Image();
        // ضبط عرض وارتفاع الصورة بالنقاط
        img.setFixWidth (100);
        img.setFixHeight (100);
        // ضبط نوع الصورة كـ SVG
        img.setFileType (ImageFileType.Svg);
        // المسار لملف المصدر
        img.setFile (_dataDir + "aspose-logo.jpg");
        page.getParagraphs().add(img);
        // ضبط خصائص الصفحة
        page.getPageInfo().setWidth(800);
        page.getPageInfo().setHeight(800);        
        // حفظ ملف PDF الناتج
        doc.save(_dataDir + "SetImageSize_out.pdf");
    }
}
```