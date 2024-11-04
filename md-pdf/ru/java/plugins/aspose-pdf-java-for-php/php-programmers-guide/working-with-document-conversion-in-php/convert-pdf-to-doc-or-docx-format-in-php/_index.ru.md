---
title: Преобразование PDF в формат DOC или DOCX с помощью PHP
type: docs
weight: 10
url: /java/convert-pdf-to-doc-or-docx-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Преобразование PDF в DOC или DOCX

Чтобы преобразовать PDF-документ в формат DOC или DOCX с использованием **Aspose.PDF Java for PHP**, просто вызовите модуль **PdfToDoc**.

PHP Код

```php

# Открыть целевой документ
$pdf = new Document($dataDir . 'input1.pdf');

# Сохранить объединенный выходной файл (целевой документ)
$pdf->save($dataDir . "output.doc");

print "Документ был успешно преобразован";

```

**Скачать работающий код**

Скачайте **Convert PDF to DOC or DOCX (Aspose.PDF)** с любого из указанных ниже социальных сайтов кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToDoc.php)