---
title: 读取表单值
linktitle: 读取表单值
type: docs
weight: 60
url: /java/reading-form-values/
description: 了解如何使用 Aspose.PDF 中的表单外观在 Java 中检查 PDF 表单字段名称和值。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 使用 Java 读取 PDF 表单字段名称和值
Abstract: 本节介绍在 Aspose.PDF for Java 的当前表单外观示例集中实现的 Java 表单读取工作流程。该存储库提供了一个通用的现场检查示例，并对尚无匹配的 Java 示例的专用页面使用明确的范围注释。
---
Java `FormExamples` 类演示了 Facades API 公开的主要表单处理工作流程。

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
