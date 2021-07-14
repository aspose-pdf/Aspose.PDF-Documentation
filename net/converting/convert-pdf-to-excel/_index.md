---
title: Convert PDF to Excel | C#
linktitle: Convert PDF to Excel
type: docs
weight: 90
url: /net/convert-pdf-to-excel/
aliases:
    - /net/convert-pdf-to-excel-xls/
lastmod: "2021-06-05"
keywords: convert PDF to Excel using c#, convert PDF to XLS using csharp, convert PDF to XLSX using csharp, export table from PDF to Excel in csharp.
description: Aspose.PDF for .NET allows you to convert PDF to Excel format using c#. During this, the individual pages of the PDF file are converted to Excel worksheets.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for .NET** support the feature of converting PDF files to Excel formats.

Aspose.PDF for .NET is a PDF manipulation component, we have introduced a feature that renders PDF file to Excel workbook (XLS files). During this conversion, the individual pages of the PDF file are converted to Excel worksheets.

## Live Example

Aspose.PDF for .NET presents you online free application ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), where you may try to investigate the functionality and quality it works.

[![PDF to Excel converter](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)

In order to convert PDF files to <abbr title="Microsoft Excel Spreadsheet">XLS</abbr> format, Aspose.PDF has a class called ExcelSaveOptions. An object of the ExcelSaveOptions class is passed as a second argument to the Document.Save(..) constructor.

The following code snippet shows the process for converting PDF file into XLS format with Aspose.PDF for .NET.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Load PDF document
Document pdfDocument = new Document(dataDir + "input.pdf");

// Instantiate ExcelSave Option object
Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions();

// Save the output in XLS format
pdfDocument.Save("PDFToXLS_out.xls", excelsave);
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
    pdfDocument.Save("PDFToXLS_out.xls", excelsave);
}
```

## Convert PDF to Single Excel Worksheet

When exporting a PDF file with a lot of pages to XLS, each page is exported to a different sheet in the Excel file. This is because the MinimizeTheNumberOfWorksheets property is set to false by default. To ensure that all pages are exported to one single sheet in the output Excel file, set the MinimizeTheNumberOfWorksheets property to true.

```csharp
public static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets()
{
    // For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    // Load PDF document
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // Instantiate ExcelSave Option object
    Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions {MinimizeTheNumberOfWorksheets = true};
    // Save the output in XLS format
    pdfDocument.Save("PDFToXLS_out.xls", excelsave);
}
```

## Convert to XLSX format

By default Aspose.PDF uses  XML Spreadsheet 2003 for storing data. In order to convert PDF files to XLSX format, Aspose.PDF has a class called [ExcelSaveOptions](https://apireference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions) with [Format](https://apireference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions/properties/format). An object of the [ExcelSaveOptions](https://apireference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions) class is passed as a second argument to the [Document.Save(..)](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) method.

The following code snippet shows the process for converting PDF file into XLSX format.

```csharp
public static void ConvertPDFtoExcelAdvanced_SaveXLSX()
{
    // For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET

    // Load PDF document
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // Instantiate ExcelSave Option object
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.XLSX};

    // Save the output in XLS format
    pdfDocument.Save("PDFToXLS_out.xlsx", excelSave);
}
```
