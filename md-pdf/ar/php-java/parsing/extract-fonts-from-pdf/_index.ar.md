---
title: استخراج الخطوط من PDF 
linktitle: استخراج الخطوط
type: docs
weight: 30
url: /php-java/extract-fonts-from-pdf/
description: كيفية استخراج الخطوط من PDF باستخدام Aspose.PDF لـ PHP
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

في حال أردت الحصول على جميع الخطوط من مستند PDF، يمكنك استخدام [Document.IDocumentFontUtilities.getAllFonts()](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getFontUtilities--) المقدمة في فئة الوثيقة.
يرجى مراجعة المقتطف البرمجي التالي للحصول على جميع الخطوط من مستند PDF موجود:

```php

    // إنشاء مثيل جديد لفئة الترخيص وتعيين ملف الترخيص.
    $licenceObject = new License();
    $licenceObject->setLicense($license);

    // تعيين المسار إلى الدليل الذي يحتوي على مستند PDF ودليل الإخراج للخطوط المستخرجة.
    $dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";
    $inputFile = $dataDir . DIRECTORY_SEPARATOR . "sample.pdf";

    // تهيئة متغير بيانات الاستجابة.
    $responseData = "";

    try {
        // تحميل مستند PDF.
        $document = new Document($inputFile);

        // الحصول على جميع الخطوط المستخدمة في مستند PDF.
        $fonts = java_values($document->getFontUtilities()->getAllFonts());

        // التكرار على كل خط وحفظه كملف خط TrueType.
        foreach ($fonts as $font) {
            // تعيين مسار ملف الإخراج لملف الخط.
            $outputFile = $dataDir . DIRECTORY_SEPARATOR . "results" . DIRECTORY_SEPARATOR . $font->getFontName() . ".ttf";

            // إنشاء كائن FileOutputStream لكتابة ملف الخط.
            $fontStream = new java("java.io.FileOutputStream", $outputFile);

            // حفظ الخط كملف خط TrueType.
            $font->save($fontStream);

            // إغلاق تدفق الخط.
            $fontStream->close();

            // إلحاق اسم الخط ببيانات الاستجابة.
            $responseData = $responseData . $font->getFontName() . ", ";
        }

        // إغلاق مستند PDF.
        $document->close();
    }
```