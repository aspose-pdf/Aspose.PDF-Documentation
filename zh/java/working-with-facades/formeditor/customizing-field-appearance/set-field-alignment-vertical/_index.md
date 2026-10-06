---
title: 设置字段垂直对齐
linktitle: 设置字段垂直对齐
type: docs
weight: 30
url: /zh/java/set-field-alignment-vertical/
description: 了解如何在 Java 中使用 Aspose.PDF 的 FormEditor 外观来设置 PDF 表单字段的垂直对齐。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中为 PDF 表单字段设置垂直对齐
Abstract: 本文展示了如何绑定已有 PDF，设置字段垂直对齐，并使用 Aspose.PDF for Java 中的 FormEditor 外观保存更新后的文档。
---
## 设置字段垂直对齐

1. 将源 PDF 绑定到 `FormEditor` 外观.
2. 调用 `setFieldAlignmentV(...)` 针对目标字段和所需的垂直对齐常量。
3. 保存更新后的文档。

```java
public static void setFieldAlignmentVertical(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAlignmentV("First Name", FormFieldFacade.ALIGN_BOTTOM);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
