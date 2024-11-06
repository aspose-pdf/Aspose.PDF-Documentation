---
title: نقل صفحات PDF
linktitle: نقل صفحات PDF
type: docs
weight: 20
url: ar/php-java/move-pages/
description: حاول نقل الصفحات إلى الموقع المطلوب أو إلى نهاية ملف PDF باستخدام Aspose.PDF لـ PHP عبر Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## نقل صفحة من مستند PDF إلى آخر

يشرح هذا الموضوع كيفية نقل صفحة من مستند PDF إلى نهاية مستند آخر باستخدام PHP.
لنقل صفحة يجب أن:

1. إنشاء كائن فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) مع ملف PDF المصدر
1. إنشاء كائن فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) مع ملف PDF الوجهة
1. إضافة الصفحة إلى مستند الإخراج. احفظ ملف الإخراج
1. حذف الصفحة من مستند الإدخال. احفظ مستند الإدخال المعدل
1. إغلاق المستندات
1. احفظ وأغلق مستند الإخراج

يوضح لك مقتطف الشيفرة التالي كيفية نقل صفحة واحدة.

```php

    // فتح المستند
    $document = new Document($inputFile1);
    $dstDocument = new Document($outputFile);
    
    $page = $document->getPages()->get_Item(2);
    $dstDocument->getPages()->add($page);

    // حفظ ملف الإخراج
    $dstDocument->save($srcFileName);
    $document->getPages()->delete(2);
    $document->save($dstFileName);
    $document->close();
    $dstDocument->close();
  
    // حفظ مستند الإخراج
    $document->save($outputFile);
    $document->close();
```


## نقل مجموعة من الصفحات من مستند PDF إلى آخر

1. إنشاء كائن فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) مع ملف PDF المصدر.
1. إنشاء كائن فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) مع ملف PDF الوجهة.
1. تحديد الصفحات المراد نسخها من المستند المدخل إلى المستند المخرج.
1. تشغيل حلقة عبر المصفوفة:
   1. الحصول على الصفحة في الفهرس المحدد من المستند المدخل.
   1. إضافة الصفحة إلى المستند الوجهة.
1. حفظ ملف PDF المخرج باستخدام طريقة Save.
1. حذف الصفحة في المستند المصدر باستخدام المصفوفة.
1. حفظ ملف PDF المصدر باستخدام طريقة Save.

يوضح لك مقتطف الشيفرة التالي كيفية إدراج صفحة فارغة في نهاية ملف PDF.

```php

    // فتح المستند
    $document = new Document($inputFile1);
    $dstDocument = new Document($outputFile);
    
    $pages = [1, 3 ];
    foreach ($pages as $pageIndex) {
      $page = $document->getPages()->get_Item($pageIndex);
      $dstDocument->getPages()->add(page);
    }
    // حفظ الملفات المخرجة
    $dstDocument->save($srcFileName);
    $document->getPages()->delete($pages);

    $document->save(dstFileName);

    $document->close();
    $dstDocument->close();  
```


## نقل صفحة إلى موقع جديد في مستند PDF الحالي

1. إنشاء كائن من فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) باستخدام ملف PDF المصدر.
2. الحصول على الصفحة من مجموعة [pageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection).
3. إضافة الصفحة إلى الموقع الجديد.
4. حذف الصفحة في الفهرس 2.
5. حفظ ملف PDF الناتج باستخدام طريقة الحفظ.

```php

    // فتح المستند
    $document = new Document($inputFile);
        
    $pageCollection = $document->getPages();
    
    $page = $pageCollection->get_Item(2);
    $pageCollection->add(page);
    $pageCollection->delete(2);

    // حفظ الملف الناتج
    $document->save($outputFile);
    $document->close();      
```