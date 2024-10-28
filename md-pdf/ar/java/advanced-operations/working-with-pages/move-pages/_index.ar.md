---

title: نقل صفحات PDF  
linktitle: نقل الصفحات  
type: docs  
weight: 20  
url: /java/move-pages/  
description: حاول نقل الصفحات إلى الموقع المرغوب أو إلى نهاية ملف PDF باستخدام Aspose.PDF for Java.  
lastmod: "2021-06-05"  
sitemap:  
    changefreq: "weekly"  
    priority: 0.7  

## نقل صفحة من مستند PDF إلى آخر

يشرح هذا الموضوع كيفية نقل صفحة من مستند PDF إلى نهاية مستند آخر باستخدام Java.  
لنقل صفحة يجب علينا:

1. إنشاء كائن فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) مع ملف PDF المصدر.
1. إنشاء كائن فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) مع ملف PDF الوجهة.
1. الحصول على الصفحة من مجموعة [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection).
1. إضافة الصفحة إلى مستند الوجهة.
1. حفظ ملف PDF الناتج باستخدام طريقة Save.
1. حذف الصفحة في مستند المصدر.
1. حفظ ملف PDF المصدر باستخدام طريقة Save.

يوضح لك مقتطف الشيفرة التالي كيفية نقل صفحة واحدة.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleMovePDFPages {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void MovePage() {
    String srcFileName = _dataDir + "<enter file name>";
    String dstFileName = _dataDir + "<enter file name>";
    Document srcDocument = new Document();
    Document dstDocument = new Document();
    Page page = srcDocument.getPages().get_Item(2);
    dstDocument.getPages().add(page);
    // حفظ ملف الإخراج
    dstDocument.save(srcFileName);
    srcDocument.getPages().delete(2);
    srcDocument.save(dstFileName);
  }
```

## نقل مجموعة من الصفحات من مستند PDF إلى آخر

1. إنشاء كائن فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) مع ملف PDF المصدر.
1. إنشاء كائن فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) مع ملف PDF الوجهة.
1. تحديد مصفوفة بأرقام الصفحات المراد نقلها.

1. تشغيل حلقة عبر المصفوفة:
    1. الحصول على الصفحة من مجموعة [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection).
    1. إضافة الصفحة إلى المستند الوجهة.
1. حفظ ملف PDF الناتج باستخدام طريقة Save.
1. حذف الصفحة في المستند المصدر باستخدام المصفوفة.
1. حفظ ملف PDF المصدر باستخدام طريقة Save.

يوضح لك مقطع الشيفرة التالي كيفية إدراج صفحة فارغة في نهاية ملف PDF.

```java
  public static void MoveBunchPages() {
    String srcFileName = _dataDir + "<enter file name>";
    String dstFileName = _dataDir + "<enter file name>";
    Document srcDocument = new Document(srcFileName);
    Document dstDocument = new Document();

    Integer[] pages = { 1, 3 };
    for (int pageIndex : pages) {
      Page page = srcDocument.getPages().get_Item(pageIndex);
      dstDocument.getPages().add(page);
    }
    // حفظ الملفات الناتجة
    dstDocument.save(srcFileName);
    srcDocument.getPages().delete(pages);

    srcDocument.save(dstFileName);
  }
```

## نقل صفحة إلى موقع جديد في مستند PDF الحالي

1. قم بإنشاء كائن فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) باستخدام ملف PDF المصدر.
1. احصل على الصفحة من مجموعة [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection).
1. أضف الصفحة إلى الموقع الجديد (على سبيل المثال إلى النهاية).
1. احذف الصفحة في الموقع السابق.
1. احفظ ملف PDF الناتج باستخدام طريقة Save.

```java
  public static void MovePagesInOnePDF() {
    String srcFileName = _dataDir + "<enter file name>";
    String dstFileName = _dataDir + "<enter file name>";

    Document srcDocument = new Document(srcFileName);
    Page page = srcDocument.getPages().get_Item(2);
    srcDocument.getPages().add(page);
    srcDocument.getPages().delete(2);

    // احفظ الملف الناتج
    srcDocument.save(dstFileName);
  }
}
```