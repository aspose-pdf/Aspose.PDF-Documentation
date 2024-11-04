---
title: دمج ملفات PDF في PHP
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - دمج ملفات PDF

لدمج ملفات PDF باستخدام **Aspose.PDF Java for PHP**، ببساطة قم باستدعاء فئة **ConcatenatePdfFiles**.

كود PHP

```php

# فتح المستند الهدف
$pdf1 = new Document($dataDir . 'input1.pdf');

# فتح المستند المصدر
$pdf2 = new Document($dataDir . 'input2.pdf');

# إضافة صفحات المستند المصدر إلى المستند الهدف
$pdf1->getPages()->add($pdf2->getPages());

# حفظ ملف الإخراج المدمج (المستند الهدف)
$pdf1->save($dataDir . "Concatenate_output.pdf");

print "تم حفظ المستند الجديد، يرجى التحقق من ملف الإخراج" . PHP_EOL;

```

**تنزيل الكود القابل للتشغيل**

قم بتنزيل **دمج ملفات PDF (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/ConcatenatePdfFiles.php)