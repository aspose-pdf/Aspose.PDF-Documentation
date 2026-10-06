---
title: 单行到多行
linktitle: 单行到多行
type: docs
weight: 60
url: /zh/java/single-to-multiple/
description: 了解如何在 Java 中使用 Aspose.PDF 的 FormEditor 门面，将 PDF 文档中的单行文本字段转换为多行字段。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中将单行 PDF 字段转换为多行字段
Abstract: 本文展示了如何绑定现有 PDF， 将单行字段转换为多行字段，并使用 Aspose.PDF for Java 中的 FormEditor 门面保存更新后的文档。
---
## 将单行字段转换为多行

1. 将源 PDF 绑定到 `FormEditor` 立面。
2. 调用 `single2Multiple(...)` 用于目标字段名称。
3. 保存已更新的文档。

```java
public static void singleToMultiple(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.single2Multiple("City");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
