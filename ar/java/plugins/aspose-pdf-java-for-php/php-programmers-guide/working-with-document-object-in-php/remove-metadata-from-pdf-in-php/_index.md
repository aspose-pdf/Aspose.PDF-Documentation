---
title: إزالة البيانات الوصفية من PDF في PHP
linktitle: إزالة البيانات الوصفية من PDF في PHP
type: docs
weight: 70
url: /ar/java/remove-metadata-from-pdf-in-php/
description: استكشف كيفية إزالة البيانات الوصفية من مستند PDF في PHP باستخدام Aspose.PDF لتحسين الخصوصية وأمان المستند.
lastmod: "2026-10-05"
---
## Aspose.PDF - إزالة البيانات الوصفية

لإزالة البيانات الوصفية من مستند Pdf باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء الفئة **RemoveMetadata**.

كود PHP

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

if (preg_match('/pdfaid:part/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("pdfaid:part");

}

if (preg_match('/dc:format/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("dc:format");

}

# save update document with new information
$doc->save($dataDir . "Remove_Metadata.pdf");

print "Removed metadata successfully, please check output file." . PHP_EOL;

```

**تنزيل الشفرة القابلة للتشغيل**

تحميل **Remove Metadata (Aspose.PDF)** من أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/RemoveMetadata.php)
