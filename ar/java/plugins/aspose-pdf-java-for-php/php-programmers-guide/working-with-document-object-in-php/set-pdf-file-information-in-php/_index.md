---
title: تعيين معلومات ملف PDF في PHP
type: docs
weight: 90
url: ar/java/set-pdf-file-information-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - تعيين معلومات ملف PDF

لتحديث معلومات مستند Pdf باستخدام **Aspose.PDF Java for PHP**، قم ببساطة باستدعاء فئة **SetPdfFileInfo**.

كود PHP

```php

# فتح مستند pdf.
$doc = new Document($dataDir . "input1.pdf");

# الحصول على معلومات المستند
$doc_info = $doc->getInfo();

$doc_info->setAuthor("Aspose.PDF for java");
$doc_info->setCreationDate(new Date());
$doc_info->setKeywords("Aspose.PDF, DOM, API");
$doc_info->setModDate(new Date());
$doc_info->setSubject("PDF Information");
$doc_info->setTitle("Setting PDF Document Information");

# حفظ المستند المحدث بالمعلومات الجديدة
$doc->save($dataDir . "Updated_Information.pdf");

print "تحديث معلومات المستند، يرجى التحقق من ملف الإخراج.";

```

**تنزيل الكود الجاري**

قم بتنزيل **تعيين معلومات ملف PDF (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetPdfFileInfo.php)