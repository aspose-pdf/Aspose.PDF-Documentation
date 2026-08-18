---
title: Конвертировать PDF в книгу Excel на PHP
linktitle: Конвертировать PDF в книгу Excel на PHP
type: docs
weight: 20
url: /java/convert-pdf-to-excel-workbook-in-php/
description: Узнайте, как конвертировать PDF-файлы в книги Excel на PHP с помощью Aspose.PDF, обеспечивая беспрепятственное извлечение данных и манипулирование ими.
lastmod: "2026-06-09"
---
## Aspose.PDF — конвертирование PDF в книгу Excel

Чтобы преобразовать PDF-документ в книгу Excel с помощью **Aspose.PDF Java для PHP**, просто вызовите модуль **PdfToExcel**.

PHP-код

```php
# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# Instantiate ExcelSave Option object
$excelsave = new ExcelSaveOptions();

# Save the output to XLS format
$pdf->save($dataDir . "Converted_Excel.xls", $excelsave);

print "Document has been converted successfully" . PHP_EOL;

```

**Загрузить рабочий код**

Загрузите **Конвертировать PDF в книгу Excel (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToExcel.php)
