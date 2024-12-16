---
title: إنشاء أو إضافة جدول في ملف PDF 
linktitle: إنشاء أو إضافة جدول
type: docs
weight: 10
url: /ar/php-java/add-table-in-existing-pdf-document/
description: تعلم كيفية إنشاء أو إضافة جدول إلى مستند PDF، تطبيق نمط الخلية، تقسيم الجدول على الصفحات وتخصيص الصفوف والأعمدة، إلخ.
lastmod: "2024-05-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## إضافة جدول في مستند PDF موجود

لإضافة جدول إلى ملف PDF موجود باستخدام Aspose.PDF لـ PHP، اتبع الخطوات التالية:

1. قم بتحميل الملف المصدر.
1. تهيئة جدول
1. تعيين لون حدود الجدول إلى LightGray
1. تعيين الحدود لخلايا الجدول
1. إنشاء حلقة لإضافة 10 صفوف
1. إضافة كائن الجدول إلى الصفحة الأولى من المستند المدخل
1. حفظ الملف.

توضح مقتطفات الشفرة التالية كيفية إضافة نص في ملف PDF موجود.

```php

    // افتح المستند
    $document = new Document($inputFile);        
    // تهيئة مثيل جديد للجدول
    $table = new Table();
    $colors= new Color();
    // تعيين لون حدود الجدول إلى LightGray
    $borderSide = new BorderSide();
    $borderInfo = new BorderInfo($borderSide->All, 0.5, $colors->getLightGray());
    $table->setBorder($borderInfo);
    // تعيين الحدود لخلايا الجدول
    $table->setDefaultCellBorder($borderInfo);
    // إنشاء حلقة لإضافة 10 صفوف
    for ($row_count = 1; $row_count < 10; $row_count++) {
        // إضافة صف إلى الجدول
        $row = $table->getRows()->add();
        // إضافة خلايا الجدول
        $row->getCells()->add("Column (" . $row_count . ", 1)");
        $row->getCells()->add("Column (" . $row_count . ", 2)");
        $row->getCells()->add("Column (" . $row_count . ", 3)");
    }
    // إضافة كائن الجدول إلى الصفحة الأولى من المستند المدخل
    $document->getPages()->add()->getParagraphs()->add($table);

    // احفظ مستند PDF الناتج.
    $document->save($outputFile);
    $document->close();
```