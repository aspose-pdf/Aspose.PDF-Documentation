---
title: Convert PDF to Excel in Python
linktitle: Convert PDF to Excel
type: docs
weight: 20
url: /python-net/convert-pdf-to-excel/
lastmod: "2026-04-14"
description: Learn how to convert PDF to Excel in Python, including XLS, XLSX, CSV, ODS, single worksheet output, and column handling with Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Convert PDF to Excel, XLSX, CSV, and ODS in Python
Abstract: This article shows how to convert PDF files to spreadsheet formats with Aspose.PDF for Python via .NET. It covers XLS, XLSX, XLSM, CSV, and ODS output, plus options for controlling blank columns and reducing the number of generated worksheets.
---

## Convert PDF to Excel in Python

**Aspose.PDF for Python via .NET** supports converting PDF files to Excel and other spreadsheet formats from Python code.

Use this page when you need to convert a PDF to XLS, XLSX, CSV, or ODS for table extraction, report reuse, sorting, filtering, or downstream analysis. During PDF to Excel conversion, individual PDF pages can be rendered as Excel worksheets.

The first example converts a PDF file to Spreadsheet 2003 XML format. Later sections show XLSX, XLSM, CSV, ODS, and single-worksheet output.

{{% alert color="success" %}}
**Try to convert PDF to Excel online**

Aspose.PDF presents you online application ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to Excel with App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

The following code snippet shows the process for converting PDF file into XLS or XLSX format with Aspose.PDF for Python via .NET.

Steps: Convert a PDF file to an Excel (XML Spreadsheet 2003) format

1. Load the PDF document.
1. Set up Excel save options using [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Save the converted file.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_spread_sheet2003(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convert PDF to XLSX in Python

Steps: Convert a PDF file to an XLSX format (Excel 2007+)

1. Load the PDF document.
1. Set up Excel save options using [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Save the converted file.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convert PDF to XLSX with Column Control

When converting a PDF to an Excel format, a blank column can be added as the first column in the output file. Use the `insert_blank_column_at_first` option of the `ExcelSaveOptions` class to control this behavior. Its default value is `true`.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_control_column(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.insert_blank_column_at_first = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convert PDF to a Single Excel Worksheet

Aspose.PDF for Python via .NET shows how to convert a PDF to an Excel (.xlsx) file, with the 'minimize_the_number_of_worksheets' option enabled.

Steps: Convert PDF to XLS or XLSX Single Worksheet in Python

1. Load the PDF document.
1. Set up Excel save options using [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. The 'minimize_the_number_of_worksheets' option reduces the number of Excel sheets by combining PDF pages into fewer worksheets (e.g., one worksheet for the entire document if possible).
1. Save the converted file.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_single_excel_worksheet(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.minimize_the_number_of_worksheets = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convert PDF to Excel 2007 Macro-Enabled (XLSM)

This Python example shows how to convert a PDF file into an Excel file in XLSM format (Excel Macro-Enabled Workbook).

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_macro(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSM
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convert to other spreadsheet formats

### Convert PDF to CSV

The 'convert_pdf_to_excel_2007_csv' function performs the same operation as before, but this time the target format is CSV (Comma-Separated Values) instead of XLSM.

Steps: Convert PDF to CSV in Python

1. Create an instance of [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object with the source PDF document.
1. Create an instance of [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) with **ExcelSaveOptions.ExcelFormat.CSV**
1. Save it to **CSV** format by calling [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* method and passing it [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_csv(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.CSV
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convert PDF to ODS

Steps: Convert PDF to ODS in Python

1. Create an instance of [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object with the source PDF document.
1. Create an instance of [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) with **ExcelSaveOptions.ExcelFormat.ODS**
1. Save it to **ODS** format by calling [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method and passing it [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

Conversion to ODS format performs in the same way as all other formats.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_ods(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.ODS
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Related conversions

- [Convert PDF to Word](/pdf/python-net/convert-pdf-to-word/) if your priority is editable text flow rather than spreadsheet structure.
- [Convert PDF to HTML](/pdf/python-net/convert-pdf-to-html/) when you need browser-friendly output.
- [Convert PDF to other formats](/pdf/python-net/convert-pdf-to-other-files/) for EPUB, Markdown, text, XPS, and related export workflows.
