---
title: 将PDF转换为Excel 
linktitle: 将PDF转换为Excel 
type: docs
weight: 90
url: /androidjava/convert-pdf-to-excel/
lastmod: "2021-06-05"
description: Aspose.PDF for Android via Java允许您将PDF转换为Excel格式。在此过程中，PDF文件的各个页面将被转换为Excel工作表。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for Android via Java API让您可以将PDF文件渲染为Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) 和 [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/) 文件格式。我们已经有另一个API，称为 [Aspose.Cells for Java](https://products.aspose.com/cells/java)，它提供了创建和操作现有Excel工作簿的功能。它还提供了将Excel工作簿转换为PDF格式的功能。

{{% alert color="primary" %}}

在线试用。
 您可以在此链接[products.aspose.app/pdf/conversion/pdf-to-xlsx](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)在线检查Aspose.PDF转换的质量并查看结果。

{{% /alert %}}

## 将PDF转换为Excel XLS

为了将PDF文件转换为XLS格式，Aspose.PDF有一个名为[ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions)的类。该类的对象作为第二个参数传递给Document.Save(..)构造函数。

将PDF文件转换为XLSX格式是Aspose.PDF for Java 18.6版本库的一部分。为了将PDF文件转换为XLSX格式，需要使用[ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions)类的setFormat()方法设置格式为XLSX。

以下代码片段展示了如何将PDF文件转换为xls和.xlsx格式：

```java
public void convertPDFtoExcelSimple() {
        // 打开源PDF文档
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // 实例化ExcelSave Option对象
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // 将文件保存为MS文档格式
            document.save(xlsFileName.toString(), SaveFormat.Excel);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## 将 PDF 转换为带控制列的 XLS

将 PDF 转换为 XLS 格式时，输出文件中会添加一个空白列作为第一列。在 [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) 类中使用 InsertBlankColumnAtFirst 选项来控制此列。其默认值为 true。

```java
public void convertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // 打开源 PDF 文档
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // 实例化 ExcelSave Option 对象
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setInsertBlankColumnAtFirst(false);

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // 将文件保存为 MS 文档格式
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## 将 PDF 转换为单个 Excel 工作表

当将包含很多页面的 PDF 文件导出为 XLS 时，每个页面都会导出到 Excel 文件中的不同工作表。这是因为 MinimizeTheNumberOfWorksheets 属性默认设置为 false。要确保所有页面都导出到输出 Excel 文件中的一个工作表，请将 MinimizeTheNumberOfWorksheets 属性设置为 true。

```java
 public void convertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // 打开源 PDF 文档
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // 实例化 ExcelSaveOption 对象
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setMinimizeTheNumberOfWorksheets(true);

        // 将输出保存为 XLSX
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // 将文件保存为 MS Excel 格式
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```


## 转换为 XLSX 格式

默认情况下，Aspose.PDF 使用 XML Spreadsheet 2003 存储数据。为了将 PDF 文件转换为 XLSX 格式，Aspose.PDF 有一个名为 ExcelSaveOptions 的类及其格式。一个 [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) 类的对象作为第二个参数传递给 Document.Save(..) 方法。

```java
 public void convertPDFtoExcelAdvanced_SaveCSV() {
        // 加载 PDF 文档
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // 实例化 ExcelSaveOption 对象
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);

        // 将输出保存为 CSV
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.csv");
        try {
            // 将文件保存为 CSV 格式
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```