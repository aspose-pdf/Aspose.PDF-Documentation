---
title: 使用 Java 从 AcroForm 中提取数据
linktitle: 从 AcroForm 中提取数据
type: docs
weight: 50
url: /java/extract-data-from-acroform/
description: Aspose.PDF 可以轻松地从 PDF 文件中提取表单字段数据。了解如何从 AcroForms 中提取数据并将其保存为 JSON、XML 或 FDF 格式。
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何通过 Java 从 AcroForm 中提取数据
Abstract: 本文介绍如何使用 Aspose.PDF for Java 从 PDF 文件中提取和导出 AcroForm 数据。它涵盖读取所有表单字段、按名称检索字段值、将字段数据导出为 JSON 以及将表单数据写入 XML、FDF 和 XFDF 格式。
---
## 提取所有表单字段

使用`com.aspose.pdf.facades.Form` 读取字段名称和值，而无需处理完整的文档对象模型。

1. 使用 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观打开源 PDF 表单，以便无需遍历完整文档对象模型即可读取 AcroForm 字段。
1. 调用`getFieldNames()`来收集表单中存在的所有字段标识符。
1. 迭代这些字段名称并调用 `getField(fieldName)` 来读取每个字段值。
1. 从提取的键值对构建输出字符串并打印聚合的表单数据。
1. 关闭 `finally` 块中的 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观。

```java
public static void extractFormFields(Path inputFile) {
    Form form = new Form(inputFile.toString());
    try {
        StringBuilder formValues = new StringBuilder("{");
        String[] fieldNames = form.getFieldNames();
        for (int i = 0; i < fieldNames.length; i++) {
            if (i > 0) {
                formValues.append(", ");
            }
            formValues.append(fieldNames[i]).append("=").append(form.getField(fieldNames[i]));
        }
        formValues.append("}");
        System.out.println(formValues);
    } finally {
        form.close();
    }
}
```

## 按名称检索字段值

1. 使用 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观打开源 PDF 表单。
1. 使用请求的字段名称调用 `getField(fieldName)` 以从 AcroForm 数据中读取其当前值。
1. 打印提取的字段值。
1. 关闭 `finally` 块中的 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观。

```java
public static void extractFormFieldByTitle(Path inputFile, String fieldName) {
    Form form = new Form(inputFile.toString());
    try {
        String formValue = form.getField(fieldName);
        System.out.println(formValue);
    } finally {
        form.close();
    }
}
```

## 将表单字段导出为 JSON

1. 使用 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观打开源 PDF 表单。
1. 调用 `getFieldNames()` 从 AcroForm 收集所有可用的字段标识符。
1. 迭代这些字段，转义名称和值，并构建 JSON 对象字符串。
1. 将 JSON 结果写入输出文件。
1. 关闭 `finally` 块中的 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观。

```java
public static void extractFormFieldsJson(Path inputFile, Path outputFile) throws Exception {
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

## 将表单数据导出为 XML、FDF 和 XFDF

1. 创建 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观，但尚未绑定文档。
1. 打开 XML 文件的输出流，并使用 `bindPdf(...)` 将源 PDF 绑定到外观。
1. 调用`exportXml(stream)`，将当前表单字段数据序列化为XML。
1. 导出完成后关闭 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观。

```java
public static void extractDataToXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(stream);
    } finally {
        form.close();
    }
}
```

1. 创建 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观，但尚未绑定文档。
1. 打开 FDF 文件的输出流，并使用 `bindPdf(...)` 将源 PDF 绑定到外观。
1. 调用`exportFdf(stream)`，以便将表单字段数据序列化为FDF 格式。
1. 导出完成后关闭 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观。

```java
public static void extractDataToFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(stream);
    } finally {
        form.close();
    }
}
```

1. 创建 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观，但尚未绑定文档。
1. 打开 XFDF 文件的输出流，并使用 `bindPdf(...)` 将源 PDF 绑定到外观。
1. 调用`exportXfdf(stream)`，以便表单字段数据以 XFDF 格式序列化。
1. 导出完成后关闭 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 外观。

```java
public static void extractDataToXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(stream);
    } finally {
        form.close();
    }
}
```
