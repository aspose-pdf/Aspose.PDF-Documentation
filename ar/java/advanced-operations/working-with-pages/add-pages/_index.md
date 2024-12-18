---
title: إضافة صفحات في PDF
linktitle: إضافة صفحات
type: docs
weight: 10
url: /ar/java/add-pages/
description: تعلمك هذه المقالة كيفية إدراج (إضافة) صفحة في المكان المطلوب في ملف PDF. تعلم كيفية نقل وحذف (إزالة) صفحات من ملف PDF باستخدام مكتبة Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إضافة أو إدراج صفحة في ملف PDF

يتيح لك Aspose.PDF for Java إدراج صفحة في مستند PDF في أي مكان في الملف وكذلك إضافة صفحات إلى نهاية ملف PDF. تحتاج إلى تمرير الموقع الذي تريد إدراج الصفحة الفارغة فيه إلى دالة الإدراج.
يوضح هذا القسم كيفية إضافة صفحات إلى ملف PDF باستخدام Aspose.PDF for Java.

### إدراج صفحة فارغة في ملف PDF في الموقع المطلوب

يظهر مقتطف الشيفرة التالي كيفية إدراج صفحة فارغة في ملف PDF:

1. إنشاء كائن من فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) مع ملف PDF المدخل.

1. استدعاء طريقة الإدراج [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection) مع الفهرس المحدد.
1. احفظ ملف PDF الناتج باستخدام طريقة الحفظ.

يوضح لك مقتطف الشيفرة التالي كيفية إدراج صفحة في ملف PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddPages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void InsertEmptyPageInPDFFileAtDesiredLocation() {
        Document document = new Document();

        // إضافة صفحة
        document.getPages().add();

        // إدراج صفحة فارغة في ملف PDF
        document.getPages().insert(2);

        // حفظ ملف PDF المحدث
        document.save(_dataDir + "InsertEmptyPage_out.pdf");
    }
```

في المثال أعلاه، أضفنا صفحة فارغة مع المعلمات الافتراضية. إذا كنت بحاجة لجعل حجم الصفحة نفس حجم صفحة أخرى في المستند، يجب عليك إضافة
بضع سطور من الشيفرة:

```java
    public static void InsertEmptyPageInPDFFileAtDesiredLocation01() {
        Document document = new Document();

        // إضافة صفحة
        Page page1 = document.getPages().add();

        // إدراج صفحة فارغة في ملف PDF
        Page page2 = document.getPages().insert(2);
        ;
        // نسخ معلمات الصفحة من الصفحة 1
        page2.setArtBox(page1.getArtBox());
        page2.setBleedBox(page1.getBleedBox());
        page2.setCropBox(page1.getCropBox());
        page2.setMediaBox(page1.getMediaBox());
        page2.setTrimBox(page1.getTrimBox());

        // حفظ ملف PDF المحدث
        document.save(_dataDir + "InsertEmptyPage_out.pdf");
    }
```


### إضافة صفحة فارغة في نهاية ملف PDF

أحيانًا، ترغب في التأكد من أن المستند ينتهي بصفحة فارغة. يوضح هذا الموضوع كيفية إدراج صفحة فارغة في نهاية مستند PDF.

لإدراج صفحة فارغة في نهاية ملف PDF:

1. قم بإنشاء كائن من فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) باستخدام ملف PDF المدخل.
2. استدعِ طريقة الإضافة في مجموعة [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection)، بدون أي معلمات.
3. احفظ ملف PDF الناتج باستخدام طريقة Save.

يظهر لك مقتطف الشيفرة التالي كيفية إدراج صفحة فارغة في نهاية ملف PDF.

```java
public static void AddAnEmptyPageAtTheEndOfAPDFFile() {

        Document document = new Document();
        // إضافة صفحة
        document.getPages().add();

        // إدراج صفحة فارغة في نهاية ملف PDF
        document.getPages().add();

        // حفظ ملف PDF المحدث
        document.save(_dataDir + "InsertEmptyPageAtEnd_out.pdf");
    }

}
```