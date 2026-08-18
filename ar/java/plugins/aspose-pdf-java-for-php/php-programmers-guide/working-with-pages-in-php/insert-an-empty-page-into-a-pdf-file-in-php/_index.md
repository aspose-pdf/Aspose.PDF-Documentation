---
title: إدراج صفحة فارغة في ملف PDF في PHP
linktitle: إدراج صفحة فارغة في ملف PDF في PHP
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-php/
description: تعرف على كيفية إدراج صفحة فارغة في أي موضع داخل ملف PDF في PHP باستخدام Aspose.PDF لتنظيم مرن للمستندات.
lastmod: "2026-06-09"
---
## Aspose.PDF - أدخل صفحة فارغة

لإدراج صفحة فارغة في مستند Pdf باستخدام **Aspose.PDF Java لـ PHP**، ما عليك سوى استدعاء فئة **InsertEmptyPage**.

كود PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# insert a empty page in a PDF
$pdf->getPages()->insert(1);

# Save the concatenated output file (the target document)
$pdf->save($dataDir . "output.pdf");

print "Empty page added successfully!";

```

** تنزيل كود التشغيل **

تنزيلВ **أدخل صفحة فارغة (Aspose.PDF)**В fromВ من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPage.php)
