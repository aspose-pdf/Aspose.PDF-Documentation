---
title: تحديث أبعاد الصفحة في PHP
linktitle: تحديث أبعاد الصفحة في PHP
type: docs
weight: 90
url: /ar/java/update-page-dimensions-in-php/
description: تعلم كيفية تعديل أبعاد الصفحة داخل مستند PDF في PHP باستخدام Aspose.PDF للحصول على تحكم أفضل في التخطيط.
lastmod: "2026-10-01"
---
## Aspose.PDF - تحديث أبعاد الصفحة

لتحديث أبعاد الصفحة باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء الفئة **UpdatePageDimensions**.

كود PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# get page collection
$page_collection = $pdf->getPages();

# get particular page
$pdf_page = $page_collection->get_Item(1);

# set the page size as A4 (11.7 x 8.3 in) and in Aspose.PDF, 1 inch = 72 points
# so A4 dimensions in points will be (842.4, 597.6)
$pdf_page->setPageSize(597.6,842.4);

# save the newly generated PDF file
$pdf->save($dataDir . "output.pdf");

print "Dimensions updated successfully!" . PHP_EOL;

```

**تحميل الكود الجاري**

تحميلВ **Update Page Dimensions (Aspose.PDF)**В منВ أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/UpdatePageDimensions.php)
