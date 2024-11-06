---
title: استخراج النص الخام من ملف PDF 
linktitle: استخراج النص من PDF
type: docs
weight: 10
url: ar/php-java/extract-text-from-all-pdf/
description: تصف هذه المقالة طرقًا مختلفة لاستخراج النص من مستندات PDF باستخدام Aspose.PDF for PHP. من صفحات كاملة، من جزء محدد، بناءً على الأعمدة، إلخ.
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## استخراج النص من جميع صفحات مستند PDF

استخراج النص من مستند PDF هو متطلب شائع. في هذا المثال، ستتعلم كيف يتيح لك Aspose.PDF for PHP استخراج النص من جميع صفحات مستند PDF.
لاستخراج النص من جميع صفحات PDF:

1. قم بإنشاء كائن من فئة [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber).

1. افتح ملف PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) واستدعِ طريقة [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) من مجموعة [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
2. تقوم فئة [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) بامتصاص النص من المستند وتعيده في [طريقة getText()](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/#getText--).

يُظهر لك مقطع الشيفرة التالي كيفية استخراج النص من جميع صفحات مستند PDF.

```php

    // قم بإنشاء كائن Document جديد من ملف PDF المدخل.
    $document = new Document($inputFile);

    // قم بإنشاء كائن TextAbsorber جديد لاستخراج النص من المستند.
    $textAbsorber = new TextAbsorber();

    // استخراج النص من المستند.
    $textAbsorber->visit($document);

    // الحصول على محتوى النص المستخرج.
    $content = $textAbsorber->getText();

    // حفظ النص المستخرج إلى الملف الناتج.
    file_put_contents($outputFile, $content);
```