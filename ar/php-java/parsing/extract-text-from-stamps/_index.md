---
title: استخراج النص من الطوابع
type: docs
weight: 60
url: ar/php-java/extract-text-from-stamps/
---

## استخراج النص من تعليقات الطوابع

تتيح لك Aspose.PDF for PHP عبر Java استخراج النص من تعليقات الطوابع. لاستخراج النص من تعليقات الطوابع في ملف PDF، يمكن استخدام الخطوات التالية.

1. تحميل مستند PDF
1. الحصول على الصفحة المطلوبة من المستند
1. إنشاء مثيل جديد لفئة StampAnnotation
1. إنشاء مثيل جديد لفئة AnnotationSelector وتمرير تعليق الطابع إليها
1. قبول محدد التعليقات على الصفحة
1. الحصول على تعليقات الطوابع المختارة
1. إنشاء مثيل جديد لفئة TextAbsorber
1. الحصول على أول تعليق طابع
1. الحصول على المظهر الطبيعي لتعليق الطابع
1. زيارة المظهر باستخدام مستخرج النص
1. الحصول على النص المستخرج من مستخرج النص
1. إغلاق المستند

```php
    $responseData = "";
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);
    $stampAnnotation = new StampAnnotation($document);
    $annotationSelector = new AnnotationSelector($stampAnnotation);
    $page->accept($annotationSelector);
    $stampAnnotations = $annotationSelector->getSelected();
    $textAbsorber = new TextAbsorber();
    $stampAnnotation = $stampAnnotations->get(0);    
    $appearance = $stampAnnotation->getNormalAppearance();
    $textAbsorber->visit($appearance);
    $responseData = java_values($textAbsorber->getText());       
    $document->close();
```