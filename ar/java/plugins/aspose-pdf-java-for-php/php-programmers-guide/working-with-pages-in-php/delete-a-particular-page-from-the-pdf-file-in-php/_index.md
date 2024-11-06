---
title: حذف صفحة معينة من ملف PDF في PHP
type: docs
weight: 20
url: ar/java/delete-a-particular-page-from-the-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - حذف الصفحة

لحذف صفحة معينة من مستند PDF باستخدام **Aspose.PDF Java for PHP**، قم ببساطة باستدعاء فئة **DeletePage**.

كود PHP

```php

# افتح المستند المستهدف
$pdf = new Document($dataDir . 'input1.pdf');

# احذف صفحة معينة
$pdf->getPages()->delete(2);

# احفظ ملف PDF الذي تم إنشاؤه حديثًا
$pdf->save($dataDir . "output.pdf");

print "تم حذف الصفحة بنجاح!";

```

**تنزيل التشغيل**

قم بتنزيل **حذف الصفحة (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/DeletePage.php)