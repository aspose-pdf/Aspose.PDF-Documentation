---
title: قم بتعيين معلومات ملف PDF في PHP
linktitle: قم بتعيين معلومات ملف PDF في PHP
type: docs
weight: 90
url: /java/set-pdf-file-information-in-php/
description: تعرف على كيفية تعيين خصائص ملف مختلفة، مثل البيانات التعريفية، لمستند PDF في PHP باستخدام Aspose.PDF.
lastmod: "2026-06-09"
---
## Aspose.PDF - ضبط معلومات ملف PDF

لتحديث معلومات مستند Pdf باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء فئة **SetPdfFileInfo**.

كود PHP

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get document information
$doc_info = $doc->getInfo();

$doc_info->setAuthor("Aspose.PDF for java");
$doc_info->setCreationDate(new Date());
$doc_info->setKeywords("Aspose.PDF, DOM, API");
$doc_info->setModDate(new Date());
$doc_info->setSubject("PDF Information");
$doc_info->setTitle("Setting PDF Document Information");

# save update document with new information
$doc->save($dataDir . "Updated_Information.pdf");

print "Update document information, please check output file.";

```

** تنزيل كود التشغيل **

تنزيلВ **تعيين معلومات ملف PDF (Aspose.PDF)**В fromВ من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetPdfFileInfo.php)
