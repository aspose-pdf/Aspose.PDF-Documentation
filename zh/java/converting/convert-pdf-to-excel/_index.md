---
title: 在 Java 中将 PDF 转换为 Excel
linktitle: 将 PDF 转换为 Excel
type: docs
weight: 20
url: /java/convert-pdf-to-excel/
lastmod: "2026-06-16"
description: 了解如何使用 Aspose.PDF 将 PDF 文件转换为 Java 中的 Excel，包括 XML Spreadsheet 2003、XLSX、XLSM、CSV 和 ODS 输出。
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何用 Java 将 PDF 转换为 Excel
Abstract: 本文介绍如何使用 Aspose.PDF for Java 将 PDF 文件转换为与 Excel 兼容的格式。它涵盖 XML Spreadsheet 2003、XLSX、XLSM、CSV 和 ODS 输出，以及空白列插入和最小化工作表数量的选项。
---
Aspose.PDF for Java 可以将 PDF 内容导出为具有不同布局选项的多种电子表格格式。使用 [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) 选择目标工作簿格式并控制如何将页面内容映射到工作表和列中。

## 将 PDF 转换为 Excel 2003 XML

当 PDF 内容应导出为 Excel 2003 XML 电子表格格式时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建 [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) 并将其格式设置为`XMLSpreadSheet2003`。
1. 调用 `document.save(outputFile.toString(), saveOptions)` 以便加载的 PDF 在 Excel 2003 XML 架构中序列化。
1. 保存转换后的输出文件。

```java
public static void convertPdfToExcelSpreadSheet2003(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 PDF 转换为 XLSX

当 PDF 内容应转换为 Excel 2007+ XLSX 格式时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建 [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) 并将其格式设置为`XLSX`。
1. 调用`document.save(outputFile.toString(), saveOptions)`，以便将 PDF 布局导出为 Office Open XML 工作簿。
1. 保存输出电子表格文件。

```java
public static void convertPdfToExcel2007(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 使用列控制将 PDF 转换为 XLSX

当在 PDF 到 Excel 转换期间应调整列处理时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 为 `XLSX` 输出创建 [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/)。
1. 当需要额外的前导列来改进从 PDF 生成的工作表布局时，启用 `setInsertBlankColumnAtFirst(true)`。
1. 调用`document.save(outputFile.toString(), saveOptions)`并写入转换后的XLSX文件。

```java
public static void convertPdfToExcel2007ControlColumn(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        saveOptions.setInsertBlankColumnAtFirst(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 PDF 转换为单个 Excel 工作表

Use this example when all PDF pages should be exported into one worksheet.

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 为 `XLSX` 导出创建 [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/)。
1. 启用`setMinimizeTheNumberOfWorksheets(true)`，以便将多个 PDF 页面合并为更少的工作表。
1. 调用 `document.save(outputFile.toString(), saveOptions)` 并保存 XLSX 输出文件。

```java
public static void convertPdfToExcel2007SingleExcelWorksheet(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        saveOptions.setMinimizeTheNumberOfWorksheets(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 PDF 转换为 XLSM

当 PDF 输出应保存为启用宏的 Excel 工作簿时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建[`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/)并将格式设置为`XLSM`。
1. 调用`document.save(outputFile.toString(), saveOptions)`，以便将 PDF 内容导出到启用宏的工作簿容器。
1. 保存 XLSM 文件。

```java
public static void convertPdfToExcel2007Macro(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSM);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 PDF 转换为 CSV

当 PDF 表格内容应导出为 CSV 时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建[`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/)并将格式设置为`CSV`。
1. 调用`document.save(outputFile.toString(), saveOptions)`，以便将 PDF 内容展平为以逗号分隔的文本输出。
1. 保存生成的 CSV 文件。

```java
public static void convertPdfToExcel2007Csv(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 PDF 转换为 ODS

当 PDF 内容应导出为 OpenDocument 电子表格格式时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建[`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/)并将格式设置为`ODS`。
1. 调用`document.save(outputFile.toString(), saveOptions)`，以便以 OpenDocument 电子表格格式导出 PDF。
1. 保存转换后的 ODS 文件。

```java
public static void convertPdfToOds(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
