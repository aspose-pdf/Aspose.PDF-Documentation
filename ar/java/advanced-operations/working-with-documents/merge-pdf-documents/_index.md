---
title: دمج ملفات PDF برمجياً
linktitle: دمج ملفات PDF
type: docs
weight: 50
url: ar/java/merge-pdf-documents/
description: توضح هذه الصفحة كيفية دمج مستندات PDF في ملف PDF واحد باستخدام Java.
lastmod: "2021-06-05"
---

الآن، دمج ملفات PDF هو أحد المهام المطلوبة بشدة.
توضح هذه المقالة كيفية دمج ملفات PDF متعددة في مستند PDF واحد باستخدام Aspose.PDF for Java. المثال مكتوب بلغة Java، ولكن يمكن استخدام API في لغات برمجة أخرى. يتم دمج ملفات PDF بحيث يتم إلحاق الأول في نهاية المستند الآخر.

## دمج ملفات PDF باستخدام Java

{{% alert color="primary" %}}

يمكنك دمج ملفات PDF باستخدام Aspose.PDF والحصول على النتائج عبر الإنترنت على هذا الرابط: [products.aspose.app/pdf/merger](https://products.aspose.app/pdf/merger)

{{% /alert %}}

لدمج ملفين PDF:

1. قم بإنشاء كائنين [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)، يحتوي كل منهما على واحد من ملفات PDF المدخلة.

1. ثم قم باستدعاء طريقة الإضافة الخاصة بمجموعة [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) لكائن الوثيقة الذي تريد إضافة ملف PDF الآخر إليه.
1. مرر مجموعة PageCollection الخاصة بكائن الوثيقة الثاني إلى طريقة الإضافة الخاصة بمجموعة PageCollection الأولى.
1. أخيرًا، احفظ ملف PDF الناتج باستخدام طريقة الحفظ.

يظهر جزء الكود التالي كيفية دمج ملفات PDF باستخدام Java.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleMerge {
    // المسار إلى دليل الوثائق.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Merge() {
        
        // افتح الوثيقة الأولى
        Document pdfDocument1 = new Document(_dataDir + "Concat1.pdf");
        // افتح الوثيقة الثانية
        Document pdfDocument2 = new Document(_dataDir + "Concat2.pdf");

        // أضف صفحات الوثيقة الثانية إلى الأولى
        pdfDocument1.getPages().add(pdfDocument2.getPages());

        // احفظ ملف الإخراج المدمج
        pdfDocument1.save(_dataDir+"ConcatenatePdfFiles_out.pdf");

    }

}
```