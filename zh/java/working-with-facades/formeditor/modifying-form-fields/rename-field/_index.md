---
title: 重命名字段
linktitle: 重命名字段
type: docs
weight: 50
url: /zh/java/rename-field/
description: 学习如何使用 Aspose.PDF 中的 FormEditor 类在 Java 中重命名 PDF 文档中的现有表单字段。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中重命名 PDF 表单字段
Abstract: 本文展示如何绑定现有 PDF，重命名指定字段，并使用 Aspose.PDF for Java 中的 FormEditor 类保存更新后的文档。
---
## 重命名字段

1. 将源 PDF 绑定到 `FormEditor` 对象。
2. 调用 `renameField(...)` 使用当前字段名称和新字段名称。
3. 保存更新后的文档。

```java
public static void renameField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.renameField("City", "Town");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
