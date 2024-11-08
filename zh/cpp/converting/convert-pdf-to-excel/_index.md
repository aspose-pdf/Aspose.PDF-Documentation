---
title: Convert PDF to Excel in C++
linktitle: Convert PDF to Excel
type: docs
weight: 20
url: /zh/cpp/convert-pdf-to-excel/
lastmod: "2021-11-19"
description: Aspose.PDF for C++ 允许您使用 C++ 将 PDF 转换为 Excel 格式。在此过程中，PDF 文件的各个页面将被转换为 Excel 工作表。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 概述

本文解释了如何**使用 C++ 将 PDF 转换为 Excel 格式**。它涵盖了以下主题。

_格式_：**XLS**
- [C++ PDF 到 XLS](#cpp-pdf-to-xls)
- [C++ 转换 PDF 为 XLS](#cpp-pdf-to-xls)
- [C++ 如何将 PDF 文件转换为 XLS](#cpp-pdf-to-xls)

_格式_：**XLSX**
- [C++ PDF 到 XLSX](#cpp-pdf-to-xlsx)
- [C++ 转换 PDF 为 XLSX](#cpp-pdf-to-xlsx)
- [C++ 如何将 PDF 文件转换为 XLSX](#cpp-pdf-to-xlsx)

_格式_：**Microsoft Excel XLS 格式**
- [C++ PDF 到 Excel](#cpp-pdf-to-excel-xls)
- [C++ 转换 PDF 为 Excel](#cpp-pdf-to-excel-xls)
- [C++ 如何将 PDF 文件转换为 Excel](#cpp-pdf-to-excel-xls)

_格式_：**Microsoft Excel XLSX 格式**

- [C++ PDF to Excel](#cpp-pdf-to-excel-xlsx)
- [C++ Convert PDF to Excel](#cpp-pdf-to-excel-xlsx)
- [C++ How to convert PDF file to Excel](#cpp-pdf-to-excel-xlsx)

Other topics covered by this article
- [See Also](#see-also)

## C++ PDF to Excel Conversions

**Aspose.PDF for C++** 支持将PDF文件转换为Excel格式的功能。

Aspose.PDF for C++ 是一个PDF操作组件，我们引入了一个功能，可以将PDF文件呈现为Excel工作簿（XLS文件）。在此转换过程中，PDF文件的各个页面被转换为Excel工作表。

为了将PDF文件转换为<abbr title="Microsoft Excel Spreadsheet">XLS</abbr>格式，Aspose.PDF有一个名为ExcelSaveOptions的类。ExcelSaveOptions类的对象作为第二个参数传递给Document.Save(..)构造函数。

以下代码片段显示了使用Aspose.PDF for C++将PDF文件转换为XLS格式的过程。

<a name="cpp-pdf-to-xls" id="cpp-pdf-to-xls"><strong>步骤：在C++中将PDF转换为XLS</strong></a> | <a name="cpp-pdf-to-excel-xls" id="cpp-pdf-to-excel-xls"><strong>步骤：在C++中将PDF转换为Excel XLS格式</strong></a>
```

1. 创建一个 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 对象实例，使用源 PDF 文档。
2. 通过调用 **Document->Save()** 方法将其保存为 _XLS_ 格式。

```cpp
void ConvertPDFtoExcel()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 用于路径名称的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 用于文件名称的字符串
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
    // 以 XLS 格式保存输出
    document->Save(_dataDir + outfilename, SaveFormat::Excel);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message();
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## 转换 PDF 到带控制列的 XLS

在将 PDF 转换为 XLS 格式时，会在输出文件中添加一个空白列作为第一列。 在 ExcelSaveOptions 类中的 InsertBlankColumnAtFirst 选项用于控制此列。其默认值为 true。

```cpp
void ConvertPDFtoExcel_Advanced_InsertBlankColumnAtFirst()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 文件名称的字符串
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 实例化 ExcelSave 选项对象
    auto excelSave = MakeObject<ExcelSaveOptions>();

    // 在 ExcelSaveOptions 类中的 InsertBlankColumnAtFirst 选项用于控制此列。其默认值为 true。
    excelSave->set_InsertBlankColumnAtFirst(false);

    // 以 XLS 格式保存输出
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## 将 PDF 转换为单个 Excel 工作表

当将包含大量页面的 PDF 文件导出为 XLS 时，每个页面都会导出到 Excel 文件中的不同工作表。 这是因为 MinimizeTheNumberOfWorksheets 属性默认设置为 false。为了确保所有页面都导出到输出 Excel 文件中的一个工作表中，将 MinimizeTheNumberOfWorksheets 属性设置为 true。

```cpp
void ConvertPDFtoExcel_Advanced_MinimizeTheNumberOfWorksheets()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 文件名字符串
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 实例化 ExcelSave Option 对象
    auto excelSave = MakeObject<ExcelSaveOptions>();

    excelSave->set_MinimizeTheNumberOfWorksheets(true);

    // 将输出保存为 XLS 格式
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## 转换为 XLSX 格式

默认情况下，Aspose.PDF 使用 XML Spreadsheet 2003 来存储数据。 为了将PDF文件转换为XLSX格式，Aspose.PDF提供了一个名为[ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options)的类，包含'Format'。一个[ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options)类的对象作为第二个参数传递给[Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa)方法。

以下代码片段展示了将PDF文件转换为XLSX格式的过程。

<a name="cpp-pdf-to-xlsx" id="cpp-pdf-to-xlsx"><strong>步骤：在C++中将PDF转换为XLSX</strong></a> | <a name="cpp-pdf-to-excel-xlsx" id="cpp-pdf-to-excel-xlsx"><strong>步骤：在C++中将PDF转换为Excel XLSX格式</strong></a>

1. 使用源PDF文档创建一个[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)对象的实例。
2. 创建一个 [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options) 的实例。
3. 将格式设置为 _ExcelSaveOptions::ExcelFormat::XLSX_。
4. 通过调用 **Document->Save()** 方法并传递 _ExcelSaveOptions_ 的实例，将其保存为 _XLSX_ 格式。

```cpp
void ConvertPDFtoExcel_Advanced_SaveXLSX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 文件名的字符串
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 实例化 ExcelSave Option 对象
    auto excelSave = MakeObject<ExcelSaveOptions>();

    excelSave->set_Format(ExcelSaveOptions::ExcelFormat::XLSX);

    // 以 XLS 格式保存输出
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}

**尝试在线将 PDF 转换为 Excel**
Aspose.PDF for C++ 为您提供在线免费应用程序 ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)，您可以尝试调查其功能和质量。

[![Aspose.PDF 转换 PDF 到 Excel 免费应用](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## 另请参阅

本文还涵盖了这些主题。代码与上述相同。

_格式_: **Microsoft Excel XLS 格式**
- [C++ PDF 到 Excel XLS 代码](#cpp-pdf-to-excel-xls)
- [C++ PDF 到 Excel XLS 编程实现](#cpp-pdf-to-excel-xls)
- [C++ PDF 到 Excel XLS 库](#cpp-pdf-to-excel-xls)
- [C++ 将 PDF 保存为 Excel XLS](#cpp-pdf-to-excel-xls)
- [C++ 从 PDF 生成 Excel XLS](#cpp-pdf-to-excel-xls)
- [C++ 从 PDF 创建 Excel XLS](#cpp-pdf-to-excel-xls)
- [C++ PDF 到 Excel XLS 转换器](#cpp-pdf-to-excel-xls)

_格式_: **Microsoft Excel XLSX 格式**
- [C++ PDF 到 Excel XLSX 代码](#cpp-pdf-to-excel-xlsx)

- [C++ PDF 到 Excel XLSX 编程实现](#cpp-pdf-to-excel-xlsx)
- [C++ PDF 转 Excel XLSX 库](#cpp-pdf-to-excel-xlsx)
- [C++ 将 PDF 保存为 Excel XLSX](#cpp-pdf-to-excel-xlsx)
- [C++ 从 PDF 生成 Excel XLSX](#cpp-pdf-to-excel-xlsx)
- [C++ 从 PDF 创建 Excel XLSX](#cpp-pdf-to-excel-xlsx)
- [C++ PDF 转 Excel XLSX 转换器](#cpp-pdf-to-excel-xlsx)

_格式_: **XLS**
- [C++ PDF 转 XLS 代码](#cpp-pdf-to-xls)
- [C++ 编程方式 PDF 转 XLS](#cpp-pdf-to-xls)
- [C++ PDF 转 XLS 库](#cpp-pdf-to-xls)
- [C++ 将 PDF 保存为 XLS](#cpp-pdf-to-xls)
- [C++ 从 PDF 生成 XLS](#cpp-pdf-to-xls)
- [C++ 从 PDF 创建 XLS](#cpp-pdf-to-xls)
- [C++ PDF 转 XLS 转换器](#cpp-pdf-to-xls)

_格式_: **XLSX**
- [C++ PDF 转 XLSX 代码](#cpp-pdf-to-xlsx)
- [C++ 编程方式 PDF 转 XLSX](#cpp-pdf-to-xlsx)
- [C++ PDF 转 XLSX 库](#cpp-pdf-to-xlsx)
- [C++ 将 PDF 保存为 XLSX](#cpp-pdf-to-xlsx)
- [C++ 从 PDF 生成 XLSX](#cpp-pdf-to-xlsx)
- [C++ 从 PDF 创建 XLSX](#cpp-pdf-to-xlsx)
- [C++ PDF 转 XLSX 转换器](#cpp-pdf-to-xlsx)