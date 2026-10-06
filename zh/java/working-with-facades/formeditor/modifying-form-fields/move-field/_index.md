---
title: 移动字段
linktitle: 移动字段
type: docs
weight: 30
url: /zh/java/move-field/
description: 了解如何在 Java 中使用 Aspose.PDF 的 FormEditor 类来移动 PDF 文档中现有的表单字段。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中将 PDF 表单字段移动到新位置
Abstract: 本文展示了如何绑定现有 PDF，使用 Aspose.PDF for Java 的 FormEditor 类将字段移动到新坐标，并保存更新后的文档。
---
## 移动字段

1. 将源 PDF 绑定到 `FormEditor` 对象。
2. 调用 `moveField(...)` 使用目标字段名称和新的矩形坐标。
3. 保存更新后的文档。

```java
public static void moveField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.moveField("Country", 200, 600, 280, 620);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
