---
title: Convert PDF to Excel in .NET
linktitle: Convert PDF to Excel
type: docs
weight: 20
url: /net/convert-pdf-to-excel/
lastmod: "2021-11-01"
keywords: convert PDF to Excel using c#, convert PDF to XLS using csharp, convert PDF to XLSX using csharp, export table from PDF to Excel in csharp.
description: Aspose.PDF for .NET library allows you to convert PDF to Excel format using C#. These formats include XLS, XLSX, XML 2003 Spreadsheet, CSV, ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Overview

This article explains how to **convert PDF to Excel formats using C#**. It covers the following topics.

_Format_: **XLS**
- [C# PDF to XLS](#csharp-pdf-to-xls)
- [C# Convert PDF to XLS](#csharp-pdf-to-xls)
- [C# How to convert PDF file to XLS](#csharp-pdf-to-xls)

_Format_: **XLSX**
- [C# PDF to XLSX](#csharp-pdf-to-xlsx)
- [C# Convert PDF to XLSX](#csharp-pdf-to-xlsx)
- [C# How to convert PDF file to XLSX](#csharp-pdf-to-xlsx)

_Format_: **Excel**
- [C# PDF to Excel](#csharp-pdf-to-xlsx)
- [C# PDF to Excel XLS](#csharp-pdf-to-xls)
- [C# PDF to Excel XLSX](#csharp-pdf-to-xlsx)

_Format_: **Single Excel Worksheet**
- [C# Convert PDF to XLS having Single Worksheet](#csharp-pdf-to-excel-single)
- [C# Convert PDF to XLSX having Single Worksheet](#csharp-pdf-to-excel-single)

_Format_: **XML Spreadsheet 2003 format**
- [C# PDF to XML Excel](#csharp-pdf-to-excel-xml-2003)
- [C# Convert PDF to XML Excel Spreadsheet](#csharp-pdf-to-excel-xml-2003)

_Format_: **CSV**
- [C# PDF to CSV](#csharp-pdf-to-csv)
- [C# Convert PDF to CSV](#csharp-pdf-to-csv)
- [C# How to convert PDF file to CSV](#csharp-pdf-to-csv)

_Format_: **ODS**
- [C# PDF to ODS](#csharp-pdf-to-ods)
- [C# Convert PDF to ODS](#csharp-pdf-to-ods)
- [C# How to convert PDF file to ODS](#csharp-pdf-to-ods)

## C# PDF to Excel Conversions

**Aspose.PDF for .NET** support the feature of converting PDF files to Excel 2007, CSV and SpeadsheetML formats.

Aspose.PDF for .NET is a PDF manipulation component, we have introduced a feature that renders PDF file to Excel workbook (XLSX files). During this conversion, the individual pages of the PDF file are converted to Excel worksheets.

{{% alert color="success" %}}
**Try to convert PDF to Excel online**

Aspose.PDF for .NET presents you online free application ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

In order to convert PDF files to <abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr> format, Aspose.PDF has a class called [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions). An object of the ExcelSaveOptions class is passed as a second argument to the Document.Save(..) constructor.

The following code snippet shows the process for converting PDF file into XLS or XLSX format with Aspose.PDF for .NET.

<a name="csharp-pdf-to-xls"><strong>Steps: Convert PDF to XLS in C#</strong></a>

1. Create an instance of **Document** object with the source PDF document.
2. Create an instance of **ExcelSaveOptions**.
3. Save it to **XLS** format specifying **.xls extension** by calling **Document.Save()** method and passing it **ExcelSaveOptions**

<a name="csharp-pdf-to-xlsx"><strong>Steps: Convert PDF to XLSX in C#</strong></a>

1. Create an instance of **Document** object with the source PDF document.
2. Create an instance of **ExcelSaveOptions**.
3. Save it to **XLSX** format specifying **.xlsx extension** by calling **Document.Save()** method and passing it **ExcelSaveOptions**

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Load PDF document
Document pdfDocument = new Document(dataDir + "input.pdf");

// Instantiate ExcelSave Option object
Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions();

// Save the output in XLS format
pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
```

## Convert PDF to XLS with Control Column

When converting a PDF to XLS format, a blank column is added to the output file as first column. The in ExcelSaveOptions class' InsertBlankColumnAtFirst option is used to control this column. Its default value is true.

```csharp
public static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst()
{
    // For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    // Load PDF document
    Document pdfDocument = new Document(_dataDir + "input.pdf");
    // Instantiate ExcelSave Option object
    Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions {InsertBlankColumnAtFirst = false};
    // Save the output in XLS format
    pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
}
```

## Convert PDF to Single Excel Worksheet

When exporting a PDF file with a lot of pages to XLS, each page is exported to a different sheet in the Excel file. This is because the MinimizeTheNumberOfWorksheets property is set to false by default. To ensure that all pages are exported to one single sheet in the output Excel file, set the MinimizeTheNumberOfWorksheets property to true.

<a name="csharp-pdf-to-excel-single"><strong>Steps: Convert PDF to XLS or XLSX Single Worksheet in C#</strong></a>

1. Create an instance of **Document** object with the source PDF document.
2. Create an instance of **ExcelSaveOptions** with **MinimizeTheNumberOfWorksheets = true**.
3. Save it to **XLS** or **XLSX** format having single worksheet by calling **Document.Save()** method and passing it **ExcelSaveOptions**.

```csharp
public static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets()
{
    // For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    // Load PDF document
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // Instantiate ExcelSave Option object
    Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions {MinimizeTheNumberOfWorksheets = true};
    // Save the output in XLS format
    pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
}
```

## Convert to other spreadsheet formats

### Convert to XML Spreadsheet 2003 format

Since version 20.8 Aspose.PDF uses Microsoft Excel Open XML Spreadsheet 2007 file format as default for storing data. In order to convert PDF files to XML Spreadsheet 2003 format, Aspose.PDF has a class called [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions) with [Format](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions/properties/format). An object of the [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions) class is passed as a second argument to the [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) method.

The following code snippet shows the process for converting PDF file into XLS Excel 2003 XML format.

<a name="csharp-pdf-to-excel-xml-2003"><strong>Steps: Convert PDF to Excel 2003 XML Format in C#</strong></a>

1. Create an instance of **Document** object with the source PDF document.
2. Create an instance of **ExcelSaveOptions** with **Format = ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003**
3. Save it to **XLS - Excel 2003 XML Format** format by calling **Document.Save()** method and passing it **ExcelSaveOptions**.

```csharp
public static void ConvertPDFtoExcelAdvanced_SaveXLS2003()
{
    // For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET

    // Load PDF document
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // Instantiate ExcelSave Option object
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003 };

    // Save the output in XLS format
    pdfDocument.Save("PDFToXLS_out.xls", excelSave);
}
```

### Convert to CSV

Conversion to CSV format performs in the same way as above. All is what you need - set the appropriate format.

<a name="csharp-pdf-to-csv"><strong>Steps: Convert PDF to CSV in C#</strong></a>

1. Create an instance of **Document** object with the source PDF document.
2. Create an instance of **ExcelSaveOptions** with **Format = ExcelSaveOptions.ExcelFormat.CSV**
3. Save it to **CSV** format by calling **Document.Save()** method and passing it **ExcelSaveOptions**.


```csharp
 // Instantiate ExcelSave Option object
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.CSV };
```

### Convert to ODS

<a name="csharp-pdf-to-ods"><strong>Steps: Convert PDF to ODS in C#</strong></a>

1. Create an instance of **Document** object with the source PDF document.
2. Create an instance of **ExcelSaveOptions** with **Format = ExcelSaveOptions.ExcelFormat.ODS**
3. Save it to **ODS** format by calling **Document.Save()** method and passing it **ExcelSaveOptions**.


Conversion to ODS format performs in the same way as all other formats.

```csharp
 // Instantiate ExcelSave Option object
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.ODS };
```

## See Also 

This article also covers these topics. The codes are same as above.

_Format_: **Excel**
- [C# PDF to Excel Code](#csharp-pdf-to-xlsx)
- [C# PDF to Excel API](#csharp-pdf-to-xlsx)
- [C# PDF to Excel Programmatically](#csharp-pdf-to-xlsx)
- [C# PDF to Excel Library](#csharp-pdf-to-xlsx)
- [C# Save PDF as Excel](#csharp-pdf-to-xlsx)
- [C# Generate Excel from PDF](#csharp-pdf-to-xlsx)
- [C# Create Excel from PDF](#csharp-pdf-to-xlsx)
- [C# PDF to Excel Converter](#csharp-pdf-to-xlsx)

_Format_: **XLS**
- [C# PDF to XLS Code](#csharp-pdf-to-xls)
- [C# PDF to XLS API](#csharp-pdf-to-xls)
- [C# PDF to XLS Programmatically](#csharp-pdf-to-xls)
- [C# PDF to XLS Library](#csharp-pdf-to-xls)
- [C# Save PDF as XLS](#csharp-pdf-to-xls)
- [C# Generate XLS from PDF](#csharp-pdf-to-xls)
- [C# Create XLS from PDF](#csharp-pdf-to-xls)
- [C# PDF to XLS Converter](#csharp-pdf-to-xls)

_Format_: **XLSX**
- [C# PDF to XLSX Code](#csharp-pdf-to-xlsx)
- [C# PDF to XLSX API](#csharp-pdf-to-xlsx)
- [C# PDF to XLSX Programmatically](#csharp-pdf-to-xlsx)
- [C# PDF to XLSX Library](#csharp-pdf-to-xlsx)
- [C# Save PDF as XLSX](#csharp-pdf-to-xlsx)
- [C# Generate XLSX from PDF](#csharp-pdf-to-xlsx)
- [C# Create XLSX from PDF](#csharp-pdf-to-xlsx)
- [C# PDF to XLSX Converter](#csharp-pdf-to-xlsx)

_Format_: **CSV**
- [C# PDF to CSV Code](#csharp-pdf-to-csv)
- [C# PDF to CSV API](#csharp-pdf-to-csv)
- [C# PDF to CSV Programmatically](#csharp-pdf-to-csv)
- [C# PDF to CSV Library](#csharp-pdf-to-csv)
- [C# Save PDF as CSV](#csharp-pdf-to-csv)
- [C# Generate CSV from PDF](#csharp-pdf-to-csv)
- [C# Create CSV from PDF](#csharp-pdf-to-csv)
- [C# PDF to CSV Converter](#csharp-pdf-to-csv)

_Format_: **ODS**
- [C# PDF to ODS Code](#csharp-pdf-to-ods)
- [C# PDF to ODS API](#csharp-pdf-to-ods)
- [C# PDF to ODS Programmatically](#csharp-pdf-to-ods)
- [C# PDF to ODS Library](#csharp-pdf-to-ods)
- [C# Save PDF as ODS](#csharp-pdf-to-ods)
- [C# Generate ODS from PDF](#csharp-pdf-to-ods)
- [C# Create ODS from PDF](#csharp-pdf-to-ods)
- [C# PDF to ODS Converter](#csharp-pdf-to-ods)
