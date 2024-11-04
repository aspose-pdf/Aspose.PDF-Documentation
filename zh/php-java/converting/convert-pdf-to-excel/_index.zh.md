---
title: 将 PDF 转换为 Microsoft Excel
linktitle: 将 PDF 转换为 Excel
type: docs
weight: 20
url: /php-java/convert-pdf-to-excel/
lastmod: "2024-05-20"
keywords: 使用 PHP 将 PDF 转换为 Excel, 使用 PHP 将 PDF 转换为 XLS, 使用 PHP 将 PDF 转换为 XLSX, 在 PHP 中从 PDF 导出表格到 Excel。
description: Aspose.PDF for PHP 允许您使用 PHP 将 PDF 转换为 Excel 格式。在此过程中，PDF 文件的各个页面被转换为 Excel 工作表。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for PHP API 允许您将 PDF 文件渲染为 Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) 和 [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/) 文件格式。我们已经有另一个 API，称为 [Aspose.Cells for PHP via Java](https://products.aspose.com/cells/php-java)，提供了创建和操作现有 Excel 工作簿的功能。它还提供了将 Excel 工作簿转换为 PDF 格式的功能。

{{% alert color="primary" %}}

**尝试在线将 PDF 转换为 Excel**

Aspose.PDF for PHP 为您提供在线免费应用程序 ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)，您可以在此尝试调查其功能和工作质量。

[![Aspose.PDF 转换 PDF 为 Excel 使用免费应用程序](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## 转换 PDF 为 Excel XLS

为了将 PDF 文件转换为 XLS 格式，Aspose.PDF 具有一个名为 [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) 的类。该类的 [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) 对象作为第二个参数传递给 Document.Save(..) 方法。

将 PDF 文件转换为 XLSX 格式是 Aspose.PDF for PHP 18.6 版本库的一部分。为了将 PDF 文件转换为 XLSX 格式，您需要使用 [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) 类的 setFormat() 方法将格式设置为 XLSX。

以下代码片段显示如何将 PDF 文件转换为 XLS 和 XLSX 格式：

```php
// 使用 Document 类加载输入的 PDF 文档。
$document = new Document($inputFile);

// 创建 ExcelSaveOptions 类的实例以指定保存选项。
$saveOption = new ExcelSaveOptions();

// 设置输出格式为 XLS。
// $saveOption->setFormat(ExcelSaveOptions_ExcelFormat::$XMLSpreadSheet2003);

// 设置输出格式为 XLSX。
    $excelSaveOptions_ExcelFormat = new ExcelSaveOptions_ExcelFormat();
    $saveOption->setFormat($excelSaveOptions_ExcelFormat->XLSX);

// 使用指定的保存选项将 PDF 文档保存为 Excel 文件。
$document->save($outputFile, $saveOption);
```