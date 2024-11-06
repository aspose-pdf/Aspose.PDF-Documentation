---
title: 使用Python将PDF转换为Excel
linktitle: 将PDF转换为Excel
type: docs
weight: 20
url: zh/python-net/convert-pdf-to-excel/
lastmod: "2022-12-23"
keywords: 使用python将PDF转换为Excel, 使用python将PDF转换为XLS, 使用python将PDF转换为XLSX, 在python中从PDF导出表格到Excel。
description: Aspose.PDF for Python库允许您使用Python将PDF格式转换为Excel格式。这些格式包括XLS, XLSX, XML 2003电子表格, CSV, ODS。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 概述

本文解释了如何使用Python将**PDF转换为Excel格式**。它涵盖了以下主题。

_格式_: **XLS**

- [Python PDF到XLS](#python-pdf-to-xls)
- [Python 将PDF转换为XLS](#python-pdf-to-xls)
- [Python 如何将PDF文件转换为XLS](#python-pdf-to-xls)

_格式_: **XLSX**

- [Python PDF到XLSX](#python-pdf-to-xlsx)
- [Python 将PDF转换为XLSX](#python-pdf-to-xlsx)
- [Python 如何将PDF文件转换为XLSX](#python-pdf-to-xlsx)

_格式_: **Excel**

- [Python PDF to Excel](#python-pdf-to-xlsx)
- [Python PDF to Excel XLS](#python-pdf-to-xls)
- [Python PDF to Excel XLSX](#python-pdf-to-xlsx)

_格式_: **CSV**

- [Python PDF to CSV](#python-pdf-to-csv)
- [Python Convert PDF to CSV](#python-pdf-to-csv)
- [Python How to convert PDF file to CSV](#python-pdf-to-csv)

_格式_: **ODS**

- [Python PDF to ODS](#python-pdf-to-ods)
- [Python Convert PDF to ODS](#python-pdf-to-ods)
- [Python How to convert PDF file to ODS](#python-pdf-to-ods)

## 通过 Python 进行 PDF 转换为 EXCEL

**Aspose.PDF for Python via .NET** 支持将 PDF 文件转换为 Excel 和 CSV 格式的功能。

Aspose.PDF for Python via .NET 是一个 PDF 操作组件，我们引入了一项功能，可以将 PDF 文件渲染为 Excel 工作簿（XLSX 文件）。在此转换过程中，PDF 文件的各个页面被转换为 Excel 工作表。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 Excel**

Aspose.PDF 为您提供了在线免费应用程序 ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)，您可以尝试调查其功能和工作质量。

[![Aspose.PDF 转换 PDF 为 Excel 的免费应用](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

以下代码片段展示了如何使用 Aspose.PDF for Python via .NET 将 PDF 文件转换为 XLS 或 XLSX 格式的过程。

<a name="python-pdf-to-xls"><strong>步骤：在 Python 中将 PDF 转换为 XLS</strong></a>

1. 使用源 PDF 文档创建 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象的实例。
2. 创建 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) 的实例。
3. 通过调用 [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法并传递 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)，指定 **.xls 扩展名** 将其保存为 **XLS** 格式。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xls.xls"
    # 打开 PDF 文档
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003

    # 将文件保存为 MS Excel 格式
    document.save(output_pdf, save_option)
```


<a name="python-pdf-to-xlsx"><strong>步骤：在 Python 中将 PDF 转换为 XLSX</strong></a>

1. 使用源 PDF 文档创建 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象的实例。
2. 创建 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) 的实例。
3. 调用 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法并传递 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)，将其保存为 **XLSX** 格式并指定 **.xlsx 扩展名**。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_xlsx.xlsx"
    # 打开 PDF 文档
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()

    # 将文件保存为 MS Excel 格式
    document.save(output_pdf, save_option)
```

## 将 PDF 转换为具有控制列的 XLS

当将 PDF 转换为 XLS 格式时，空白列作为第一列添加到输出文件中。
 在 'ExcelSaveOptions class' 中，InsertBlankColumnAtFirst 选项用于控制此列。其默认值为 true。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xlsx_with_control_column.xls"
    # 打开 PDF 文档
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    save_option.insert_blank_column_at_first = True

    # 将文件保存为 MS Excel 格式
    document.save(output_pdf, save_option)
```

## 将 PDF 转换为单个 Excel 工作表

将包含大量页面的 PDF 文件导出为 XLS 时，每页都会导出到 Excel 文件中的不同工作表。这是因为 MinimizeTheNumberOfWorksheets 属性默认设置为 false。为了确保所有页面都导出到输出 Excel 文件中的一个工作表，请将 MinimizeTheNumberOfWorksheets 属性设置为 true。

<a name="python-pdf-to-excel-single"><strong>步骤：在 Python 中将 PDF 转换为 XLS 或 XLSX 单个工作表</strong></a>
1. 创建一个 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象的实例，使用源 PDF 文档。
2. 创建一个 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) 的实例，设置 **MinimizeTheNumberOfWorksheets = true**。
3. 调用 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法并传递 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)，将其保存为具有单个工作表的 **XLS** 或 **XLSX** 格式。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xlsx_single_excel_worksheet.xls"
    # 打开 PDF 文档
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    save_option.minimize_the_number_of_worksheets = True

    # 将文件保存为 MS Excel 格式
    document.save(output_pdf, save_option)

```


## 转换为其他电子表格格式

### 转换为 CSV

转换为 CSV 格式的操作与上述方法相同。你需要做的就是设置适当的格式。

<a name="python-pdf-to-csv"><strong>步骤：在 Python 中将 PDF 转换为 CSV</strong></a>

1. 使用源 PDF 文档创建 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象的实例。
2. 创建 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) 的实例，并设置 **Format = ExcelSaveOptions.ExcelFormat.CSV**。
3. 通过调用 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法并传递 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)，将其保存为 **CSV** 格式。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_csv.csv"
    # 打开 PDF 文档
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.CSV

    # 保存文件
    document.save(output_pdf, save_option)
```


### 转换为 ODS

<a name="python-pdf-to-ods"><strong>步骤：在 Python 中将 PDF 转换为 ODS</strong></a>

1. 使用源 PDF 文档创建 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象的实例。
2. 使用 **Format = ExcelSaveOptions.ExcelFormat.ODS** 创建 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) 的实例。
3. 通过调用 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法并传递 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) 将其保存为 **ODS** 格式。

转换为 ODS 格式的过程与其他格式相同。

```python

    import aspose.pdf as ap
    
    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_ods.ods"
    # 打开 PDF 文档
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.ODS

    # 保存文件
    document.save(output_pdf, save_option)
```


## 另请参阅

本文还涵盖这些主题。代码与上面相同。

_格式_：**Excel**
- [Python PDF 到 Excel 代码](#python-pdf-to-xlsx)
- [Python PDF 到 Excel API](#python-pdf-to-xlsx)
- [Python PDF 到 Excel 编程](#python-pdf-to-xlsx)
- [Python PDF 到 Excel 库](#python-pdf-to-xlsx)
- [Python 将 PDF 保存为 Excel](#python-pdf-to-xlsx)
- [Python 从 PDF 生成 Excel](#python-pdf-to-xlsx)
- [Python 从 PDF 创建 Excel](#python-pdf-to-xlsx)
- [Python PDF 到 Excel 转换器](#python-pdf-to-xlsx)

_格式_：**XLS**
- [Python PDF 到 XLS 代码](#python-pdf-to-xls)
- [Python PDF 到 XLS API](#python-pdf-to-xls)
- [Python PDF 到 XLS 编程](#python-pdf-to-xls)
- [Python PDF 到 XLS 库](#python-pdf-to-xls)
- [Python 将 PDF 保存为 XLS](#python-pdf-to-xls)
- [Python 从 PDF 生成 XLS](#python-pdf-to-xls)
- [Python 从 PDF 创建 XLS](#python-pdf-to-xls)
- [Python PDF 到 XLS 转换器](#python-pdf-to-xls)

_格式_：**XLSX**

- [Python PDF 到 XLSX 代码](#python-pdf-to-xlsx)
- [Python PDF to XLSX API](#python-pdf-to-xlsx)
- [Python PDF to XLSX Programmatically](#python-pdf-to-xlsx)
- [Python PDF to XLSX Library](#python-pdf-to-xlsx)
- [Python Save PDF as XLSX](#python-pdf-to-xlsx)
- [Python Generate XLSX from PDF](#python-pdf-to-xlsx)
- [Python Create XLSX from PDF](#python-pdf-to-xlsx)
- [Python PDF to XLSX Converter](#python-pdf-to-xlsx)

_格式_: **CSV**
- [Python PDF to CSV Code](#python-pdf-to-csv)
- [Python PDF to CSV API](#python-pdf-to-csv)
- [Python PDF to CSV Programmatically](#python-pdf-to-csv)
- [Python PDF to CSV Library](#python-pdf-to-csv)
- [Python Save PDF as CSV](#python-pdf-to-csv)
- [Python Generate CSV from PDF](#python-pdf-to-csv)
- [Python Create CSV from PDF](#python-pdf-to-csv)
- [Python PDF to CSV Converter](#python-pdf-to-csv)

_格式_: **ODS**
- [Python PDF to ODS Code](#python-pdf-to-ods)
- [Python PDF to ODS API](#python-pdf-to-ods)
- [Python PDF to ODS Programmatically](#python-pdf-to-ods)
- [Python PDF to ODS Library](#python-pdf-to-ods)

- [Python Save PDF as ODS](#python-pdf-to-ods)
- [Python 从 PDF 生成 ODS](#python-pdf-to-ods)
- [Python 从 PDF 创建 ODS](#python-pdf-to-ods)
- [Python PDF 到 ODS 转换器](#python-pdf-to-ods)