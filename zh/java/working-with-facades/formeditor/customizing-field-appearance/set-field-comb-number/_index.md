---
title: 设置字段组合编号
linktitle: 设置字段组合编号
type: docs
weight: 60
url: /zh/java/set-field-comb-number/
description: 了解如何在 Java 中使用 Aspose.PDF 中的 FormEditor facade 为 PDF 表单字段设置组合编号。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中为 PDF 表单字段设置组合编号
Abstract: 本文演示了如何绑定现有 PDF，为字段设置组合编号，并使用 Aspose.PDF for Java 中的 FormEditor facade 保存更新后的文档。
---
## 设置字段组合编号

1. 将源 PDF 绑定到 `FormEditor` 外观。
2. 调用 `setFieldCombNumber(...)` 针对目标字段和组合值。
3. 保存更新后的文档。

```java
public static void setFieldCombNumber(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldCombNumber("textCombField", 5);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
