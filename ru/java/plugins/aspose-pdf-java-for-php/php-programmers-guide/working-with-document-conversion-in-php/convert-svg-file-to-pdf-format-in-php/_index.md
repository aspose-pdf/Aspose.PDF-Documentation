---
title: Конвертировать файл SVG в формат PDF в PHP
linktitle: Конвертировать файл SVG в формат PDF в PHP
type: docs
weight: 40
url: /java/convert-svg-file-to-pdf-format-in-php/
description: Узнайте, как конвертировать файлы SVG в формат PDF на PHP с помощью Aspose.PDF для эффективного управления документами.
lastmod: "2026-06-09"
---
## Aspose.PDF — конвертирование SVG в PDF

Чтобы преобразовать файл SVG в формат PDF с помощью **Aspose.PDF Java для PHP**, просто вызовите модуль **SvgToPdf**.

PHP-код

```php
# Instantiate LoadOption object using SVG load option
$options = new SvgLoadOptions();

# Create document object
$pdf = new Document($dataDir . 'Example.svg', $options);

# Save the output to XLS format
$pdf->save($dataDir . "SVG.pdf");

print "Document has been converted successfully";

```

**Загрузить рабочий код**

Загрузите **Конвертируйте SVG в PDF (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/SvgToPdf.php)
