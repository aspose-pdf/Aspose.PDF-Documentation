---
title: 读取表单值
linktitle: 读取表单值
type: docs
weight: 60
url: /zh/java/reading-form-values/
description: 了解如何在 Java 中使用 Aspose.PDF 的 Form 类检查 PDF 表单字段名称和数值。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中读取 PDF 表单字段名称和数值
Abstract: 本节介绍在 Aspose.PDF for Java 当前 Form 类示例集中实现的 Java 表单读取工作流。该仓库提供通用字段检查示例，并对尚未拥有匹配 Java 示例的专用页面使用明确的范围说明。
---
Java `FormExamples` 类演示了 Facades API 所公开的主要表单处理工作流。

## 获取字段值

使用 `FormExamples.inspectFormFields(...)` 检查字段名称及其当前值。

```java
public static void inspectFormFields(Path inputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        System.out.println("Field names: " + Arrays.toString(form.getFieldNames()));
        for (String fieldName : form.getFieldNames()) {
            System.out.println(fieldName + " = " + form.getField(fieldName));
        }
    } finally {
        form.close();
    }
}
```
