---
title: Convert PDF to Excel 
linktitle: Convert PDF to Excel 
type: docs
weight: 90
url: /java/convert-pdf-to-excel/
lastmod: "2021-02-04"
description: Aspose.PDF for Java allows you to convert PDF to Excel format. During this, the individual pages of the PDF file are converted to Excel worksheets.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for Java API lets you render your PDF files to Excel [XLS](https://wiki.fileformat.com/spreadsheet/xls/) and [XLSX](https://wiki.fileformat.com/spreadsheet/xlsx/) file formats. We already have another API, known as [Aspose.Cells for Java](https://products.aspose.com/cells/java), that provides the capability to create and manipulate existing Excel workbooks. It also provides the capability to transform Excel workbooks to PDF format.

{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-xlsx](https://products.aspose.app/pdf/conversion/pdf-to-xlsx) 

{{% /alert %}}

## Convert PDF to Excel XLS

To convert PDF files to XLS format, Aspose.PDF has a class called [ExcelSaveOptions](https://apireference.aspose.com/java/pdf/com.aspose.pdf/ExcelSaveOptions). An object of the [ExcelSaveOptions](https://apireference.aspose.com/java/pdf/com.aspose.pdf/ExcelSaveOptions) class is passed as a second argument to the Document.Save(..) constructor. 

Converting a PDF file into XLSX format is part of the library from Aspose.PDF for Java 18.6 version. In order to convert PDF files to XLSX format, you need to set format as XLSX using setFormat() method of [ExcelSaveOptions](https://apireference.aspose.com/java/pdf/com.aspose.pdf/ExcelSaveOptions) Class.

Following code snippet shows how to convert a PDF file into xls and .xlsx format:

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPDFtoXLSX {

    private ConvertPDFtoXLSX() {

    }

    // The path to the documents directory.
    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {

        ConvertPDFtoExcelSimple();
        ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst();
        ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets();
        ConvertPDFtoExcelAdvanced_SaveXLSX();
    }

    public static void ConvertPDFtoExcelSimple() {
        // Load PDF document
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelsave = new ExcelSaveOptions();

        // Save the output in XLS format
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
```
## Convert PDF to XLS with Control Column

When converting a PDF to XLS format, a blank column is added to the output file as first column. The in [ExcelSaveOptions](https://apireference.aspose.com/java/pdf/com.aspose.pdf/ExcelSaveOptions) class InsertBlankColumnAtFirst option is used to control this column. Its default value is true.

```java
    public static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // Load PDF document
        Document pdfDocument = new Document(_dataDir + "input.pdf");
        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelsave = new ExcelSaveOptions();
        excelsave.setInsertBlankColumnAtFirst(false);
        // Save the output in XLS format
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
```
## Convert PDF to Single Excel Worksheet 

When exporting a PDF file with a lot of pages to XLS, each page is exported to a different sheet in the Excel file. This is because the MinimizeTheNumberOfWorksheets property is set to false by default. To ensure that all pages are exported to one single sheet in the output Excel file, set the MinimizeTheNumberOfWorksheets property to true.

```java
    public static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // Load PDF document
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelsave = new ExcelSaveOptions();
        excelsave.setMinimizeTheNumberOfWorksheets(true);

        // Save the output in XLS format
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
```
## Convert to XLSX format 

By default Aspose.PDF uses XML Spreadsheet 2003 for storing data. In order to convert PDF files to XLSX format, Aspose.PDF has a class called ExcelSaveOptions with Format. An object of the [ExcelSaveOptions](https://apireference.aspose.com/java/pdf/com.aspose.pdf/ExcelSaveOptions) class is passed as a second argument to the Document.Save(..) method.

```java
    public static void ConvertPDFtoExcelAdvanced_SaveXLSX() {
        // Load PDF document
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);

        // Save the output in XLS format
        pdfDocument.save("PDFToXLS_out.xlsx", excelSave);
    }
}
```