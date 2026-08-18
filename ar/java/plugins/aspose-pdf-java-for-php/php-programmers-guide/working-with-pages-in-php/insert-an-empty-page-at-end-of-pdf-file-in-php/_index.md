---
title: أدخل صفحة فارغة في نهاية ملف PDF في PHP
linktitle: أدخل صفحة فارغة في نهاية ملف PDF في PHP
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-php/
description: تعرف على كيفية إدراج صفحة فارغة في نهاية مستند PDF في PHP باستخدام Aspose.PDF لتوسيع المستند.
lastmod: "2026-06-09"
---
## Aspose.PDF - أدخل صفحة فارغة في نهاية ملف PDF

لإدراج صفحة فارغة في نهاية مستند PDF باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء فئة **InsertEmptyPageAtEndOfFile**.

كود PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# insert a empty page in a PDF
$pdf->getPages()->add();

# Save the concatenated output file (the target document)
$pdf->save($dataDir . "output.pdf");

print "Empty page added successfully!" . PHP_EOL;

```

## تحميل كود التشغيل

قم بتنزيل **أدخل صفحة فارغة في نهاية ملف PDF (Aspose.PDF)**В fromВ أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPageAtEndOfFile.php)
