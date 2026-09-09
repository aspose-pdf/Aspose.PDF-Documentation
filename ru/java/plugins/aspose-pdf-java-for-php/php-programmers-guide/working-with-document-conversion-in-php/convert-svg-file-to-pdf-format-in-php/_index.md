---
title: Конвертировать файл SVG в формат PDF в PHP
linktitle: Конвертировать файл SVG в формат PDF в PHP
type: docs
weight: 40
url: /ru/java/convert-svg-file-to-pdf-format-in-php/
description: Узнайте, как конвертировать файлы SVG в формат PDF в PHP с использованием Aspose.PDF для эффективного управления документами.
lastmod: "2026-08-19"
---
## Aspose.PDF - Конвертировать SVG в PDF

Чтобы конвертировать файл SVG в формат PDF с помощью **Aspose.PDF Java for PHP**, просто вызовите модуль **SvgToPdf**.

Код PHP

```php
# Instantiate LoadOption object using SVG load option
$options = new SvgLoadOptions();

# Create document object
$pdf = new Document($dataDir . 'Example.svg', $options);

# Save the output to XLS format
$pdf->save($dataDir . "SVG.pdf");

print "Document has been converted successfully";

```

**Загрузить исполняемый код**

СкачатьВ **Convert SVG to PDF (Aspose.PDF)**В изВ любого из ниже перечисленных сайтов для совместного кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/SvgToPdf.php)


