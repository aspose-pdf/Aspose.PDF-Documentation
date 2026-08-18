---
title: 删除现场行动
linktitle: 删除现场行动
type: docs
weight: 50
url: /java/remove-field-action/
description: 了解如何使用 Aspose.PDF 中的 FormEditor 外观从 Java 中的 PDF 表单字段中删除字段操作。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 在 Java 中删除 PDF 表单字段操作
Abstract: 本文介绍如何绑定现有 PDF、删除与特定字段关联的操作以及使用 Aspose.PDF for Java 中的 FormEditor 外观保存更新的文档。
---
## 删除字段操作

1. 将源 PDF 绑定到 `FormEditor` 外观。
2. 为目标字段调用`removeFieldAction(...)`。
3. 保存更新的文档。

```java
public static void removeFieldAction(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeFieldAction("Script_Demo_Button");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
