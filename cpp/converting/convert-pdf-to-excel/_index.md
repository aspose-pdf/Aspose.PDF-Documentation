---
title: Convert PDF to Excel 
linktitle: Convert PDF to Excel
type: docs
weight: 90
url: /cpp/convert-pdf-to-excel/
lastmod: "2021-06-05"
description: Aspose.PDF for C++ allows you to convert PDF to Excel format using C++. During this, the individual pages of the PDF file are converted to Excel worksheets.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for .C++** support the feature of converting PDF files to Excel formats.

Aspose.PDF for C++ is a PDF manipulation component, we have introduced a feature that renders PDF file to Excel workbook (XLS files). During this conversion, the individual pages of the PDF file are converted to Excel worksheets.

## Live Example

Aspose.PDF for C++ presents you online free application ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), where you may try to investigate the functionality and quality it works.

[![PDF to Excel converter](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)

In order to convert PDF files to <abbr title="Microsoft Excel Spreadsheet">XLS</abbr> format, Aspose.PDF has a class called ExcelSaveOptions. An object of the ExcelSaveOptions class is passed as a second argument to the Document.Save(..) constructor.

The following code snippet shows the process for converting PDF file into XLS format with Aspose.PDF for C++.

```cpp
void ConvertPDFtoExcel()
{
 std::clog << __func__ << ": Start" << std::endl;
 // String for path name
 String _dataDir("C:\\Samples\\Conversion\\");

 // String for file name
 String infilename("sample.pdf");
 String outfilename("PDFToExcel.xlsx");

 // Open document
 auto document = MakeObject<Document>(_dataDir + infilename);

 try {
  // Save the output in XLSX format
  document->Save(_dataDir + outfilename, SaveFormat::Excel);
 }
 catch (Exception ex) {
  std::cerr << ex->get_Message();
 }
 std::clog << __func__ << ": Finish" << std::endl;
}
```

## Convert PDF to XLS with Control Column

When converting a PDF to XLS format, a blank column is added to the output file as first column. The in ExcelSaveOptions class' InsertBlankColumnAtFirst option is used to control this column. Its default value is true.

```cpp
void ConvertPDFtoExcel_Advanced_InsertBlankColumnAtFirst()
{
 std::clog << __func__ << ": Start" << std::endl;
 // String for path name
 String _dataDir("C:\\Samples\\Conversion\\");

 // String for file name
 String infilename("sample.pdf");
 String outfilename("PDFToExcel.xls");

 // Open document
 auto document = MakeObject<Document>(_dataDir + infilename);

 // Instantiate ExcelSave Option object
 auto excelSave = MakeObject<ExcelSaveOptions>();

 // The in ExcelSaveOptions class' InsertBlankColumnAtFirst option is used to control this column. Its default value is true.
 excelSave->set_InsertBlankColumnAtFirst(false);

 // Save the output in XLS format
 document->Save(outfilename, excelSave);
 std::clog << __func__ << ": Finish" << std::endl;
}
```

## Convert PDF to Single Excel Worksheet

When exporting a PDF file with a lot of pages to XLS, each page is exported to a different sheet in the Excel file. This is because the MinimizeTheNumberOfWorksheets property is set to false by default. To ensure that all pages are exported to one single sheet in the output Excel file, set the MinimizeTheNumberOfWorksheets property to true.

```cpp
void ConvertPDFtoExcel_Advanced_MinimizeTheNumberOfWorksheets()
{
 std::clog << __func__ << ": Start" << std::endl;
 // String for path name
 String _dataDir("C:\\Samples\\Conversion\\");

 // String for file name
 String infilename("sample.pdf");
 String outfilename("PDFToExcel.xls");

 // Open document
 auto document = MakeObject<Document>(_dataDir + infilename);

 // Instantiate ExcelSave Option object
 auto excelSave = MakeObject<ExcelSaveOptions>();

 excelSave->set_MinimizeTheNumberOfWorksheets(true);

 // Save the output in XLS format
 document->Save(outfilename, excelSave);
 std::clog << __func__ << ": Finish" << std::endl;
}
```

## Convert to XLSX format

By default Aspose.PDF uses  XML Spreadsheet 2003 for storing data. In order to convert PDF files to XLSX format, Aspose.PDF has a class called [ExcelSaveOptions](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options) with 'Format'. An object of the [ExcelSaveOptions](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options) class is passed as a second argument to the [Save](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) method.

The following code snippet shows the process for converting PDF file into XLSX format.

```cpp
void ConvertPDFtoExcel_Advanced_SaveXLSX()
{
 std::clog << __func__ << ": Start" << std::endl;
 // String for path name
 String _dataDir("C:\\Samples\\Conversion\\");

 // String for file name
 String infilename("sample.pdf");
 String outfilename("PDFToExcel.xls");

 // Open document
 auto document = MakeObject<Document>(_dataDir + infilename);

 // Instantiate ExcelSave Option object
 auto excelSave = MakeObject<ExcelSaveOptions>();

 excelSave->set_Format(ExcelSaveOptions::ExcelFormat::XLSX);

 // Save the output in XLS format
 document->Save(outfilename, excelSave);
 std::clog << __func__ << ": Finish" << std::endl;
}
```
