---
title: تغيير حجم صفحة PDF برمجياً
linktitle: تغيير حجم الصفحة
type: docs
weight: 50
url: ar/java/change-page-size/
description: تغيير حجم الصفحة من ملف PDF الخاص بك باستخدام مكتبة Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## تغيير حجم صفحة PDF

تتيح لك Aspose.PDF for Java تغيير حجم صفحة PDF بأكواد بسيطة في تطبيقات Java الخاصة بك. يشرح هذا الموضوع كيفية تحديث/تغيير أبعاد الصفحة (الحجم) لملف PDF موجود.

تحتوي فئة [Page](https://reference.aspose.com/pdf//java/com.aspose.pdf/page) على طريقة SetPageSize(...) التي تتيح لك تعيين حجم الصفحة. يقوم مقتطف الكود أدناه بتحديث أبعاد الصفحة في بضع خطوات سهلة:

1. تحميل ملف PDF المصدر.
2. الحصول على الصفحات في كائن [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection).
3. الحصول على صفحة معينة.
4. استدعاء طريقة SetPageSize(..) لتحديث أبعادها.

1. استدعاء طريقة Save(..) لفئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) لتوليد ملف PDF بأبعاد الصفحة المحدثة.

{{% alert color="primary" %}}

يرجى ملاحظة أن خصائص الطول والعرض تستخدم النقاط كوحدة أساسية، حيث 1 بوصة = 72 نقطة و1 سم = 1/2.54 بوصة = 0.3937 بوصة = 28.3 نقطة.

{{% /alert %}}

يوضح مقتطف الشيفرة التالي كيفية تغيير أبعاد صفحة PDF إلى حجم A4.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleChangePDFPageSize {
    // المسار إلى دليل المستندات.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ChangePDFPageSize() {
        
        // فتح المستند الأول
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
                
        // الحصول على مجموعة الصفحات
        PageCollection pageCollection = pdfDocument.getPages();

        // الحصول على صفحة معينة
        Page pdfPage = pageCollection.get_Item(1);

        // تعيين حجم الصفحة إلى A4 (11.7 × 8.3 بوصة) وفي Aspose.Pdf، 1 بوصة = 72 نقطة
        // لذا أبعاد A4 بالنقاط ستكون (842.4, 597.6)
        pdfPage.setPageSize(597.6, 842.4);

        _dataDir = _dataDir + "UpdateDimensions_out.pdf";
        
        // حفظ المستند المحدث
        pdfDocument.save(_dataDir);
    }
```


## الحصول على حجم صفحة PDF

يمكنك قراءة حجم صفحة PDF لملف PDF موجود باستخدام Aspose.PDF لـ Java. يوضح نموذج الشيفرة التالي كيفية قراءة أبعاد صفحة PDF باستخدام Java.

```java
    public static void GetPDFPageSize() {
        
        // افتح المستند الأول
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
                
        // إضافة صفحة فارغة إلى مستند pdf
        Page page = pdfDocument.getPages().size() > 0 ? pdfDocument.getPages().get_Item(1) : pdfDocument.getPages().add();
        
        // الحصول على معلومات ارتفاع وعرض الصفحة
        System.out.println(page.getPageRect(true).getWidth() + ":" + page.getPageRect(true).getHeight());
        
        // تدوير الصفحة بزاوية 90 درجة
        page.setRotate (Rotation.on90);

        // الحصول على معلومات ارتفاع وعرض الصفحة
        System.out.println(page.getPageRect(true).getWidth() + ":" + page.getPageRect(true).getHeight());
        
        // احفظ المستند المحدث
        _dataDir = _dataDir + "UpdateDimensions_out.pdf";
        pdfDocument.save(_dataDir);
    }

}
```