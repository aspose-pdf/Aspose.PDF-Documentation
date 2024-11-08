---
title: الحصول على معلومات ملف PDF في PHP
type: docs
weight: 40
url: /ar/java/get-pdf-file-information-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - الحصول على معلومات ملف PDF

للحصول على معلومات ملف وثيقة Pdf باستخدام **Aspose.PDF Java for PHP**، قم ببساطة باستدعاء فئة **GetPdfFileInfo**.

كود PHP

```php

# فتح مستند pdf.
$doc = new Document($dataDir . "input1.pdf");

# الحصول على معلومات المستند
$doc_info = $doc->getInfo();

# عرض معلومات المستند
print "المؤلف:-" . $doc_info->getAuthor();
print "تاريخ الإنشاء:-" . $doc_info->getCreationDate();
print "الكلمات المفتاحية:-" . $doc_info->getKeywords();
print "تاريخ التعديل:-" . $doc_info->getModDate();
print "الموضوع:-" . $doc_info->getSubject();
print "العنوان:-" . $doc_info->getTitle();

```

**تحميل الكود القابل للتشغيل**

قم بتحميل **الحصول على معلومات ملف PDF (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetPdfFileInfo.php)