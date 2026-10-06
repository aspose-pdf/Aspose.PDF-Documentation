---
title: 添加列表项
linktitle: 添加列表项
type: docs
weight: 10
url: /zh/java/add-list-item/
description: 了解如何在 Java 中使用 Aspose.PDF 的 FormEditor 外观向 PDF 文档中的列表字段添加项。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中向 PDF 表单字段添加列表项
Abstract: 本文展示了如何绑定现有 PDF，向列表字段添加新项，并使用 Aspose.PDF for Java 中的 FormEditor 外观保存更新后的文档。
---
## 向列表字段添加项

1. 将源 PDF 绑定到 `FormEditor` 外观。
2. 调用 `addListItem(...)` 用于目标字段和新的显示/值对。
3. 保存更新后的文档。

```java
public static void addListItem(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addListItem("Country", new String[] {"New Zealand", "New Zealand"});
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
