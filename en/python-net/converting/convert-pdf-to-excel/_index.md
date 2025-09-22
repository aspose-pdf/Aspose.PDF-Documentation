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

## PDF to EXCEL conversion via Python

**Aspose.PDF for Python via .NET** support the feature of converting PDF files to Excel, and CSV formats.

Aspose.PDF for Python via .NET is a PDF manipulation component, we have introduced a feature that renders PDF file to Excel workbook (XLSX files). During this conversion, the individual pages of the PDF file are converted to Excel worksheets.

{{% alert color="success" %}}
**Try to convert PDF to Excel online**

Aspose.PDF presents you online free application ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

The following code snippet shows the process for converting PDF file into XLS or XLSX format with Aspose.PDF for Python via .NET.

Steps: Convert a PDF file to an Excel (XML Spreadsheet 2003) format

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

Steps: Convert a PDF file to an XLSX format (Excel 2007+)

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

Steps: Convert PDF to XLS or XLSX Single Worksheet in Python

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

Steps: Convert PDF to CSV in Python

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

Steps: Convert PDF to ODS in Python

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
