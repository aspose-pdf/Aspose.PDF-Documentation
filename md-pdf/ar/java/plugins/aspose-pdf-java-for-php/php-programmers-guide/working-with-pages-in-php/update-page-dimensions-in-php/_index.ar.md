---
title: تحديث أبعاد الصفحة في PHP
type: docs
weight: 90
url: /java/update-page-dimensions-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - تحديث أبعاد الصفحة

لتحديث أبعاد الصفحة باستخدام **Aspose.PDF Java for PHP**، ببساطة قم باستدعاء فئة **UpdatePageDimensions**.

كود PHP

```php

# افتح المستند الهدف
$pdf = new Document($dataDir . 'input1.pdf');

# احصل على مجموعة الصفحات
$page_collection = $pdf->getPages();

# احصل على صفحة معينة
$pdf_page = $page_collection->get_Item(1);

# قم بتعيين حجم الصفحة كـ A4 (11.7 × 8.3 بوصة) وفي Aspose.PDF، 1 بوصة = 72 نقطة
# لذلك ستكون أبعاد A4 بالنقاط (842.4، 597.6)
$pdf_page->setPageSize(597.6,842.4);

# احفظ ملف PDF الجديد الذي تم إنشاؤه
$pdf->save($dataDir . "output.pdf");

print "تم تحديث الأبعاد بنجاح!" . PHP_EOL;

```

**تحميل الكود الجاري**

قم بتحميل **تحديث أبعاد الصفحة (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/UpdatePageDimensions.php)