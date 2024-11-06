---
title: استخراج الصور من PDF 
linktitle: استخراج الصور
type: docs
weight: 20
url: ar/php-java/extract-images-from-the-pdf-file/
description: كيفية استخراج جزء من الصورة من PDF باستخدام Aspose.PDF لـ PHP
lastmod: "2024-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

تحتوي كل صفحة في مستند PDF على موارد (صور، نماذج وخطوط). يمكننا الوصول إلى هذه الموارد عن طريق استدعاء طريقة [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--). تحتوي فئة [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) على [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) ويمكننا الحصول على قائمة الصور عن طريق استدعاء طريقة [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--).

لذلك لاستخراج صورة من الصفحة، نحتاج إلى الحصول على مرجع للصفحة، ثم إلى موارد الصفحة وأخيرًا إلى مجموعة الصور.
يمكننا استخراج صورة معينة على سبيل المثال بواسطة الفهرس.

يُرجع فهرس الصورة كائن [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage).
هذا الكائن يوفر طريقة [حفظ](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) التي يمكن استخدامها لحفظ الصورة المستخرجة. يوضح مقطع الشيفرة التالي كيفية استخراج الصور من ملف PDF.

```php

    // تحميل مستند PDF
    $document = new Document($inputFile);

    // الحصول على الصفحة الأولى من المستند
    $page = $document->getPages()->get_Item(1);

    // الحصول على مجموعة الصور في الصفحة
    $xImageCollection = $page->getResources()->getImages();

    // الحصول على الصورة الأولى من المجموعة
    $xImage = $xImageCollection->get_Item(1);

    // إنشاء كائن FileOutputStream جديد لحفظ الصورة
    $outputImage = new java("java.io.FileOutputStream", $outputFile);

    // حفظ الصورة في ملف الإخراج
    $xImage->save($outputImage);

    // إغلاق ملف صورة الإخراج
    $outputImage->close();
```