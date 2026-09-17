---
title: Конвертация PDF в формат DOC или DOCX с помощью PHP
linktitle: Конвертация PDF в формат DOC или DOCX с помощью PHP
type: docs
weight: 10
url: /ru/java/convert-pdf-to-doc-or-docx-format-in-php/
description: Узнайте, как конвертировать PDF‑документы в форматы DOC или DOCX в PHP с использованием Aspose.PDF для более удобного редактирования документов.
lastmod: "2026-09-17"
---
## Aspose.PDF — Конвертация PDF в DOC или DOCX

Чтобы конвертировать PDF‑документ в формат DOC или DOCX с использованием **Aspose.PDF Java for PHP**, просто вызовите модуль **PdfToDoc**.

Код PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# Save the concatenated output file (the target document)
$pdf->save($dataDir . "output.doc");

print "Document has been converted successfully";

```

**Скачать исполняемый код**

Скачайте **Convert PDF to DOC or DOCX (Aspose.PDF)** с любого из перечисленных ниже сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToDoc.php)


