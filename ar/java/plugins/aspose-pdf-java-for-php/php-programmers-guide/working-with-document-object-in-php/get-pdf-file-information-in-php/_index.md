---
title: الحصول على معلومات ملف PDF في PHP
linktitle: الحصول على معلومات ملف PDF في PHP
type: docs
weight: 40
url: /java/get-pdf-file-information-in-php/
description: اكتشف كيفية استرداد معلومات تفصيلية حول ملف PDF، بما في ذلك البيانات التعريفية والخصائص، في PHP باستخدام Aspose.PDF.
lastmod: "2026-06-09"
---
## Aspose.PDF - احصل على معلومات ملف PDF

للحصول على معلومات ملف مستند Pdf باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء فئة **GetPdfFileInfo**.

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

** تنزيل كود التشغيل **

تنزيلВ **احصل على معلومات ملف PDF (Aspose.PDF)**В fromВ من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetPdfFileInfo.php)
