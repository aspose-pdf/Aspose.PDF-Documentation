---
title: استخراج النص من جميع صفحات مستند PDF في PHP
type: docs
weight: 30
url: ar/java/extract-text-from-all-the-pages-of-a-pdf-document-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - استخراج النص من جميع الصفحات

لاستخراج النص من جميع صفحات مستند PDF باستخدام **Aspose.PDF Java for PHP**، ببساطة قم باستدعاء وحدة **ExtractTextFromAllPages**.
كود PHP

```php

# افتح المستند المستهدف
$pdf = new Document($dataDir . 'input1.pdf');

# إنشاء كائن TextAbsorber لاستخراج النص
$text_absorber = new TextAbsorber();

# قبول المستخلص لجميع الصفحات
$pdf->getPages()->accept($text_absorber);

# لاستخراج النص من صفحة معينة من المستند، نحتاج إلى تحديد الصفحة المعينة باستخدام فهرسها ضد طريقة accept(..).
# قبول المستخلص لصفحة PDF معينة
# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

# الحصول على النص المستخرج
$extracted_text = $text_absorber->getText();

# إنشاء كاتب وفتح الملف
$writer = new FileWriter(new File($dataDir . "extracted_text.out.txt"));
$writer->write($extracted_text);
# كتابة سطر من النص إلى الملف
# tw.WriteLine(extractedText);
# إغلاق التيار
$writer->close();

print "تم استخراج النص بنجاح. تحقق من ملف الإخراج." . PHP_EOL;

```


**تنزيل الشيفرة الجاهزة للتشغيل**

قم بتنزيل **استخراج النص من جميع الصفحات (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/ExtractTextFromAllPages.php)