---
title: Convertir PDF a Libro de Excel en PHP
type: docs
weight: 20
url: /java/convert-pdf-to-excel-workbook-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Convertir PDF a Libro de Excel

Para convertir un documento PDF a un Libro de Excel usando **Aspose.PDF Java para PHP**, simplemente invoca el módulo **PdfToExcel**.

Código PHP

```php
# Abre el documento de destino
$pdf = new Document($dataDir . 'input1.pdf');

# Instanciar objeto de opción de guardado de Excel
$excelsave = new ExcelSaveOptions();

# Guarda la salida en formato XLS
$pdf->save($dataDir . "Converted_Excel.xls", $excelsave);

print "El documento ha sido convertido exitosamente" . PHP_EOL;

```

**Descargar Código en Ejecución**

Descarga **Convertir PDF a Libro de Excel (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToExcel.php)