---
title: إدراج صفحة فارغة في ملف PDF باستخدام PHP
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - إدراج صفحة فارغة

لإدراج صفحة فارغة في مستند PDF باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء فئة **InsertEmptyPage**.

كود PHP

```php

# افتح المستند الهدف
$pdf = new Document($dataDir . 'input1.pdf');

# إدراج صفحة فارغة في ملف PDF
$pdf->getPages()->insert(1);

# احفظ ملف الخرج المدمج (المستند الهدف)
$pdf->save($dataDir . "output.pdf");

print "تمت إضافة الصفحة الفارغة بنجاح!";

```

**تنزيل الكود التشغيلي**

قم بتنزيل **إدراج صفحة فارغة (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPage.php)