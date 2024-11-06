---
title: ملء نماذج AcroForms
linktitle: ملء نماذج AcroForms
type: docs
weight: 20
url: ar/php-java/fill-form/
description: تشرح هذه القسم كيفية ملء حقل النموذج في مستند PDF باستخدام Aspose.PDF for PHP عبر Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

مستندات PDF رائعة، وهي بالفعل النوع المفضل من الملفات لإنشاء النماذج.

يسمح لك Aspose.PDF for PHP عبر Java بملء حقل نموذج، والحصول على الحقل من مجموعة النموذج الخاصة بكائن المستند.

لننظر إلى المثال التالي لكيفية حل هذه المهمة:

```php

    // تحميل نموذج XFA
    $document = new Document($inputFile);
    
    // الحصول على أسماء حقول نموذج XFA
    $names = $document->getForm()->getXFA()->getFieldNames();
        
    // تعيين قيم الحقول        
    $document->getForm()->getXFA()->set_Item($names[0],"Field 0");
    $document->getForm()->getXFA()->set_Item($names[1],"Field 1");
        
    // حفظ المستند المحدث
    $document->save($outputFile);
    
    // حفظ ملف PDF المعدل    
    $document->close();
```