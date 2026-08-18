---
title: احصل على بيانات تعريف XMP من ملف PDF في PHP
linktitle: احصل على بيانات تعريف XMP من ملف PDF في PHP
type: docs
weight: 50
url: /java/get-xmp-metadata-from-pdf-file-in-php/
description: تعرف على كيفية استخراج بيانات تعريف XMP من مستندات PDF في PHP باستخدام Aspose.PDF لتحليل المحتوى المتقدم.
lastmod: "2026-06-09"
---
## Aspose.PDF - احصل على بيانات تعريف XMP

للحصول على بيانات تعريف XMP من مستند Pdf باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء فئة **GetXMPMetadata**.

كود PHP

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get properties
print "xmp:CreateDate: " + $doc->getMetadata()->get_Item("xmp:CreateDate") . PHP_EOL;
print "xmp:Nickname: " + $doc->getMetadata()->get_Item("xmp:Nickname") . PHP_EOL;
print "xmp:CustomProperty: " + $doc->getMetadata()->get_Item("xmp:CustomProperty") . PHP_EOL;

```

** تنزيل كود التشغيل **

تنزيل ** احصل على بيانات تعريف XMP (Aspose.PDF) ** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetXMPMetadata.php)
