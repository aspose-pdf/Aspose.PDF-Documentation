---
title: Convertir PDF a Microsoft Excel 
linktitle: Convertir PDF a Excel
type: docs
weight: 20
url: es/php-java/convert-pdf-to-excel/
lastmod: "2024-05-20"
keywords: convertir PDF a Excel usando PHP, convertir PDF a XLS usando PHP, convertir PDF a XLSX usando PHP, exportar tabla de PDF a Excel en PHP.
description: Aspose.PDF para PHP te permite convertir PDF a formato Excel usando PHP. Durante esto, las páginas individuales del archivo PDF se convierten en hojas de cálculo de Excel.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF para PHP API te permite renderizar tus archivos PDF a formatos de archivo Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) y [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/). Ya tenemos otra API, conocida como [Aspose.Cells para PHP vía Java](https://products.aspose.com/cells/php-java), que proporciona la capacidad de crear y manipular libros de Excel existentes. También proporciona la capacidad de transformar libros de Excel a formato PDF.

{{% alert color="primary" %}}

**Intenta convertir PDF a Excel en línea**

Aspose.PDF para PHP presenta una aplicación gratuita en línea ["PDF a XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Conversión de PDF a Excel con App Gratuita de Aspose.PDF](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## Convertir PDF a Excel XLS

Para convertir archivos PDF a formato XLS, Aspose.PDF tiene una clase llamada [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). Un objeto de la clase [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) se pasa como segundo argumento al método Document.Save(..).

La conversión de un archivo PDF a formato XLSX es parte de la biblioteca de Aspose.PDF para PHP versión 18.6. Para convertir archivos PDF a formato XLSX, necesitas establecer el formato como XLSX usando el método setFormat() de la Clase [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions).

Los siguientes fragmentos de código muestran cómo convertir un archivo PDF a formato XLS y XLSX:

```php
// Cargar el documento PDF de entrada utilizando la clase Document.
$document = new Document($inputFile);

// Crear una instancia de la clase ExcelSaveOptions para especificar las opciones de guardado.
$saveOption = new ExcelSaveOptions();

// Establecer el formato de salida a XLS.
// $saveOption->setFormat(ExcelSaveOptions_ExcelFormat::$XMLSpreadSheet2003);

// Establecer el formato de salida a XLSX.
    $excelSaveOptions_ExcelFormat = new ExcelSaveOptions_ExcelFormat();
    $saveOption->setFormat($excelSaveOptions_ExcelFormat->XLSX);

// Guardar el documento PDF como un archivo de Excel utilizando las opciones de guardado especificadas.
$document->save($outputFile, $saveOption);
```