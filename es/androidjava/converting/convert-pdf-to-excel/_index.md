---
title: Convertir PDF a Excel
linktitle: Convertir PDF a Excel
type: docs
weight: 90
url: /es/androidjava/convert-pdf-to-excel/
lastmod: "2026-06-30"
description: Aspose.PDF for Android via Java le permite convertir PDF al formato Excel. Durante este proceso, las páginas individuales del archivo PDF se convierten en hojas de cálculo de Excel.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for Android via Java API le permite renderizar sus archivos PDF a Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) y [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/) formatos de archivo. Ya tenemos otra API, conocida como [Aspose.Cells for Java](https://products.aspose.com/cells/java), que proporciona la capacidad de crear y manipular libros de Excel existentes. También proporciona la capacidad de transformar libros de Excel al formato PDF.

{{% alert color="primary" %}}

Prueba en línea. Puedes comprobar la calidad de la conversión de Aspose.PDF y ver los resultados en línea en este enlace [products.aspose.app/pdf/conversion/pdf-to-xlsx](https://products.aspose.app/pdf/conversion/pdf-to-xlsx) 

{{% /alert %}}

## Convertir PDF a Excel XLS

Para convertir archivos PDF al formato XLS, Aspose.PDF tiene una clase llamada [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). Un objeto de la [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) clase se pasa como segundo argumento al constructor Document.Save(..) constructor. 

Convertir un archivo PDF al formato XLSX es parte de la biblioteca de Aspose.PDF for Java versión 18.6. Para convertir archivos PDF al formato XLSX, necesita establecer el formato como XLSX usando el método setFormat() de [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) Clase.

El siguiente fragmento de código muestra cómo convertir un archivo PDF a formato xls y .xlsx:

```java
public void convertPDFtoExcelSimple() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS document format
            document.save(xlsFileName.toString(), SaveFormat.Excel);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Convertir PDF a XLS con Columna de Control

Al convertir un PDF al formato XLS, se agrega una columna en blanco al archivo de salida como primera columna. El [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) La opción class InsertBlankColumnAtFirst se usa para controlar esta columna. Su valor predeterminado es true.

```java
public void convertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setInsertBlankColumnAtFirst(false);

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS document format
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Convertir PDF a una sola hoja de Excel 

Al exportar un archivo PDF con muchas páginas a XLS, cada página se exporta a una hoja diferente en el archivo Excel. Esto se debe a que la propiedad MinimizeTheNumberOfWorksheets está establecida en false por defecto. Para garantizar que todas las páginas se exporten a una sola hoja en el archivo Excel de salida, establezca la propiedad MinimizeTheNumberOfWorksheets en true.

```java
 public void convertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setMinimizeTheNumberOfWorksheets(true);

        // Save the output in XLSX
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS Excel format
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```

## Convertir al formato XLSX 

Por defecto, Aspose.PDF utiliza XML Spreadsheet 2003 para almacenar datos. Para convertir archivos PDF al formato XLSX, Aspose.PDF tiene una clase llamada ExcelSaveOptions con Format. Un objeto de la [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) clase se pasa como segundo argumento al método Document.Save(..).

```java
 public void convertPDFtoExcelAdvanced_SaveCSV() {
        // Load PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);

        // Save the output in CSV
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.csv");
        try {
            // Save the file into CSV format
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```
