---
title: احصل على عدد صفحات PDF في PHP
linktitle: احصل على عدد صفحات PDF في PHP
type: docs
weight: 40
url: /ar/java/get-page-count-of-pdf-in-php/
description: اكتشف كيفية استرداد العدد الكلي لصفحات مستند PDF في PHP باستخدام Aspose.PDF لتحليل المستندات.
lastmod: "2026-10-01"
---
## Aspose.PDF - الحصول على عدد الصفحات

للحصول على عدد صفحات مستند Pdf باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء فئة **GetNumberOfPages**.

كود PHP

```php

# Create PDF document

$pdf = new Document($dataDir . 'input1.pdf');

$page_count = $pdf->getPages()->size();

print "Page Count:" . $page_count . PHP_EOL;

```

**تحميل الكود القائم**

DownloadВ **احصل على عدد الصفحات (Aspose.PDF)**В منВ أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetNumberOfPages.php)
