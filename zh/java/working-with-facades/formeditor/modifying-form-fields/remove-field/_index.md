---
title: 删除字段
linktitle: 删除字段
type: docs
weight: 40
url: /zh/java/remove-field/
description: 了解如何在 Java 中使用 Aspose.PDF 的 FormEditor 门面从 PDF 文档中删除现有表单字段。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中删除 PDF 表单字段
Abstract: 本文展示了如何绑定现有 PDF，删除指定字段，并使用 Aspose.PDF for Java 中的 FormEditor 门面保存更新后的文档。
---
## 删除字段

1. 将源 PDF 绑定到 `FormEditor` 立面。
2. 调用 `removeField(...)` 用于目标字段名称。
3. 保存更新后的文档。

```java
public static void removeField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeField("Country");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
