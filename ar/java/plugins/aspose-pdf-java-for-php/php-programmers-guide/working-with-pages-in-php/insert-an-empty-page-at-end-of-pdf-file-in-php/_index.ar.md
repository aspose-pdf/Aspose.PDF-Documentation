---
title: إدراج صفحة فارغة في نهاية ملف PDF باستخدام PHP
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - إدراج صفحة فارغة في نهاية ملف PDF

لإدراج صفحة فارغة في نهاية مستند PDF باستخدام **Aspose.PDF Java for PHP**، ببساطة استدعاء فئة **InsertEmptyPageAtEndOfFile**.

كود PHP

```php

# افتح المستند المستهدف
$pdf = new Document($dataDir . 'input1.pdf');

# إدراج صفحة فارغة في PDF
$pdf->getPages()->add();

# احفظ ملف الإخراج المدمج (المستند المستهدف)
$pdf->save($dataDir . "output.pdf");

print "تمت إضافة الصفحة الفارغة بنجاح!" . PHP_EOL;

```

## تنزيل الكود التشغيلي

قم بتنزيل **إدراج صفحة فارغة في نهاية ملف PDF (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPageAtEndOfFile.php)