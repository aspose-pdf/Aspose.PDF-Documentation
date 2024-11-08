---
title: الحصول على بيانات XMP الوصفية من ملف PDF في PHP
type: docs
weight: 50
url: /ar/java/get-xmp-metadata-from-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - الحصول على بيانات XMP الوصفية

للحصول على بيانات XMP الوصفية من مستند Pdf باستخدام **Aspose.PDF Java for PHP**، ببساطة قم باستدعاء فئة **GetXMPMetadata**.

كود PHP

```php

# فتح مستند pdf.
$doc = new Document($dataDir . "input1.pdf");

# الحصول على الخصائص
print "xmp:CreateDate: " + $doc->getMetadata()->get_Item("xmp:CreateDate") . PHP_EOL;
print "xmp:Nickname: " + $doc->getMetadata()->get_Item("xmp:Nickname") . PHP_EOL;
print "xmp:CustomProperty: " + $doc->getMetadata()->get_Item("xmp:CustomProperty") . PHP_EOL;

```

**تحميل الكود الجاري**

قم بتحميل **الحصول على بيانات XMP الوصفية (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetXMPMetadata.php)