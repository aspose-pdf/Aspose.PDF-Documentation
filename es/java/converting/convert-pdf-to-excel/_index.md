---
title: Convertir PDF a Excel 
linktitle: Convertir PDF a Excel
type: docs
weight: 20
url: /es/java/convert-pdf-to-excel/
lastmod: "2021-11-19"
keywords: convertir PDF a Excel usando Java, convertir PDF a XLS usando Java, convertir PDF a XLSX usando Java, exportar tabla de PDF a Excel en Java
description: Aspose.PDF para Java te permite convertir PDF al formato Excel usando Java. Durante esto, las páginas individuales del archivo PDF se convierten en hojas de trabajo de Excel.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF para Java API te permite renderizar tus archivos PDF a formatos de archivo Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) y [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/). Ya tenemos otra API, conocida como [Aspose.Cells para Java](https://products.aspose.com/cells/java), que proporciona la capacidad de crear y manipular libros de trabajo Excel existentes. También proporciona la capacidad de transformar libros de trabajo Excel al formato PDF.

{{% alert color="primary" %}}

**Intenta convertir PDF a Excel en línea**

Aspose.PDF para Java presenta una aplicación gratuita en línea ["PDF a XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Conversión de Aspose.PDF de PDF a Excel con Aplicación Gratuita](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## Convertir PDF a Excel XLS

Para convertir archivos PDF a formato XLS, Aspose.PDF tiene una clase llamada [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). Un objeto de la clase [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) se pasa como segundo argumento al método Document.Save(..).

Convertir un archivo PDF a formato XLSX es parte de la biblioteca de Aspose.PDF para la versión Java 18.6. Para convertir archivos PDF a formato XLSX, necesita establecer el formato como XLSX usando el método setFormat() de la Clase [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions).

El siguiente fragmento de código muestra cómo convertir un archivo PDF en formato xls y .xlsx:

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPDFtoXLSX {

    private ConvertPDFtoXLSX() {

    }

    // La ruta al directorio de documentos.
    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {

        ConvertPDFtoExcelSimple();
        ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst();
        ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets();
        ConvertPDFtoExcelAdvanced_SaveXLSX();
    }

    public static void ConvertPDFtoExcelSimple() {
        // Cargar documento PDF
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // Instanciar objeto de opción de guardado de Excel
        ExcelSaveOptions excelsave = new ExcelSaveOptions();

        // Guardar la salida en formato XLS
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
}
```

## Convertir PDF a XLS con Control de Columna

Cuando se convierte un PDF a formato XLS, se añade una columna en blanco al archivo de salida como primera columna. En la clase [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions), se utiliza la opción InsertBlankColumnAtFirst para controlar esta columna. Su valor predeterminado es verdadero.

```java
    public static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // Cargar documento PDF
        Document pdfDocument = new Document(_dataDir + "input.pdf");
        // Instanciar objeto de opción de guardado de Excel
        ExcelSaveOptions excelsave = new ExcelSaveOptions();
        excelsave.setInsertBlankColumnAtFirst(false);
        // Guardar la salida en formato XLS
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
```

## Convertir PDF a una sola hoja de cálculo de Excel

Al exportar un archivo PDF con muchas páginas a XLS, cada página se exporta a una hoja diferente en el archivo de Excel.
 Esto se debe a que la propiedad MinimizeTheNumberOfWorksheets está configurada en false por defecto. Para asegurarse de que todas las páginas se exporten a una sola hoja en el archivo Excel de salida, configure la propiedad MinimizeTheNumberOfWorksheets en true.

```java
    public static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // Cargar documento PDF
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // Instanciar objeto de opción de guardado de Excel
        ExcelSaveOptions excelsave = new ExcelSaveOptions();
        excelsave.setMinimizeTheNumberOfWorksheets(true);

        // Guardar la salida en formato XLS
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
```

## Convertir a formato XLSX

Por defecto, Aspose.PDF utiliza XML Spreadsheet 2003 para almacenar datos. Para convertir archivos PDF al formato XLSX, Aspose.PDF tiene una clase llamada ExcelSaveOptions con Format. Un objeto de la clase [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) se pasa como segundo argumento al método Document.Save(..).

```java
    public static void ConvertPDFtoExcelAdvanced_SaveXLSX() {
        // Cargar documento PDF
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // Instanciar objeto de opción de guardado de Excel
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);

        // Guardar la salida en formato XLS
        pdfDocument.save("PDFToXLS_out.xlsx", excelSave);
    }
```