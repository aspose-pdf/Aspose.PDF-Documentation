---
title: الحصول على معلومات ملف PDF في PHP
linktitle: الحصول على معلومات ملف PDF في PHP
type: docs
weight: 40
url: /ar/java/get-pdf-file-information-in-php/
description: اكتشف كيف يمكن استخراج معلومات مفصلة عن ملف PDF، بما في ذلك البيانات الوصفية والخصائص، في PHP باستخدام Aspose.PDF.
lastmod: "2026-10-01"
---
## Aspose.PDF - الحصول على معلومات ملف PDF

للحصول على معلومات ملف مستند PDF باستخدام **Aspose.PDF Java for PHP**، قم ببساطة باستدعاء الفئة **GetPdfFileInfo**.

كود PHP

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get document information
$doc_info = $doc->getInfo();

# Show document information
print "Author:-" . $doc_info->getAuthor();
print "Creation Date:-" . $doc_info->getCreationDate();
print "Keywords:-" . $doc_info->getKeywords();
print "Modify Date:-" . $doc_info->getModDate();
print "Subject:-" . $doc_info->getSubject();
print "Title:-" . $doc_info->getTitle();

```

**تحميل الشيفرة الجارية**

تنزيلВ **احصل على معلومات ملف PDF (Aspose.PDF)**В منВ أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetPdfFileInfo.php)
