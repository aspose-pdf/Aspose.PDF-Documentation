---
title: Convertir PDF a libro de Excel en PHP
linktitle: Convertir PDF a libro de Excel en PHP
type: docs
weight: 20
url: /es/java/convert-pdf-to-excel-workbook-in-php/
description: Aprenda cómo convertir archivos PDF a libros de Excel en PHP usando Aspose.PDF, lo que permite una extracción y manipulación de datos sin problemas.
lastmod: "2026-09-29"
---
## Aspose.PDF - convertir PDF a libro de Excel

Para convertir un documento PDF a libro de Excel usando **Aspose.PDF Java for PHP**, simplemente invoque el módulo **PdfToExcel**.

Código PHP

```php
# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# Instantiate ExcelSave Option object
$excelsave = new ExcelSaveOptions();

# Save the output to XLS format
$pdf->save($dataDir . "Converted_Excel.xls", $excelsave);

print "Document has been converted successfully" . PHP_EOL;

```

**Descargar Código en Ejecución**

Descargar **Convertir PDF a Libro de Excel (Aspose.PDF)** desde cualquier sitio de codificación social mencionado a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToExcel.php)
