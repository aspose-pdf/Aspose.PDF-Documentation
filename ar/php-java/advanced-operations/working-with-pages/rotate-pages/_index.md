---
title: تدوير صفحات PDF برمجيًا
linktitle: تدوير صفحات PDF
type: docs
weight: 60
url: /ar/php-java/rotate-pages/
description: تغيير اتجاه الصفحة وتعديل محتوى الصفحة ليتناسب مع الاتجاه الجديد باستخدام Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## تغيير اتجاه الصفحة

تصف هذه المقالة كيفية تحديث أو تغيير اتجاه الصفحة للصفحات في ملف PDF موجود.

يمتلك Aspose.PDF for PHP عبر Java ميزة تغيير اتجاه الصفحة من أفقي إلى عمودي والعكس صحيح.

1. افتح المستند باستخدام الملف المحدد كمدخل.
1. احصل على جميع صفحات المستند.
1. قم بالتكرار عبر كل صفحة واضبط الدوران على 90 درجة.
1. احفظ المستند المعدل في الملف المحدد كخرج.
1. أغلق المستند.

```php

    // فتح المستند
    $document = new Document($inputFile);                
    $pages = $document->getPages();
    $pagesSize = java_values($pages->size());
       
    // التكرار عبر جميع الصفحات
    for ($pageCount = 1; $pageCount <= $pagesSize; $pageCount++) {
        $page = $pages->get_Item($pageCount);
       
        $page->setRotate((new Rotation())->On90);
    }

    // حفظ مستند الخرج
    $document->save($outputFile);
    $document->close();
```