---
title: Конвертировать PDF в книгу Excel в PHP
linktitle: Конвертировать PDF в книгу Excel в PHP
type: docs
weight: 20
url: /ru/java/convert-pdf-to-excel-workbook-in-php/
description: Узнайте, как конвертировать файлы PDF в книги Excel в PHP с помощью Aspose.PDF, обеспечивая бесшовное извлечение и обработку данных.
lastmod: "2026-08-19"
---
## Aspose.PDF - Конвертировать PDF в книгу Excel

Чтобы конвертировать документ PDF в книгу Excel, используя **Aspose.PDF Java for PHP**, просто вызовите модуль **PdfToExcel**.

Код PHP

```php
# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# Instantiate ExcelSave Option object
$excelsave = new ExcelSaveOptions();

# Save the output to XLS format
$pdf->save($dataDir . "Converted_Excel.xls", $excelsave);

print "Document has been converted successfully" . PHP_EOL;

```

**Скачать исполняемый код**

СкачатьВ **Convert PDF to Excel Workbook (Aspose.PDF)**В изВ любой из нижеупомянутых сайтов совместного кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToExcel.php)


