---
title: احصل على عدد صفحات PDF في PHP
type: docs
weight: 40
url: ar/java/get-page-count-of-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - احصل على عدد الصفحات

للحصول على عدد صفحات وثيقة Pdf باستخدام **Aspose.PDF Java for PHP**، قم ببساطة باستدعاء فئة **GetNumberOfPages**.

كود PHP

```php

# إنشاء وثيقة PDF

$pdf = new Document($dataDir . 'input1.pdf');

$page_count = $pdf->getPages()->size();

print "عدد الصفحات:" . $page_count . PHP_EOL;

```

**تحميل الكود التشغيلي**

قم بتحميل **احصل على عدد الصفحات (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetNumberOfPages.php)