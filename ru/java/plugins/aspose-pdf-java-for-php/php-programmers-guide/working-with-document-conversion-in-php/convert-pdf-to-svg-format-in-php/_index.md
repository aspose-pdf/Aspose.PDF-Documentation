---
title: Конвертировать PDF в формат SVG в PHP
linktitle: Конвертировать PDF в формат SVG в PHP
type: docs
weight: 30
url: /java/convert-pdf-to-svg-format-in-php/
description: Узнайте, как конвертировать PDF-документы в формат SVG на PHP с помощью Aspose.PDF для высококачественного преобразования векторной графики.
lastmod: "2026-06-09"
---
## Aspose.PDF — конвертирование PDF в SVG

Чтобы преобразовать PDF в формат SVG с помощью **Aspose.PDF Java для PHP**, просто вызовите модуль **PdfToSvg**.

PHP-код

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# instantiate an object of SvgSaveOptions
$save_options = new SvgSaveOptions();

# do not compress SVG image to Zip archive
$save_options->CompressOutputToZipArchive = false;

# Save the output to XLS format
$pdf->save($dataDir . "Output.svg", $save_options);

print "Document has been converted successfully" . PHP_EOL;

```

**Загрузить рабочий код**

Загрузите **Конвертируйте PDF в формат SVG (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToSvg.php)
