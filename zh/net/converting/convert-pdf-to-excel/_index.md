---
title: 在 .NET 中将 PDF 转换为 Excel
linktitle: 将 PDF 转换为 Excel
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/convert-pdf-to-excel/
lastmod: "2021-11-01"
description: Aspose.PDF for .NET 库允许您使用 C# 将 PDF 转换为 Excel 格式。这些格式包括 XLS、XLSX、XML 2003 电子表格、CSV、ODS。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to Excel in .NET",
    "alternativeHeadline": "Convert PDF Files to Excel Formats with C#",
    "abstract": "发现 Aspose.PDF for .NET 强大的能力，可以轻松将 PDF 文档转换为各种 Excel 格式，包括 XLS、XLSX、CSV 和 ODS，使用 C#。此功能不仅允许将单个 PDF 页面转换为单独的 Excel 工作表，还提供组合工作表的选项，为用户高效管理 PDF 数据提供灵活性。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1169",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/convert-pdf-to-excel/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-excel/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 概述

本文解释了如何 **使用 C# 将 PDF 转换为 Excel 格式**。它涵盖以下主题。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

- [将 PDF 转换为 XLS](#csharp-pdf-to-xls)
- [将 PDF 转换为 XLSX](#csharp-pdf-to-xlsx)
- [将 PDF 转换为 Excel](#csharp-pdf-to-xlsx)
- [将 PDF 转换为具有单个工作表的 XLS](#csharp-pdf-to-excel-single)
- [将 PDF 转换为具有单个工作表的 XLSX](#csharp-pdf-to-excel-single)
- [将 PDF 转换为 XML Excel](#csharp-pdf-to-excel-xml-2003)
- [将 PDF 转换为 CSV](#csharp-pdf-to-csv)
- [将 PDF 转换为 ODS](#csharp-pdf-to-ods)
- [将 PDF 转换为 XLSM](#csharp-pdf-to-xlsm)

## C# PDF 到 Excel 转换

**Aspose.PDF for .NET** 支持将 PDF 文件转换为 Excel 2007、CSV 和 SpreadsheetML 格式的功能。

Aspose.PDF for .NET 是一个 PDF 操作组件，我们引入了一项功能，可以将 PDF 文件呈现为 Excel 工作簿（XLSX 文件）。在此转换过程中，PDF 文件的各个页面被转换为 Excel 工作表。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 Excel**

Aspose.PDF for .NET 为您提供在线免费应用程序 ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)，您可以尝试探索其功能和工作质量。

[![Aspose.PDF 将 PDF 转换为 Excel 的免费应用](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

为了将 PDF 文件转换为 <abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr> 格式，Aspose.PDF 有一个名为 [ExcelSaveOptions](https://reference.aspose.com/pdf/zh/net/aspose.pdf/excelsaveoptions) 的类。ExcelSaveOptions 类的对象作为第二个参数传递给 Document.Save(..) 构造函数。

以下代码片段展示了使用 Aspose.PDF for .NET 将 PDF 文件转换为 XLS 或 XLSX 格式的过程。

<a name="csharp-pdf-to-xls" id="cshart-pdf-to-xls"><strong>将 PDF 转换为 XLS</strong></a>

1. 创建一个 **Document** 对象的实例，使用源 PDF 文档。
2. 创建一个 **ExcelSaveOptions** 的实例。
3. 通过调用 **Document.Save()** 方法并传递 **ExcelSaveOptions**，将其保存为指定 **.xls 扩展名** 的 **XLS** 格式。

<a name="csharp-pdf-to-xlsx" id="cshart-pdf-to-xlsx"><strong>将 PDF 转换为 XLSX</strong></a>

1. 创建一个 **Document** 对象的实例，使用源 PDF 文档。
2. 创建一个 **ExcelSaveOptions** 的实例。
3. 通过调用 **Document.Save()** 方法并传递 **ExcelSaveOptions**，将其保存为指定 **.xlsx 扩展名** 的 **XLSX** 格式。

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertPDFtoExcel()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
     {
         // Instantiate ExcelSaveOptions object
         var saveOptions = new Aspose.Pdf.ExcelSaveOptions();

         // Save the file in XLSX format
         document.Save(dataDir + "PDFToXLS_out.xlsx", saveOptions);
     }
 }
```

## 将 PDF 转换为具有控制列的 XLS

将 PDF 转换为 XLS 格式时，输出文件的第一列会添加一个空白列。ExcelSaveOptions 类的 InsertBlankColumnAtFirst 选项用于控制此列。默认值为 `false`，这意味着不会插入空白列。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            InsertBlankColumnAtFirst = false
        };

        // Save the file in XLSX format
        document.Save(dataDir + "PDFToXLS_out.xlsx", saveOptions);
    }
}
```

## 将 PDF 转换为单个 Excel 工作表

当将包含大量页面的 PDF 文件导出为 XLS 时，每个页面会导出到 Excel 文件中的不同工作表。这是因为 MinimizeTheNumberOfWorksheets 属性默认设置为 false。要确保所有页面都导出到输出 Excel 文件的单个工作表中，请将 MinimizeTheNumberOfWorksheets 属性设置为 true。

<a name="csharp-pdf-to-excel-single" id="cshart-pdf-to-excel-single"><strong>将 PDF 转换为 XLS 或 XLSX 单个工作表</strong></a>

1. 创建一个 **Document** 对象的实例，使用源 PDF 文档。
2. 创建一个 **ExcelSaveOptions** 的实例，设置 **MinimizeTheNumberOfWorksheets = true**。
3. 通过调用 **Document.Save()** 方法并传递 **ExcelSaveOptions**，将其保存为具有单个工作表的 **XLS** 或 **XLSX** 格式。

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            MinimizeTheNumberOfWorksheets = true
        };

        // Save the file in XLSX format
        document.Save(dataDir + "PDFToXLS_out.xlsx", saveOptions);
    }
}
```

## 转换为其他电子表格格式

### 转换为 XML 电子表格 2003 格式

自版本 20.8 起，Aspose.PDF 使用 Microsoft Excel Open XML Spreadsheet 2007 文件格式作为存储数据的默认格式。为了将 PDF 文件转换为 XML 电子表格 2003 格式，Aspose.PDF 有一个名为 [ExcelSaveOptions](https://reference.aspose.com/pdf/zh/net/aspose.pdf/excelsaveoptions) 的类，具有 [Format](https://reference.aspose.com/pdf/zh/net/aspose.pdf/excelsaveoptions/properties/format)。将 [ExcelSaveOptions](https://reference.aspose.com/pdf/zh/net/aspose.pdf/excelsaveoptions) 类的对象作为第二个参数传递给 [Document.Save(..)](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document/methods/save/index) 方法。

以下代码片段展示了将 PDF 文件转换为 XLS Excel 2003 XML 格式的过程。

<a name="csharp-pdf-to-excel-xml-2003" id="cshart-pdf-to-excel-xml-2003"><strong>将 PDF 转换为 Excel 2003 XML 格式</strong></a>

1. 创建一个 **Document** 对象的实例，使用源 PDF 文档。
2. 创建一个 **ExcelSaveOptions** 的实例，设置 **Format = ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003**。
3. 通过调用 **Document.Save()** 方法并传递 **ExcelSaveOptions**，将其保存为 **XLS - Excel 2003 XML 格式** 格式。

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertPDFtoExcelAdvanced_SaveXLS2003()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
     {
         // Instantiate ExcelSaveOptions object
         var saveOptions = new Aspose.Pdf.ExcelSaveOptions
         {
             Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
         };

         // Save the file in XLS format
         document.Save(dataDir + "PDFToXLS_out.xls", saveOptions);
     }
 }
```

### 转换为 CSV

转换为 CSV 格式的过程与上述相同。您所需要做的就是设置适当的格式。

<a name="csharp-pdf-to-csv"  id="cshart-pdf-to-csv"><strong>将 PDF 转换为 CSV</strong></a>

1. 创建一个 **Document** 对象的实例，使用源 PDF 文档。
2. 创建一个 **ExcelSaveOptions** 的实例，设置 **Format = ExcelSaveOptions.ExcelFormat.CSV**。
3. 通过调用 **Document.Save()** 方法并传递 **ExcelSaveOptions**，将其保存为 **CSV** 格式。


```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToCSV()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.CSV
        };
        
        // Save the file in CSV format
        document.Save(dataDir + "PDFToXLS_out.csv", saveOptions);
    }
}
```

### 转换为 ODS

<a name="csharp-pdf-to-ods"  id="cshart-pdf-to-ods"><strong>将 PDF 转换为 ODS</strong></a>

1. 创建一个 **Document** 对象的实例，使用源 PDF 文档。
2. 创建一个 **ExcelSaveOptions** 的实例，设置 **Format = ExcelSaveOptions.ExcelFormat.ODS**。
3. 通过调用 **Document.Save()** 方法并传递 **ExcelSaveOptions**，将其保存为 **ODS** 格式。


转换为 ODS 格式的过程与所有其他格式相同。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToODS()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.ODS
        };

        // Save the file in ODS format
        document.Save(dataDir + "PDFToODS_out.ods", saveOptions);
    }
}
```

### 转换为 XLSM

<a name="csharp-pdf-to-xlsm" id="cshart-pdf-to-xlsm"><strong>将 PDF 转换为 XLSM</strong></a>

1. 创建一个 **Document** 对象的实例，使用源 PDF 文档。
2. 创建一个 **ExcelSaveOptions** 的实例，设置 **Format = ExcelSaveOptions.ExcelFormat.XLSM**。
3. 通过调用 **Document.Save()** 方法并传递 **ExcelSaveOptions**，将其保存为 **XLSM** 格式。

转换为 XLSM 格式的过程与所有其他格式相同。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToXLSM()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.XLSM
        };

        // Save the file in ODS format
        document.Save(dataDir + "PDFToODS_out.xlsm", saveOptions);
    }
}
```