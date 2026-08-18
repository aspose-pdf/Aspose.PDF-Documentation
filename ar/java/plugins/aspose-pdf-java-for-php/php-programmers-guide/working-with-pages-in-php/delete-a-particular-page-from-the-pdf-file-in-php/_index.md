---
title: حذف صفحة معينة من ملف PDF في PHP
linktitle: حذف صفحة معينة من ملف PDF في PHP
type: docs
weight: 20
url: /java/delete-a-particular-page-from-the-pdf-file-in-php/
description: اكتشف كيفية حذف صفحة معينة من مستند PDF في PHP باستخدام Aspose.PDF، مما يبسط عملية تحرير المستند.
lastmod: "2026-06-09"
---
## Aspose.PDF - حذف الصفحة

لحذف صفحة معينة من مستند PDF باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء فئة **DeletePage**.

كود PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# delete a particular page
$pdf->getPages()->delete(2);

# save the newly generated PDF file
$pdf->save($dataDir . "output.pdf");

print "Page deleted successfully!";

```

**تحميل جاري**

قم بتنزيل **حذف الصفحة (Aspose.PDF)**В من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/DeletePage.php)
