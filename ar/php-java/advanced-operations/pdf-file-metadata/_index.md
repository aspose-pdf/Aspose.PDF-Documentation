---
title: العمل مع بيانات التعريف لملف PDF
linktitle: بيانات تعريف ملف PDF
type: docs
weight: 140
url: ar/php-java/pdf-file-metadata/
description: تشرح هذه القسم كيفية الحصول على معلومات ملف PDF، وكيفية الحصول على بيانات XMP من ملف PDF، وتعيين معلومات ملف PDF.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## الحصول على معلومات ملف PDF

للحصول على معلومات محددة عن ملف PDF، أولاً احصل على كائن 'docInfo' باستخدام فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) [getInfo()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getInfo--). بمجرد استرداد كائن 'docInfo'، يمكنك الحصول على قيم الخصائص الفردية.

يظهر لك مقتطف الشيفرة التالي كيفية تعيين معلومات ملف PDF.

```php

    // افتح المستند
    $document = new Document($inputFile);
    
    // احصل على معلومات المستند
    $docInfo = $document->getInfo();

    // عرض معلومات المستند
    $responseData1 = "المؤلف: " . $docInfo->getAuthor() . ", ";
    $responseData2 = "تاريخ الإنشاء: " . $docInfo->getCreationDate() . ", ";
    $responseData3 = "الكلمات المفتاحية: " . $docInfo->getKeywords() . ", ";
    $responseData4 = "تاريخ التعديل: " . $docInfo->getModDate() . ", ";
    $responseData5 = "الموضوع: " . $docInfo->getSubject() . ", ";
    $responseData6 = "العنوان: " . $docInfo->getTitle() . "";

    $document->close();
```