---
title: Convert PDF to Excel in Python
linktitle: Convert PDF to Excel
type: docs
weight: 20
url: /python-net/convert-pdf-to-excel/
lastmod: "2025-09-27"
description: Convert PDFs to Excel spreadsheets effortlessly with Aspose.PDF for Python via .NET. Follow this guide for accurate PDF to XLSX conversions
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to Convert PDF to Excel in Python
Abstract: This article provides a comprehensive guide on converting PDF files to various Excel formats using Python, specifically with the Aspose.PDF for Python via .NET library. It details the conversion processes for XLS, XLSX, CSV, and ODS formats. The document explains the steps needed to convert PDF to XLS and XLSX, highlighting the creation of Document and ExcelSaveOptions instances, and the use of the Document.Save() method to specify output formats. The article also discusses features such as controlling the insertion of blank columns and minimizing worksheet numbers during conversion. Additionally, it provides examples of converting PDFs to single Excel worksheets and other formats like CSV and ODS, emphasizing the flexibility and functionality of Aspose.PDF. An online tool for PDF to XLSX conversion is also mentioned, allowing users to explore the conversion quality. The article concludes with a list of related topics and code snippets to further aid in understanding and implementing these conversions programmatically.
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

<a name="python-pdf-to-xls"><strong>Steps: Convert a PDF file to an Excel (XML Spreadsheet 2003) format</strong></a>

1. Load the PDF document.
1. Set up Excel save options using [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Save the converted file.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

<a name="python-pdf-to-xlsx"><strong>Steps: Convert a PDF file to an XLSX format (Excel 2007+)</strong></a>

1. Load the PDF document.
1. Set up Excel save options using [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Save the converted file.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSX
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convert PDF to XLS with control Column

When converting a PDF to XLS format, a blank column is added to the output file as first column. The in 'ExcelSaveOptions class' 'insert_blank_column_at_first' option is used to control this column. Its default value is true.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.insert_blank_column_at_first = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convert PDF to Single Excel Worksheet

Aspose.PDF for Python via .NET shows how to convert a PDF to an Excel (.xlsx) file, with the 'minimize_the_number_of_worksheets' option enabled.

<a name="python-pdf-to-excel-single"><strong>Steps: Convert PDF to XLS or XLSX Single Worksheet in Python</strong></a>

1. Load the PDF document.
1. Set up Excel save options using [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. The 'minimize_the_number_of_worksheets' option reduces the number of Excel sheets by combining PDF pages into fewer worksheets (e.g., one worksheet for the entire document if possible).
1. Save the converted file.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.minimize_the_number_of_worksheets = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convert PDF file into an Excel file in XLSM format

This Python example shows how to convert a PDF file into an Excel file in XLSM format (Excel Macro-Enabled Workbook).

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSM
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convert to other spreadsheet formats

### Convert to CSV

The 'convert_pdf_to_excel_2007_csv' function performs the same operation as before, but this time the target format is CSV (Comma-Separated Values) instead of XLSM.

<a name="python-pdf-to-csv"><strong>Steps: Convert PDF to CSV in Python</strong></a>

1. Create an instance of [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object with the source PDF document.
1. Create an instance of [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) with **ExcelSaveOptions.ExcelFormat.CSV**
1. Save it to **CSV** format by calling [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* method and passing it [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convert to ODS

<a name="python-pdf-to-ods"><strong>Steps: Convert PDF to ODS in Python</strong></a>

1. Create an instance of [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object with the source PDF document.
1. Create an instance of [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) with **ExcelSaveOptions.ExcelFormat.ODS**
1. Save it to **ODS** format by calling [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method and passing it [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

Conversion to ODS format performs in the same way as all other formats.

```python

    from os import path
    import aspose.pdf as apdf
    
    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.ODS
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
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
