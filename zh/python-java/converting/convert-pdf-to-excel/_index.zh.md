---
title: 使用 Python 将 PDF 转换为 Excel
linktitle: 将 PDF 转换为 Excel
type: docs
weight: 20
url: /python-java/convert-pdf-to-excel/
lastmod: "2022-12-23"
keywords: 使用 Python 将 PDF 转换为 Excel, 使用 Python 将 PDF 转换为 XLS, 使用 Python 将 PDF 转换为 XLSX, 在 Python 中将表格从 PDF 导出到 Excel。
description: Aspose.PDF for Python 库允许您使用 Python 将 PDF 转换为 Excel 格式。这些格式包括 XLS、XLSX、XML 2003 电子表格、CSV、ODS。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 概述

本文解释了如何**使用 Python 将 PDF 转换为 Excel 格式**。它涵盖以下主题。

_格式_: **XLS**
- [Python PDF 到 XLS](#python-pdf-to-xls)
- [Python 将 PDF 转换为 XLS](#python-pdf-to-xls)
- [Python 如何将 PDF 文件转换为 XLS](#python-pdf-to-xls)

_格式_: **XLSX**
- [Python PDF 到 XLSX](#python-pdf-to-xlsx)
- [Python 将 PDF 转换为 XLSX](#python-pdf-to-xlsx)
- [Python 如何将 PDF 文件转换为 XLSX](#python-pdf-to-xlsx)

_格式_: **Excel**
- [Python PDF 转 Excel](#python-pdf-to-xlsx)
- [Python PDF 转 Excel XLS](#python-pdf-to-xls)
- [Python PDF 转 Excel XLSX](#python-pdf-to-xlsx)

_格式_: **CSV**
- [Python PDF 转 CSV](#python-pdf-to-csv)
- [Python 将 PDF 转换为 CSV](#python-pdf-to-csv)
- [Python 如何将 PDF 文件转换为 CSV](#python-pdf-to-csv)

_格式_: **ODS**
- [Python PDF 转 ODS](#python-pdf-to-ods)
- [Python 将 PDF 转换为 ODS](#python-pdf-to-ods)
- [Python 如何将 PDF 文件转换为 ODS](#python-pdf-to-ods)

## 通过 Python 将 PDF 转换为 Excel

**Aspose.PDF for Python via .NET** 支持将 PDF 文件转换为 Excel 和 CSV 格式的功能。

Aspose.PDF for Python via Java 是一个 PDF 操作组件，我们引入了一个功能，可以将 PDF 文件渲染为 Excel 工作簿（XLSX 文件）。在此转换过程中，PDF 文件的各个页面将被转换为 Excel 工作表。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 Excel**

Aspose.PDF 向您提供在线免费应用程序 ["PDF 转 XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)，您可以尝试调查其功能和工作质量。

[![Aspose.PDF Convertion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

以下代码片段展示了使用 Aspose.PDF for Python via Java 将 PDF 文件转换为 XLS 或 XLSX 格式的过程。

<a name="python-pdf-to-xls"><strong>步骤：在 Python 中将 PDF 转换为 XLS</strong></a>

1. 使用源 PDF 文档创建 [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) 对象的实例。
2. 创建 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) 的实例。
3. 通过调用 [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) 方法并传递 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) 将其保存为 **XLS** 格式，指定 **.xls 扩展名**。

```python



from asposepdf import Api


# 初始化许可证
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# 从字节数组转换
documentName = "testdata/source.pdf"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array)
documentOutName = "testout/result1.xls"
doc.save(documentOutName, Api.SaveFormat.Excel)

# 从文件转换
documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result2.xls"
doc.save(documentOutName, Api.SaveFormat.Excel)


# 从字节数组转换
documentName = "testdata/source.pdf"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array)
documentOutName = "testout/result3.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
doc.save(documentOutName, Api.SaveFormat.Excel)

# 从文件转换
documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result4.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
doc.save(documentOutName, Api.SaveFormat.Excel)
```


<a name="python-pdf-to-xlsx"><strong>步骤：在 Python 中将 PDF 转换为 XLSX</strong></a>

1. 使用源 PDF 文档创建 [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) 对象的实例。
2. 创建 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) 的实例。
3. 通过调用 [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) 方法并传递 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) 将其保存为 **XLSX** 格式，指定 **.xlsx 扩展名**。

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.xlsx"
doc.save(documentOutName, save_option)
```

## 转换 PDF 为具有控制列的 XLS

在将 PDF 转换为 XLS 格式时，会在输出文件中添加一个空白列作为第一列。
 在 'ExcelSaveOptions 类' 中，InsertBlankColumnAtFirst 选项用于控制此列。其默认值为 true。

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

## 将 PDF 转换为单个 Excel 工作表

当将包含很多页面的 PDF 文件导出为 XLS 时，每个页面都被导出到 Excel 文件中的不同工作表。这是因为 MinimizeTheNumberOfWorksheets 属性默认设置为 false。为了确保所有页面都导出到输出 Excel 文件中的一个单独的工作表中，将 MinimizeTheNumberOfWorksheets 属性设置为 true。

<a name="python-pdf-to-excel-single"><strong>步骤：在 Python 中将 PDF 转换为 XLS 或 XLSX 单个工作表</strong></a>
1. 创建一个 [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) 对象的实例，使用源 PDF 文档。
2. 创建一个 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) 的实例，并设置 **MinimizeTheNumberOfWorksheets = True**。
3. 通过调用 [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) 方法并传递 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/)，将其保存为具有单个工作表的 **XLS** 或 **XLSX** 格式。

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
save_option._minimizeTheNumberOfWorksheets = True
# 将文件保存为 MS Excel 格式
doc.save(documentOutName, save_option)

```

## 转换为其他电子表格格式

### 转换为 CSV

转化为CSV格式的过程与上述相同。您所需要做的就是设置适当的格式。

<a name="python-pdf-to-csv"><strong>步骤：在Python中将PDF转换为CSV</strong></a>

1. 使用源PDF文档创建一个[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)对象的实例。
2. 创建一个[ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/)实例，设置**Format = ExcelSaveOptions.ExcelFormat.CSV**。
3. 通过调用[Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods)方法并传入[ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/)来保存为**CSV**格式。


```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.csv"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.CSV
doc.save(documentOutName, save_option)
```


### 转换为 ODS

<a name="python-pdf-to-ods"><strong>步骤：在 Python 中将 PDF 转换为 ODS</strong></a>

1. 使用源 PDF 文档创建 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象的实例。
2. 创建 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) 的实例，并设置 **Format = ExcelSaveOptions.ExcelFormat.ODS**
3. 调用 [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) 方法并传递 [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) 将其保存为 **ODS** 格式。

转换为 ODS 格式的过程与其他格式相同。

```python

from asposepdf import Api

documentName = "../../testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "../../testout/result1.ods"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.ODS
doc.save(documentOutName, save_option)
```


## 另请参阅

本文还涵盖这些主题。代码与上述相同。

_格式_: **Excel**
- [Python PDF 转 Excel 代码](#python-pdf-to-xlsx)
- [Python PDF 转 Excel API](#python-pdf-to-xlsx)
- [Python PDF 程序化转 Excel](#python-pdf-to-xlsx)
- [Python PDF 转 Excel 库](#python-pdf-to-xlsx)
- [Python 将 PDF 保存为 Excel](#python-pdf-to-xlsx)
- [Python 从 PDF 生成 Excel](#python-pdf-to-xlsx)
- [Python 从 PDF 创建 Excel](#python-pdf-to-xlsx)
- [Python PDF 转 Excel 转换器](#python-pdf-to-xlsx)

_格式_: **XLS**
- [Python PDF 转 XLS 代码](#python-pdf-to-xls)
- [Python PDF 转 XLS API](#python-pdf-to-xls)
- [Python PDF 程序化转 XLS](#python-pdf-to-xls)
- [Python PDF 转 XLS 库](#python-pdf-to-xls)
- [Python 将 PDF 保存为 XLS](#python-pdf-to-xls)
- [Python 从 PDF 生成 XLS](#python-pdf-to-xls)
- [Python 从 PDF 创建 XLS](#python-pdf-to-xls)
- [Python PDF 转 XLS 转换器](#python-pdf-to-xls)

_格式_: **XLSX**

- [Python PDF 转 XLSX 代码](#python-pdf-to-xlsx)
- [Python PDF 转 XLSX API](#python-pdf-to-xlsx)
- [Python PDF 转 XLSX 编程实现](#python-pdf-to-xlsx)
- [Python PDF 转 XLSX 库](#python-pdf-to-xlsx)
- [Python 将 PDF 保存为 XLSX](#python-pdf-to-xlsx)
- [Python 从 PDF 生成 XLSX](#python-pdf-to-xlsx)
- [Python 从 PDF 创建 XLSX](#python-pdf-to-xlsx)
- [Python PDF 转 XLSX 转换器](#python-pdf-to-xlsx)

_格式_: **CSV**
- [Python PDF 转 CSV 代码](#python-pdf-to-csv)
- [Python PDF 转 CSV API](#python-pdf-to-csv)
- [Python PDF 转 CSV 编程实现](#python-pdf-to-csv)
- [Python PDF 转 CSV 库](#python-pdf-to-csv)
- [Python 将 PDF 保存为 CSV](#python-pdf-to-csv)
- [Python 从 PDF 生成 CSV](#python-pdf-to-csv)
- [Python 从 PDF 创建 CSV](#python-pdf-to-csv)
- [Python PDF 转 CSV 转换器](#python-pdf-to-csv)

_格式_: **ODS**
- [Python PDF 转 ODS 代码](#python-pdf-to-ods)
- [Python PDF 转 ODS API](#python-pdf-to-ods)
- [Python PDF 转 ODS 编程实现](#python-pdf-to-ods)
- [Python PDF 转 ODS 库](#python-pdf-to-ods)

- [Python 将 PDF 保存为 ODS](#python-pdf-to-ods)
- [Python 从 PDF 生成 ODS](#python-pdf-to-ods)  
- [Python 从 PDF 创建 ODS](#python-pdf-to-ods)  
- [Python PDF 到 ODS 转换器](#python-pdf-to-ods)