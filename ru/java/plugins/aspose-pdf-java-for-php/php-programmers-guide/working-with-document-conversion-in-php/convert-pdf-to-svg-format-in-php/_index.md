---
title: Преобразование PDF в SVG формат на PHP
type: docs
weight: 30
url: /ru/java/convert-pdf-to-svg-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Преобразование PDF в SVG

Чтобы преобразовать PDF в формат SVG с использованием **Aspose.PDF Java for PHP**, просто вызовите модуль **PdfToSvg**.

PHP Код

```php

# Открыть целевой документ
$pdf = new Document($dataDir . 'input1.pdf');

# создать объект SvgSaveOptions
$save_options = new SvgSaveOptions();

# не сжимать SVG изображение в Zip архив
$save_options->CompressOutputToZipArchive = false;

# Сохранить результат в формате XLS
$pdf->save($dataDir . "Output.svg", $save_options);

print "Документ был успешно преобразован" . PHP_EOL;

```

**Скачать Запускаемый Код**

Скачайте **Преобразование PDF в SVG формат (Aspose.PDF)** с любого из нижеупомянутых социальных кодинг сайтов:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToSvg.php)