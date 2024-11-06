---
title: إضافة نص إلى ملف PDF
linktitle: إضافة نص إلى ملف PDF
type: docs
weight: 10
url: ar/php-java/add-text-to-pdf-file/
description: تصف هذه المقالة الجوانب المختلفة للعمل مع النص في Aspose.PDF. تعلم كيفية إضافة نص إلى PDF، إضافة شظايا HTML، أو استخدام خطوط OTF مخصصة.
lastmod: "2024-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

لإضافة نص إلى ملف PDF موجود:

1. افتح ملف PDF المدخل باستخدام كائن Document.
1. احصل على الصفحة المعينة التي ترغب في إضافة النص إليها.
1. أنشئ جزء نصي يحتوي على المحتوى "Aspose.PDF".
1. حدد موضع الجزء النصي على الصفحة.
1. حدد خصائص النص للجزء النصي.
1. أنشئ كائن TextBuilder للصفحة.
1. أضف الجزء النصي إلى صفحة PDF.
4. احفظ مستند PDF الناتج في ملف الإخراج.

## إضافة نص

يظهر لك مقطع الشفرة التالي كيفية إضافة نص في ملف PDF موجود.

```php

    // افتح المستند
    $document = new Document($inputFile);
    
    // احصل على الصفحة المعينة
    $page = $document->getPages()->add();
    
    // أنشئ جزء نصي
    $textFragment = new TextFragment("Aspose.PDF");
    $textFragment->setPosition(new Position(80, 700));

    // حدد خصائص النص
    $fontRepository = new FontRepository();
    
    $colors = new Color();
    $textFragment->getTextState()->setFont($fontRepository->findFont("Verdana"));
    $textFragment->getTextState()->setFontSize(14);
    $textFragment->getTextState()->setForegroundColor($colors->getBlue());
    $textFragment->getTextState()->setBackgroundColor($colors->getLightGray());

    // أنشئ كائن TextBuilder
    $textBuilder = new TextBuilder($page);
    // أضف الجزء النصي إلى صفحة PDF
    $textBuilder->appendText($textFragment);

    // احفظ مستند PDF الناتج.
    $document->save($outputFile);
    $document->close();
```