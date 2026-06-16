---
title: Convert PDF to Excel in Java
linktitle: Convert PDF to Excel
type: docs
weight: 20
url: /java/convert-pdf-to-excel/
lastmod: "2026-06-16"
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

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`ExcelSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/excelsaveoptions/) and set its format to `XMLSpreadSheet2003` for Excel 2003 XML output.
1. Pass the prepared save options to the shared save method so the loaded PDF is exported with those spreadsheet settings.
1. Write the converted workbook to the target output path.

```java
public static void convertPdfToExcelSpreadSheet2003(Path inputFile, Path outputFile) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003);
        saveDocument(inputFile, outputFile, saveOptions);
    }
```

## Convert PDF to XLSX

Use this example when PDF content should be converted into the Excel 2007+ XLSX format.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`ExcelSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/excelsaveoptions/) and set its format to `XLSX`.
1. Pass the configured save options to the shared save method so Aspose.PDF exports the table and text layout to an `.xlsx` workbook.
1. Save the generated spreadsheet file.

```java
public static void convertPdfToExcel2007(Path inputFile, Path outputFile) {
    ExcelSaveOptions saveOptions = new ExcelSaveOptions();
    saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
    saveDocument(inputFile, outputFile, saveOptions);
}
```

## Convert PDF to XLSX with column control

Use this example when column handling should be adjusted during PDF-to-Excel conversion.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`ExcelSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/excelsaveoptions/) for `XLSX` output.
1. Enable `setInsertBlankColumnAtFirst(true)` when an extra leading column is needed to improve downstream worksheet layout.
1. Save the converted XLSX file through the shared save method.

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

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`ExcelSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/excelsaveoptions/) for `XLSX` export.
1. Enable `setMinimizeTheNumberOfWorksheets(true)` so multiple PDF pages are consolidated into fewer Excel worksheets.
1. Save the XLSX output file through the shared save method.

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

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`ExcelSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/excelsaveoptions/) and set the format to `XLSM`.
1. Pass the configured options to the shared save method so the PDF content is exported in a macro-enabled workbook container.
1. Save the generated XLSM file.

```java
public static void convertPdfToExcel2007Macro(Path inputFile, Path outputFile) {
    ExcelSaveOptions saveOptions = new ExcelSaveOptions();
    saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSM);
    saveDocument(inputFile, outputFile, saveOptions);
}
```

## Convert PDF to CSV

Use this example when PDF tabular content should be exported as CSV.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`ExcelSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/excelsaveoptions/) and set the format to `CSV`.
1. Pass the configured options to the shared save method so tabular PDF content is flattened to comma-separated output.
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

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`ExcelSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/excelsaveoptions/) and set the format to `ODS`.
1. Pass the configured options to the shared save method so the output is written in OpenDocument spreadsheet format.
1. Save the converted ODS file.

```java
public static void convertPdfToOds(Path inputFile, Path outputFile) {
    ExcelSaveOptions saveOptions = new ExcelSaveOptions();
    saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
    saveDocument(inputFile, outputFile, saveOptions);
}
```

## Reuse a shared Excel save method

Use this method when several Excel conversion examples should save the document through one common export routine.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Pass the prepared [`ExcelSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/excelsaveoptions/) into the method together with the input and output paths.
1. Call `document.save(outputFile.toString(), saveOptions)` so the selected Excel export format is applied during serialization.
1. Save the converted spreadsheet output and release the document resources with try-with-resources.

```java
private static void saveDocument(Path inputFile, Path outputFile, ExcelSaveOptions saveOptions) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
