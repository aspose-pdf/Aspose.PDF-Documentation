---
title: إزالة الجداول من ملف PDF موجود
linktitle: إزالة الجداول
type: docs
weight: 40
url: /ar/java/remove-tables-from-existing-pdf/
description: تتيح Aspose.PDF for Java لك إزالة الجدول والعديد من الجداول من مستند PDF الخاص بك.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

تقدم Aspose.PDF for Java إمكانيات لإدراج/إنشاء جدول داخل مستند PDF أثناء إنشائه من البداية أو يمكنك أيضًا إضافة كائن الجدول في أي مستند PDF موجود. ومع ذلك، قد يكون لديك متطلب [التعامل مع الجداول في PDF موجود](https://docs.aspose.com/pdf/java/manipulate-tables-in-existing-pdf/) حيث يمكنك تحديث المحتويات في خلايا الجدول الموجودة. ومع ذلك، قد تواجه متطلبًا لإزالة كائنات الجداول من مستند PDF موجود.

{{% /alert %}}

لإزالة الجداول، نحتاج إلى استخدام فئة [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber) للتمكن من الوصول إلى الجداول في PDF الموجود ثم استدعاء طريقة [Remove](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#remove-com.aspose.pdf.AbsorbedTable-) لإزالتها.

## إزالة الجدول من مستند PDF

لقد أضفنا وظيفة جديدة وهي Remove() إلى الفئة الحالية [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber) من أجل إزالة الجدول من مستند PDF. بمجرد أن يجد المنصة الجداول على الصفحة بنجاح، يصبح قادراً على إزالتها. يرجى التحقق من المقتطف البرمجي التالي الذي يوضح كيفية إزالة جدول من مستند PDF:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleRemoveTable {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RemoveTable() {
        // تحميل مستند PDF الموجود
        Document pdfDocument = new Document(_dataDir + "Table_input.pdf");

        // إنشاء كائن TableAbsorber للعثور على الجداول
        TableAbsorber absorber = new TableAbsorber();

        // زيارة الصفحة الأولى باستخدام المنصة
        absorber.visit(pdfDocument.getPages().get_Item(1));

        // الحصول على الجدول الأول في الصفحة
        AbsorbedTable table = absorber.getTableList().get(0);

        // إزالة الجدول
        absorber.remove(table);

        // حفظ PDF
        pdfDocument.save(_dataDir + "Table_out.pdf");
    }  
```


## إزالة جداول متعددة من ملف PDF

أحيانًا قد يحتوي ملف PDF على أكثر من جدول وقد تحتاج إلى إزالة جداول متعددة منه. لإزالة جداول متعددة من ملف PDF، يُرجى استخدام جزء الشيفرة التالي:

```java
    public static void RemoveMultipleTable() {
        // تحميل مستند PDF موجود
        Document pdfDocument = new Document(_dataDir + "Table_input2.pdf");

        // إنشاء كائن TableAbsorber للعثور على الجداول
        TableAbsorber absorber = new TableAbsorber();

        // زيارة الصفحة الثانية مع الماص
        absorber.visit(pdfDocument.getPages().get_Item(2));

        // تكرار عبر نسخة من المجموعة وإزالة الجداول
        for (AbsorbedTable table : absorber.getTableList())
            absorber.remove(table);

        // حفظ المستند
        pdfDocument.save(_dataDir + "Table2_out.pdf");
    }
}
```