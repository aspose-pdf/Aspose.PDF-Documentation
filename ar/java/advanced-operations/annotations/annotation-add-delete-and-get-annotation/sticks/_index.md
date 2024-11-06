---
title: التعليقات اللاصقة في PDF
linktitle: التعليق اللاصق
type: docs
weight: 50
url: ar/java/sticky-annotations/
description: هذا الموضوع يتعلق بالتعليقات اللاصقة، كمثال نعرض تعليق العلامة المائية في النص. يُستخدم لتمثيل الرسومات على الصفحة. تحقق من مقتطف الشيفرة لحل هذه المهمة.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إضافة تعليق العلامة المائية

يجب استخدام تعليق العلامة المائية لتمثيل الرسومات التي يجب طباعتها بحجم وموقع ثابت على الصفحة، بغض النظر عن أبعاد الصفحة المطبوعة.

يمكنك إضافة نص العلامة المائية باستخدام [WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/WatermarkAnnotation) في موضع محدد من صفحة PDF. يمكن أيضًا التحكم في شفافية العلامة المائية باستخدام خاصية الشفافية.

يرجى التحقق من مقتطف الشيفرة التالي لإضافة WatermarkAnnotation.

```java
 package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleWatermarkAnnotation {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddWaterMarkAnnotation()
    {
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        //إنشاء تعليق
        WatermarkAnnotation wa = new WatermarkAnnotation(page, new Rectangle(100, 500, 400, 600));

        //إضافة التعليق إلى مجموعة التعليقات في الصفحة
        page.getAnnotations().add(wa);

        //إنشاء TextState لإعدادات الخط
        TextState ts = new TextState();

        ts.setForegroundColor(Color.getBlue());
        ts.setFont(FontRepository.findFont("Times New Roman"));
        ts.setFontSize(32);

        //تعيين مستوى شفافية نص التعليق
        wa.setOpacity(0.5);

        //إضافة النص إلى التعليق
        wa.setTextAndState(new String[] { "Aspose.PDF", "Watermark", "Demo" }, ts);

        //حفظ المستند
        document.save(_dataDir + "sample_watermark.pdf");
    }
}
```


## الحصول على تعليق العلامة المائية

```java
    public static void GetWatermarkAnnotation() {
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "sample_watermark.pdf");

        // تصفية التعليقات باستخدام AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new WatermarkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> WatermarkAnnotations = annotationSelector.getSelected();

        // طباعة النتائج
        for (Annotation fa : WatermarkAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```

## حذف تعليق العلامة المائية

```java
    public static void DeleteWatermarkAnnotation() {
         // تحميل ملف PDF
         Document document = new Document(_dataDir + "sample_watermark.pdf");

         // تصفية التعليقات باستخدام AnnotationSelector
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new WatermarkAnnotation(page, Rectangle.getTrivial()));
         page.accept(annotationSelector);
         List<Annotation> WatermarkAnnotations = annotationSelector.getSelected();

         // حذف التعليقات
         for (Annotation fa : WatermarkAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_watermark_del.pdf");
    }
```