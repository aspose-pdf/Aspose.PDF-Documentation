---
title: Конвертировать PDF в Excel Workbook на PHP
type: docs
weight: 20
url: ru/java/convert-pdf-to-excel-workbook-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Конвертировать PDF в Excel Workbook

Чтобы конвертировать PDF-документ в Excel Workbook с использованием **Aspose.PDF Java for PHP**, просто вызовите модуль **PdfToExcel**.

Код PHP

```php
# Открыть целевой документ
$pdf = new Document($dataDir . 'input1.pdf');

# Создать объект ExcelSave Option
$excelsave = new ExcelSaveOptions();

# Сохранить результат в формате XLS
$pdf->save($dataDir . "Converted_Excel.xls", $excelsave);

print "Документ был успешно конвертирован" . PHP_EOL;

```

**Скачать исполняемый код**

Скачайте **Конвертировать PDF в Excel Workbook (Aspose.PDF)** с любого из указанных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToExcel.php)