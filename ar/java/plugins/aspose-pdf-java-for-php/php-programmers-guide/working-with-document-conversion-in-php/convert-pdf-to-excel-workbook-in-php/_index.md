---
title: تحويل PDF إلى Excel Workbook في PHP
type: docs
weight: 20
url: /ar/java/convert-pdf-to-excel-workbook-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - تحويل PDF إلى Excel Workbook

لتحويل مستند PDF إلى Excel Workbook باستخدام **Aspose.PDF Java for PHP**، ببساطة قم باستدعاء وحدة **PdfToExcel**.

كود PHP

```php
# افتح المستند المستهدف
$pdf = new Document($dataDir . 'input1.pdf');

# إنشاء كائن ExcelSave Option
$excelsave = new ExcelSaveOptions();

# احفظ الناتج بتنسيق XLS
$pdf->save($dataDir . "Converted_Excel.xls", $excelsave);

print "تم تحويل المستند بنجاح" . PHP_EOL;

```

**تحميل الكود الجاهز للتشغيل**

قم بتحميل **تحويل PDF إلى Excel Workbook (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToExcel.php)