---
title: تحويل PDF إلى دفتر عمل Excel في PHP
linktitle: تحويل PDF إلى دفتر عمل Excel في PHP
type: docs
weight: 20
url: /ar/java/convert-pdf-to-excel-workbook-in-php/
description: تعلم كيفية تحويل ملفات PDF إلى دفاتر عمل Excel في PHP باستخدام Aspose.PDF، مما يتيح استخراج البيانات ومعالجتها بسلاسة.
lastmod: "2026-10-01"
---
## Aspose.PDF - تحويل PDF إلى دفتر عمل Excel

لتحويل مستند PDF إلى دفتر عمل Excel باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء وحدة **PdfToExcel**.

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

**تحميل تشغيل الشيفرة**

تحميل **تحويل PDF إلى مصنف Excel (Aspose.PDF)** من أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToExcel.php)
