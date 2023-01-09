---
title: Convert PDF to Excel in Python
linktitle: Convert PDF to Excel
type: docs
weight: 20
url: /python-net/convert-pdf-to-excel/
lastmod: "2022-12-23"
keywords: convert PDF to Excel using python, convert PDF to XLS using python, convert PDF to XLSX using python, export table from PDF to Excel in python.
description: Aspose.PDF for Python library allows you to convert PDF to Excel format using Python. These formats include XLS, XLSX, XML 2003 Spreadsheet, CSV, ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Overview

This article explains how to **convert PDF to Excel formats using Python**. It covers the following topics.

_Format_: **XLS**
- [Python PDF to XLS](#python-pdf-to-xls)
- [Python Convert PDF to XLS](#python-pdf-to-xls)
- [Python How to convert PDF file to XLS](#python-pdf-to-xls)

_Format_: **XLSX**
- [Python PDF to XLSX](#python-pdf-to-xlsx)
- [Python Convert PDF to XLSX](#python-pdf-to-xlsx)
- [Python How to convert PDF file to XLSX](#python-pdf-to-xlsx)

_Format_: **Excel**
- [Python PDF to Excel](#python-pdf-to-xlsx)
- [Python PDF to Excel XLS](#python-pdf-to-xls)
- [Python PDF to Excel XLSX](#python-pdf-to-xlsx)

_Format_: **CSV**
- [Python PDF to CSV](#python-pdf-to-csv)
- [Python Convert PDF to CSV](#python-pdf-to-csv)
- [Python How to convert PDF file to CSV](#python-pdf-to-csv)

_Format_: **ODS**
- [Python PDF to ODS](#python-pdf-to-ods)
- [Python Convert PDF to ODS](#python-pdf-to-ods)
- [Python How to convert PDF file to ODS](#python-pdf-to-ods)

## PDF to EXCEL conversion via Python

**Aspose.PDF for Python via .NET** support the feature of converting PDF files to Excel, and CSV formats.

Aspose.PDF for Python via .NET is a PDF manipulation component, we have introduced a feature that renders PDF file to Excel workbook (XLSX files). During this conversion, the individual pages of the PDF file are converted to Excel worksheets.

{{% alert color="success" %}}
**Try to convert PDF to Excel online**

Aspose.PDF presents you online free application ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

The following code snippet shows the process for converting PDF file into XLS or XLSX format with Aspose.PDF for Python via .NET.

<a name="python-pdf-to-xls"><strong>Steps: Convert PDF to XLS in Python</strong></a>

1. Create an instance of **Document** object with the source PDF document.
2. Create an instance of **ExcelSaveOptions**.
3. Save it to **XLS** format specifying **.xls extension** by calling **Document.Save()** method and passing it **ExcelSaveOptions**

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xls.xls"
    # Open PDF document
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003

    # Save the file into MS Excel format
    document.save(output_pdf, save_option)
```


<a name="python-pdf-to-xlsx"><strong>Steps: Convert PDF to XLSX in Python</strong></a>

1. Create an instance of **Document** object with the source PDF document.
2. Create an instance of **ExcelSaveOptions**.
3. Save it to **XLSX** format specifying **.xlsx extension** by calling **Document.Save()** method and passing it **ExcelSaveOptions**

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_xlsx.xlsx"
    # Open PDF document
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()

    # Save the file into MS Excel format
    document.save(output_pdf, save_option)
```

## Convert PDF to XLS with control Column

When converting a PDF to XLS format, a blank column is added to the output file as first column. The in 'ExcelSaveOptions class' InsertBlankColumnAtFirst option is used to control this column. Its default value is true.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xlsx_with_control_column.xls"
    # Open PDF document
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    save_option.insert_blank_column_at_first = True

    # Save the file into MS Excel format
    document.save(output_pdf, save_option)
```

## Convert PDF to Single Excel Worksheet

When exporting a PDF file with a lot of pages to XLS, each page is exported to a different sheet in the Excel file. This is because the MinimizeTheNumberOfWorksheets property is set to false by default. To ensure that all pages are exported to one single sheet in the output Excel file, set the MinimizeTheNumberOfWorksheets property to true.

<a name="python-pdf-to-excel-single"><strong>Steps: Convert PDF to XLS or XLSX Single Worksheet in Python</strong></a>

1. Create an instance of **Document** object with the source PDF document.
2. Create an instance of **ExcelSaveOptions** with **MinimizeTheNumberOfWorksheets = true**.
3. Save it to **XLS** or **XLSX** format having single worksheet by calling **Document.Save()** method and passing it **ExcelSaveOptions**.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xlsx_single_excel_worksheet.xls"
    # Open PDF document
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    save_option.minimize_the_number_of_worksheets = True

    # Save the file into MS Excel format
    document.save(output_pdf, save_option)

```

## Convert to other spreadsheet formats

### Convert to CSV

Conversion to CSV format performs in the same way as above. All is what you need - set the appropriate format.

<a name="python-pdf-to-csv"><strong>Steps: Convert PDF to CSV in Python</strong></a>

1. Create an instance of **Document** object with the source PDF document.
2. Create an instance of **ExcelSaveOptions** with **Format = ExcelSaveOptions.ExcelFormat.CSV**
3. Save it to **CSV** format by calling **Document.Save()** method and passing it **ExcelSaveOptions**.


```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_csv.csv"
    # Open PDF document
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.CSV

    # Save the file
    document.save(output_pdf, save_option)
```

### Convert to ODS

<a name="python-pdf-to-ods"><strong>Steps: Convert PDF to ODS in Python</strong></a>

1. Create an instance of **Document** object with the source PDF document.
2. Create an instance of **ExcelSaveOptions** with **Format = ExcelSaveOptions.ExcelFormat.ODS**
3. Save it to **ODS** format by calling **Document.Save()** method and passing it **ExcelSaveOptions**.


Conversion to ODS format performs in the same way as all other formats.

```python

    import aspose.pdf as ap
    
    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_ods.ods"
    # Open PDF document
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.ODS

    # Save the file
    document.save(output_pdf, save_option)
```

## See Also 

This article also covers these topics. The codes are same as above.

_Format_: **Excel**
- [Python PDF to Excel Code](#python-pdf-to-xlsx)
- [Python PDF to Excel API](#python-pdf-to-xlsx)
- [Python PDF to Excel Programmatically](#python-pdf-to-xlsx)
- [Python PDF to Excel Library](#python-pdf-to-xlsx)
- [Python Save PDF as Excel](#python-pdf-to-xlsx)
- [Python Generate Excel from PDF](#python-pdf-to-xlsx)
- [Python Create Excel from PDF](#python-pdf-to-xlsx)
- [Python PDF to Excel Converter](#python-pdf-to-xlsx)

_Format_: **XLS**
- [Python PDF to XLS Code](#python-pdf-to-xls)
- [Python PDF to XLS API](#python-pdf-to-xls)
- [Python PDF to XLS Programmatically](#python-pdf-to-xls)
- [Python PDF to XLS Library](#python-pdf-to-xls)
- [Python Save PDF as XLS](#python-pdf-to-xls)
- [Python Generate XLS from PDF](#python-pdf-to-xls)
- [Python Create XLS from PDF](#python-pdf-to-xls)
- [Python PDF to XLS Converter](#python-pdf-to-xls)

_Format_: **XLSX**
- [Python PDF to XLSX Code](#python-pdf-to-xlsx)
- [Python PDF to XLSX API](#python-pdf-to-xlsx)
- [Python PDF to XLSX Programmatically](#python-pdf-to-xlsx)
- [Python PDF to XLSX Library](#python-pdf-to-xlsx)
- [Python Save PDF as XLSX](#python-pdf-to-xlsx)
- [Python Generate XLSX from PDF](#python-pdf-to-xlsx)
- [Python Create XLSX from PDF](#python-pdf-to-xlsx)
- [Python PDF to XLSX Converter](#python-pdf-to-xlsx)

_Format_: **CSV**
- [Python PDF to CSV Code](#python-pdf-to-csv)
- [Python PDF to CSV API](#python-pdf-to-csv)
- [Python PDF to CSV Programmatically](#python-pdf-to-csv)
- [Python PDF to CSV Library](#python-pdf-to-csv)
- [Python Save PDF as CSV](#python-pdf-to-csv)
- [Python Generate CSV from PDF](#python-pdf-to-csv)
- [Python Create CSV from PDF](#python-pdf-to-csv)
- [Python PDF to CSV Converter](#python-pdf-to-csv)

_Format_: **ODS**
- [Python PDF to ODS Code](#python-pdf-to-ods)
- [Python PDF to ODS API](#python-pdf-to-ods)
- [Python PDF to ODS Programmatically](#python-pdf-to-ods)
- [Python PDF to ODS Library](#python-pdf-to-ods)
- [Python Save PDF as ODS](#python-pdf-to-ods)
- [Python Generate ODS from PDF](#python-pdf-to-ods)
- [Python Create ODS from PDF](#python-pdf-to-ods)
- [Python PDF to ODS Converter](#python-pdf-to-ods)
