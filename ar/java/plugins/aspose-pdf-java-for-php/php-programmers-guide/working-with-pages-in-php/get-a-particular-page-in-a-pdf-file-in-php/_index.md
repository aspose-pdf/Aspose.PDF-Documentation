---
title: الحصول على صفحة معينة في ملف PDF باستخدام PHP
linktitle: الحصول على صفحة معينة في ملف PDF باستخدام PHP
type: docs
weight: 30
url: /ar/java/get-a-particular-page-in-a-pdf-file-in-php/
description: تعلم كيفية استرجاع صفحة معينة من ملف PDF في PHP باستخدام Aspose.PDF لمعالجة الصفحات المستهدفة.
lastmod: "2026-10-05"
---
## Aspose.PDF - الحصول على الصفحة

للحصول على صفحة معينة في مستند PDF باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء الفئة **GetPage**.

كود Ruby

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# get the page at particular index of Page Collection
$pdf_page = $pdf->getPages()->get_Item(1);

# create a new Document object
$new_document = new Document();

# add page to pages collection of new document object
$new_document->getPages()->add($pdf_page);

# save the newly generated PDF file
$new_document->save($dataDir . "output.pdf");

print "Process completed successfully!";

```

## تنزيل الكود الجاري

تحميل **Get Page (Aspose.PDF)** من أي من المواقع الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPage.php)
