---
title: تعديل AcroForms
linktitle: تعديل AcroForms
type: docs
weight: 40
url: ar/java/modifing-form/
description: يشرح هذا القسم كيفية تعديل النماذج في مستند PDF الخاص بك باستخدام Aspose.PDF لـ PHP عبر Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إعداد خط مخصص لحقل النموذج

يمكن تكوين حقول النموذج في ملفات PDF الخاصة بأدوبي لاستخدام خطوط افتراضية محددة. يسمح Aspose.PDF للمطورين بتطبيق أي خط كخط افتراضي للحقل، سواء كان واحدًا من الـ 14 خطًا الأساسيًا أو خطًا مخصصًا. لتعيين وتحديث الخط الافتراضي المستخدم لحقول النموذج، يحتوي Aspose.PDF على فئة DefaultAppearance (Font font, double size, Color color). يمكن الوصول إلى هذه الفئة باستخدام com.aspose.pdf.DefaultAppearance. لاستخدام هذا الكائن، استخدم طريقة setDefaultAppearance(..) لفئة Field.

يُظهر لك مقتطف الشيفرة التالي كيفية تعيين الخط الافتراضي لحقل نموذج PDF.

```php

    // افتح مستندًا
    $document = new Document($inputFile);

    // احصل على حقل نموذج معين من المستند
    $field = $document->getForm()->get("textbox1");

    // إنشاء كائن الخط
    $fontRepository = new FontRepository();
    $font = $fontRepository->findFont("ComicSansMS");

    $colors = new Color();
    $blackColor = $colors->getBlack();

    // تعيين معلومات الخط لحقل النموذج
    $field->setDefaultAppearance(new DefaultAppearance($font, 10, $blackColor));

    // احفظ المستند المحدّث
    $document->save($outputFile);
    $document->close();        

    $document->close();
```


## الحصول/تعيين حد الحقل

يوضح هذا الكود كيفية استخدام فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) لفتح مستند، استرجاع حقل نموذج، تعيين الحد الأقصى لطوله، واسترجاع الحد الأقصى للطول باستخدام طريقتي 'setMaxLen' و 'getMaxLen'.

```php

    // فتح مستند
    $document = new Document($inputFile);

    // الحصول على حقل نموذج معين من المستند
    $field = $document->getForm()->get("textbox1");
    
    $field->setMaxLen(10);

    // الحصول على الحد الأقصى للحقل باستخدام DOM
    $responseData = "الحد: " . $field->getMaxLen();          

    $document->close();
```

يمكنك أيضًا الحصول على نفس القيمة باستخدام مساحة الأسماء Aspose.PDF.Facades باستخدام جزء الكود التالي.

```php

    // فتح مستند
    $document = new Document($inputFile);

    // الحصول على حقل نموذج معين من المستند
    $field = $document->getForm()->get("textbox1");

    // الحصول على الحد الأقصى للحقل باستخدام DOM
    $responseData = "الحد: " . $field->getMaxLen();          

    $document->close();
```


Similarly, Aspose.PDF has a method that gets the field limit using the DOM approach. The following code snippet shows the steps.

```php

    // فتح مستند
    $document = new Document($inputFile);

    // الحصول على حقل نموذج معين من المستند
    $field = $document->getForm()->get("textbox1");

    // حذف الحقل
    $field->delete();
    
    $document->close();
```
## حذف حقل نموذج معين من مستند PDF

تحتوي جميع حقول النماذج على مجموعة النموذج الخاصة بكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). توفر هذه المجموعة طرقًا مختلفة تدير حقول النماذج، بما في ذلك طريقة الحذف. إذا كنت ترغب في حذف حقل معين، مرر اسم الحقل كمعامل إلى طريقة الحذف ثم قم بحفظ مستند PDF المحدث.

يوضح مقتطف الشيفرة البرمجية التالي كيفية حذف حقل مسمى من مستند PDF.

```php

    // فتح مستند
    $document = new Document($inputFile);

    // الحصول على حقل نموذج معين من المستند
    $field = $document->getForm()->get("textbox1");

    // حذف الحقل
    $field->delete();
    
    $document->close();
```


## تعديل حقل النموذج في مستند PDF

تتيح لك مجموعة النموذج الخاصة بكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) إدارة حقول النماذج في مستند PDF.

لتعديل حقل نموذج، قم بالحصول على الحقل من مجموعة النموذج وقم بتعيين خصائصه. ثم احفظ مستند PDF المحدث.

يوضح مقتطف الشفرة التالي كيفية تعديل حقل نموذج موجود في مستند PDF.

```php

    // فتح مستند
    $document = new Document($inputFile);

    // الحصول على حقل نموذج معين من المستند
    $field = $document->getForm()->get("textbox1");

    // تعديل قيمة الحقل
    $field->setValue("قيمة محدثة");

    // تعيين الحقل كقراءة فقط
    $field->setReadOnly(true);

    // حفظ المستند المحدث
    $document->save($outputFile);        
    $document->close();
```

### نقل حقل النموذج إلى موقع جديد في ملف PDF

إذا كنت ترغب في نقل حقل نموذج إلى موقع جديد على صفحة PDF، احصل أولاً على كائن الحقل ثم حدد قيمة جديدة لطريقة setRect الخاصة به.
 A [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) كائن بإحداثيات جديدة يتم تعيينه لطريقة setRect(..). ثم احفظ ملف PDF المحدث باستخدام طريقة الحفظ لكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

يظهر لك مقتطف الشيفرة التالي كيفية نقل حقل نموذج إلى موقع جديد.

```php

    // فتح مستند
    $document = new Document($inputFile);

    // الحصول على حقل نموذج معين من المستند
    $field = $document->getForm()->get("textbox1");

    // تعديل موقع الحقل
    $field->setRect(new Rectangle(300, 400, 600, 500));

    // حفظ المستند المحدث
    $document->save($outputFile);        
    $document->close();
```