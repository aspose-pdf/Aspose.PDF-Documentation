---
title: إزالة البيانات الوصفية من PDF في PHP
type: docs
weight: 70
url: /java/remove-metadata-from-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - إزالة البيانات الوصفية

لإزالة البيانات الوصفية من مستند PDF باستخدام **Aspose.PDF Java for PHP**، ببساطة قم باستدعاء فئة **RemoveMetadata**.

كود PHP

```php

# فتح مستند pdf.
$doc = new Document($dataDir . "input1.pdf");

if (preg_match('/pdfaid:part/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("pdfaid:part");

}

if (preg_match('/dc:format/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("dc:format");

}

# حفظ المستند المحدث مع المعلومات الجديدة
$doc->save($dataDir . "Remove_Metadata.pdf");

print "تمت إزالة البيانات الوصفية بنجاح، يرجى التحقق من ملف الإخراج." . PHP_EOL;

```

**تحميل الكود التشغيلي**

قم بتحميل **إزالة البيانات الوصفية (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/RemoveMetadata.php)