---
title: Convert PDF to Excel in Python
linktitle: Convert PDF to Excel
type: docs
weight: 20
url: /python-java/convert-pdf-to-excel/
lastmod: "2022-12-23"
description: Learn how to convert PDFs to Excel files using Aspose.PDF for Python via Java. Achieve precision and efficiency with our comprehensive tutorial.
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

Aspose.PDF for Python via Java is a PDF manipulation component, we have introduced a feature that renders PDF file to Excel workbook (XLSX files). During this conversion, the individual pages of the PDF file are converted to Excel worksheets.

{{% alert color="success" %}}
**Try to convert PDF to Excel online**

Aspose.PDF presents you online free application ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

The following code snippet shows the process for converting PDF file into XLS or XLSX format with Aspose.PDF for Python via Java.

<a name="python-pdf-to-xls"><strong>Steps: Convert PDF to XLS in Python</strong></a>

1. Create an instance of [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) object with the source PDF document.
2. Create an instance of [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).
3. Save it to **XLS** format specifying **.xls extension** by calling [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) method and passing it [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

```python



from asposepdf import Api


# init license
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# conversion from byte array
documentName = "testdata/source.pdf"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array)
documentOutName = "testout/result1.xls"
doc.save(documentOutName, Api.SaveFormat.Excel)

# conversion from file
documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result2.xls"
doc.save(documentOutName, Api.SaveFormat.Excel)


# conversion from byte array
documentName = "testdata/source.pdf"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array)
documentOutName = "testout/result3.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
doc.save(documentOutName, Api.SaveFormat.Excel)

# conversion from file
documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result4.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
doc.save(documentOutName, Api.SaveFormat.Excel)
```


<a name="python-pdf-to-xlsx"><strong>Steps: Convert PDF to XLSX in Python</strong></a>

1. Create an instance of [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) object with the source PDF document.
2. Create an instance of [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).
3. Save it to **XLSX** format specifying **.xlsx extension** by calling [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) method and passing it [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.xlsx"
doc.save(documentOutName, save_option)
```

## Convert PDF to XLS with control Column

When converting a PDF to XLS format, a blank column is added to the output file as first column. The in 'ExcelSaveOptions class' InsertBlankColumnAtFirst option is used to control this column. Its default value is true.

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.xlsx"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
save_option._insertBlankColumnAtFirst = True
doc.save(documentOutName, save_option)

```

## Convert PDF to Single Excel Worksheet

When exporting a PDF file with a lot of pages to XLS, each page is exported to a different sheet in the Excel file. This is because the MinimizeTheNumberOfWorksheets property is set to false by default. To ensure that all pages are exported to one single sheet in the output Excel file, set the MinimizeTheNumberOfWorksheets property to true.

<a name="python-pdf-to-excel-single"><strong>Steps: Convert PDF to XLS or XLSX Single Worksheet in Python</strong></a>

1. Create an instance of [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) object with the source PDF document.
2. Create an instance of [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) with **MinimizeTheNumberOfWorksheets = True**.
3. Save it to **XLS** or **XLSX** format having single worksheet by calling [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) method and passing it [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
save_option._minimizeTheNumberOfWorksheets = True
# Save the file into MS Excel format
doc.save(documentOutName, save_option)

```

## Convert to other spreadsheet formats

### Convert to CSV

Conversion to CSV format performs in the same way as above. All is what you need - set the appropriate format.

<a name="python-pdf-to-csv"><strong>Steps: Convert PDF to CSV in Python</strong></a>

1. Create an instance of [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object with the source PDF document.
2. Create an instance of [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) with **Format = ExcelSaveOptions.ExcelFormat.CSV**
3. Save it to **CSV** format by calling [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods)* method and passing it [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).


```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.csv"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.CSV
doc.save(documentOutName, save_option)
```

### Convert to ODS

<a name="python-pdf-to-ods"><strong>Steps: Convert PDF to ODS in Python</strong></a>

1. Create an instance of [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object with the source PDF document.
2. Create an instance of [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) with **Format = ExcelSaveOptions.ExcelFormat.ODS**
3. Save it to **ODS** format by calling [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) method and passing it [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).


Conversion to ODS format performs in the same way as all other formats.

```python

from asposepdf import Api

documentName = "../../testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "../../testout/result1.ods"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.ODS
doc.save(documentOutName, save_option)
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
