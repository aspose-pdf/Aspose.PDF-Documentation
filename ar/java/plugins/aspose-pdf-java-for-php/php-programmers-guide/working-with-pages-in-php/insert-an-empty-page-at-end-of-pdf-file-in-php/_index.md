---
title: إدراج صفحة فارغة في نهاية ملف PDF باستخدام PHP
linktitle: إدراج صفحة فارغة في نهاية ملف PDF باستخدام PHP
type: docs
weight: 60
url: /ar/java/insert-an-empty-page-at-end-of-pdf-file-in-php/
description: تعلم كيفية إدراج صفحة فارغة في نهاية مستند PDF باستخدام PHP و Aspose.PDF لتوسيع المستند.
lastmod: "2026-10-01"
---
## Aspose.PDF - إدراج صفحة فارغة في نهاية ملف PDF

لإدراج صفحة فارغة في نهاية مستند PDF باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء الفئة **InsertEmptyPageAtEndOfFile**.

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

## تنزيل الكود الجاري

تنزيل **إدراج صفحة فارغة في نهاية ملف PDF (Aspose.PDF)** من أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPageAtEndOfFile.php)
