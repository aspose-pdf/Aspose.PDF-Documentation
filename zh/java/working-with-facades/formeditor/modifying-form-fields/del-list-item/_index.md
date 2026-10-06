---
title: 删除列表项
linktitle: 删除列表项
type: docs
weight: 20
url: /zh/java/del-list-item/
description: 了解如何在 Java 中使用 Aspose.PDF 的 FormEditor 外观从 PDF 文档的列表字段中删除项目。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中从 PDF 表单字段删除列表项
Abstract: 本文展示了如何绑定现有 PDF，移除列表字段中的特定项，并使用 Aspose.PDF for Java 中的 FormEditor 外观保存更新后的文档。
---
## 从列表字段删除项目

1. 将源 PDF 绑定到 `FormEditor` 外观。
2. 调用 `delListItem(...)` 用于目标字段和要删除的项。
3. 保存更新后的文档。

```java
public static void deleteListItem(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.delListItem("Country", "UK");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
