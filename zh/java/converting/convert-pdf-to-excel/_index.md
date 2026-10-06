---
title: 在 Java 中将 PDF 转换为 Excel
linktitle: 将 PDF 转换为 Excel
type: docs
weight: 20
url: /zh/java/convert-pdf-to-excel/
lastmod: "2026-10-06"
description: 了解如何使用 Aspose.PDF 在 Java 中将 PDF 文件转换为 Excel，包括 XML Spreadsheet 2003、XLSX、XLSM、CSV 和 ODS 输出。
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何在 Java 中将 PDF 转换为 Excel
Abstract: 本文说明如何使用 Aspose.PDF for Java 将 PDF 文件转换为兼容 Excel 的格式。它涵盖 XML Spreadsheet 2003、XLSX、XLSM、CSV 和 ODS 输出，并提供插入空列以及最小化工作表数量的选项。
---
Aspose.PDF for Java 可以将 PDF 内容导出为多种电子表格格式，并提供不同的布局选项。使用 [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) 选择目标工作簿格式并控制页面内容如何映射到工作表和列中。

## 将 PDF 转换为 Excel 2003 XML

当需要将 PDF 内容导出为 Excel 2003 XML 电子表格格式时，请使用此示例。

1. 使用 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例打开源 PDF。
1. 创建 [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) 并将其格式设置为 `XMLSpreadSheet2003`。
1. 调用 `document.save(outputFile.toString(), saveOptions)` 因此，加载的 PDF 被序列化为 Excel 2003 XML 架构。
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

当 PDF 内容需要转换为 Excel 2007+ XLSX 格式时，请使用此示例。

1. 使用 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例打开源 PDF。
1. 创建 [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) 并将其格式设置为 `XLSX`。
1. 调用 `document.save(outputFile.toString(), saveOptions)` 因此，PDF 布局被导出为 Office Open XML 工作簿。
1. 保存输出的电子表格文件。

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

## 将 PDF 转换为 XLSX 并进行列控制

在 PDF 转 Excel 转换过程中需要调整列处理时，请使用此示例。

1. 使用 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例打开源 PDF。
1. 创建 [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) 用于 `XLSX` 输出。
1. 启用 `setInsertBlankColumnAtFirst(true)` 当需要额外的前置列来改进从 PDF 生成的工作表布局时。
1. 调用 `document.save(outputFile.toString(), saveOptions)` 并写入转换后的 XLSX 文件。

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

当所有 PDF 页面应导出到同一工作表时，请使用此示例。

1. 使用 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例打开源 PDF。
1. 创建 [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) 用于 `XLSX` 导出。
1. 启用 `setMinimizeTheNumberOfWorksheets(true)` 因此，多个 PDF 页面被合并为更少的工作表。
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

当 PDF 输出需要保存为启用宏的 Excel 工作簿时，请使用此示例。

1. 使用 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例打开源 PDF。
1. 创建 [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) 并将格式设置为 `XLSM`。
1. 调用 `document.save(outputFile.toString(), saveOptions)` 因此，PDF 内容被导出到一个启用宏的工作簿容器中。
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

当需要将 PDF 表格内容导出为 CSV 时，请使用此示例。

1. 使用 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例打开源 PDF。
1. 创建 [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) 并将格式设置为 `CSV`。
1. 调用 `document.save(outputFile.toString(), saveOptions)` 因此，PDF 内容被展平为逗号分隔的文本输出。
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

当需要将 PDF 内容导出为 OpenDocument 电子表格格式时，请使用此示例。

1. 使用 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例打开源 PDF。
1. 创建 [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) 并将格式设置为 `ODS`。
1. 调用 `document.save(outputFile.toString(), saveOptions)` 因此 PDF 已导出为 OpenDocument 电子表格格式。
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
