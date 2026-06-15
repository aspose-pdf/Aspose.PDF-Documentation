---
title: Convert PDF to Excel in Java
linktitle: Convert PDF to Excel
type: docs
weight: 20
url: /java/convert-pdf-to-excel/
lastmod: "2026-06-09"
description: Learn how to convert PDF files to Excel in Java with Aspose.PDF, including XML Spreadsheet 2003, XLSX, XLSM, CSV, and ODS output.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to Convert PDF to Excel in Java
Abstract: This article explains how to convert PDF files to Excel-compatible formats with Aspose.PDF for Java. It covers XML Spreadsheet 2003, XLSX, XLSM, CSV, and ODS output, along with options for blank-column insertion and minimizing the number of worksheets.
---
Aspose.PDF for Java can export PDF content to multiple spreadsheet formats with different layout options.

## Convert PDF to Excel 2003 XML

Use this example when PDF content should be exported to the Excel 2003 XML spreadsheet format.

1. Open the source PDF document.
1. Configure Excel save options for the Spreadsheet 2003 format.
1. Save the converted output file.

```java
public static void convertPdfToExcelSpreadSheet2003(Path inputFile, Path outputFile) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003);
        saveDocument(inputFile, outputFile, saveOptions);
    }
```

## Convert PDF to XLSX

Use this example when PDF content should be converted into the Excel 2007+ XLSX format.

1. Open the source PDF document.
1. Configure XLSX save options.
1. Save the output spreadsheet file.

```java
public static void convertPdfToExcel2007(Path inputFile, Path outputFile) {
    ExcelSaveOptions saveOptions = new ExcelSaveOptions();
    saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
    saveDocument(inputFile, outputFile, saveOptions);
}
```

## Convert PDF to XLSX with column control

Use this example when column handling should be adjusted during PDF-to-Excel conversion.

1. Open the source PDF document.
1. Set the Excel save options that control column behavior.
1. Save the converted XLSX file.

```java
public static void convertPdfToExcel2007ControlColumn(Path inputFile, Path outputFile) {
    ExcelSaveOptions saveOptions = new ExcelSaveOptions();
    saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
    saveOptions.setInsertBlankColumnAtFirst(true);
    saveDocument(inputFile, outputFile, saveOptions);
}
```

## Convert PDF to a single Excel worksheet

Use this example when all PDF pages should be exported into one worksheet.

1. Open the source PDF document.
1. Configure the Excel save options for a single worksheet.
1. Save the XLSX output file.

```java
public static void convertPdfToExcel2007SingleExcelWorksheet(Path inputFile, Path outputFile) {
    ExcelSaveOptions saveOptions = new ExcelSaveOptions();
    saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
    saveOptions.setMinimizeTheNumberOfWorksheets(true);
    saveDocument(inputFile, outputFile, saveOptions);
}
```

## Convert PDF to XLSM

Use this example when the PDF output should be saved as a macro-enabled Excel workbook.

1. Open the source PDF document.
1. Configure Excel save options for macro-enabled output.
1. Save the XLSM file.

```java
public static void convertPdfToExcel2007Macro(Path inputFile, Path outputFile) {
    ExcelSaveOptions saveOptions = new ExcelSaveOptions();
    saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSM);
    saveDocument(inputFile, outputFile, saveOptions);
}
```

## Convert PDF to CSV

Use this example when PDF tabular content should be exported as CSV.

1. Open the source PDF document.
1. Set the spreadsheet save options for CSV output.
1. Save the generated CSV file.

```java
public static void convertPdfToExcel2007Csv(Path inputFile, Path outputFile) {
    ExcelSaveOptions saveOptions = new ExcelSaveOptions();
    saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);
    saveDocument(inputFile, outputFile, saveOptions);
}
```

## Convert PDF to ODS

Use this example when PDF content should be exported to the OpenDocument spreadsheet format.

1. Open the source PDF document.
1. Configure spreadsheet save options for ODS.
1. Save the converted ODS file.

```java
public static void convertPdfToOds(Path inputFile, Path outputFile) {
    ExcelSaveOptions saveOptions = new ExcelSaveOptions();
    saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
    saveDocument(inputFile, outputFile, saveOptions);
}
```

## Reuse a shared Excel save helper

Use this helper when several Excel conversion examples should save the document through a common method.

1. Open the source PDF document.
1. Pass the prepared `ExcelSaveOptions` to the helper.
1. Save the converted spreadsheet output.

```java
private static void saveDocument(Path inputFile, Path outputFile, ExcelSaveOptions saveOptions) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
