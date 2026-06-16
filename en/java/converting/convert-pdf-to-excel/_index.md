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
Aspose.PDF for Java can export PDF content to multiple spreadsheet formats with different layout options. Use [`ExcelSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/excelsaveoptions/) to choose the target workbook format and control how page content is mapped into worksheets and columns.

## Convert PDF to Excel 2003 XML

Use this example when PDF content should be exported to the Excel 2003 XML spreadsheet format.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`ExcelSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/excelsaveoptions/) and set its format to `XMLSpreadSheet2003`.
1. Call `document.save(outputFile.toString(), saveOptions)` so the loaded PDF is serialized in the Excel 2003 XML schema.
1. Save the converted output file.

```java
public static void convertPdfToExcelSpreadSheet2003(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PDF to XLSX

Use this example when PDF content should be converted into the Excel 2007+ XLSX format.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`ExcelSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/excelsaveoptions/) and set its format to `XLSX`.
1. Call `document.save(outputFile.toString(), saveOptions)` so the PDF layout is exported as an Office Open XML workbook.
1. Save the output spreadsheet file.

```java
public static void convertPdfToExcel2007(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PDF to XLSX with column control

Use this example when column handling should be adjusted during PDF-to-Excel conversion.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`ExcelSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/excelsaveoptions/) for `XLSX` output.
1. Enable `setInsertBlankColumnAtFirst(true)` when an extra leading column is needed to improve the worksheet layout produced from the PDF.
1. Call `document.save(outputFile.toString(), saveOptions)` and write the converted XLSX file.

```java
public static void convertPdfToExcel2007ControlColumn(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        saveOptions.setInsertBlankColumnAtFirst(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PDF to a single Excel worksheet

Use this example when all PDF pages should be exported into one worksheet.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`ExcelSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/excelsaveoptions/) for `XLSX` export.
1. Enable `setMinimizeTheNumberOfWorksheets(true)` so multiple PDF pages are consolidated into fewer worksheets.
1. Call `document.save(outputFile.toString(), saveOptions)` and save the XLSX output file.

```java
public static void convertPdfToExcel2007SingleExcelWorksheet(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        saveOptions.setMinimizeTheNumberOfWorksheets(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PDF to XLSM

Use this example when the PDF output should be saved as a macro-enabled Excel workbook.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`ExcelSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/excelsaveoptions/) and set the format to `XLSM`.
1. Call `document.save(outputFile.toString(), saveOptions)` so the PDF content is exported to a macro-enabled workbook container.
1. Save the XLSM file.

```java
public static void convertPdfToExcel2007Macro(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSM);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PDF to CSV

Use this example when PDF tabular content should be exported as CSV.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`ExcelSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/excelsaveoptions/) and set the format to `CSV`.
1. Call `document.save(outputFile.toString(), saveOptions)` so the PDF content is flattened to comma-separated text output.
1. Save the generated CSV file.

```java
public static void convertPdfToExcel2007Csv(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PDF to ODS

Use this example when PDF content should be exported to the OpenDocument spreadsheet format.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`ExcelSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/excelsaveoptions/) and set the format to `ODS`.
1. Call `document.save(outputFile.toString(), saveOptions)` so the PDF is exported in OpenDocument spreadsheet format.
1. Save the converted ODS file.

```java
public static void convertPdfToOds(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
