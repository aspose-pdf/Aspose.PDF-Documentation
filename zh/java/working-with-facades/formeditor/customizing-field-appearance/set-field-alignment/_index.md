---
title: 设置字段对齐
linktitle: 设置字段对齐
type: docs
weight: 20
url: /zh/java/set-field-alignment/
description: 了解如何在 Java 中使用 Aspose.PDF 的 FormEditor 门面设置 PDF 表单字段的水平文本对齐。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中设置 PDF 表单字段对齐
Abstract: 本文展示了如何绑定现有 PDF、设置水平字段对齐，并使用 Aspose.PDF for Java 的 FormEditor 门面保存更新后的文档。
---
## 设置水平字段对齐

1. 将源 PDF 绑定到 `FormEditor` 外观。
2. 呼叫 `setFieldAlignment(...)` 用于目标字段和所需的对齐常量。
3. 保存更新后的文档。

```java
public static void setFieldAlignment(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAlignment("First Name", FormFieldFacade.ALIGN_CENTER);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
