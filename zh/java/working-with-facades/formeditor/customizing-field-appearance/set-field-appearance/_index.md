---
title: 设置字段外观
linktitle: 设置字段外观
type: docs
weight: 40
url: /zh/java/set-field-appearance/
description: 了解如何在 Java 中使用 Aspose.PDF 的 FormEditor 类更改 PDF 表单字段的可视外观标志。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中更改 PDF 表单字段的外观标志
Abstract: 本文展示了如何绑定现有 PDF，向字段应用外观标志，并使用 Aspose.PDF for Java 的 FormEditor 类保存更新后的文档。
---
## 设置字段外观标志

1. 将源 PDF 绑定到 `FormEditor` 对象。
2. 呼叫 `setFieldAppearance(...)` 针对目标字段和选定的注释标志。
3. 保存更新后的文档。

```java
public static void setFieldAppearance(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAppearance("First Name", AnnotationFlags.Hidden);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
