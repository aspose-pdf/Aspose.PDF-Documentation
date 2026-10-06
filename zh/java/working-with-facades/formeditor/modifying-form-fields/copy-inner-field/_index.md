---
title: 复制内部字段
linktitle: 复制内部字段
type: docs
weight: 70
url: /zh/java/copy-inner-field/
description: 了解如何在 Java 中使用 Aspose.PDF 的 FormEditor 类将表单字段复制到同一 PDF 文档中的新位置。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中复制同一文档内的 PDF 表单字段
Abstract: 本文展示了如何绑定现有 PDF，将字段复制到另一页及位置，并使用 Aspose.PDF for Java 的 FormEditor 类保存更新后的文档。
---
## 复制同一 PDF 中的字段

1. 将源 PDF 绑定到 `FormEditor` 立面。
2. 调用 `copyInnerField(...)` 带有源字段名称、新字段名称、页面和坐标。
3. 保存已更新的文档。

```java
public static void copyInnerField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.copyInnerField("First Name", "First Name Copy", 2, 200, 600);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
