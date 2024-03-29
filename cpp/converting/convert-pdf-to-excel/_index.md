---
title: Convert PDF to Excel in C++
linktitle: Convert PDF to Excel
type: docs
weight: 20
url: /cpp/convert-pdf-to-excel/
lastmod: "2021-11-19"
description: Aspose.PDF for C++ allows you to convert PDF to Excel format using C++. During this, the individual pages of the PDF file are converted to Excel worksheets.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Overview

This article explains how to **convert PDF to Excel formats using C++**. It covers the following topics.

_Format_: **XLS**
- [C++ PDF to XLS](#cpp-pdf-to-xls)
- [C++ Convert PDF to XLS](#cpp-pdf-to-xls)
- [C++ How to convert PDF file to XLS](#cpp-pdf-to-xls)

_Format_: **XLSX**
- [C++ PDF to XLSX](#cpp-pdf-to-xlsx)
- [C++ Convert PDF to XLSX](#cpp-pdf-to-xlsx)
- [C++ How to convert PDF file to XLSX](#cpp-pdf-to-xlsx)

_Format_: **Microsoft Excel XLS format**
- [C++ PDF to Excel](#cpp-pdf-to-excel-xls)
- [C++ Convert PDF to Excel](#cpp-pdf-to-excel-xls)
- [C++ How to convert PDF file to Excel](#cpp-pdf-to-excel-xls)

_Format_: **Microsoft Excel XLSX format**
- [C++ PDF to Excel](#cpp-pdf-to-excel-xlsx)
- [C++ Convert PDF to Excel](#cpp-pdf-to-excel-xlsx)
- [C++ How to convert PDF file to Excel](#cpp-pdf-to-excel-xlsx)

Other topics covered by this article
- [See Also](#see-also)

## C++ PDF to Excel Conversions

**Aspose.PDF for C++** support the feature of converting PDF files to Excel formats.

Aspose.PDF for C++ is a PDF manipulation component, we have introduced a feature that renders PDF file to Excel workbook (XLS files). During this conversion, the individual pages of the PDF file are converted to Excel worksheets.

In order to convert PDF files to <abbr title="Microsoft Excel Spreadsheet">XLS</abbr> format, Aspose.PDF has a class called ExcelSaveOptions. An object of the ExcelSaveOptions class is passed as a second argument to the Document.Save(..) constructor.

The following code snippet shows the process for converting PDF file into XLS format with Aspose.PDF for C++.

<a name="cpp-pdf-to-xls" id="cpp-pdf-to-xls"><strong>Steps: Convert PDF to XLS in C++</strong></a> | <a name="cpp-pdf-to-excel-xls" id="cpp-pdf-to-excel-xls"><strong>Steps: Convert PDF to Excel XLS format in C++</strong></a>

1. Create an instance of [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) object with the source PDF document.
2. Save it to _XLS_ format by calling **Document->Save()** method.

```cpp
void ConvertPDFtoExcel()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
    // Save the output in XLS format
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

By default Aspose.PDF uses  XML Spreadsheet 2003 for storing data. In order to convert PDF files to XLSX format, Aspose.PDF has a class called [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options) with 'Format'. An object of the [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options) class is passed as a second argument to the [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) method.

The following code snippet shows the process for converting PDF file into XLSX format.

<a name="cpp-pdf-to-xlsx" id="cpp-pdf-to-xlsx"><strong>Steps: Convert PDF to XLSX in C++</strong></a> | <a name="cpp-pdf-to-excel-xlsx" id="cpp-pdf-to-excel-xlsx"><strong>Steps: Convert PDF to Excel XLSX format in C++</strong></a>

1. Create an instance of [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) object with the source PDF document.
2. Create an instance of [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options).
3. Set the format as _ExcelSaveOptions::ExcelFormat::XLSX_.
4. Save it to _XLSX_ format by calling **Document->Save()** method and passing it instance of _ExcelSaveOptions_.

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

{{% alert color="success" %}}
**Try to convert PDF to Excel online**

Aspose.PDF for C++ presents you online free application ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## See Also

This article also covers these topics. The codes are same as above.

_Format_: **Microsoft Excel XLS format**
- [C++ PDF to Excel XLS Code](#cpp-pdf-to-excel-xls)
- [C++ PDF to Excel XLS Programmatically](#cpp-pdf-to-excel-xls)
- [C++ PDF to Excel XLS Library](#cpp-pdf-to-excel-xls)
- [C++ Save PDF as Excel XLS](#cpp-pdf-to-excel-xls)
- [C++ Generate Excel XLS from PDF](#cpp-pdf-to-excel-xls)
- [C++ Create Excel XLS from PDF](#cpp-pdf-to-excel-xls)
- [C++ PDF to Excel XLS Converter](#cpp-pdf-to-excel-xls)

_Format_: **Microsoft Excel XLSX format**
- [C++ PDF to Excel XLSX Code](#cpp-pdf-to-excel-xlsx)
- [C++ PDF to Excel XLSX Programmatically](#cpp-pdf-to-excel-xlsx)
- [C++ PDF to Excel XLSX Library](#cpp-pdf-to-excel-xlsx)
- [C++ Save PDF as Excel XLSX](#cpp-pdf-to-excel-xlsx)
- [C++ Generate Excel XLSX from PDF](#cpp-pdf-to-excel-xlsx)
- [C++ Create Excel XLSX from PDF](#cpp-pdf-to-excel-xlsx)
- [C++ PDF to Excel XLSX Converter](#cpp-pdf-to-excel-xlsx)

_Format_: **XLS**
- [C++ PDF to XLS Code](#cpp-pdf-to-xls)
- [C++ PDF to XLS Programmatically](#cpp-pdf-to-xls)
- [C++ PDF to XLS Library](#cpp-pdf-to-xls)
- [C++ Save PDF as XLS](#cpp-pdf-to-xls)
- [C++ Generate XLS from PDF](#cpp-pdf-to-xls)
- [C++ Create XLS from PDF](#cpp-pdf-to-xls)
- [C++ PDF to XLS Converter](#cpp-pdf-to-xls)

_Format_: **XLSX**
- [C++ PDF to XLSX Code](#cpp-pdf-to-xlsx)
- [C++ PDF to XLSX Programmatically](#cpp-pdf-to-xlsx)
- [C++ PDF to XLSX Library](#cpp-pdf-to-xlsx)
- [C++ Save PDF as XLSX](#cpp-pdf-to-xlsx)
- [C++ Generate XLSX from PDF](#cpp-pdf-to-xlsx)
- [C++ Create XLSX from PDF](#cpp-pdf-to-xlsx)
- [C++ PDF to XLSX Converter](#cpp-pdf-to-xlsx)
