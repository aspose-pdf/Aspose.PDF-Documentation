---
title: إدراج صفحة فارغة في ملف PDF باستخدام PHP
linktitle: إدراج صفحة فارغة في ملف PDF باستخدام PHP
type: docs
weight: 70
url: /ar/java/insert-an-empty-page-into-a-pdf-file-in-php/
description: تعلم كيفية إدراج صفحة فارغة في أي موضع داخل ملف PDF باستخدام PHP مع Aspose.PDF لتكوين مرن للوثائق.
lastmod: "2026-10-01"
---
## Aspose.PDF - إدراج صفحة فارغة

لإدراج صفحة فارغة في مستند Pdf باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء الفئة **InsertEmptyPage**.

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

**تحميل الكود الجاري**

تحميلВ **إدراج صفحة فارغة (Aspose.PDF)**В منВ أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPage.php)
