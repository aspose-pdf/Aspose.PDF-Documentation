---
title: الحصول على عدد الصفحات من PDF في PHP
linktitle: الحصول على عدد الصفحات من PDF في PHP
type: docs
weight: 40
url: /java/get-page-count-of-pdf-in-php/
description: اكتشف كيفية استرداد إجمالي عدد الصفحات لمستند PDF في PHP باستخدام Aspose.PDF لتحليل المستندات.
lastmod: "2026-06-09"
---
## Aspose.PDF - احصل على عدد الصفحات

للحصول على عدد صفحات مستند Pdf باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء فئة **GetNumberOfPages**.

كود PHP

```php

# Create PDF document

$pdf = new Document($dataDir . 'input1.pdf');

$page_count = $pdf->getPages()->size();

print "Page Count:" . $page_count . PHP_EOL;

```

** تنزيل كود التشغيل **

تنزيلВ **احصل على عدد الصفحات (Aspose.PDF)**В fromВ من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetNumberOfPages.php)
