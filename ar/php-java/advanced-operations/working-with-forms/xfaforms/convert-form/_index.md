---
title: تحويل نموذج XFA إلى AcroForm
linktitle: تحويل نموذج XFA
type: docs
weight: 10
url: ar/php-java/convert-form/
description: يشرح هذا القسم كيفية تحويل نموذج XFA إلى AcroForm باستخدام Aspose.PDF لـ PHP عبر Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## تحويل نموذج XFA ديناميكي إلى AcroForm قياسي

النماذج الديناميكية تعتمد على مواصفات XML تعرف بإسم XFA، "هندسة النماذج XML". يمكن أيضاً تحويل نموذج XFA الديناميكي إلى Acroform قياسي. المعلومات حول النموذج (بقدر ما يتعلق الأمر بـ PDF) غير واضحة جداً - تحدد وجود الحقول، مع الخصائص، وأحداث JavaScript، ولكن لا تحدد أي عرض. يتم رسم كائنات نموذج XFA في وقت تحميل المستند.

حالياً، يدعم PDF طريقتين مختلفتين لدمج البيانات ونماذج PDF:

- AcroForms (تُعرف أيضاً بنماذج Acrobat)، تم تقديمها وضمها في مواصفات تنسيق PDF 1.2.

- تم تقديم نماذج Adobe XML Forms Architecture (XFA) في مواصفات تنسيق PDF 1.5 كميزة اختيارية. (مواصفات XFA غير مضمنة في مواصفات PDF، إنها مذكورة فقط.)

لا يمكن استخراج أو معالجة صفحات نماذج XFA، لأن محتوى النموذج يتم إنشاؤه في وقت التشغيل (أثناء عرض نموذج XFA) داخل التطبيق الذي يحاول عرض أو تقديم نموذج XFA. يحتوي Aspose.PDF على ميزة تتيح للمطورين تحويل نماذج XFA إلى نماذج AcroForms القياسية.

```php

        // تحميل نموذج XFA
        $document = new Document($inputFile);
        
        // تعيين نوع حقول النموذج كـ AcroForm قياسي
        $formType = new FormType();
        $document->getForm()->setType($formType->getStandard());
            
        // حفظ المستند المحدث
        $document->save($outputFile);
        
        // حفظ PDF المعدل   
        $document->close();
```