---
title: تحويل PDF إلى Excel Workbook في PHP
linktitle: تحويل PDF إلى Excel Workbook في PHP
type: docs
weight: 20
url: /java/convert-pdf-to-excel-workbook-in-php/
description: تعرف على كيفية تحويل ملفات PDF إلى مصنفات Excel في PHP باستخدام Aspose.PDF، مما يتيح استخراج البيانات ومعالجتها بسلاسة.
lastmod: "2026-06-09"
---
## Aspose.PDF - تحويل PDF إلى مصنف Excel

لتحويل مستند PDF إلى Excel Workbook باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء وحدة **PdfToExcel**.

كود PHP

```php
# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# Instantiate ExcelSave Option object
$excelsave = new ExcelSaveOptions();

# Save the output to XLS format
$pdf->save($dataDir . "Converted_Excel.xls", $excelsave);

print "Document has been converted successfully" . PHP_EOL;

```

** تنزيل كود التشغيل **

تنزيل ** تحويل PDF إلى Excel Workbook (Aspose.PDF) ** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToExcel.php)
