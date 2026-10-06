---
title: 使用 Java 从 AcroForm 提取数据
linktitle: 从 AcroForm 提取数据
type: docs
weight: 50
url: /zh/java/extract-data-from-acroform/
description: Aspose.PDF 使从 PDF 文件中提取表单字段数据变得轻松。了解如何从 AcroForms 提取数据并将其保存为 JSON、XML 或 FDF 格式。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何通过 Java 从 AcroForm 提取数据
Abstract: 本文介绍了如何使用 Aspose.PDF for Java 从 PDF 文件中提取和导出 AcroForm 数据。它涵盖了读取所有表单字段、按名称检索字段值、将字段数据导出为 JSON，以及将表单数据写入 XML、FDF 和 XFDF 格式。
---

## 从 PDF 文档中提取表单字段

使用 `com.aspose.pdf.facades.Form` 读取字段名称和值，而无需遍历完整的文档对象模型。

1. 使用此方式打开源 PDF 表单 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) facade，使得可以在不遍历完整文档对象模型的情况下读取 AcroForm 字段。
1. 呼叫 `getFieldNames()` 收集表单中所有存在的字段标识符。
1. 遍历这些字段名并调用 `getField(fieldName)` 读取每个字段的值。
1. 从提取的键值对构建输出字符串，并打印聚合的表单数据。
1. 在 `finally` 块中关闭 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 对象。

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

## 通过名称检索表单字段值

当您知道 PDF 表单中定义的确切字段名称时，您可以直接使用 `getField(fieldName)`
无需遍历整个字段集合。

1. 使用 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 对象打开源 PDF 表单。
1. 呼叫 `getField(fieldName)` 使用所请求的字段名称从 AcroForm 数据中读取其当前值。
1. 打印提取的字段值。
1. 在 `finally` 块中关闭 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 对象。

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

## 从 PDF 文档中提取表单字段为 JSON

表单字段值也可以提取并存储为 JSON。这在需要消费 PDF 表单数据时很有用。
Web 应用程序、API 或其他与 JSON 交互的系统。

1. 使用 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 对象打开源 PDF 表单。
1. 呼叫 `getFieldNames()` 从 AcroForm 中收集所有可用的字段标识符。
1. 遍历这些字段，转义名称和值，并构建 JSON 对象字符串。
1. 将 JSON 结果写入输出文件。
1. 在 `finally` 块中关闭 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 对象。

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

## 从 PDF 文件导出表单数据为 XML

当需要将 PDF 表单数据提供给使用结构化 XML 数据的系统时，XML 导出非常有用。

1. 创建尚未绑定文档的 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 对象。
1. 为 XML 文件打开输出流，并使用 facade 将源 PDF 绑定 `bindPdf(...)`。
1. 呼叫 `exportXml(stream)` 因此，当前的表单字段数据被序列化为 XML。
1. 关闭 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 导出完成后，facade。

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

## 从 PDF 文件导出数据为 FDF

FDF（Forms Data Format）通常用于在不依赖 PDF 文档的情况下交换 AcroForm 字段数据。

1. 创建尚未绑定文档的 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 对象。
1. 为 FDF 文件打开输出流，并使用 facade 将源 PDF 绑定 `bindPdf(...)`。
1. 呼叫 `exportFdf(stream)` 因此，FormField 数据以 FDF 格式进行序列化。
1. 关闭 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 导出完成后，facade。

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

## 从 PDF 文件导出数据到 XFDF

XFDF 是基于 XML 的 Forms Data Format 表示，并且便于与使用 XML 的系统交换表单数据。

1. 创建尚未绑定文档的 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 对象。
1. 为 XFDF 文件打开输出流，并使用 `bindPdf(...)` 将源 PDF 绑定到 Facades 对象。
1. 呼叫 `exportXfdf(stream)` 所以表单字段数据以 XFDF 格式序列化。
1. 关闭 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 导出完成后，facade。

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
