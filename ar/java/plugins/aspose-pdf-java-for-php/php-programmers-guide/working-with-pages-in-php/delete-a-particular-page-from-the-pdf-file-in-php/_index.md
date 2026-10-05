---
title: حذف صفحة معينة من ملف PDF في PHP
linktitle: حذف صفحة معينة من ملف PDF في PHP
type: docs
weight: 20
url: /ar/java/delete-a-particular-page-from-the-pdf-file-in-php/
description: استكشف كيفية حذف صفحة محددة من مستند PDF في PHP باستخدام Aspose.PDF، مما يبسط تحرير المستندات.
lastmod: "2026-10-05"
---
## Aspose.PDF - حذف صفحة

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

**تنزيل الشفرة القابلة للتشغيل**

تنزيل **حذف الصفحة (Aspose.PDF)** من أيٍّ من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/DeletePage.php)
