---
title: 将PDF转换为Excel 
linktitle: 将PDF转换为Excel
type: docs
weight: 20
url: /zh/java/convert-pdf-to-excel/
lastmod: "2021-11-19"
description: Aspose.PDF for Java允许您使用Java将PDF转换为Excel格式。在此过程中，PDF文件的各个页面被转换为Excel工作表。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for Java API允许您将PDF文件渲染为Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) 和 [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/) 文件格式。我们已经有另一个API，称为 [Aspose.Cells for Java](https://products.aspose.com/cells/java)，它提供了创建和操作现有Excel工作簿的功能。它还提供了将Excel工作簿转换为PDF格式的功能。

{{% alert color="primary" %}}

**尝试在线将PDF转换为Excel**

Aspose.PDF for Java 为您提供在线免费应用程序 ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)，您可以在此尝试研究其功能和工作质量。

[![Aspose.PDF 转换 PDF 到 Excel 使用免费应用程序](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## 将 PDF 转换为 Excel XLS

要将 PDF 文件转换为 XLS 格式，Aspose.PDF 有一个名为 [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) 的类。 [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) 类的对象作为第二个参数传递给 Document.Save(..) 方法。

将 PDF 文件转换为 XLSX 格式是 Aspose.PDF for Java 18.6 版本库的一部分。为了将 PDF 文件转换为 XLSX 格式，您需要使用 [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) 类的 setFormat() 方法将格式设置为 XLSX。

以下代码片段展示了如何将 PDF 文件转换为 xls 和 .xlsx 格式：

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPDFtoXLSX {

    private ConvertPDFtoXLSX() {

    }

    // 文档目录的路径。
    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {

        ConvertPDFtoExcelSimple();
        ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst();
        ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets();
        ConvertPDFtoExcelAdvanced_SaveXLSX();
    }

    public static void ConvertPDFtoExcelSimple() {
        // 加载 PDF 文档
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // 实例化 ExcelSave 选项对象
        ExcelSaveOptions excelsave = new ExcelSaveOptions();

        // 以 XLS 格式保存输出
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
}
```

## 将 PDF 转换为带控制列的 XLS

当将PDF转换为XLS格式时，输出文件中会在第一列添加一个空白列。在 [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) 类中使用 InsertBlankColumnAtFirst 选项来控制这一列。其默认值为 true。

```java
    public static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // 加载PDF文档
        Document pdfDocument = new Document(_dataDir + "input.pdf");
        // 实例化 ExcelSave Option 对象
        ExcelSaveOptions excelsave = new ExcelSaveOptions();
        excelsave.setInsertBlankColumnAtFirst(false);
        // 以XLS格式保存输出
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
```

## 将PDF转换为单个Excel工作表

当将包含许多页面的PDF文件导出到XLS时，每个页面将导出到Excel文件中的不同工作表。
 这是因为 MinimizeTheNumberOfWorksheets 属性默认设置为 false。为了确保所有页面都导出到输出 Excel 文件中的一个单独工作表中，将 MinimizeTheNumberOfWorksheets 属性设置为 true。

```java
    public static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // 加载PDF文档
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // 实例化 ExcelSave Option 对象
        ExcelSaveOptions excelsave = new ExcelSaveOptions();
        excelsave.setMinimizeTheNumberOfWorksheets(true);

        // 以 XLS 格式保存输出
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
```

## 转换为 XLSX 格式

默认情况下，Aspose.PDF 使用 XML Spreadsheet 2003 来存储数据。 为了将PDF文件转换为XLSX格式，Aspose.PDF有一个名为ExcelSaveOptions的类，其包含Format。一个[ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions)类的对象作为第二个参数传递给Document.Save(..)方法。

```java
    public static void ConvertPDFtoExcelAdvanced_SaveXLSX() {
        // 加载PDF文档
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // 实例化Excel保存选项对象
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);

        // 以XLS格式保存输出
        pdfDocument.save("PDFToXLS_out.xlsx", excelSave);
    }
```