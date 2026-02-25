---
title: 在 Python 中将 PDF 转换为 Excel
linktitle: 将 PDF 转换为 Excel
type: docs
weight: 20
url: /zh/python-net/convert-pdf-to-excel/
lastmod: "2025-09-27"
description: 使用 Aspose.PDF for Python via .NET 轻松将 PDF 转换为 Excel 电子表格。请遵循本指南进行准确的 PDF 转 XLSX 转换
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何在 Python 中将 PDF 转换为 Excel
Abstract: 本篇文章提供了使用 Python（尤其是 Aspose.PDF for Python via .NET 库）将 PDF 文件转换为多种 Excel 格式的综合指南。文中详细说明了 XLS、XLSX、CSV 和 ODS 格式的转换过程。文档阐述了将 PDF 转换为 XLS 和 XLSX 所需的步骤，重点介绍了创建 Document 和 ExcelSaveOptions 实例，以及使用 Document.Save() 方法指定输出格式。文章还讨论了控制插入空列和在转换期间最小化工作表数量等功能。此外，还提供了将 PDF 转换为单个 Excel 工作表以及其他格式（如 CSV 和 ODS）的示例，强调了 Aspose.PDF 的灵活性和功能性。文中还提到了一款在线的 PDF 转 XLSX 工具，供用户体验转换质量。文章最后列出了相关主题和代码片段，以进一步帮助读者理解并在编程中实现这些转换。
---

## 使用 Python 将 PDF 转换为 EXCEL

**Aspose.PDF for Python via .NET** 支持将 PDF 文件转换为 Excel 和 CSV 格式的功能。

Aspose.PDF for Python via .NET 是一款 PDF 操作组件，我们引入了一项功能，可将 PDF 文件渲染为 Excel 工作簿（XLSX 文件）。在此转换过程中，PDF 文件的各个页面会被转换为 Excel 工作表。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 Excel**

Aspose.PDF 为您提供在线免费应用 ["PDF 转 XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)，您可以尝试了解其功能和质量。

[![Aspose.PDF 将 PDF 转换为 Excel 的免费应用](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

以下代码片段展示了使用 Aspose.PDF for Python via .NET 将 PDF 文件转换为 XLS 或 XLSX 格式的过程。

步骤：将 PDF 文件转换为 Excel（XML Spreadsheet 2003）格式

1. 加载 PDF 文档。
1. 使用 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) 设置 Excel 保存选项。
1. 保存转换后的文件。

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

步骤：将 PDF 文件转换为 XLSX 格式（Excel 2007+）

1. 加载 PDF 文档。
1. 使用 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) 设置 Excel 保存选项。
1. 保存转换后的文件。

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

## 将 PDF 转换为 XLS 并控制列

将 PDF 转换为 XLS 格式时，输出文件的第一列会添加一个空列。'ExcelSaveOptions 类' 中的 'insert_blank_column_at_first' 选项用于控制此列。默认值为 true。

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

## 将 PDF 转换为单个 Excel 工作表

Aspose.PDF for Python via .NET 展示了如何将 PDF 转换为 Excel（.xlsx）文件，并启用了 'minimize_the_number_of_worksheets' 选项。

步骤：在 Python 中将 PDF 转换为 XLS 或 XLSX 单工作表

1. 加载 PDF 文档。
1. 使用 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) 设置 Excel 保存选项。
1. 'minimize_the_number_of_worksheets' 选项通过将 PDF 页面合并为更少的工作表来减少 Excel 工作表的数量（例如，若可能，则整篇文档只有一个工作表）。
1. 保存转换后的文件。

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

## 将 PDF 文件转换为 XLSM 格式的 Excel 文件

此 Python 示例展示了如何将 PDF 文件转换为 XLSM 格式（Excel 宏启用工作簿）的 Excel 文件。

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

## 转换为其他电子表格格式

### 转换为 CSV

'convert_pdf_to_excel_2007_csv' 函数执行与之前相同的操作，但此时目标格式为 CSV（逗号分隔值），而非 XLSM。

步骤：在 Python 中将 PDF 转换为 CSV

1. 使用源 PDF 文档创建 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象的实例。
1. 使用 **ExcelSaveOptions.ExcelFormat.CSV** 创建 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) 实例。
1. 通过调用 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* 方法并传入 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)，将其保存为 **CSV** 格式。

```python

from os import path
import aspose.pdf as apdf

def convert_pdf_to_excel_2007_csv(infile, outfile):
    path_infile = path.join(data_dir, infile)
    path_outfile = path.join(data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### 转换为 ODS

步骤：在 Python 中将 PDF 转换为 ODS

1. 使用源 PDF 文档创建一个 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象的实例。
1. 使用 **ExcelSaveOptions.ExcelFormat.ODS** 创建一个 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) 的实例。
1. 通过调用 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法并传入 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/)，将其保存为 **ODS** 格式。

转换为 ODS 格式的方式与所有其他格式相同。

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

