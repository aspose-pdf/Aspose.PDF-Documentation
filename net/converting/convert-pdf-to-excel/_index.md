---
title: Convert PDF to Excel 
type: docs
weight: 240
url: /net/convert-pdf-to-excel/
---
# Convert PDF to Excel 
Aspose.PDF for .NET is a PDF manipulation component, we have introduced a feature that renders PDF file to Excel workbook (XLS files). During this conversion, the individual pages of the PDF file are converted to Excel worksheets.

## Convert PDF to XLS

> Try online. You can check the quality of Aspose.PDF conversion and view the results online at this [link](https://products.aspose.app/pdf/conversion/pdf-to-xlsx) 

In order to convert PDF files to XLS format, Aspose.PDF has a class called ExcelSaveOptions. An object of the ExcelSaveOptions class is passed as a second argument to the Document.Save(..) constructor. The following code snippet shows the process for converting PDF file into XLS format.

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

### Convert PDF to XLS with Control Column

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

### Convert PDF to Single Excel Worksheet

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

### Convert to XLSX format

By default Aspose.PDF uses  XML Spreadsheet 2003 for storing data. In order to convert PDF files to XLSX format, Aspose.PDF has a class called `ExcelSaveOptions` with `Format`. An object of the `ExcelSaveOptions` class is passed as a second argument to the `Document.Save(..)` constructor. The following code snippet shows the process for converting PDF file into XLSX format.

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

