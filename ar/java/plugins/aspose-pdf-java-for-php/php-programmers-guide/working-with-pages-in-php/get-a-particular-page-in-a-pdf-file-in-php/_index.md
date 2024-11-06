---
title: احصل على صفحة معينة في ملف PDF باستخدام PHP
type: docs
weight: 30
url: ar/java/get-a-particular-page-in-a-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - الحصول على الصفحة

للحصول على صفحة معينة في مستند PDF باستخدام **Aspose.PDF Java for Ruby**، ببساطة قم باستدعاء فئة **GetPage**.

كود روبي

```php

# افتح المستند المستهدف
$pdf = new Document($dataDir . 'input1.pdf');

# الحصول على الصفحة عند فهرس معين من مجموعة الصفحات
$pdf_page = $pdf->getPages()->get_Item(1);

# إنشاء كائن مستند جديد
$new_document = new Document();

# إضافة الصفحة إلى مجموعة الصفحات الخاصة بكائن المستند الجديد
$new_document->getPages()->add($pdf_page);

# حفظ ملف PDF المُنشى حديثًا
$new_document->save($dataDir . "output.pdf");

print "تم إكمال العملية بنجاح!";

```

## تحميل الكود الجاري

قم بتحميل **احصل على الصفحة (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPage.php)