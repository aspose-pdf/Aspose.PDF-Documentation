---
title: Конвертировать PDF в формат SVG в PHP
linktitle: Конвертировать PDF в формат SVG в PHP
type: docs
weight: 30
url: /ru/java/convert-pdf-to-svg-format-in-php/
description: Узнайте, как конвертировать PDF‑документы в формат SVG в PHP с помощью Aspose.PDF для высококачественного преобразования векторной графики.
lastmod: "2026-08-19"
---
## Aspose.PDF - Конвертировать PDF в SVG

Чтобы конвертировать PDF в формат SVG, используя **Aspose.PDF Java for PHP**, просто вызовите модуль **PdfToSvg**.

Код PHP

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

**Скачать исполняемый код**

Скачать **Convert PDF to SVG Format (Aspose.PDF)** с любого из указанных ниже сайтов для совместного кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToSvg.php)

