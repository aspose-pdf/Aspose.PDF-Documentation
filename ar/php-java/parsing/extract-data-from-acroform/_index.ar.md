---
title: استخراج البيانات من AcroForm
linktitle: استخراج البيانات من AcroForm
type: docs
weight: 50
url: /php-java/extract-data-from-acroform/
description: توجد AcroForms في العديد من مستندات PDF. يهدف هذا المقال إلى مساعدتك على فهم كيفية استخراج البيانات من AcroForms باستخدام PHP وAspose.PDF.
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## استخراج حقول النموذج من مستند PDF

Aspose.PDF for PHP لا يتيح لك فقط إنشاء وملء حقول النماذج، بل يسهل أيضًا استخراج بيانات حقول النماذج أو معلومات حقول النماذج من ملفات PDF.

افترض أننا لا نعرف أسماء حقول النماذج مسبقًا. ثم يجب أن نقوم بالتكرار على كل صفحة في PDF لاستخراج معلومات حول جميع AcroForms في PDF وكذلك قيم حقول النماذج. للوصول إلى النموذج، نحتاج إلى استخدام [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) طريقة.

```php

    // إنشاء مثيل جديد لفئة الترخيص وتعيين ملف الترخيص
    $licenceObject = new License();
    $licenceObject->setLicense($license);

    // تعيين المسار إلى الدليل الذي يحتوي على مستند PDF
    $dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";

    // تعيين المسار إلى ملف PDF المدخل
    $inputFile = $dataDir . DIRECTORY_SEPARATOR . "StudentInfoFormElectronic.pdf";

    // تعيين ترويسة الاستجابة للإشارة إلى أن الاستجابة ستكون بتنسيق JSON
    header('Content-Type: application/json; charset=utf-8');

    // تهيئة متغير بيانات الاستجابة
    $responseData = "";

    try {
        // إنشاء مثيل جديد لفئة المستند وتحميل ملف PDF المدخل
        $document = new Document($inputFile);

        // الحصول على حقول النموذج من المستند وتحويلها إلى قيم PHP
        $fields = java_values($document->getForm()->getFields());

        // حلقة عبر كل حقل نموذج واستخراج اسم الحقل والقيمة
        foreach ($fields as $formField) {
            // دمج اسم الحقل والقيمة مع بيانات الاستجابة
            $responseData = $responseData . "(Field Name: " . $formField->getPartialName() . " |";
            $responseData = $responseData . " Value: " . $formField->getValue() . "),";
        }

        // إغلاق المستند
        $document->close();
    }
```


إذا كنت تعرف أسماء حقول النموذج التي ترغب في استخراج القيم منها، يمكنك استخدام الفهرس في مجموعة Documents.Form لاسترداد هذه البيانات بسرعة.

## استخراج البيانات إلى XML من ملف PDF

تسمح لك فئة Form بتصدير البيانات إلى ملف XML من ملف PDF باستخدام طريقة ExportXml. من أجل تصدير البيانات إلى XML، تحتاج إلى إنشاء كائن من فئة Form ثم استدعاء طريقة ExportXml باستخدام كائن FileStream. وأخيراً، يمكنك إغلاق كائن FileStream وإدارة كائن Form. يوضح لك مقتطف الكود التالي كيفية تصدير البيانات إلى ملف XML.

```php

    // فتح المستند
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // إنشاء كائن FileOutputStream لكتابة ملف الخط.
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.xml");

    // تصدير البيانات
    $form->exportXml($xmlOutputStream);

    // إغلاق تدفق الملف
    $xmlOutputStream->close();

    // إغلاق المستند
    $form->close();
```

## تصدير البيانات إلى FDF من ملف PDF

لتصدير بيانات نماذج PDF إلى ملف XFDF، يمكننا استخدام طريقة [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) في فئة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

يرجى ملاحظة أن هذه الفئة من `com.aspose.pdf.facades`. على الرغم من الاسم المتشابه، فإن لهذه الفئة غرضًا مختلفًا قليلاً.

لتصدير البيانات إلى FDF، تحتاج إلى إنشاء كائن من فئة `Form` ثم استدعاء طريقة `exportXfdf` باستخدام كائن `OutputStream`. يوضح لك مقتطف الشيفرة التالي كيفية تصدير البيانات إلى ملف XFDF.

```php

    // فتح المستند
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // إنشاء كائن FileOutputStream لكتابة ملف الخط.
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.fdf");

    // تصدير البيانات
    $form->exportFdf($xmlOutputStream);

    // إغلاق تدفق الملف
    $xmlOutputStream->close();

    // إغلاق المستند
    $form->close();
```

## تصدير البيانات إلى XFDF من ملف PDF

لتصدير بيانات النماذج في PDF إلى ملف XFDF، يمكننا استخدام طريقة [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) في فئة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

من أجل تصدير البيانات إلى XFDF، تحتاج إلى إنشاء كائن من فئة `Form` ثم استدعاء طريقة `exportXfdf` باستخدام كائن `OutputStream`. يوضح لك مقطع الكود التالي كيفية تصدير البيانات إلى ملف XFDF.

```php

    // افتح المستند
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // أنشئ كائن FileOutputStream لكتابة ملف الخط.
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.xfdf");

    // تصدير البيانات
    $form->exportXfdf($xmlOutputStream);

    // اغلق تدفق الملف
    $xmlOutputStream->close();

    // اغلق المستند
    $form->close();
```