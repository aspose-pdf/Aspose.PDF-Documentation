---
title: 在 .NET 中将 PDF 转换为 Excel
linktitle: 将 PDF 转换为 Excel
type: docs
weight: 20
url: /net/convert-pdf-to-excel/
lastmod: "2021-11-01"
keywords: 使用 c# 将 PDF 转换为 Excel, 使用 csharp 将 PDF 转换为 XLS, 使用 csharp 将 PDF 转换为 XLSX, 在 csharp 中从 PDF 导出表格到 Excel.
description: Aspose.PDF for .NET 库允许您使用 C# 将 PDF 转换为 Excel 格式。这些格式包括 XLS, XLSX, XML 2003 Spreadsheet, CSV, ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 概览

本文介绍如何**使用 C# 将 PDF 转换为 Excel 格式**。它涵盖以下主题。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

_格式_: **XLS**

- [C# PDF 到 XLS](#csharp-pdf-to-xls)
- [C# 将 PDF 转换为 XLS](#csharp-pdf-to-xls)
- [C# 如何将 PDF 文件转换为 XLS](#csharp-pdf-to-xls)

_格式_: **XLSX**

- [C# PDF 到 XLSX](#csharp-pdf-to-xlsx)
- [C# 将 PDF 转换为 XLSX](#csharp-pdf-to-xlsx)
- [C# 如何将 PDF 文件转换为 XLSX](#csharp-pdf-to-xlsx)
- [C# 如何将 PDF 文件转换为 XLSX](#csharp-pdf-to-xlsx)

_格式_: **Excel**

- [C# PDF 转 Excel](#csharp-pdf-to-xlsx)
- [C# PDF 转 Excel XLS](#csharp-pdf-to-xls)
- [C# PDF 转 Excel XLSX](#csharp-pdf-to-xlsx)

_格式_: **单个 Excel 工作表**

- [C# 将 PDF 转换为具有单个工作表的 XLS](#csharp-pdf-to-excel-single)
- [C# 将 PDF 转换为具有单个工作表的 XLSX](#csharp-pdf-to-excel-single)

_格式_: **XML Spreadsheet 2003 格式**

- [C# PDF 转 XML Excel](#csharp-pdf-to-excel-xml-2003)
- [C# 将 PDF 转换为 XML Excel 表格](#csharp-pdf-to-excel-xml-2003)

_格式_: **CSV**

- [C# PDF 转 CSV](#csharp-pdf-to-csv)
- [C# 将 PDF 转换为 CSV](#csharp-pdf-to-csv)
- [C# 如何将 PDF 文件转换为 CSV](#csharp-pdf-to-csv)

_格式_: **ODS**

- [C# PDF 转 ODS](#csharp-pdf-to-ods)
- [C# 将 PDF 转换为 ODS](#csharp-pdf-to-ods)
- [C# 如何将 PDF 文件转换为 ODS](#csharp-pdf-to-ods)

## C# PDF 转 Excel 转换

**Aspose.PDF for .NET** 支持将 PDF 文件转换为 Excel 2007、CSV 和 SpeadsheetML 格式的功能。
**Aspose.PDF for .NET** 支持将 PDF 文件转换为 Excel 2007、CSV 和 SpeadsheetML 格式的功能。

Aspose.PDF for .NET 是一个 PDF 操作组件，我们引入了一个功能，该功能将 PDF 文件渲染为 Excel 工作簿（XLSX 文件）。在此转换过程中，PDF 文件的各个页面被转换为 Excel 工作表。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 Excel**

Aspose.PDF for .NET 为您提供在线免费应用程序 ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)，您可以在此尝试探索其功能和工作质量。

[![Aspose.PDF Convertion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

为了将 PDF 文件转换为 <abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr> 格式，Aspose.PDF 提供了一个名为 [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions) 的类。
为了将 PDF 文件转换为 <abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr> 格式，Aspose.PDF 提供了一个名为 [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions) 的类。

以下代码片段显示了使用 Aspose.PDF for .NET 将 PDF 文件转换为 XLS 或 XLSX 格式的过程。

<a name="csharp-pdf-to-xls"><strong>步骤：在 C# 中将 PDF 转换为 XLS</strong></a>

1. 使用源 PDF 文档创建 **Document** 对象的实例。
2. 创建 **ExcelSaveOptions** 的实例。
3. 通过调用 **Document.Save()** 方法并传递 **ExcelSaveOptions**，将其保存为 **XLS** 格式并指定 **.xls 扩展名**

<a name="csharp-pdf-to-xlsx"><strong>步骤：在 C# 中将 PDF 转换为 XLSX</strong></a>

1. 使用源 PDF 文档创建 **Document** 对象的实例。
2. 创建 **ExcelSaveOptions** 的实例。
3. 通过调用 **Document.Save()** 方法并传递 **ExcelSaveOptions**，将其保存为 **XLSX** 格式并指定 **.xlsx 扩展名**

```csharp
// 代码示例将在这里给出，确保使用正确的 C# 语法和风格
```
```csharp
// 有关完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// 加载 PDF 文档
Document pdfDocument = new Document(dataDir + "input.pdf");

// 实例化 ExcelSave 选项对象
Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions();

// 以 XLS 格式保存输出
pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
```

## 将 PDF 转换为带控制列的 XLS

将 PDF 转换为 XLS 格式时，在输出文件中会添加一个空白列作为第一列。在 ExcelSaveOptions 类的 InsertBlankColumnAtFirst 选项用于控制这一列。默认值为 `false`，这意味着不会插入空白列。

```csharp
public static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst()
{
    // 有关完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    // 加载 PDF 文档
    Document pdfDocument = new Document(_dataDir + "input.pdf");
    // 实例化 ExcelSave 选项对象
    Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions {InsertBlankColumnAtFirst = false};
    // 以 XLS 格式保存输出
    pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
}
```
## 将PDF转换为单个Excel工作表

当将一个包含多页的PDF文件导出到XLS时，每一页将被导出到Excel文件中的不同工作表。这是因为默认情况下MinimizeTheNumberOfWorksheets属性设置为false。为了确保所有页面都导出到输出Excel文件的一个单独工作表中，请将MinimizeTheNumberOfWorksheets属性设置为true。

<a name="csharp-pdf-to-excel-single"><strong>步骤：在C#中将PDF转换为XLS或XLSX单个工作表</strong></a>

1. 使用源PDF文档创建**Document**对象的实例。
2. 创建**ExcelSaveOptions**的实例，其中**MinimizeTheNumberOfWorksheets = true**。
3. 通过调用**Document.Save()**方法并传递**ExcelSaveOptions**，将其保存为具有单个工作表的**XLS**或**XLSX**格式。

```csharp
public static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets()
{
    // 完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    // 加载PDF文档
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // 实例化ExcelSave选项对象
    Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions {MinimizeTheNumberOfWorksheets = true};
    // 保存输出为XLS格式
    pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
}
```
## 转换为其他电子表格格式

### 转换为 XML 电子表格 2003 格式

自 20.8 版本起，Aspose.PDF 使用 Microsoft Excel Open XML Spreadsheet 2007 文件格式作为默认存储数据的格式。为了将 PDF 文件转换为 XML Spreadsheet 2003 格式，Aspose.PDF 提供了一个名为 [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions) 的类，该类中有一个 [Format](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions/properties/format) 属性。一个 [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions) 类的对象作为第二个参数传递给 [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) 方法。

以下代码片段展示了将 PDF 文件转换为 XLS Excel 2003 XML 格式的过程。

<a name="csharp-pdf-to-excel-xml-2003"><strong>步骤：在 C# 中将 PDF 转换为 Excel 2003 XML 格式</strong></a>

1. 使用源 PDF 文档创建 **Document** 对象的实例。
2.
2.
3. 通过调用 **Document.Save()** 方法并传递 **ExcelSaveOptions**，将其保存为 **XLS - Excel 2003 XML格式**。

```csharp
public static void ConvertPDFtoExcelAdvanced_SaveXLS2003()
{
    // 有关完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET

    // 加载PDF文档
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // 实例化ExcelSave Option对象
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003 };

    // 保存输出为XLS格式
    pdfDocument.Save("PDFToXLS_out.xls", excelSave);
}
```

### 转换为CSV

转换为CSV格式的操作与上述相同。您需要做的就是设置适当的格式。

<a name="csharp-pdf-to-csv"><strong>步骤：在C#中将PDF转换为CSV</strong></a>

1. 使用源PDF文档创建 **Document** 对象的实例。
2.
2.
3. 通过调用 **Document.Save()** 方法并传递 **ExcelSaveOptions**，将其保存为**CSV**格式。


```csharp
 // 实例化 ExcelSave Option 对象
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.CSV };
```

### 转换为 ODS

<a name="csharp-pdf-to-ods"><strong>步骤：在 C# 中将 PDF 转换为 ODS</strong></a>

1. 使用源 PDF 文档创建 **Document** 对象的实例。
2. 创建 **ExcelSaveOptions** 的实例，设置 **Format = ExcelSaveOptions.ExcelFormat.ODS**
3. 通过调用 **Document.Save()** 方法并传递 **ExcelSaveOptions**，将其保存为 **ODS** 格式。

转换为 ODS 格式的操作与其他格式相同。

```csharp
 // 实例化 ExcelSave Option 对象
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.ODS };
```

## 另见

本文还涵盖了以下主题。代码与上述相同。

_格式_：**Excel**
- [C# PDF 转 Excel 代码](#csharp-pdf-to-xlsx)
- [C# PDF 转 Excel API](#csharp-pdf-to-xlsx)
- [C# PDF 转 Excel API](#csharp-pdf-to-xlsx)
- [C# 编程方式 PDF 转 Excel](#csharp-pdf-to-xlsx)
- [C# PDF 转 Excel 库](#csharp-pdf-to-xlsx)
- [C# 将 PDF 保存为 Excel](#csharp-pdf-to-xlsx)
- [C# 从 PDF 生成 Excel](#csharp-pdf-to-xlsx)
- [C# 从 PDF 创建 Excel](#csharp-pdf-to-xlsx)
- [C# PDF 转 Excel 转换器](#csharp-pdf-to-xlsx)

_格式_: **XLS**
- [C# PDF 转 XLS 代码](#csharp-pdf-to-xls)
- [C# PDF 转 XLS API](#csharp-pdf-to-xls)
- [C# 编程方式 PDF 转 XLS](#csharp-pdf-to-xls)
- [C# PDF 转 XLS 库](#csharp-pdf-to-xls)
- [C# 将 PDF 保存为 XLS](#csharp-pdf-to-xls)
- [C# 从 PDF 生成 XLS](#csharp-pdf-to-xls)
- [C# 从 PDF 创建 XLS](#csharp-pdf-to-xls)
- [C# PDF 转 XLS 转换器](#csharp-pdf-to-xls)

_格式_: **XLSX**
- [C# PDF 转 XLSX 代码](#csharp-pdf-to-xlsx)
- [C# PDF 转 XLSX API](#csharp-pdf-to-xlsx)
- [C# 编程方式 PDF 转 XLSX](#csharp-pdf-to-xlsx)
- [C# PDF 转 XLSX 库](#csharp-pdf-to-xlsx)
- [C# 将 PDF 保存为 XLSX](#csharp-pdf-to-xlsx)
- [C# 从 PDF 生成 XLSX](#csharp-pdf-to-xlsx)
- [C# 从PDF生成XLSX](#csharp-pdf-to-xlsx)
- [C# 从PDF创建XLSX](#csharp-pdf-to-xlsx)
- [C# PDF到XLSX转换器](#csharp-pdf-to-xlsx)

格式: **CSV**
- [C# PDF到CSV代码](#csharp-pdf-to-csv)
- [C# PDF到CSV API](#csharp-pdf-to-csv)
- [C# 以编程方式从PDF到CSV](#csharp-pdf-to-csv)
- [C# PDF到CSV库](#csharp-pdf-to-csv)
- [C# 将PDF保存为CSV](#csharp-pdf-to-csv)
- [C# 从PDF生成CSV](#csharp-pdf-to-csv)
- [C# 从PDF创建CSV](#csharp-pdf-to-csv)
- [C# PDF到CSV转换器](#csharp-pdf-to-csv)

格式: **ODS**
- [C# PDF到ODS代码](#csharp-pdf-to-ods)
- [C# PDF到ODS API](#csharp-pdf-to-ods)
- [C# 以编程方式从PDF到ODS](#csharp-pdf-to-ods)
- [C# PDF到ODS库](#csharp-pdf-to-ods)
- [C# 将PDF保存为ODS](#csharp-pdf-to-ods)
- [C# 从PDF生成ODS](#csharp-pdf-to-ods)
- [C# 从PDF创建ODS](#csharp-pdf-to-ods)
- [C# PDF到ODS转换器](#csharp-pdf-to-ods)
