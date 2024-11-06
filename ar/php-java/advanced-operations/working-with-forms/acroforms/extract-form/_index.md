---
title: استخراج البيانات من نماذج AcroForms
linktitle: استخراج البيانات من نماذج AcroForms
type: docs
weight: 30
url: ar/php-java/extract-form/
description: يوضح هذا القسم كيفية استخراج النماذج من مستند PDF الخاص بك باستخدام Aspose.PDF لـ PHP عبر Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## الحصول على قيمة من حقل فردي في مستند PDF

تسمح لك [طريقة getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) لحقل النموذج بالحصول على قيمة حقل معين.

للحصول على القيمة، احصل على حقل النموذج من مجموعة النماذج في كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

يختار هذا المثال [textBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) ويسترجع قيمته باستخدام [طريقة getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```php

    // فتح مستند
    $document = new Document($inputFile);

    // الحصول على حقل
    $textBoxField = $document->getForm()->get("textbox1");

    // الحصول على اسم الحقل
    $responseData = "PartialName: " . $textBoxField->getPartialName();

    // الحصول على قيمة الحقل
    $responseData = $responseData . " Value: " . $textBoxField->getValue();
    $document->close();
```