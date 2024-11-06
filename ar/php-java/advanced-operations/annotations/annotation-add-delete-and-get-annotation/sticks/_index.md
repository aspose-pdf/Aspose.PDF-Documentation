---
title: PDF Sticky Annotations 
linktitle: Sticky Annotation
type: docs
weight: 50
url: ar/php-java/sticky-annotations/
description: هذا الموضوع عن التعليقات التوضيحية اللاصقة، كمثال نظهر التعليق التوضيحي للعلامة المائية في النص. يُستخدم لتمثيل الرسومات على الصفحة. تحقق من مقتطف الكود لحل هذه المهمة.
lastmod: "2024-06-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إضافة تعليق توضيحي للعلامة المائية

يجب استخدام تعليق توضيحي للعلامة المائية لتمثيل الرسومات التي يجب طباعتها بحجم وموقع ثابتين على الصفحة، بغض النظر عن أبعاد الصفحة المطبوعة.

يمكنك إضافة نص علامة مائية باستخدام [WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/WatermarkAnnotation) في موقع محدد من صفحة PDF. يمكن أيضًا التحكم في شفافية العلامة المائية باستخدام خاصية الشفافية.

يرجى التحقق من مقتطف الكود التالي لإضافة WatermarkAnnotation.

```php

    // فتح المستند
    $document = new Document($inputFile);
    $fontRepository = new FontRepository();
    $colors = new Color();
    // الحصول على صفحة معينة
    $page = $document->getPages()->get_Item(1);
    
    // إنشاء التعليق التوضيحي
    $wa = new WatermarkAnnotation($page, new Rectangle(100, 500, 400, 600));

    // إضافة التعليق التوضيحي إلى مجموعة التعليقات التوضيحية في الصفحة
    $page->getAnnotations()->add($wa);

    // إنشاء TextState لإعدادات الخط
    $ts = new TextState();

    $ts->setForegroundColor($colors->getBlue());
    $ts->setFont($fontRepository->findFont("Times New Roman"));
    $ts->setFontSize(32);

    // تعيين مستوى الشفافية لنص التعليق التوضيحي
    $wa->setOpacity(0.5);
            
    $watermarkStrings = ["Aspose.PDF", "علامة مائية", "تجريبي" ];
    // إضافة نص إلى التعليق التوضيحي
    $wa->setTextAndState($watermarkStrings, $ts);

    // حفظ مستند PDF الناتج.
    $document->save($outputFile);
    $document->close();
```