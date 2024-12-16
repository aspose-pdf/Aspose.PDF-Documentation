---
title: تغيير حجم صفحة PDF برمجيًا
linktitle: تغيير حجم صفحة PDF
type: docs
weight: 50
url: /ar/php-java/change-page-size/
description: تغيير حجم الصفحة في ملف PDF باستخدام PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## تغيير حجم صفحة PDF

Aspose.PDF لـ PHP عبر Java يتيح لك تغيير حجم صفحة PDF بخطوط بسيطة من التعليمات البرمجية في تطبيقات Java الخاصة بك. يشرح هذا الموضوع كيفية تحديث/تغيير أبعاد الصفحة (الحجم) لملف PDF موجود.

تحتوي فئة [Page](https://reference.aspose.com/pdf//java/com.aspose.pdf/page) على طريقة SetPageSize(...) التي تتيح لك تعيين حجم الصفحة. يقوم مقتطف الشيفرة أدناه بتحديث أبعاد الصفحة في بضع خطوات بسيطة:

1. قم بتحميل ملف PDF المصدر.
2. احصل على الصفحات في كائن [pageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection).
3. احصل على صفحة معينة.
4. استدعِ طريقة setPageSize(..) لتحديث أبعادها.

1. قم باستدعاء طريقة الحفظ(..) للفئة [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) لإنشاء ملف PDF بأبعاد صفحة محدثة.

يوضح مقتطف الشيفرة التالي كيفية تغيير أبعاد صفحة PDF إلى حجم A4.

```php

    // فتح المستند
    $document = new Document($inputFile);
      
    // الحصول على مجموعة الصفحات
    $pageCollection = $document->getPages();

    // الحصول على صفحة معينة
    $page = $pageCollection->get_Item(1);

    // تعيين حجم الصفحة كـ A4 (11.7 × 8.3 بوصة) وفي Aspose.Pdf، 1 بوصة = 72 نقطة
    // لذلك ستكون أبعاد A4 بالنقاط هي (842.4، 597.6)
    $page.setPageSize(597.6, 842.4);

    // حفظ المستند الناتج
    $document->save($outputFile);
    $document->close();
```

## الحصول على حجم صفحة PDF

يمكنك قراءة حجم صفحة PDF لملف PDF موجود باستخدام Aspose.PDF لـ PHP عبر Java. يوضح نموذج الشيفرة التالي كيفية قراءة أبعاد صفحة PDF باستخدام PHP.

```php

    // فتح المستند
    $document = new Document($inputFile);
      
    // إضافة صفحة فارغة إلى مستند pdf
    $page = $document->getPages()->size() > 0 
        ? $document->getPages()->get_Item(1) 
        : $document->getPages()->add();
    
    // الحصول على معلومات ارتفاع وعرض الصفحة
    $responseData = $page->getPageRect(true)->getWidth() . ":" . $page->getPageRect(true)->getHeight();
    
    // تدوير الصفحة بزاوية 90 درجة
    $rotation = new Rotation();
    $page->setRotate($rotation->getOn90());

    // الحصول على معلومات ارتفاع وعرض الصفحة
    $responseData = $responseData . $page->getPageRect(true)->getWidth() . ":" . $page->getPageRect(true)->getHeight();
    
    // حفظ المستند الناتج
    $document->save($outputFile);
    $document->close();
```