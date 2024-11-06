---
title: Convertir PDF a Excel 
linktitle: Convertir PDF a Excel 
type: docs
weight: 90
url: es/androidjava/convert-pdf-to-excel/
lastmod: "2021-06-05"
description: Aspose.PDF para Android a través de Java te permite convertir PDF a formato Excel. Durante esto, las páginas individuales del archivo PDF se convierten en hojas de trabajo de Excel.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF para Android a través de la API de Java te permite renderizar tus archivos PDF a formatos de archivo Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) y [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/). Ya tenemos otra API, conocida como [Aspose.Cells para Java](https://products.aspose.com/cells/java), que proporciona la capacidad de crear y manipular libros de trabajo de Excel existentes. También proporciona la capacidad de transformar libros de trabajo de Excel a formato PDF.

{{% alert color="primary" %}}

Prueba en línea.
 Puedes comprobar la calidad de la conversión de Aspose.PDF y ver los resultados en línea en este enlace [products.aspose.app/pdf/conversion/pdf-to-xlsx](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)

{{% /alert %}}

## Convertir PDF a Excel XLS

Para convertir archivos PDF a formato XLS, Aspose.PDF tiene una clase llamada [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). Un objeto de la clase [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) se pasa como segundo argumento al constructor Document.Save(..).

Convertir un archivo PDF a formato XLSX es parte de la biblioteca de Aspose.PDF para Java versión 18.6. Para convertir archivos PDF a formato XLSX, necesitas establecer el formato como XLSX utilizando el método setFormat() de la Clase [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions).

El siguiente fragmento de código muestra cómo convertir un archivo PDF a formato xls y .xlsx:

```java
public void convertPDFtoExcelSimple() {
        // Abrir el documento PDF de origen
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instanciar objeto de opción de guardado de Excel
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Guardar el archivo en formato de documento MS
            document.save(xlsFileName.toString(), SaveFormat.Excel);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Convertir PDF a XLS con Control de Columna

Al convertir un PDF al formato XLS, se agrega una columna en blanco al archivo de salida como primera columna. En la clase [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) se utiliza la opción InsertBlankColumnAtFirst para controlar esta columna. Su valor predeterminado es verdadero.

```java
public void convertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // Abrir el documento PDF de origen
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instanciar objeto de opción de guardado de Excel
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setInsertBlankColumnAtFirst(false);

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Guardar el archivo en formato de documento de MS
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## Convertir PDF a una Hoja de Cálculo de Excel Única

Al exportar un archivo PDF con muchas páginas a XLS, cada página se exporta a una hoja diferente en el archivo de Excel. Esto se debe a que la propiedad MinimizeTheNumberOfWorksheets está configurada como false por defecto. Para asegurarse de que todas las páginas se exporten a una sola hoja en el archivo de Excel de salida, configure la propiedad MinimizeTheNumberOfWorksheets a true.

```java
 public void convertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // Abrir el documento PDF fuente
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instanciar el objeto ExcelSave Option
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setMinimizeTheNumberOfWorksheets(true);

        // Guardar la salida en XLSX
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Guardar el archivo en formato MS Excel
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```


## Convertir a formato XLSX

Por defecto, Aspose.PDF usa XML Spreadsheet 2003 para almacenar datos. Para convertir archivos PDF al formato XLSX, Aspose.PDF tiene una clase llamada ExcelSaveOptions con Format. Un objeto de la clase [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) se pasa como segundo argumento al método Document.Save(..).

```java
 public void convertPDFtoExcelAdvanced_SaveCSV() {
        // Cargar documento PDF
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instanciar el objeto de opción de guardado de Excel
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);

        // Guardar la salida en CSV
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.csv");
        try {
            // Guardar el archivo en formato CSV
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```