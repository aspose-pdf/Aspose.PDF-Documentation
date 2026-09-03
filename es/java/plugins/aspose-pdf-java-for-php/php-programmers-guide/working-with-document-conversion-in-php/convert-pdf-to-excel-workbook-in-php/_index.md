---
title: Convertir PDF a Libro de Excel en PHP
linktitle: Convertir PDF a Libro de Excel en PHP
type: docs
weight: 20
url: /es/java/convert-pdf-to-excel-workbook-in-php/
description: Aprende cómo convertir archivos PDF a libros de Excel en PHP usando Aspose.PDF, permitiendo una extracción y manipulación de datos sin problemas.
lastmod: "2026-09-03"
---
## Aspose.PDF - Convertir PDF a Libro de Excel

Para convertir un documento PDF a Libro de Excel usando **Aspose.PDF Java for PHP**, simplemente invoque el módulo **PdfToExcel**.

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

**Descargar código en ejecución**

Download\u0412\u00A0**Convertir PDF a libro de Excel (Aspose.PDF)**\u0412\u00A0de\u0412\u00A0cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToExcel.php)
