---
title: استخراج نموذج XFA
linktitle: استخراج نموذج XFA
type: docs
weight: 30
url: ar/php-java/extract-form/
description: تشرح هذه القسم كيفية استخراج النماذج من مستند PDF الخاص بك باستخدام Aspose.PDF لـ PHP عبر Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## الحصول على قيمة من حقل نموذج في مستند PDF

تتيح لك طريقة [getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) الخاصة بحقل النموذج الحصول على قيمة حقل معين.

للحصول على القيمة، احصل على حقل النموذج من مجموعة النماذج الخاصة بكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

يقوم هذا المثال باختيار [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) واسترجاع قيمته باستخدام طريقة [getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```php

    // تحميل نموذج XFA
    $document = new Document($inputFile);
    
    // الحصول على أسماء حقول نموذج XFA
    $names = $document->getForm()->getXFA()->getFieldNames();
        
    // الحصول على قيم الحقول
    $document->getForm()->getXFA()->get_Item($names[0]);
    $document->getForm()->getXFA()->get_Item($names[1]);
    
    // حفظ PDF المعدل    
    $document->close();
```