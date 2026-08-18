---
title: 导入和导出表单数据
linktitle: 导入和导出表单数据
type: docs
weight: 80
url: /java/import-export-form-data/
description: 使用 Aspose.PDF for Java 导入和导出 XML、FDF、XFDF 和 JSON 格式的 AcroForm 字段数据。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 使用Java导入和导出PDF表单数据
Abstract: 本文介绍如何使用 Aspose.PDF for Java 与外部格式交换 AcroForm 数据。它涵盖通过表单外观导入和导出 XML、FDF 和 XFDF 数据以及将表单字段值提取为 JSON。
---
Aspose.PDF for Java 支持多种常见的交互式表单数据交换格式。

## 从 XML 导入表单数据

当表单值存储在 XML 文件中并且应应用于 PDF 表单时，请使用此示例。

1. 创建一个 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观并绑定源 PDF。
1. 打开 XML 输入流并将数据导入到表单中。
1. 保存更新的 PDF 文档。

```java
public static void importDataFromXml(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXml(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## 将表单数据导出为 XML

当您需要以 XML 格式存储当前 AcroForm 值时，请使用此示例。

1. 创建一个 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观并绑定源 PDF。
1. 打开 XML 文件的输出流。
1. 将表单数据导出为 XML。

```java
public static void exportDataToXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(stream);
    } finally {
        form.close();
    }
}
```

## 从 FDF 导入表单数据

当表单值以 FDF 交换格式到达时使用此示例。

1. 创建一个 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观并绑定源 PDF。
1. 打开 FDF 输入流并导入数据。
1. 保存填写好的PDF文档。

```java
public static void importDataFromFdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importFdf(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## 将表单数据导出到 FDF

当 PDF 表单值应作为 FDF 文件共享时，请使用此示例。

1. 创建一个 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观并绑定源 PDF。
1. 打开 FDF 文件的输出流。
1. 以 FDF 格式导出表单数据。

```java
public static void exportDataToFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(stream);
    } finally {
        form.close();
    }
}
```

## 从 XFDF 导入表单数据

当表单数据以 XFDF 格式提供并且必须合并到 PDF 中时，请使用此示例。

1. 创建一个 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观并绑定源 PDF。
1. 打开 XFDF 输入流并导入值。
1. 保存更新的 PDF 文档。

```java
public static void importDataFromXfdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXfdf(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## 将表单数据导出到 XFDF

当您需要 AcroForm 值的基于 XML 的交换文件时，请使用此示例。

1. 创建一个 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观并绑定源 PDF。
1. 打开 XFDF 文件的输出流。
1. 将当前表单值导出到 XFDF。

```java
public static void exportDataToXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(stream);
    } finally {
        form.close();
    }
}
```

## 将表单字段提取为 JSON

当表单值应导出为轻量级 JSON 表示形式时，请使用此示例。

1. 使用 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观打开 PDF。
1. 迭代字段名称并将其值序列化为 JSON 文本。
1. 将 JSON 内容写入目标文件。

```java
public static void extractFormFieldsToJson(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form(inputFile.toString());
    try {
        StringBuilder json = new StringBuilder();
        json.append("{\n");
        String[] fieldNames = form.getFieldNames();
        for (int i = 0; i < fieldNames.length; i++) {
            String fieldName = fieldNames[i];
            json.append("    \"").append(escapeJson(fieldName)).append("\": \"")
                    .append(escapeJson(form.getField(fieldName))).append("\"");
            if (i < fieldNames.length - 1) {
                json.append(",");
            }
            json.append("\n");
        }
        json.append("}\n");
        Files.writeString(outputFile, json.toString());
    } finally {
        form.close();
    }
}
```

## 重用 JSON 提取助手

当您需要一个委托给主 JSON 导出例程的专用包装方法时，请使用此示例。

1. 使用源 PDF 和输出路径调用现有的 JSON 提取助手。
1. 重用相同的提取逻辑，无需重复序列化代码。

```java
public static void extractFormFieldsToJsonDoc(Path inputFile, Path outputFile) throws Exception {
    extractFormFieldsToJson(inputFile, outputFile);
}
```
