---
title: 设置字段限制
linktitle: 设置字段限制
type: docs
weight: 50
url: /zh/java/set-field-limit/
description: 了解如何在 Java 中使用 Aspose.PDF 的 FormEditor 类为 PDF 表单字段设置最大字符限制。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中为 PDF 表单字段设置字符限制
Abstract: 本文展示如何绑定现有 PDF、设置字段的最大字符限制，并使用 Aspose.PDF for Java 的 FormEditor 类保存更新后的文档。
---
## 设置字段字符限制

1. 将源 PDF 绑定到 `FormEditor` 对象。
2. 调用 `setFieldLimit(...)` 用于目标字段和最大字符计数。
3. 保存更新后的文档。

```java
public static void setFieldLimit(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldLimit("First Name", 15);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
