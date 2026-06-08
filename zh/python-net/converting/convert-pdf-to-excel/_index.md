---
title: 在 Python 中将 PDF 转换为 Excel
linktitle: 将 PDF 转换为 Excel
type: docs
weight: 20
url: /zh/python-net/convert-pdf-to-excel/
lastmod: "2026-06-08"
description: 了解如何在 Python 中使用 Aspose.PDF 将 PDF 转换为 Excel，包括 XLS、XLSX、CSV、ODS，单工作表输出以及列处理。
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中将 PDF 转换为 Excel、XLSX、CSV 和 ODS
Abstract: 本文展示了如何使用 Aspose.PDF for Python via .NET 将 PDF 文件转换为电子表格格式。它涵盖了 XLS、XLSX、XLSM、CSV 和 ODS 输出，以及控制空列和减少生成工作表数量的选项。
---

## 在 Python 中将 PDF 转换为 Excel

**Aspose.PDF for Python via .NET** 支持从 Python 代码将 PDF 文件转换为 Excel 和其他电子表格格式。

当您需要将 PDF 转换为 XLS、XLSX、CSV 或 ODS 进行表格提取、报告复用、排序、过滤或下游分析时，请使用此页面。在 PDF 转 Excel 转换过程中，单个 PDF 页面可以渲染为 Excel 工作表。

第一个示例将 PDF 文件转换为 Spreadsheet 2003 XML 格式。后面的章节展示了 XLSX、XLSM、CSV、ODS，以及单工作表输出。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 Excel**

Aspose.PDF 为您提供在线应用程序 ["PDF 转 XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)，在此您可以尝试调查其功能以及其工作质量。

[![Aspose.PDF 将 PDF 转换为 Excel 的应用](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

以下代码片段展示了使用 Aspose.PDF for Python via .NET 将 PDF 文件转换为 XLS 或 XLSX 格式的过程。

步骤：将 PDF 文件转换为 Excel（XML 电子表格 2003）格式

1. 加载 PDF 文档。
1. 使用设置 Excel 保存选项 [Excel保存选项](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. 保存已转换的文件。

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

## 在 Python 中将 PDF 转换为 XLSX

步骤：将 PDF 文件转换为 XLSX 格式（Excel 2007+）

1. 加载 PDF 文档。
1. 使用设置 Excel 保存选项 [Excel保存选项](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. 保存已转换的文件。

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

## 将 PDF 转换为 XLSX 并进行列控制

在将 PDF 转换为 Excel 格式时，可以在输出文件的第一列添加一个空列。使用 `insert_blank_column_at_first` 选项的 `ExcelSaveOptions` 用于控制此行为的类。其默认值是 `true`.

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

## 将 PDF 转换为单个 Excel 工作表

Aspose.PDF for Python via .NET 展示了如何将 PDF 转换为 Excel (.xlsx) 文件，并启用了 'minimize_the_number_of_worksheets' 选项。

步骤：在 Python 中将 PDF 转换为单个工作表的 XLS 或 XLSX

1. 加载 PDF 文档。
1. 使用设置 Excel 保存选项 [Excel保存选项](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. 'minimize_the_number_of_worksheets' 选项通过将 PDF 页面合并到更少的工作表中来减少 Excel 工作表的数量（例如，如果可能的话，整个文档使用一个工作表）。
1. 保存已转换的文件。

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

## 将 PDF 转换为 Excel 2007 宏启用文件 (XLSM)

此 Python 示例展示了如何将 PDF 文件转换为 XLSM 格式的 Excel 文件（Excel 宏启用工作簿）。

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

## 转换为其他电子表格格式

### 将 PDF 转换为 CSV

'convert_pdf_to_excel_2007_csv' 函数执行与之前相同的操作，但这次目标格式是 CSV（逗号分隔值），而不是 XLSM。

步骤：在 Python 中将 PDF 转换为 CSV

1. 创建实例 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 包含源 PDF 文档的对象。
1. 创建实例 [Excel保存选项](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) 使用 **ExcelSaveOptions.ExcelFormat.CSV**
1. 通过调用将其保存为 **CSV** 格式 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* 方法并传递它 [Excel保存选项](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

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

### 将 PDF 转换为 ODS

步骤：在Python中将PDF转换为ODS

1. 创建实例 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 包含源 PDF 文档的对象。
1. 创建实例 [Excel保存选项](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) 使用 **ExcelSaveOptions.ExcelFormat.ODS**
1. 通过调用将其保存为 **ODS** 格式 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法和传递它 [Excel保存选项](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

转换为 ODS 格式的方式与所有其他格式相同。

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

## 相关转换

- [转换 PDF 为 Word](/pdf/zh/python-net/convert-pdf-to-word/) 如果你的优先考虑是可编辑的文本流，而不是电子表格结构。
- [将 PDF 转换为 HTML](/pdf/zh/python-net/convert-pdf-to-html/) 当您需要浏览器友好的输出时。
- [将 PDF 转换为其他格式](/pdf/zh/python-net/convert-pdf-to-other-files/) 用于 EPUB、Markdown、文本、XPS 以及相关的导出工作流。
