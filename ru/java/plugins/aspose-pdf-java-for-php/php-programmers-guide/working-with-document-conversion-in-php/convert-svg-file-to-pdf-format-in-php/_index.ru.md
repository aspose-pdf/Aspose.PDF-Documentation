---
title: Преобразование файла SVG в формат PDF на PHP
type: docs
weight: 40
url: /java/convert-svg-file-to-pdf-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Преобразование SVG в PDF

Чтобы преобразовать файл SVG в формат PDF с использованием **Aspose.PDF Java для PHP**, просто вызовите модуль **SvgToPdf**.

Код PHP

```php
# Создание экземпляра объекта LoadOption с использованием опции загрузки SVG
$options = new SvgLoadOptions();

# Создание объекта документа
$pdf = new Document($dataDir . 'Example.svg', $options);

# Сохраните вывод в формате XLS
$pdf->save($dataDir . "SVG.pdf");

print "Документ успешно преобразован";

```

**Скачать работающий код**

Скачайте **Преобразование SVG в PDF (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/SvgToPdf.php)