---
title: تعيين معلومات ملف PDF في PHP
linktitle: تعيين معلومات ملف PDF في PHP
type: docs
weight: 90
url: /ar/java/set-pdf-file-information-in-php/
description: تعلم كيفية تعيين خصائص ملف مختلفة، مثل البيانات الوصفية، لوثيقة PDF في PHP باستخدام Aspose.PDF.
lastmod: "2026-10-05"
---
## Aspose.PDF - تعيين معلومات ملف PDF

لتحديث معلومات مستند Pdf باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء الفئة **SetPdfFileInfo**.

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

**تنزيل الشفرة القابلة للتشغيل**

تحميل **تحديد معلومات ملف PDF (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetPdfFileInfo.php)
