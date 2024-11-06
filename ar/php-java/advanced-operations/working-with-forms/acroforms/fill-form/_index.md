---
title: ملء AcroForms
linktitle: ملء AcroForms
type: docs
weight: 20
url: ar/php-java/fill-form/
description: يوضح هذا القسم كيفية ملء حقل نموذج في مستند PDF باستخدام Aspose.PDF لـ PHP عبر Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

تعتبر مستندات PDF رائعة، وهي حقًا نوع الملف المفضل، لإنشاء النماذج.

يسمح لك Aspose.PDF لـ PHP عبر Java بملء حقل نموذج، والحصول على الحقل من مجموعة النماذج لكائن المستند.

لنلقِ نظرة على المثال التالي لكيفية حل هذه المهمة:

```php

    // افتح المستند
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);
    
    // احصل على حقل    
    $textBoxField = $document->getForm()->get("textbox1");

    // تعديل قيمة الحقل
    $textBoxField->setValue("القيمة التي سيتم ملؤها في الحقل");
        
    // احفظ المستند المحدث
    $document->save($outputFile);
    $document->close();
```