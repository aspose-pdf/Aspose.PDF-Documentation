---
title: Convertir PDF a Excel en .NET
linktitle: Convertir PDF a Excel
type: docs
weight: 20
url: es/net/convert-pdf-to-excel/
lastmod: "2021-11-01"
keywords: convertir PDF a Excel usando c#, convertir PDF a XLS usando csharp, convertir PDF a XLSX usando csharp, exportar tabla desde PDF a Excel en csharp.
description: La biblioteca Aspose.PDF para .NET te permite convertir PDF a formato Excel usando C#. Estos formatos incluyen XLS, XLSX, Hoja de cálculo XML 2003, CSV, ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Descripción general

Este artículo explica cómo **convertir formatos PDF a Excel usando C#**. Cubre los siguientes temas.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

_Formato_: **XLS**

- [C# PDF a XLS](#csharp-pdf-to-xls)
- [C# Convertir PDF a XLS](#csharp-pdf-to-xls)
- [C# Cómo convertir un archivo PDF a XLS](#csharp-pdf-to-xls)

_Formato_: **XLSX**

- [C# PDF a XLSX](#csharp-pdf-to-xlsx)
- [C# Convertir PDF a XLSX](#csharp-pdf-to-xlsx)
- [C# Cómo convertir un archivo PDF a XLSX](#csharp-pdf-to-xlsx)
- [C# Cómo convertir un archivo PDF a XLSX](#csharp-pdf-to-xlsx)

_Formato_: **Excel**

- [C# PDF a Excel](#csharp-pdf-to-xlsx)
- [C# PDF a Excel XLS](#csharp-pdf-to-xls)
- [C# PDF a Excel XLSX](#csharp-pdf-to-xlsx)

_Formato_: **Una sola hoja de Excel**

- [C# Convertir PDF a XLS con una sola hoja](#csharp-pdf-to-excel-single)
- [C# Convertir PDF a XLSX con una sola hoja](#csharp-pdf-to-excel-single)

_Formato_: **Formato de hoja de cálculo XML 2003**

- [C# PDF a Excel XML](#csharp-pdf-to-excel-xml-2003)
- [C# Convertir PDF a hoja de cálculo XML Excel](#csharp-pdf-to-excel-xml-2003)

_Formato_: **CSV**

- [C# PDF a CSV](#csharp-pdf-to-csv)
- [C# Convertir PDF a CSV](#csharp-pdf-to-csv)
- [C# Cómo convertir un archivo PDF a CSV](#csharp-pdf-to-csv)

_Formato_: **ODS**

- [C# PDF a ODS](#csharp-pdf-to-ods)
- [C# Convertir PDF a ODS](#csharp-pdf-to-ods)
- [C# Cómo convertir un archivo PDF a ODS](#csharp-pdf-to-ods)

## Conversiones de PDF a Excel en C#

**Aspose.PDF for .NET** soporta la característica de convertir archivos PDF a formatos Excel 2007, CSV y SpeadsheetML.
**Aspose.PDF para .NET** admite la función de convertir archivos PDF a formatos Excel 2007, CSV y SpeadsheetML.

Aspose.PDF para .NET es un componente de manipulación de PDF, hemos introducido una función que renderiza archivos PDF a libros de trabajo de Excel (archivos XLSX). Durante esta conversión, las páginas individuales del archivo PDF se convierten en hojas de cálculo de Excel.

{{% alert color="success" %}}
**Intenta convertir PDF a Excel en línea**

Aspose.PDF para .NET te presenta una aplicación gratuita en línea ["PDF a XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), donde puedes intentar investigar la funcionalidad y calidad con la que funciona.

[![Conversión de Aspose.PDF de PDF a Excel con Aplicación Gratuita](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

Para convertir archivos PDF al formato <abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr>, Aspose.PDF tiene una clase llamada [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions).
Para convertir archivos PDF al formato <abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr>, Aspose.PDF tiene una clase llamada [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions).

El siguiente fragmento de código muestra el proceso para convertir un archivo PDF en formato XLS o XLSX con Aspose.PDF para .NET.

<a name="csharp-pdf-to-xls"><strong>Pasos: Convertir PDF a XLS en C#</strong></a>

1. Crear una instancia del objeto **Document** con el documento PDF fuente.
2. Crear una instancia de **ExcelSaveOptions**.
3. Guardarlo en formato **XLS** especificando **extensión .xls** al llamar al método **Document.Save()** y pasándole **ExcelSaveOptions**

<a name="csharp-pdf-to-xlsx"><strong>Pasos: Convertir PDF a XLSX en C#</strong></a>

1. Crear una instancia del objeto **Document** con el documento PDF fuente.
2. Crear una instancia de **ExcelSaveOptions**.
3. Guardarlo en formato **XLSX** especificando **extensión .xlsx** al llamar al método **Document.Save()** y pasándole **ExcelSaveOptions**

```csharp
```
```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Cargar documento PDF
Document pdfDocument = new Document(dataDir + "input.pdf");

// Instanciar objeto de opción de guardado Excel
Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions();

// Guardar el resultado en formato XLS
pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
```

## Convertir PDF a XLS con Control de Columna

Al convertir un PDF a formato XLS, se añade una columna en blanco al archivo de salida como primera columna. La opción `InsertBlankColumnAtFirst` de la clase ExcelSaveOptions se utiliza para controlar esta columna. El valor predeterminado es `false`, lo que significa que no se insertarán columnas en blanco.

```csharp
public static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst()
{
    // Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    // Cargar documento PDF
    Document pdfDocument = new Document(_dataDir + "input.pdf");
    // Instanciar objeto de opción de guardado Excel
    Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions {InsertBlankColumnAtFirst = false};
    // Guardar el resultado en formato XLS
    pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
}
```
## Convertir PDF a una única hoja de cálculo de Excel

Al exportar un archivo PDF con muchas páginas a XLS, cada página se exporta a una hoja diferente en el archivo Excel. Esto se debe a que la propiedad MinimizeTheNumberOfWorksheets está configurada en false por defecto. Para asegurarse de que todas las páginas se exporten a una sola hoja en el archivo Excel de salida, configure la propiedad MinimizeTheNumberOfWorksheets en true.

<a name="csharp-pdf-to-excel-single"><strong>Pasos: Convertir PDF a XLS o XLSX en una sola hoja de cálculo en C#</strong></a>

1. Crear una instancia del objeto **Document** con el documento PDF fuente.
2. Crear una instancia de **ExcelSaveOptions** con **MinimizeTheNumberOfWorksheets = true**.
3. Guardarlo en formato **XLS** o **XLSX** teniendo una sola hoja de cálculo al llamar al método **Document.Save()** y pasándole **ExcelSaveOptions**.

```csharp
public static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets()
{
    // Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    // Cargar documento PDF
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // Instanciar objeto de opciones de guardado de Excel
    Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions {MinimizeTheNumberOfWorksheets = true};
    // Guardar la salida en formato XLS
    pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
}
```
## Convertir a otros formatos de hojas de cálculo

### Convertir al formato XML Spreadsheet 2003

Desde la versión 20.8 Aspose.PDF utiliza el formato de archivo Microsoft Excel Open XML Spreadsheet 2007 como predeterminado para almacenar datos. Para convertir archivos PDF al formato XML Spreadsheet 2003, Aspose.PDF tiene una clase llamada [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions) con [Format](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions/properties/format). Un objeto de la clase [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions) se pasa como segundo argumento al método [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index).

El siguiente fragmento de código muestra el proceso para convertir un archivo PDF al formato XLS Excel 2003 XML.

<a name="csharp-pdf-to-excel-xml-2003"><strong>Pasos: Convertir PDF a formato Excel 2003 XML en C#</strong></a>

1. Crear una instancia del objeto **Document** con el documento PDF fuente.
2.
2.
3. Guárdelo en formato **XLS - Excel 2003 XML Format** llamando al método **Document.Save()** y pasando **ExcelSaveOptions**.

```csharp
public static void ConvertPDFtoExcelAdvanced_SaveXLS2003()
{
    // Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET

    // Cargar documento PDF
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // Instanciar objeto de opciones de guardado de Excel
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003 };

    // Guardar la salida en formato XLS
    pdfDocument.Save("PDFToXLS_out.xls", excelSave);
}
```

### Convertir a CSV

La conversión a formato CSV se realiza de la misma manera que arriba. Todo lo que necesita es establecer el formato apropiado.

<a name="csharp-pdf-to-csv"><strong>Pasos: Convertir PDF a CSV en C#</strong></a>

1. Cree una instancia del objeto **Document** con el documento PDF fuente.
2.
2.
3. Guárdelo en formato **CSV** llamando al método **Document.Save()** y pasando **ExcelSaveOptions**.

```csharp
 // Instanciar objeto ExcelSave Options
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.CSV };
```

### Convertir a ODS

<a name="csharp-pdf-to-ods"><strong>Pasos: Convertir PDF a ODS en C#</strong></a>

1. Cree una instancia del objeto **Document** con el documento PDF fuente.
2. Cree una instancia de **ExcelSaveOptions** con **Format = ExcelSaveOptions.ExcelFormat.ODS**
3. Guárdelo en formato **ODS** llamando al método **Document.Save()** y pasando **ExcelSaveOptions**.

La conversión al formato ODS se realiza de la misma manera que todos los otros formatos.

```csharp
 // Instanciar objeto ExcelSave Options
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.ODS };
```

## Ver también

Este artículo también cubre estos temas. Los códigos son los mismos que arriba.

_Format_: **Excel**
- [Código de C# PDF a Excel](#csharp-pdf-to-xlsx)
- [API de C# PDF a Excel](#csharp-pdf-to-xlsx)
- [API de C# PDF a Excel](#csharp-pdf-to-xlsx)
- [C# PDF a Excel Programáticamente](#csharp-pdf-to-xlsx)
- [Biblioteca de C# PDF a Excel](#csharp-pdf-to-xlsx)
- [C# Guardar PDF como Excel](#csharp-pdf-to-xlsx)
- [C# Generar Excel desde PDF](#csharp-pdf-to-xlsx)
- [C# Crear Excel desde PDF](#csharp-pdf-to-xlsx)
- [Convertidor de C# PDF a Excel](#csharp-pdf-to-xlsx)

_Formato_: **XLS**
- [Código de C# PDF a XLS](#csharp-pdf-to-xls)
- [API de C# PDF a XLS](#csharp-pdf-to-xls)
- [C# PDF a XLS Programáticamente](#csharp-pdf-to-xls)
- [Biblioteca de C# PDF a XLS](#csharp-pdf-to-xls)
- [C# Guardar PDF como XLS](#csharp-pdf-to-xls)
- [C# Generar XLS desde PDF](#csharp-pdf-to-xls)
- [C# Crear XLS desde PDF](#csharp-pdf-to-xls)
- [Convertidor de C# PDF a XLS](#csharp-pdf-to-xls)

_Formato_: **XLSX**
- [Código de C# PDF a XLSX](#csharp-pdf-to-xlsx)
- [API de C# PDF a XLSX](#csharp-pdf-to-xlsx)
- [C# PDF a XLSX Programáticamente](#csharp-pdf-to-xlsx)
- [Biblioteca de C# PDF a XLSX](#csharp-pdf-to-xlsx)
- [C# Guardar PDF como XLSX](#csharp-pdf-to-xlsx)
- [C# Generar XLSX desde PDF](#csharp-pdf-to-xlsx)
- [C# Generar XLSX desde PDF](#csharp-pdf-to-xlsx)
- [C# Crear XLSX desde PDF](#csharp-pdf-to-xlsx)
- [C# Convertidor de PDF a XLSX](#csharp-pdf-to-xlsx)

_Formato_: **CSV**
- [C# Código PDF a CSV](#csharp-pdf-to-csv)
- [C# API PDF a CSV](#csharp-pdf-to-csv)
- [C# PDF a CSV Programáticamente](#csharp-pdf-to-csv)
- [C# Biblioteca PDF a CSV](#csharp-pdf-to-csv)
- [C# Guardar PDF como CSV](#csharp-pdf-to-csv)
- [C# Generar CSV desde PDF](#csharp-pdf-to-csv)
- [C# Crear CSV desde PDF](#csharp-pdf-to-csv)
- [C# Convertidor de PDF a CSV](#csharp-pdf-to-csv)

_Formato_: **ODS**
- [C# Código PDF a ODS](#csharp-pdf-to-ods)
- [C# API PDF a ODS](#csharp-pdf-to-ods)
- [C# PDF a ODS Programáticamente](#csharp-pdf-to-ods)
- [C# Biblioteca PDF a ODS](#csharp-pdf-to-ods)
- [C# Guardar PDF como ODS](#csharp-pdf-to-ods)
- [C# Generar ODS desde PDF](#csharp-pdf-to-ods)
- [C# Crear ODS desde PDF](#csharp-pdf-to-ods)
- [C# Convertidor de PDF a ODS](#csharp-pdf-to-ods)
