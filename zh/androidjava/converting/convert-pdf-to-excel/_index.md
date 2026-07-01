---
title: 将 PDF 转换为 Excel
linktitle: 将 PDF 转换为 Excel
type: docs
weight: 90
url: /zh/androidjava/convert-pdf-to-excel/
lastmod: "2026-07-01"
description: Aspose.PDF for Android via Java 允许您将 PDF 转换为 Excel 格式。在此过程中，PDF 文件的各个页面被转换为 Excel 工作表。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for Android via Java API 让您将 PDF 文件渲染为 Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) 和 [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/) 文件格式。我们已经有另一个 API，称为 [Aspose.Cells for Java](https://products.aspose.com/cells/java)"," 提供创建和操作现有 Excel 工作簿的功能。 它还提供将 Excel 工作簿转换为 PDF 格式的功能。

{{% alert color="primary" %}}

在线尝试。您可以在此链接检查 Aspose.PDF 转换的质量并在线查看结果。 [products.aspose.app/pdf/conversion/pdf-to-xlsx](https://products.aspose.app/pdf/conversion/pdf-to-xlsx) 

{{% /alert %}}

## 将 PDF 转换为 Excel XLS

要将 PDF 文件转换为 XLS 格式，Aspose.PDF 有一个类称为 [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). 一个对象 [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) 类作为第二个参数传递给 Document.Save(..) 构造函数。 

将 PDF 文件转换为 XLSX 格式是 Aspose.PDF for Java 18.6 版本库的一部分。为了将 PDF 文件转换为 XLSX 格式，您需要使用 setFormat() 方法的 [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) 类。

以下代码片段展示了如何将 PDF 文件转换为 xls 和 .xlsx 格式：

```java
public void convertPDFtoExcelSimple() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS document format
            document.save(xlsFileName.toString(), SaveFormat.Excel);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## 使用控制列将 PDF 转换为 XLS

在将 PDF 转换为 XLS 格式时，输出文件的第一列会添加一个空白列。The in [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) class InsertBlankColumnAtFirst 选项用于控制此列。其默认值为 true。

```java
public void convertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setInsertBlankColumnAtFirst(false);

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS document format
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

当将包含大量页的 PDF 文件导出为 XLS 时，每一页都会导出到 Excel 文件中的不同工作表。这是因为默认情况下 MinimizeTheNumberOfWorksheets 属性设置为 false。为了确保所有页都导出到输出 Excel 文件的同一个工作表，请将 MinimizeTheNumberOfWorksheets 属性设置为 true。

```java
 public void convertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setMinimizeTheNumberOfWorksheets(true);

        // Save the output in XLSX
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS Excel format
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

默认情况下 Aspose.PDF 使用 XML Spreadsheet 2003 来存储数据。为了将 PDF 文件转换为 XLSX 格式，Aspose.PDF 有一个名为 ExcelSaveOptions 且包含 Format 的类。该类的对象 [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) 该类作为第二个参数传递给 Document.Save(..) 方法。

```java
 public void convertPDFtoExcelAdvanced_SaveCSV() {
        // Load PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);

        // Save the output in CSV
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.csv");
        try {
            // Save the file into CSV format
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```
