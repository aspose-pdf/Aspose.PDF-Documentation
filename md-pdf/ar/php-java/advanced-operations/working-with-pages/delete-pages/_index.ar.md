---
title: حذف صفحات PDF برمجياً
linktitle: حذف صفحات PDF
type: docs
weight: 40
url: /php-java/delete-pages/
description: يمكنك حذف الصفحات من ملف PDF الخاص بك باستخدام PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## حذف صفحة من ملف PDF

1. استدعِ طريقة الحذف وحدد فهرس الصفحة
1. استدعِ طريقة الحفظ لحفظ ملف PDF المحدث
يظهر مقطع الشيفرة التالي كيفية حذف صفحة معينة من ملف PDF باستخدام PHP.

```php

    // افتح المستند
    $document = new Document($inputFile);      

    $pages = $document->getPages();

    // حذف صفحة معينة
    $pages->delete(2);

    // حفظ مستند الإخراج
    $document->save($outputFile);
    $document->close();
```