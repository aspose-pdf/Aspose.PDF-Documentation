---
title: 导入和导出表单数据
linktitle: 导入和导出表单数据
type: docs
weight: 80
url: /zh/java/import-export-form-data/
description: 使用 Aspose.PDF for Java 导入和导出 AcroForm 字段数据，支持 XML、FDF、XFDF 和 JSON 格式。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 使用 Java 导入和导出 PDF 表单数据
Abstract: 本文阐述了如何使用 Aspose.PDF for Java 在外部格式之间交换 AcroForm 数据。它涵盖了通过 Form 门面导入和导出 XML、FDF 和 XFDF 数据，并将表单字段值提取为 JSON。
---
Aspose.PDF for Java 支持多种常见的数据交换格式，用于交互式表单。

## 从 XML 导入表单数据

当表单值存储在 XML 文件中且需要应用到 PDF 表单时，请使用此示例。

1. 创建一个 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观并绑定源 PDF。
1. 打开 XML 输入流并将数据导入表单。
1. 保存更新后的 PDF 文档。

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

## 将 Form 数据导出为 XML

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

在表单值以 FDF 交换格式到达时使用此示例。

1. 创建一个 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观并绑定源 PDF。
1. 打开 FDF 输入流并导入数据。
1. 保存已填写的 PDF 文档。

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

## 导出表单数据为 FDF

当需要将 PDF 表单值共享为 FDF 文件时，请使用此示例。

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

当表单数据以 XFDF 格式提供且必须合并到 PDF 中时，使用此示例。

1. 创建一个 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观并绑定源 PDF。
1. 打开 XFDF 输入流并导入值。
1. 保存更新后的 PDF 文档。

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

## 将表单数据导出为 XFDF

当您需要用于 AcroForm 值的基于 XML 的交换文件时，请使用此示例。

1. 创建一个 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观并绑定源 PDF。
1. 打开 XFDF 文件的输出流。
1. 将当前表单值导出为XFDF。

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

## 提取表单字段为 JSON

当需要将表单值导出为轻量级 JSON 表示时，请使用此示例。

1. 使用该打开 PDF [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观。
1. 遍历字段名称并将其值序列化为 JSON 文本。
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

当您需要一个专用的包装方法来委托主 JSON 导出例程时，请使用此示例。

1. 使用源 PDF 和输出路径调用现有的 JSON 提取助手。
1. 在不重复序列化代码的情况下复用相同的提取逻辑。

```java
public static void extractFormFieldsToJsonDoc(Path inputFile, Path outputFile) throws Exception {
    extractFormFieldsToJson(inputFile, outputFile);
}
```
