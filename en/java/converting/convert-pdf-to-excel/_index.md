---
title: Convert PDF to Excel in Java
linktitle: Convert PDF to Excel
type: docs
weight: 20
url: /java/convert-pdf-to-excel/
lastmod: "2026-06-08"
description: Learn how to convert PDF files to Excel in Java with Aspose.PDF, including XML Spreadsheet 2003, XLSX, XLSM, CSV, and ODS output.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to Convert PDF to Excel in Java
Abstract: This article explains how to convert PDF files to Excel-compatible formats with Aspose.PDF for Java. It covers XML Spreadsheet 2003, XLSX, XLSM, CSV, and ODS output, along with options for blank-column insertion and minimizing the number of worksheets.
---
## Convert PDF to Excel-compatible formats

All Excel conversions use [ExcelSaveOptions](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/excelsaveoptions/) with a different target format.

1. Create [ExcelSaveOptions](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/excelsaveoptions/) for the target output format.
1. Set the Excel output format for the conversion.
1. Convert the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) by using the configured save options.

```java
public static void convertPdfToExcel2007(Path inputFile, Path outputFile) {
    ExcelSaveOptions saveOptions = new ExcelSaveOptions();
    saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
    saveDocument(inputFile, outputFile, saveOptions);
}
```
